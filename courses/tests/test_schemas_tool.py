"""US-51, US-54 et US-65 : le paquet tools/schemas range chaque schéma dans le dossier de sa formation et de sa partie."""
import subprocess
import sys

import pytest
from django.conf import settings

from tools.schemas import common, electro, moteurs

ROOT = settings.BASE_DIR


@pytest.mark.parametrize("module, part", [(1, "p1"), (4, "p1"), (5, "p2"), (7, "p2"), (8, "p3"), (11, "p3")])
def test_electro_question_diagrams_go_to_the_folder_of_their_part(module, part):
    assert electro.question_dir(module) == ROOT / "content" / "electro" / part / f"m{module}" / "schemas"


def test_an_electro_module_outside_the_three_parts_is_refused():
    with pytest.raises(ValueError):
        electro.question_dir(12)


@pytest.mark.parametrize("module, part", [(1, "p1"), (3, "p1"), (4, "p2"), (6, "p2"), (7, "p3"), (9, "p3"), (10, "p4"), (12, "p4")])
def test_moteurs_question_diagrams_go_to_the_folder_of_their_part(module, part):
    assert moteurs.question_dir(module) == ROOT / "content" / "moteurs" / part / f"m{module}" / "schemas"


def test_a_moteurs_module_outside_the_four_parts_is_refused():
    with pytest.raises(ValueError):
        moteurs.question_dir(13)


def test_regenerating_electro_rewrites_its_287_diagrams_byte_for_byte(tmp_path):
    """Garde-fou de la refactorisation (M6) : 276 schémas de sections (FR et EN) et 11 de questions, identiques."""
    common.write_formation(electro, root=tmp_path)

    written = sorted(p.relative_to(tmp_path) for p in tmp_path.rglob("*.svg"))
    committed = sorted(
        p.relative_to(ROOT) for folder in ("static/content/electro", "content/electro") for p in (ROOT / folder).rglob("*.svg")
    )
    assert written == committed
    assert len(written) == 287
    different = [str(rel) for rel in written if (tmp_path / rel).read_bytes() != (ROOT / rel).read_bytes()]
    assert different == []


def test_the_command_line_refuses_an_unknown_formation():
    result = subprocess.run([sys.executable, "-m", "tools.schemas", "froid"], cwd=ROOT, capture_output=True, text=True)

    assert result.returncode != 0
    assert "froid" in result.stderr
