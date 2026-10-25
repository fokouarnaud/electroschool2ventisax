---
name: figure-interactive
description: Ajoute une figure interactive explicative (banc isométrique du skill anatomy) à une section des formations `electro` ou `moteurs` d'Electro Acad Ventisax, sur le modèle du pilote « passe-bas RC » (grill F1 à F15) - modèle physique testé, build Node déterministe, emplacement `[[fig:<nom>]]`, carte traduite FR/EN, TDD pytest. À utiliser quand l'utilisateur demande une figure, une animation ou un schéma interactif pour une notion du cours (passe-haut RC, fréquence de coupure, déphasage, résonance, champ tournant, glissement, auto-maintien…).
---

# Figure interactive d'une section

Une figure explique **une** notion d'**une** section par un objet réel qu'on manipule (skill `anatomy` : « l'objet est l'explication »).
Le pilote fait référence : `tools/figures/rc_lowpass/` (modèle, build, test), `templates/figures/rc_lowpass.html` (carte),
`courses/figures.py` (registre), `courses/tests/test_figures.py` (tests), section `content/electro/p2/m6/03-passe-bas.*.md`.
Figures déjà livrées (M6 d'`electro`, dans l'ordre des sections) : `rc_lowpass` (03), `rc_highpass` (04), `rc_cutoff` (05), `rc_phase` (06), `rl_lowpass` (07).
« La section suivante » = la section qui suit la dernière figure livrée, en sautant les mini-projets (sections `practical`, sans figure) ; prochaine : M7 d'`electro`, `01-lc-serie` (piste « Résonance LC »).
Les règles du grill F1 à F15 (AGENTS.md) s'appliquent à toutes les figures. Lis d'abord le skill `anatomy` (SKILL.md et `references/craft.md`) si tu ne l'as pas en tête.

## Règles qui ne se négocient pas
- **Exactitude** (F1) : chaque nombre et chaque mouvement sort d'un modèle pur (`model.mjs`) dont la formule est celle de la section. Une image fausse « pour simplifier » est interdite. Seule la cadence peut être ralentie, et la carte le dit.
- **Valeurs fixes, non notées** (F4, F14) : une seule commande (en général la fréquence), des repères, aucune donnée enregistrée, aucune question qui s'appuie sur la figure, aucun circuit libre (sinon c'est un simulateur, hors scope).
- **Production sans Node** (F6) : Node ne sert qu'au poste de développement ; les fichiers générés sont committés et jamais retouchés à la main.
- **Budgets** (F8) : SVG ≤ 80 Ko, script ≤ 8 Ko ; page < 200 Ko ; CSS + JS de la page < 60 Ko (HTMX non compté).
- **Charte** (F9) : `static/acad/css/figures.css` est partagé ; un seul accent teal (`lit`) pour la pièce à observer ; thèmes clair et sombre ; pas de WebGL.
- **SVG sans texte** (F11) : un seul dessin pour les deux langues ; tout texte vit dans la carte HTML traduite.
- **Sobriété** (F12) : immobile au chargement, animation après action, pause, arrêt hors écran, figée sous `prefers-reduced-motion`, commandes masquées sans JavaScript.
- **CSP** : aucun script en ligne ; le script de la figure se charge seulement sur sa section.
- **Contenu original** (E2) : rien du livre de référence ni de NetAcad.
- **`moteurs`** : normes CEI, ≤ 24 V pour tout ce qui est manipulé, aucun nombre complexe (M2, M5, M9).

## Étapes (dans cet ordre, en TDD)

