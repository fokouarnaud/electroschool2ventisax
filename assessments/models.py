import random
import uuid

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.uploads import ACTIVE_SVG, RandomFilename, validate_inert_svg


class QuestionQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=Question.Status.PUBLISHED)


class Question(models.Model):
    class Type(models.TextChoices):
        SINGLE = "single", _("QCM une réponse")
        MULTIPLE = "multiple", _("QCM plusieurs réponses")
        TRUE_FALSE = "truefalse", _("Vrai / Faux")
        NUMERIC = "numeric", _("Réponse numérique")
        MATCHING = "matching", _("Appariement")
        HOTSPOT = "hotspot", _("Zone cliquable sur schéma")

    class Usage(models.TextChoices):
        QUIZ = "quiz", _("Quiz de module")
        EXAM = "exam", _("Examen de partie")

    class Status(models.TextChoices):
        DRAFT = "draft", _("Brouillon")
        PUBLISHED = "published", _("Publiée")

    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # identifiant des URL et formulaires
    module = models.ForeignKey("courses.Module", on_delete=models.CASCADE, related_name="questions")
    qtype = models.CharField(_("type"), max_length=10, choices=Type.choices, default=Type.SINGLE)
    usage = models.CharField(_("usage"), max_length=5, choices=Usage.choices, default=Usage.QUIZ)
    status = models.CharField(_("statut"), max_length=10, choices=Status.choices, default=Status.DRAFT)
    prompt = models.TextField(_("énoncé"))
    explanation = models.TextField(_("explication"), blank=True)
    # FileField plutôt qu'ImageField : Pillow est exclu (budget disque, AGENTS.md).
    image = models.FileField(
        _("image"), upload_to=RandomFilename("questions"), blank=True,
        validators=[FileExtensionValidator(["webp", "png", "jpg", "jpeg", "svg"]), validate_inert_svg],
    )
    # Numérique (E13) : valeur attendue en unité de base (ex. 4700 pour 4,7 kΩ), unité et tolérance relative.
    numeric_value = models.DecimalField(_("valeur attendue"), max_digits=24, decimal_places=12, null=True, blank=True)
    unit = models.CharField(_("unité"), max_length=10, blank=True)
    tolerance_pct = models.DecimalField(_("tolérance (%)"), max_digits=5, decimal_places=2, default=2)
    # Zone cliquable : schéma SVG affiché en ligne ; chaque choix porte sa zone (Choice.shape).
    hotspot_svg = models.TextField(_("schéma SVG"), blank=True)
    reviewed_fr = models.BooleanField(_("relue en français"), default=False)
    reviewed_en = models.BooleanField(_("relue en anglais"), default=False)
    external_id = models.CharField(max_length=50, unique=True, null=True, blank=True)

    objects = QuestionQuerySet.as_manager()

    class Meta:
        ordering = ["module", "pk"]

    def __str__(self):
        return self.prompt[:60]

    def validate_for_publication(self):
        errors = []
        if not (self.reviewed_fr and self.reviewed_en):
            errors.append(_("La question doit être relue en français et en anglais."))
        choices = list(self.choices.all())
        correct = sum(c.is_correct for c in choices)
        if self.qtype == self.Type.SINGLE and correct != 1:
            errors.append(_("Un QCM à une réponse doit avoir exactement une bonne réponse."))
        if self.qtype == self.Type.MULTIPLE and correct < 2:
            errors.append(_("Un QCM à plusieurs réponses doit avoir au moins deux bonnes réponses."))
        if self.qtype == self.Type.TRUE_FALSE and (len(choices) != 2 or correct != 1):
            errors.append(_("Une question Vrai/Faux doit avoir deux choix dont un seul correct."))
        if self.qtype == self.Type.NUMERIC:
            if self.numeric_value is None:
                errors.append(_("Une question numérique doit avoir une valeur attendue."))
            if choices:
                errors.append(_("Une question numérique n'a pas de choix."))
        if self.qtype == self.Type.MATCHING and self.pairs.count() < 2:
            errors.append(_("Une question d'appariement doit avoir au moins deux paires."))
        if self.qtype == self.Type.HOTSPOT:
            if "<svg" not in self.hotspot_svg:
                errors.append(_("Une question sur schéma doit avoir un schéma SVG."))
            elif ACTIVE_SVG.search(self.hotspot_svg.encode("utf-8")):
                errors.append(_("Ce SVG contient du script ou un lien actif : il est refusé."))
            if correct != 1:
                errors.append(_("Une question sur schéma doit avoir exactement une bonne zone."))
            if any(not c.shape for c in choices):
                errors.append(_("Chaque zone d'une question sur schéma doit avoir une forme."))
        if errors:
            raise ValidationError(errors)

    def expected_value_display(self):
        """« 4,7 kΩ » : valeur attendue d'une question numérique, avec préfixe SI et séparateur de la langue."""
        if self.qtype != self.Type.NUMERIC or self.numeric_value is None:
            return ""
        from .scoring import format_quantity

        return format_quantity(self.numeric_value, self.unit)

    def publish(self):
        self.validate_for_publication()
        self.status = self.Status.PUBLISHED
        self.save(update_fields=["status"])


