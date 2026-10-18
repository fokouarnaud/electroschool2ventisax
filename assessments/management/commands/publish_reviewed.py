"""Publie les questions en brouillon relues en français et en anglais (US-33), sans jamais forcer les autres."""
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from assessments.models import Question


class Command(BaseCommand):
    help = "Publie les questions en brouillon marquées relues en FR et en EN ; signale celles qui sont incohérentes."

    def handle(self, *args, **options):
        published, refused = 0, []
        drafts = Question.objects.filter(status=Question.Status.DRAFT, reviewed_fr=True, reviewed_en=True)
        for question in drafts.select_related("module"):
            try:
                question.publish()
                published += 1
            except ValidationError as exc:
                refused.append(f"{question.external_id or question.pk} : {' '.join(exc.messages)}")
        self.stdout.write(f"{published} question(s) publiée(s).")
        for reason in refused:
            self.stdout.write(f"Refusée {reason}")