### 0. Cadrer
1. Repère la section (`content/<formation>/p<P>/m<N>/<NN>-<slug>.fr.md`) et sa formule. Nomme la figure en `snake_case` anglais (`rc_highpass`, `rc_cutoff`, `rc_phase`, `lc_resonance`, `rotating_field`, `slip`, `latching`…).
2. Écris, **à la main**, le tableau des littéraux : 3 à 5 points (basse, coupure ou point remarquable, haute) avec leurs valeurs à 3 chiffres. Recalcule-les deux fois (écart < 0,1 %). Une erreur s'est déjà glissée ainsi (0,0995 au lieu de 0,0990).
3. Invente l'objet et écris en une phrase ce qui bouge et ce que ce mouvement signifie, puis la table de correspondance objet → grandeur (elle devient la légende). Pistes :
   - **Passe-haut RC** : même banc hydraulique, mais le soufflet **en série** dans la ligne et la vanne vers le bac ; le manomètre lit la pression aux bornes de la vanne (Vs aux bornes de R).
   - **Fréquence de coupure** (livrée, `rc_cutoff`) : le banc du passe-bas, manomètre différentiel sur la vanne (VR) et manomètre du nœud (Vs), une aiguille de crête teal par cadran ; à fc, les deux crêtes se posent sur 0,707.
   - **Déphasage** (livrée, `rc_phase`) : traceur à deux voies (papier qui défile, deux plumes, réglette fixe), générateur et boîtier du filtre reliés par câbles ; vitesse du papier proportionnelle à f pour qu'une période fasse toujours 8 graduations (45° chacune) ; accolade Δt entre les crêtes. Objet léger : 40 Ko au lieu de 79.
   - **Filtres RL** (livrée, `rl_lowpass`) : build dérivé du passe-haut RC, cloche remplacée par un carter de roue à aubes et un volant d'inertie teal en série ; repère du volant en quadrature avec le courant, amplitude ∝ I ; arrondir les grandeurs à 6 chiffres significatifs avant de les formater (« 100 Ω », pas « 100,0 Ω »).
   - **Résonance LC** : volant d'inertie (L) et ressort (C) entraînés par un excentrique ; l'amplitude culmine à f0 = 1/(2π√(LC)).
   - **Champ tournant** (`moteurs`) : trois bobines à 120° et une aiguille aimantée ; vitesse de synchronisme 60·f/p.
   - **Glissement** : disque synchrone stroboscopique et rotor qui décroche ; g = (ns − n)/ns en %.
   - **Auto-maintien** : contacteur 24 V, boutons marche-arrêt, contact 13-14 qui garde la bobine alimentée.
4. Si la notion, l'objet ou la section n'ont pas été tranchés avec l'utilisateur, demande-le avant d'écrire du code (F2 et F15 prévoient un grill pour la liste des figures). Quand l'utilisateur désigne lui-même « la section suivante », il tranche la section : prends la piste ci-dessus pour l'objet, dis-le dans le rapport et consigne l'exception au grill dans AGENTS.md (GOALS point 25, hors scope, écart d'implémentation).
5. Repères : ceux du texte de la section (fc / 10, fc, 10 × fc, ou l'exemple chiffré qu'elle donne, comme « Xc = 577 Ω »), pas des fréquences arbitraires.

