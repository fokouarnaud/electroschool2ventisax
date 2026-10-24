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
