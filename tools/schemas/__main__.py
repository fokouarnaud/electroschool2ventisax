"""python -m tools.schemas <formation> : écrit les schémas de la formation (electro, moteurs ou esp32)."""
import argparse

from . import common, electro, esp32, moteurs

FORMATIONS = {module.SLUG: module for module in (electro, moteurs, esp32)}

parser = argparse.ArgumentParser(prog="python -m tools.schemas", description=__doc__)
parser.add_argument("formation", choices=sorted(FORMATIONS))
common.write_formation(FORMATIONS[parser.parse_args().formation])
