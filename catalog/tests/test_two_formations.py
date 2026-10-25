"""US-60 et US-61 (formation `moteurs`) : deux formations côte à côte, sans fuite de l'une vers l'autre."""
import pytest

from accounts.models import Promotion, User
from assessments.models import Assessment
from assessments.services import save_answer, start_attempt, submit_attempt
from catalog.models import Enrollment
from conftest import enroll, make_question
from courses.models import Formation, Module, Partie

ENGINE_PATH = 'd="M12 5v3"'  # tracé propre à templates/icons/engine.svg
CPU_PATH = 'd="M9 9h6v6h-6z"'  # tracé propre à templates/icons/cpu.svg


@pytest.fixture
def moteurs(db):
    formation = Formation.objects.create(
        title_fr="Moteurs électriques et commande", slug="moteurs", order=2, is_open=True, icon="engine",
    )
    partie = Partie.objects.create(formation=formation, title_fr="Sécurité, schémas et distribution", order=1, slug="p1")
    Module.objects.create(partie=partie, title_fr="La sécurité électrique", order=1, duration_hours=8)
    return formation


@pytest.fixture
def moteurs_module(moteurs):
    return Module.objects.get(partie__formation=moteurs)


@pytest.fixture
def moteurs_promotion(moteurs):
    return Promotion.objects.create(name="Électrotechnique 2026", formation=moteurs)


@pytest.fixture
def moteurs_trainer(moteurs_promotion):
    user = User.objects.create_user(username="ngono", password="x-Secret-123", role=User.Role.TRAINER)
    moteurs_promotion.trainers.add(user)
    return user


@pytest.fixture
def electro_trainer(promotion):
    user = User.objects.create_user(username="macaire", password="x-Secret-123", role=User.Role.TRAINER)
    promotion.trainers.add(user)
    return user


@pytest.fixture
def both(learner, promotion, moteurs_promotion):
    """Apprenant inscrit à `electro` (promotion de la fixture commune) et à `moteurs`."""
    enroll(learner, promotion)
    return enroll(learner, moteurs_promotion)


def submitted_quiz(user, module):
    make_question(module)
    attempt = start_attempt(user, Assessment.quiz_for(module))
    for aq in attempt.attempt_questions.select_related("question"):
        ids = aq.question.choices.filter(is_correct=True).values_list("public_id", flat=True)[:1]
        save_answer(attempt, aq.question.public_id, list(ids))
    return submit_attempt(attempt)


# --- US-60 : l'apprenant ---------------------------------------------------------------------------------------------


def test_joining_moteurs_from_the_catalogue_does_not_enroll_in_electro(client, learner, moteurs, partie):
    client.force_login(learner)

    client.post(f"/fr/catalogue/{moteurs.public_id}/inscription/")

    assert list(Enrollment.objects.filter(user=learner).values_list("formation__slug", flat=True)) == ["moteurs"]


def test_dashboard_shows_both_formations_in_catalogue_order_each_with_its_icon(client, both):
    client.force_login(both)

    response = client.get("/fr/")

    assert [row["partie"].formation.slug for row in response.context["parts"]] == ["electro", "moteurs"]
    html = response.content.decode()
    electro, moteurs = html.split('course-formation"')[1:3]
    assert CPU_PATH in electro and ENGINE_PATH not in electro
    assert ENGINE_PATH in moteurs and CPU_PATH not in moteurs


# --- US-61 : le formateur ne voit que la formation de ses promotions -------------------------------------------------


def test_moteurs_trainer_table_holds_only_the_moteurs_formation(client, moteurs_trainer, both):
    client.force_login(moteurs_trainer)

    tables = client.get("/fr/formateur/").context["tables"]

    assert [t["formation"].slug for t in tables] == ["moteurs"]


def test_moteurs_trainer_cannot_read_the_electro_attempt_of_a_shared_learner(client, moteurs_trainer, both, module):
    attempt = submitted_quiz(both, module)  # `module` : fixture commune, dans `electro`
    client.force_login(moteurs_trainer)

    assert client.get(f"/fr/formateur/tentatives/{attempt.public_id}/").status_code == 404


def test_electro_trainer_cannot_read_the_moteurs_attempt_of_a_shared_learner(client, electro_trainer, both, moteurs_module):
    attempt = submitted_quiz(both, moteurs_module)
    client.force_login(electro_trainer)

    assert client.get(f"/fr/formateur/tentatives/{attempt.public_id}/").status_code == 404


