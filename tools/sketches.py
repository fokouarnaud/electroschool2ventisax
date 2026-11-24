"""python tools/sketches.py : compile chaque croquis d'`esp32` (C17, C20) avec PlatformIO, au poste de développement.

Chaque croquis vit dans content/esp32/sketches/m<N>/<nom>/main.<fr|en>.cpp ; il est compilé seul, dans un projet
temporaire qui reprend le platformio.ini de référence (et secrets.example.h comme include/secrets.h s'il existe).
Jamais lancé par deploy.sh ni sur le serveur.
"""
import argparse
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKETCHES = ROOT / "content" / "esp32" / "sketches"
LANGS = ("fr", "en")


@dataclass(frozen=True)
class Sketch:
    name: str  # « m2/blink »
    lang: str
    path: Path


def discover(root=SKETCHES):
    """Croquis triés par nom puis langue."""
    found = []
    for path in Path(root).glob("m*/*/main.*.cpp"):
        lang = path.name.split(".")[1]
        if lang in LANGS:
            found.append(Sketch(f"{path.parent.parent.name}/{path.parent.name}", lang, path))
    return sorted(found, key=lambda s: (s.name, s.lang))


def project(sketch, ini, workdir):
    """Projet PlatformIO d'un croquis : platformio.ini, src/main.cpp et, au besoin, include/secrets.h."""
    workdir = Path(workdir)
    (workdir / "src").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ini, workdir / "platformio.ini")
    shutil.copyfile(sketch.path, workdir / "src" / "main.cpp")
    secrets = sketch.path.parent / "secrets.example.h"
    if secrets.exists():
        (workdir / "include").mkdir(exist_ok=True)
        shutil.copyfile(secrets, workdir / "include" / "secrets.h")
    return workdir


def pio():
    """Chemin de PlatformIO : sur le PATH, sinon dans son environnement par défaut."""
    found = shutil.which("pio") or shutil.which("platformio")
    if found:
        return found
    default = Path.home() / ".platformio" / "penv" / ("Scripts/pio.exe" if sys.platform == "win32" else "bin/pio")
    return str(default) if default.exists() else None


def run_platformio(project_dir):
    return subprocess.run([pio(), "run", "-d", str(project_dir)]).returncode


def compile_all(root=SKETCHES, runner=run_platformio):
    """Compile les croquis un à un ; s'arrête au premier échec et renvoie son nom (liste vide si tout compile)."""
    root = Path(root)
    for sketch in discover(root):
        with tempfile.TemporaryDirectory() as workdir:
            if runner(project(sketch, root / "platformio.ini", workdir)) != 0:
                return [f"{sketch.name} ({sketch.lang})"]
    return []


def main(argv=None, runner=None):
    parser = argparse.ArgumentParser(prog="python tools/sketches.py", description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=SKETCHES)
    args = parser.parse_args(argv)
    if runner is None:
        if pio() is None:
            print("PlatformIO introuvable : installez-le (VS Code) avant de compiler les croquis.", file=sys.stderr)
            return 2
        runner = run_platformio
    failures = compile_all(args.root, runner)
    for name in failures:
        print(f"Échec de compilation : {name}", file=sys.stderr)
    print(f"{len(discover(args.root))} croquis, {len(failures)} échec.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