class Choice(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # identifiant des URL et formulaires
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(_("texte"), max_length=300)
    is_correct = models.BooleanField(_("bonne réponse"), default=False)
    order = models.PositiveIntegerField(default=0)
    # Zone d'une question sur schéma, en unités du viewBox : {"x", "y", "w", "h"}.
    shape = models.JSONField(_("zone"), null=True, blank=True)

    class Meta:
        ordering = ["order", "pk"]

    def __str__(self):
        return self.text


class MatchPair(models.Model):
    """Paire juste d'une question d'appariement ; la colonne de droite est mélangée à chaque tentative."""

    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # identifiant des URL et formulaires
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="pairs")
    left = models.CharField(_("élément"), max_length=200)
    right = models.CharField(_("correspondance"), max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "pk"]

    def __str__(self):
        return f"{self.left} → {self.right}"


class Assessment(models.Model):
    class Kind(models.TextChoices):
        MODULE_QUIZ = "module_quiz", _("Quiz de module")
        PART_EXAM = "part_exam", _("Examen de partie")

    kind = models.CharField(max_length=12, choices=Kind.choices)
    module = models.OneToOneField(
        "courses.Module", on_delete=models.CASCADE, null=True, blank=True, related_name="quiz"
    )
    partie = models.OneToOneField(
        "courses.Partie", on_delete=models.CASCADE, null=True, blank=True, related_name="exam"
    )
    pass_threshold = models.PositiveSmallIntegerField(_("seuil de réussite (%)"), default=70)
    max_attempts = models.PositiveSmallIntegerField(_("tentatives maximum"), null=True, blank=True)
    duration_minutes = models.PositiveSmallIntegerField(_("durée (minutes)"), null=True, blank=True)
    questions_per_module = models.PositiveSmallIntegerField(_("questions par module"), default=10)
    shuffle = models.BooleanField(_("mélanger questions et choix"), default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(kind="module_quiz", module__isnull=False, partie__isnull=True)
                    | models.Q(kind="part_exam", module__isnull=True, partie__isnull=False)
                ),
                name="assessment_target_matches_kind",
            )
        ]

    def __str__(self):
        return f"{self.get_kind_display()} : {self.module or self.partie}"

    @classmethod
    def quiz_for(cls, module):
        return cls.objects.get_or_create(kind=cls.Kind.MODULE_QUIZ, module=module)[0]

    @classmethod
    def exam_for(cls, partie):
        return cls.objects.get_or_create(
            kind=cls.Kind.PART_EXAM,
            partie=partie,
            defaults={"max_attempts": 3, "duration_minutes": 60, "shuffle": True},
        )[0]

    @property
    def is_exam(self):
        return self.kind == self.Kind.PART_EXAM

    def question_pool(self, rng=random):
        published = Question.objects.published()
        if not self.is_exam:
            return list(published.filter(module=self.module, usage=Question.Usage.QUIZ))
        drawn = []
        for module in self.partie.modules.all():
            candidates = list(published.filter(module=module, usage=Question.Usage.EXAM))
            drawn += rng.sample(candidates, min(self.questions_per_module, len(candidates)))
        if self.shuffle:
            rng.shuffle(drawn)
        return drawn

    def best_attempt(self, user):
        return (
            self.attempts.filter(user=user, submitted_at__isnull=False)
            .order_by("-score_pct", "submitted_at")
            .first()
        )