def test_moteurs_trainer_still_reads_the_moteurs_attempt_of_a_shared_learner(client, moteurs_trainer, both, moteurs_module):
    attempt = submitted_quiz(both, moteurs_module)
    client.force_login(moteurs_trainer)

    assert client.get(f"/fr/formateur/tentatives/{attempt.public_id}/").status_code == 200


def test_electro_trainer_question_stats_ignore_moteurs_questions(client, electro_trainer, both, module, moteurs_module):
    submitted_quiz(both, module)
    submitted_quiz(both, moteurs_module)
    client.force_login(electro_trainer)

    stats = client.get("/fr/formateur/questions/").context["stats"]

    assert {s["question"].module.partie.formation.slug for s in stats} == {"electro"}


def test_moteurs_trainer_csv_export_lists_no_electro_module(client, moteurs_trainer, both, module):
    client.force_login(moteurs_trainer)

    csv = client.get("/fr/formateur/export.csv").content.decode("utf-8")

    assert "La sécurité électrique" in csv
    assert module.title not in csv


# --- Tableau de bord à plusieurs formations : une formation par bloc, reprise, parties repliées ----------------------


def sections(module, n):
    from courses.models import Section

    return [Section.objects.create(module=module, title_fr=f"Section {k}", order=k) for k in range(1, n + 1)]


@pytest.fixture
def two_parts(partie, module, moteurs_module):
    """`electro` : Partie 1 (un module de 2 sections) et Partie 2 (un module de 2 sections) ; `moteurs` : un module de 2 sections."""
    second_partie = Partie.objects.create(formation=partie.formation, title_fr="Courant alternatif", order=2, slug="p2")
    second = Module.objects.create(partie=second_partie, title_fr="Le courant alternatif", order=1, duration_hours=8)
    for m in (module, second, moteurs_module):
        sections(m, 2)
    return module, second


def test_dashboard_groups_parts_by_formation_with_a_resume_link(client, both, two_parts):
    first, _ = two_parts
    client.force_login(both)

    response = client.get("/fr/")

    blocks = response.context["formations"]
    assert [b["formation"].slug for b in blocks] == ["electro", "moteurs"]
    assert [[row["partie"].slug for row in b["parts"]] for b in blocks] == [["p1", "p2"], ["p1"]]
    assert blocks[0]["resume"] == first and blocks[0]["progress"] == 0
    assert f'class="btn formation-resume" href="/fr/modules/{first.public_id}/"' in response.content.decode()


def test_resume_moves_past_finished_modules_and_formation_progress_counts_their_steps(client, both, two_parts):
    from progress.services import mark_section_viewed

    first, second = two_parts
    for section in first.sections.all():
        mark_section_viewed(both, section)
    client.force_login(both)

    electro = client.get("/fr/").context["formations"][0]

    assert electro["resume"] == second
    assert electro["progress"] == 50  # 2 sections vues sur 4 dans la formation


def test_finished_formation_has_no_resume_link(client, both, two_parts):
    from progress.services import mark_section_viewed

    for m in two_parts:
        for section in m.sections.all():
            mark_section_viewed(both, section)
    client.force_login(both)

    electro = client.get("/fr/").context["formations"][0]

    assert (electro["resume"], electro["progress"]) == (None, 100)


def test_only_the_part_holding_the_resume_module_is_unfolded(client, both, two_parts):
    from progress.services import mark_section_viewed

    first, second = two_parts
    for section in first.sections.all():
        mark_section_viewed(both, section)
    client.force_login(both)

    html = client.get("/fr/").content.decode()

    electro = html.split('<section class="formation"')[1]
    p1, p2 = electro.split('<details class="part')[1:3]
    assert not p1.startswith(' panel" open') and p2.startswith(' panel" open')


def test_jump_links_appear_only_for_a_learner_of_two_formations(client, both, learner, two_parts, moteurs):
    client.force_login(both)
    html = client.get("/fr/").content.decode()
    assert f'href="#formation-{moteurs.public_id}"' in html

    solo = User.objects.create_user(username="solo", password="x-Secret-123")
    Enrollment.objects.create(user=solo, formation=moteurs)
    client.force_login(solo)
    assert 'class="formation-jump"' not in client.get("/fr/").content.decode()
