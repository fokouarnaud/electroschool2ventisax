"""US-117 (formation `esp32`) : trois formations côte à côte, sans fuite de l'une vers les autres."""
import pytest

from accounts.models import Promotion, User
from catalog.models import Enrollment
from catalog.tests.test_two_formations import submitted_quiz
from certificates.models import Certificate
from certificates.tests.test_achievements import complete_module, take_exam
from conftest import enroll, make_question
from courses.models import Formation, Module, Partie, Section


@pytest.fixture
def esp32(db):
    formation = Formation.objects.create(title_fr="Microcontrôleurs : l'ESP32", slug="esp32", order=3, is_open=True, icon="code")
    partie = Partie.objects.create(formation=formation, title_fr="Premiers pas et entrées-sorties", order=1, slug="p1")
    Module.objects.create(partie=partie, title_fr="L'ESP32 et sa carte", order=1, duration_hours=6)
    return formation


@pytest.fixture
def esp32_module(esp32):
    return Module.objects.get(partie__formation=esp32)


@pytest.fixture
def esp32_promotion(esp32):
    return Promotion.objects.create(name="Embarqué 2026", formation=esp32)


@pytest.fixture
def esp32_trainer(esp32_promotion):
    user = User.objects.create_user(username="tchana", password="x-Secret-123", role=User.Role.TRAINER)
    esp32_promotion.trainers.add(user)
    return user


@pytest.fixture
def three(learner, promotion, esp32_promotion, moteurs_promotion):
    """Apprenant inscrit à `electro`, `moteurs` et `esp32`."""
    enroll(learner, promotion)
    enroll(learner, moteurs_promotion)
    return enroll(learner, esp32_promotion)


@pytest.fixture
def moteurs_promotion(db):
    formation = Formation.objects.create(title_fr="Moteurs électriques et commande", slug="moteurs", order=2, is_open=True,
                                         icon="engine")
    partie = Partie.objects.create(formation=formation, title_fr="Sécurité, schémas et distribution", order=1, slug="p1")
    Module.objects.create(partie=partie, title_fr="La sécurité électrique", order=1, duration_hours=8)
    return Promotion.objects.create(name="Électrotechnique 2026", formation=formation)


@pytest.fixture
def moteurs_module(moteurs_promotion):
    return Module.objects.get(partie__formation=moteurs_promotion.formation)


def test_esp32_trainer_table_holds_only_the_esp32_formation(client, esp32_trainer, three):
    client.force_login(esp32_trainer)

    tables = client.get("/fr/formateur/").context["tables"]

    assert [t["formation"].slug for t in tables] == ["esp32"]


@pytest.mark.parametrize("other", ["electro", "moteurs"])
def test_esp32_trainer_cannot_read_an_attempt_of_another_formation(client, esp32_trainer, three, module, moteurs_module, other):
    attempt = submitted_quiz(three, module if other == "electro" else moteurs_module)
    client.force_login(esp32_trainer)

    assert client.get(f"/fr/formateur/tentatives/{attempt.public_id}/").status_code == 404


def test_esp32_trainer_reads_the_esp32_attempt_of_a_shared_learner(client, esp32_trainer, three, esp32_module):
    attempt = submitted_quiz(three, esp32_module)
    client.force_login(esp32_trainer)

    assert client.get(f"/fr/formateur/tentatives/{attempt.public_id}/").status_code == 200


def test_other_trainers_cannot_read_the_esp32_attempt(client, three, promotion, moteurs_promotion, esp32_module):
    attempt = submitted_quiz(three, esp32_module)
    for name, promo in (("macaire", promotion), ("ngono", moteurs_promotion)):
        trainer = User.objects.create_user(username=name, password="x-Secret-123", role=User.Role.TRAINER)
        promo.trainers.add(trainer)
        client.force_login(trainer)

        assert client.get(f"/fr/formateur/tentatives/{attempt.public_id}/").status_code == 404


def test_esp32_trainer_question_stats_and_csv_ignore_the_other_formations(client, esp32_trainer, three, module,
                                                                          moteurs_module, esp32_module):
    for m in (module, moteurs_module, esp32_module):
        submitted_quiz(three, m)
    client.force_login(esp32_trainer)

    stats = client.get("/fr/formateur/questions/").context["stats"]
    csv = client.get("/fr/formateur/export.csv").content.decode("utf-8")

    assert {s["question"].module.partie.formation.slug for s in stats} == {"esp32"}
    assert "L'ESP32 et sa carte" in csv
    assert module.title not in csv and moteurs_module.title not in csv


def test_a_learner_of_electro_only_cannot_read_an_esp32_section(client, learner, promotion, esp32_module):
    enroll(learner, promotion)
    section = Section.objects.create(module=esp32_module, title_fr="Du composant au microcontrôleur", order=1)
    client.force_login(learner)

    assert client.get(f"/fr/sections/{section.public_id}/").status_code in (302, 404)


def test_joining_esp32_from_the_catalogue_enrolls_in_esp32_only(client, learner, esp32, partie):
    client.force_login(learner)

    client.post(f"/fr/catalogue/{esp32.public_id}/inscription/")

    assert list(Enrollment.objects.filter(user=learner).values_list("formation__slug", flat=True)) == ["esp32"]


def test_a_learner_of_the_three_formations_gets_a_distinct_esp32_certificate(three, partie, module, esp32):
    three.first_name, three.last_name = "Awa", "Nkoulou"
    three.save()
    esp32_part = esp32.parties.get()
    for p in (partie, esp32_part):
        for m in p.modules.all():
            Section.objects.create(module=m, title_fr=f"Section de {m.title}", order=1)
            make_question(m)
            for _ in range(4):
                make_question(m, usage="exam")
            complete_module(three, m)
        take_exam(three, p, right=True)

    certificates = Certificate.objects.filter(user=three).order_by("partie__formation__order")
    assert [c.partie.formation.slug for c in certificates] == ["electro", "esp32"]
    assert certificates[0].public_id != certificates[1].public_id