class Attempt(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # identifiant des URL et formulaires
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="attempts")
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name="attempts")
    number = models.PositiveIntegerField()
    started_at = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    score_pct = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    auto_submitted = models.BooleanField(default=False)

    class Meta:
        ordering = ["assessment", "user", "number"]
        constraints = [
            models.UniqueConstraint(fields=["user", "assessment", "number"], name="unique_attempt_number")
        ]

    def __str__(self):
        return f"{self.user} – {self.assessment} #{self.number}"

    @property
    def passed(self):
        return self.score_pct is not None and self.score_pct >= self.assessment.pass_threshold

    def module_scores(self):
        from .services import percentage

        by_module = {}
        for item in self.feedback():
            by_module.setdefault(item["question"].module, []).append(item["score"])
        ordered = sorted(by_module.items(), key=lambda kv: (kv[0].order, kv[0].pk))
        return {module: percentage(scores) for module, scores in ordered}

    def feedback(self):
        items = []
        for aq in self.attempt_questions.select_related("question").prefetch_related(
            "question__choices", "question__pairs", "selected_choices"
        ):
            question = aq.question
            correct = [c.pk for c in question.choices.all() if c.is_correct]
            selected = sorted(c.pk for c in aq.selected_choices.all())
            items.append({
                "question": question,
                "correct_choice_ids": correct,
                "selected_choice_ids": selected,
                "answer_text": aq.answer_text,
                "answer_pairs": aq.answer_json,
                "pair_rows": aq.pair_rows(),
                "expected_value": question.expected_value_display(),
                "explanation": question.explanation,
                "score": aq.score(correct, selected),
            })
        return items


class AttemptQuestion(models.Model):
    """Question tirée pour une tentative, avec la réponse de l'apprenant (l'entité Answer du PRD)."""

    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE, related_name="attempt_questions")
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    order = models.PositiveIntegerField()
    selected_choices = models.ManyToManyField(Choice, blank=True)
    answered_at = models.DateTimeField(null=True, blank=True)
    choice_order = models.JSONField(default=list, blank=True)  # choix, ou paires (colonne de droite) d'un appariement
    answer_text = models.CharField(max_length=50, blank=True)  # réponse numérique saisie
    answer_json = models.JSONField(default=dict, blank=True)  # appariement : {paire de gauche: paire de droite}
    time_spent_s = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(fields=["attempt", "question"], name="unique_question_per_attempt")
        ]

    def ordered_choices(self):
        choices = {c.pk: c for c in self.question.choices.all()}
        ordered = [choices.pop(pk) for pk in self.choice_order if pk in choices]
        return ordered + list(choices.values())

    def ordered_pairs(self):
        pairs = {p.pk: p for p in self.question.pairs.all()}
        ordered = [pairs.pop(pk) for pk in self.choice_order if pk in pairs]
        return ordered + list(pairs.values())

    def pair_rows(self):
        """Appariement corrigé : pour chaque élément de gauche, la correspondance donnée et l'attendue."""
        pairs = {str(p.public_id): p for p in self.question.pairs.all()}
        rows = []
        for key, pair in pairs.items():
            given = pairs.get(self.answer_json.get(key, ""))
            rows.append({
                "left": pair.left, "given": given.right if given else "", "expected": pair.right, "ok": given is pair,
            })
        return rows

    def score(self, correct_choice_ids, selected_choice_ids):
        from .scoring import score_answer, score_matching, score_numeric

        question = self.question
        if question.qtype == Question.Type.NUMERIC:
            return score_numeric(question.numeric_value, question.unit, question.tolerance_pct, self.answer_text)
        if question.qtype == Question.Type.MATCHING:
            expected = {str(p.public_id): str(p.public_id) for p in question.pairs.all()}
            return score_matching(expected, self.answer_json)
        return score_answer(question.qtype, correct_choice_ids, selected_choice_ids)
