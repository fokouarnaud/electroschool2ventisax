"""US-51 et US-54 : tools/schemas.py range chaque schéma de question dans le dossier de sa partie."""
import importlib.util

import pytest
from django.conf import settings

SPEC = importlib.util.spec_from_file_location("schemas_tool", settings.BASE_DIR / "tools" / "schemas.py")
schemas = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(schemas)


@pytest.mark.parametrize("module, part", [(1, "p1"), (4, "p1"), (5, "p2"), (7, "p2"), (8, "p3"), (11, "p3")])
def test_question_diagrams_go_to_the_folder_of_their_part(module, part):
    assert schemas.question_dir(module) == settings.BASE_DIR / "content" / "electro" / part / f"m{module}" / "schemas"


def test_a_module_outside_the_three_parts_is_refused():
    with pytest.raises(ValueError):
        schemas.question_dir(12)