### 1. Modèle (rouge puis vert)
- `tools/figures/<nom>/model.test.mjs` : un test par grandeur, avec les littéraux du tableau et une tolérance explicite (copie la forme de `rc_lowpass/model.test.mjs`).
- Lance `node --test "tools/figures/**/*.test.mjs"` : il doit échouer, module introuvable. Passe un **motif**, pas un dossier : `node --test tools/figures/` échoue sous Node 24 pour une autre raison.
- Écris `tools/figures/<nom>/model.mjs` : constantes et fonctions pures, `export` en tête de ligne, commentaires sur leur propre ligne (le build retire `export ` et les lignes `//` pour l'intégrer au script).
- Relance jusqu'au vert, puis lance `pytest` : `test_physical_models_of_the_figures_pass_their_hand_checked_literals` exécute tous les `model.test.mjs`.
- Toute grandeur que le dessin anime (une phase, une seconde tension) sort du modèle et a son test, même si elle n'est pas affichée ; ajoute un test de cohérence (loi des mailles VR + Vs = Ve, avance + retard = 90°).

### 2. Registre (rouge puis vert)
- Dans `courses/tests/test_figures.py`, ajoute d'abord l'entrée attendue dans `test_registry_describes_each_figure_by_its_drawing_card_and_script` (et dans `FIGURES == (...)`). Lance `pytest` : rouge.
- Ajoute l'entrée dans `REGISTRY` de `courses/figures.py` : `Figure(drawing="figures/<nom>.svg", card="figures/<nom>.html", script="acad/js/figures/<nom>.js")`. Lance `pytest`.
- Les tests paramétrés sur `FIGURES` (fichiers présents, budgets, SVG inerte, sans texte ni NaN, régénération octet pour octet, aucun appel réseau) couvrent alors automatiquement la nouvelle figure : ils échouent tant que le build n'existe pas. C'est le rouge attendu.

### 3. Build (vert)
Copie `tools/figures/rc_lowpass/build.mjs` et garde son ossature :
- import du kit `../kit/iso-kit.mjs` (copie MIT du skill anatomy, licence dans `tools/figures/kit/LICENSE`) ;
- plan en unités monde, `fitProjection` sur 640 × 360, azimut 35 à 45° ;
- pièces fixes dessinées une fois ; pièces mobiles dans `<g data-part="…">` et déplacées **par translation seulement** (`up(dz)` ou la base `O, EX, EY, EZ`) ; un soufflet ou un ressort se déplace pli par pli (`data-step`), jamais par `scale` (qui écrase les ellipses) ; aiguilles et pointeurs recalculés par `seg()` sur une face du dessus ;
- `figureSvg(...).replace(' role="img" aria-label=""', ' aria-hidden="true" focusable="false"')` : le texte alternatif est dans la carte ;
- script généré : modèle intégré, IIFE qui cible `.fig[data-fig="<nom>"]`, `Intl.NumberFormat(document.documentElement.lang)`, `requestAnimationFrame` seulement quand la figure joue, est visible et sans `reduced-motion`, `IntersectionObserver`, `[data-fig-controls]` démasqué par le script ;
- sortie déterministe en LF ; option `--out <dossier>` (utilisée par le test de régénération).

Pièges déjà rencontrés :
- Une dalle sans `d` (ou sans `w`) produit des tracés `NaN` : le navigateur les refuse, et le test `..._has_only_finite_coordinates` les attrape.
- Le poids monte vite : vise des cylindres à 12 à 24 segments (36 pour un cadran), des molettes à 28 stries, des biseaux seulement sur les grosses pièces. Mesure avec le compte par classe de tracé (voir l'historique du pilote) avant de supprimer des pièces.
- `sed` sur des nombres de segments s'enchaîne (48 → 28 → 18 dans la même commande) : modifie une valeur à la fois.
- Pour dériver un build d'un autre ou faire plusieurs remplacements, écris un script Python dans le scratchpad (Write), chaque remplacement vérifié présent une seule fois : un long heredoc Python passé à Bash casse le shell (« unexpected EOF while looking for matching »).
- `Path.write_text` sous Windows écrit du CRLF : passe toujours `newline="\n"` (Python, Markdown, `.po`).
- Sans JavaScript, la figure doit rester parlante : calcule dans le build l'état du repère de départ (tracés, aiguilles de crête) au lieu de laisser `d=""`.
- Affiche les rapports à 3 chiffres significatifs (`maximumSignificantDigits: 3`) : « 0,0995 », pas « 0,100 » qui contredirait le récit ; un retard s'affiche en positif sous l'étiquette « Retard », jamais « Retard : −45° ».

Contrôle `lines.mjs` du skill anatomy : il veut une page HTML, pas un SVG. Dans le scratchpad, écris une page qui contient `figures.css` (avec `--surface`, `--teal-ink` et `--teal` définis) et le SVG dans `<div class="fig"><div class="fig-stage">`, puis `node ~/.claude/skills/anatomy/scripts/lines.mjs <page.html>`. Corrections habituelles : graduations posées sur une ligne de base ou un cercle, rainure arrêtée par deux points, lignes imprimées tirées jusqu'aux bords, symboles faits de contours fermés reliés aux bords du capot. Objectif : `0 of N ends float`.

Lance `node tools/figures/<nom>/build.mjs`, puis `pytest`.

### 4. Carte et traductions
- Copie `templates/figures/rc_lowpass.html` en `templates/figures/<nom>.html`. Garde `class="fig" data-fig="<nom>"`, `data-fig-controls hidden`, `aria-live="polite"` sur le relevé et des boutons de 44 px. Donne des `id` uniques (`fig-<nom>-freq`) : deux figures peuvent partager une page.
- Écris d'abord, dans `test_figures.py`, le test de traduction de la carte (une chaîne anglaise attendue, avec le deux-points dans la chaîne : « Throttled valve: »), puis lance `pytest` : rouge.
- Typographie : deux-points intégrés aux chaînes traduites (« Piston : » / « Piston: »), aucun tiret long, virgule décimale en FR. En anglais, Vin et Vout (pas Ve et Vs).
- `python manage.py makemessages -l en --ignore=.venv --ignore=node_modules --ignore=staticfiles --ignore=tools`, remplis les `msgstr` (retire les `#, fuzzy` devinés par gettext), puis `python manage.py compilemessages -l en`. Aucune chaîne vide. Lance `pytest`.
- Pour remplir : un script du scratchpad avec un dictionnaire `msgid → msgstr` qui réécrit chaque bloc (garde les lignes `#:`, retire `#,` et `#|`) et échoue si un `msgid` attendu manque. Contrôle ensuite : `grep -c '#, fuzzy'` à 0 et aucun `msgstr ""` isolé.
- Les étiquettes du relevé qui nomment une tension passent aussi par gettext (« Vs / Ve » → « Vout / Vin »).

### 5. Contenu
- Écris d'abord le test de placement, sur le modèle de `test_lowpass_section_carries_the_figure_under_its_corrected_story` (emplacement en FR et en EN, ordre schéma → récit → figure → courbe) et, si un récit fautif circulait, le test de ses formulations interdites. Lance `pytest` : rouge.
- Dans la section FR et EN : un sous-titre de récit (« Ce qui se passe dans le circuit » ou équivalent), un récit exact en 2 ou 3 paragraphes, puis `[[fig:<nom>]]` **seul sur sa ligne**, entre le schéma CEI existant et la courbe. Les schémas CEI existants restent en place (F10). Le contenu doit rester conforme aux garde-fous (`courses/tests/test_content_files.py` : schémas par section, unités, etc.).
- `python manage.py import_content content/*/formation.json`, puis `pytest`.

### 6. Vérifier dans le navigateur
- `python manage.py runserver 127.0.0.1:8765 --noreload` en arrière-plan, compte de démonstration `awa` (mot de passe dans `.playwright-mcp/audit_p2.js`), page de la section en `/fr/` et `/en/`, à 1280 px et à 360 px, en thème clair puis sombre (`page.emulateMedia({ colorScheme: "dark" })`). Identifiant public de la section : `manage.py shell -c "from courses.models import Section; print(Section.objects.get(module__partie__formation__slug='electro', title_fr='<titre>').public_id)"`.
- Travaille dans un contexte de navigateur séparé (`page.context().browser().newContext(...)`) pour ne pas perdre une session PythonAnywhere ouverte dans la page principale ; `reducedMotion: "reduce"` et `javaScriptEnabled: false` se passent à `newContext`.
- Pour zoomer, retire l'en-tête collant et élargis la scène (`.fig-stage` à 1800 px) avant la capture.
- Contrôle : zéro erreur console ou CSP, aucun débordement (`scrollWidth > clientWidth`), relevé conforme aux littéraux à chaque repère, Lecture et Pause, curseur au clavier, figure figée sous `reduced-motion` et sans JavaScript.
- Lis les captures et zoome : chaque pièce repose sur une autre, chaque trait finit sur quelque chose, aucune surface nue (règles anatomy).
- Mesure CSS + JS de la page (< 60 Ko) et le poids de la page (< 200 Ko). Une section qui contient aussi un calculateur charge `calculators.js` (11,5 Ko) : avec un script de figure de 4,6 Ko, la page frôle 60 Ko (`05-coupure` : 59,6 Kio) ; signale-le.
- Arrête le serveur à la fin (PowerShell : `Get-NetTCPConnection -LocalPort 8765 -State Listen | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -Confirm:$false }`).

### 7. Clore
- `pytest` complet, `node --test "tools/figures/**/*.test.mjs"`, `python manage.py makemigrations --check --dry-run` : tout vert, sans aucun test ignoré non justifié.
- AGENTS.md : user story de la figure, ligne du registre et littéraux du modèle dans la modélisation, écart d'implémentation s'il y en a ; puis CLAUDE.md = son en-tête (4 lignes) + AGENTS.md à partir de la ligne 4, vérifié par `diff <(tail -n +7 AGENTS.md) <(tail -n +8 CLAUDE.md)`.
- Commits sur `develop` seulement si l'utilisateur le demande. En pratique une figure part en un `feat(courses)` (modèle, build, fichiers générés, registre, tests, carte, section, traductions : un commit plus fin aurait des tests rouges sans les fichiers générés), puis un `docs`. Déploiement : skill `deploy`.

## Rapport final
Dis ce qui a été vérifié et comment (nombre de tests, littéraux, captures), ce qui ne l'a pas été (audit de contraste, thème sombre, `--audit` du kit), et les compromis faits pour tenir le budget.
