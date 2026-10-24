#!/usr/bin/env bash
# Mise à jour d'Electro Acad Ventisax sur PythonAnywhere : bash ~/electroschool2ventisax/deploy.sh
set -euo pipefail
cd "$(dirname "$0")"
VENV="${VENV:-$HOME/.virtualenvs/electro}"
PY="$VENV/bin/python"

git pull --ff-only
"$VENV/bin/pip" install --quiet -r requirements.txt
"$PY" manage.py migrate --noinput
# Toutes les formations du dépôt (content/<slug>/formation.json), par ordre alphabétique (US-63).
"$PY" manage.py import_content content/*/formation.json
# Publie les questions relues en FR et en EN (drapeaux « reviewed » du contenu versionné) ; les autres restent en brouillon.
"$PY" manage.py publish_reviewed
"$PY" manage.py collectstatic --noinput --verbosity 0
"$PY" manage.py check --deploy --fail-level ERROR
# Recharge l'application web (le fichier WSGI de PythonAnywhere).
touch "/var/www/${PA_DOMAIN:-electroacadventisax_pythonanywhere_com}_wsgi.py"
echo "Déploiement terminé."
