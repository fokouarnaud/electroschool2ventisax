# AGENTS.md : Electro Acad Ventisax

> Source de vérité du projet. [CLAUDE.md](CLAUDE.md) en est la copie pour Claude Code ; en cas de divergence, AGENTS.md prime.

Plateforme de formation et d'évaluation en ligne inspirée des principes d'interface de Cisco NetAcad, forkée d'Acad Ventisax (dépôt `school2ventisax`). Première formation : électronique, Parties 1 à 3.
Hébergement visé : PythonAnywhere gratuit, compte `electroacadventisax` (https://electroacadventisax.pythonanywhere.com/fr/).

## Commandes utiles
| Commande | Usage |
|---|---|
| `python -m venv .venv` puis `.venv/Scripts/python -m pip install -r requirements-dev.txt` | Environnement local (Windows) |
| `.venv/Scripts/python -m pytest` | Toute la suite de tests (TDD : test rouge d'abord) |
| `.venv/Scripts/python manage.py makemigrations --check --dry-run` | Aucune migration oubliée |
| `.venv/Scripts/python manage.py import_content content/electro/formation.json` | Import idempotent du contenu (ne publie jamais) |
| `.venv/Scripts/python manage.py publish_reviewed` | Publie les questions relues en FR et en EN ; signale les incohérentes |
| `bash ~/electroschool2ventisax/deploy.sh` (console PythonAnywhere) | Pull, dépendances, migrations, import, publication des questions relues, collectstatic, check, rechargement |
| `DJANGO_DEBUG=0 DJANGO_SECRET_KEY=<clé de test> .venv/Scripts/python manage.py check --deploy` | Réglages de production |

## Sécurité (règle absolue)
- Aucun identifiant, mot de passe, jeton d'API, mot de passe d'application ni SECRET_KEY dans le dépôt, AGENTS.md et CLAUDE.md compris. Secrets dans `.env` (ignoré par git) et dans la configuration PythonAnywhere ; `.env.example` sans valeurs.
- Aucun texte, question, logo ni asset de NetAcad/Cisco : seuls les *principes d'interface* sont repris.
- `reference/electronic.pdf` (livre Wiley protégé) n'est jamais committé ni reproduit : il sert uniquement de plan pédagogique.

## Questions du grill (réponses stabilisées, 2026-10-18)
Les réponses Q1 à Q16 du grill d'Acad Ventisax (`school2ventisax/AGENTS.md`) restent valables sauf là où les réponses ci-dessous les modifient.

| # | Question | Réponse retenue |
|---|---|---|
| E1 | Point de départ du code ? | Fork de school2ventisax (architecture, tests, règles d'examen) |
| E2 | Droits sur le PDF ? | Contenu original : le livre sert de plan ; texte, exercices et schémas SVG rédigés de zéro, aucune phrase copiée |
| E3 | Périmètre de la Partie 1 ? | Chapitres 1 à 4, soit 4 modules : révision DC, diode, transistor, transistor en commutation |
| E4 | Extras NetAcad en v1 ? | Certificat PDF + badge, activités interactives, catalogue + auto-inscription, carnet de notes formateur |
| E5 | Certificat ? | ~~fpdf2~~ générateur PDF maison sans dépendance (voir E23), PDF produit à la demande (non stocké), numéro unique, page publique `/verify/<uuid>/`, badge SVG sur le profil |
| E6 | Activités interactives ? | Numérique avec tolérance (notée), appariement / glisser-déposer avec alternative clavier (noté), calculateurs dans le cours (non notés), zone cliquable sur schéma SVG (notée) ; JS vanilla + HTMX |
| E7 | Inscription ? | Catalogue public ; inscription libre aux cours ouverts ou par code de promotion ; mot de passe oublié par e-mail (Gmail SMTP) |
| E8 | Périmètre de Django Unfold ? | Back-office seul ; tableau, carnet de notes, annonces et dates limites du formateur dans le front |
| E9 | Modèle d'inscription ? | `Enrollment(user, formation, promotion facultative)` ; plusieurs formations par apprenant ; inscrits libres suivis par l'admin (« groupe ouvert ») |
| E10 | Règle du certificat ? | 1 certificat par partie dont l'examen est réussi (≥ 70 %, meilleure note) ; nom complet obligatoire ; badge par module terminé et par partie réussie |
| E11 | Échéances et annonces ? | Dates limites indicatives (marqueur « en retard », aucun blocage) ; annonces sur le tableau de bord, sans e-mail |
| E12 | Volume du contenu ? | Rédigé en FR puis traduit en EN. Par module : 6 à 8 sections, 15 questions de quiz (≥ 4 numériques, 2 interactives) et 12 d'examen ; 2 ou 3 schémas SVG par section ; brouillon jusqu'à la relecture |
| E13 | Notation des nouveaux types ? | Numérique : valeur + unité imposée + tolérance de 2 %, préfixes SI, virgule ou point, tout ou rien. Appariement : score partiel. Zone cliquable : tout ou rien. Valeurs fixes |
| E14 | Identité ? | « Electro Acad Ventisax », charte Ventisax déclinée avec un accent électronique (skill design-taste-frontend) ; mobile d'abord ; < 200 Ko par page |
| E15 | Carnet de notes ? | Détail de chaque tentative envoyée (réponse, juste/faux, temps passé), taux de réussite par question, export CSV ; les tentatives en cours ne sont jamais visibles |
| E16 | Observation ? | L'utilisateur se connecte lui-même à NetAcad ; Claude se connecte à acadventisax avec le compte apprenant ; principes d'interface seulement ; preuves dans `docs/observation/` |
| E17 | Qui déploie ? | Claude : première connexion à PythonAnywhere via Playwright MCP pour créer le jeton d'API (dans `.env`), puis déploiement par l'API et la console |
| E18 | Tests ? | TDD avec pytest-django (test rouge d'abord, tests de school2ventisax repris et adaptés, intrusion comprise) + parcours de bout en bout rejoués avec Playwright MCP avant chaque déploiement |
| E19 | Anti-abus de l'inscription ? | E-mail vérifié, champ piège à robots, limite par IP et par heure, purge des comptes non vérifiés après 7 jours |
| E20 | Pratique ? | 1 mini-projet original par module (consignes, schéma SVG, nomenclature, tableau de mesures), affiché, non noté |
| E21 | Expéditeur des e-mails ? | Boîte Gmail désignée par l'utilisateur ; adresse et mot de passe d'application dans `.env` uniquement |
| E23 | fpdf2 tire Pillow et fonttools (~40 Mo) : que faire ? (2026-10-18) | Mini-générateur PDF en Python pur dans `certificates/pdf.py` (Helvetica standard, WinAnsi) ; fpdf2 retiré des dépendances |
| E24 | Relecture des questions de la Partie 1 ? (2026-10-18) | Validée par le responsable du projet : les 108 questions sont marquées relues (FR et EN) et publiées par `publish_reviewed`, lancé à chaque déploiement |
| E25 | Suite du contenu ? (2026-10-18) | Partie 2 « Courant alternatif et filtres » = chapitres 5 à 7, 3 modules (M5 courant alternatif, M6 filtres RC et RL, M7 résonance) dans la même formation `electro` ; Partie 3 (chapitres 8 à 11) hors périmètre jusqu'à décision |
| E26 | Volume et niveau de la Partie 2 ? (2026-10-18) | Volume E12 inchangé ; aucun nombre complexe (Pythagore, tan/arctan, −3 dB ≈ 70,7 %) ; angles en degrés notés en numérique (unité « ° ») |
| E27 | Calculateurs et schémas de la Partie 2 ? (2026-10-18) | Trois calculateurs : réactance, fréquence de coupure, résonance ; `tools/schemas.py` étendu aux courbes (sinusoïdes, réponse en fréquence) |
| E28 | Matériel des mini-projets de la Partie 2 ? (2026-10-18) | Oscilloscope et générateur basse fréquence, plus une variante « multimètre seul » avec transformateur 230 V → 9 ou 12 V AC |
| E29 | Ordre entre parties et mise en ligne ? (2026-10-18) | Aucun verrou entre parties (conseil dans la description) ; relecture validée d'emblée : commit sur `develop`, questions publiées, fusion dans `main`, déploiement |
| E30 | Périmètre de la Partie 3 ? (2026-10-18) | Chapitres 8 à 11, 4 modules dans la formation `electro` : M8 amplificateurs à transistor, M9 oscillateurs, M10 transformateur, M11 alimentations (dossiers `p3/m8` à `p3/m11`) ; le chapitre 12 (test final) n'est pas repris, l'examen de la Partie 3 en tient lieu |
| E31 | Titre et ordre de la Partie 3 ? (2026-10-18) | « Amplification, oscillateurs et alimentations » / « Amplifiers, oscillators and power supplies » ; description conseillant de la suivre après les Parties 1 et 2, aucun verrou |
| E32 | Volume de la Partie 3 ? (2026-10-18) | E12 inchangé : 6 à 8 sections dont 1 mini-projet, 15 questions de quiz (≥ 4 numériques, ≥ 1 appariement, ≥ 1 sur schéma) et 12 d'examen par module, soit 108 questions ; 2 ou 3 schémas par section |
| E33 | Niveau mathématique de la Partie 3 ? (2026-10-18) | Règle E26 : aucun nombre complexe ; gain exprimé en rapport, pas de décibels au-delà de −3 dB ; formules : −RC/RE, −Rf/Rin, 1 + Rf/Rin, f = 1/(2π√(LC)), Ns/Np, Zp/Zs = (Np/Ns)², ondulation ≈ I/(f·C) |
| E34 | Sections de M8 ? (2026-10-18) | Rôle de l'amplificateur et gain ; polarisation stable (pont de base, résistance d'émetteur) ; gain de l'émetteur commun ; émetteur suiveur ; analyser un amplificateur (droite de charge, point de repos) ; JFET amplificateur ; AOP inverseur et non inverseur ; mini-projet |
| E35 | Sections de M9, M10 et M11 ? (2026-10-18) | M9 : rétroaction et conditions d'oscillation, Colpitts, Hartley, Armstrong, quartz et oscillateur RC à AOP (ouverture), concevoir et dépanner, mini-projet. M10 : principe et rapport de transformation, tensions et courants, puissance et rendement, adaptation d'impédance, transformateurs en communication, mini-projet. M11 : rappel du redressement (renvoi à M2), pont de diodes et valeurs crête, lissage, ondulation, régulation Zener (renvoi à M2), régulateur intégré 78xx, mini-projet |
| E36 | Sécurité du secteur ? (2026-10-18) | Aucun travail côté 230 V : transformateur moulé ou adaptateur mural 230 V → 9 ou 12 V AC, mesures au secondaire seulement, consigne de sécurité en tête de chaque mini-projet |
| E37 | Variantes des mini-projets de la Partie 3 ? (2026-10-18) | Règle E28 pour chaque module : variante oscilloscope + générateur basse fréquence et variante « multimètre seul » (M9 : oscillateur basse fréquence vérifié par un buzzer ou une LED) |
| E38 | Calculateurs de la Partie 3 ? (2026-10-18) | `[[calc:gain]]` (émetteur commun, AOP inverseur et non inverseur), `[[calc:transformer]]` (rapport, tension et courant au secondaire), `[[calc:ripple]]` (ondulation et condensateur de lissage) ; `[[calc:resonance]]` réutilisé en M9 ; CSS + JS du projet toujours < 60 Ko |
| E39 | Relecture et mise en ligne de la Partie 3 ? (2026-10-18) | Comme E29 : questions relues d'emblée, commit sur `develop`, fusion dans `main`, `deploy.sh`, parcours de fumée en production avec le certificat de la Partie 3 |
| E40 | Documentation ? (2026-10-18) | Partie 3 sortie du hors scope dans AGENTS.md et CLAUDE.md ; description de la formation « Du courant continu aux amplificateurs, oscillateurs et alimentations… » |
| E41 | Signe du gain ? (2026-10-18) | Chaque énoncé précise « en valeur absolue » ou « avec son signe » (valeur négative attendue, déjà acceptée par la notation) ; gain sans unité (unité vide, comme β et Q) |
| E42 | Schémas de la Partie 3 ? (2026-10-18) | `tools/schemas.py` étendu : AOP, transformateur, quartz, pont de diodes, régulateur 78xx, buzzer ; courbes de tension lissée avec ondulation, d'entrée et sortie en opposition de phase, de démarrage d'une oscillation |
| E43 | Questions sur schéma de la Partie 3 ? (2026-10-18) | Une par module : M8 la résistance qui fixe le gain, M9 le réseau de rétroaction, M10 le secondaire, M11 le condensateur de lissage |
| E44 | Découpage des commits ? (2026-10-18) | `feat(courses)` calculateurs (TDD), `feat(content)` Partie 3, `style(ui)` après l'audit `audit_p3.js`, `docs` ; puis fusion dans `main` et déploiement |
| E45 | Rang des parties et des modules ? (2026-10-18) | Rang unique : une partie par rang dans sa formation, un module par rang dans sa partie (contraintes `unique_partie_order` et `unique_module_order`, migration `courses/0005`), pour que trois parties et leurs colonnes « Examen P1, P2, P3 » restent dans un ordre sans ambiguïté |
| E22 | Dépôt et disque ? | GitHub `fokouarnaud/electroschool2ventisax` ; `develop` → `main` (suivi par le serveur) ; < 150 Mo de disque ; 1 sauvegarde SQLite quotidienne |

## GOALS

### 1. Objectifs fonctionnels prioritaires
1. **Lecteur de cours** : Formation → Partie → Module → Section, sommaire repliable, sections vues cochées, barre de progression par module et par partie.
2. **Contenu Partie 1 « Courant continu et semi-conducteurs »** (en ligne) : 4 modules originaux (révision DC, diode, transistor, transistor en commutation), FR et EN, schémas SVG, 1 mini-projet par module.
3. **Contenu Partie 2 « Courant alternatif et filtres »** (chapitres 5 à 7 du livre, servant uniquement de plan) : 3 modules originaux dans la même formation `electro`, à la suite de la Partie 1 :
   - **M5 Le courant alternatif** : sinusoïde, valeurs crête, crête à crête et efficace, résistance en alternatif, condensateur et réactance Xc, bobine et réactance XL, générateur et oscilloscope, mini-projet ;
   - **M6 Les filtres RC et RL** : rappel de trigonométrie, RC série et impédance, passe-bas, passe-haut, fréquence de coupure et −3 dB, déphasage, filtres RL, mini-projet ;
   - **M7 La résonance** : LC série, LC parallèle, courbe de réponse, bande passante et facteur Q, ouverture vers les oscillateurs, mini-projet.
   Volume identique à la Partie 1 (E12) ; relecture validée par le responsable du projet, questions publiées au déploiement.
4. **Contenu Partie 3 « Amplification, oscillateurs et alimentations »** (chapitres 8 à 11 du livre, servant uniquement de plan, E30) : 4 modules originaux dans la même formation `electro`, à la suite de la Partie 2 :
   - **M8 Les amplificateurs à transistor** : rôle de l'amplificateur et gain, polarisation stable par pont de base et résistance d'émetteur, gain de l'émetteur commun, émetteur suiveur, analyse (droite de charge, point de repos), JFET amplificateur, AOP inverseur et non inverseur, mini-projet ;
   - **M9 Les oscillateurs** : rétroaction et conditions d'oscillation, Colpitts, Hartley, Armstrong, quartz et oscillateur RC à AOP en ouverture, concevoir et dépanner, mini-projet ;
   - **M10 Le transformateur** : principe et rapport de transformation, tensions et courants, puissance et rendement, adaptation d'impédance, transformateurs en communication, mini-projet ;
   - **M11 Les alimentations** : rappel du redressement (renvoi à M2), pont de diodes et valeurs crête, lissage par condensateur, ondulation, régulation Zener (renvoi à M2), régulateur intégré 78xx, mini-projet.
   Volume E12 (108 questions), relues d'emblée et publiées au déploiement (E39) ; une question sur schéma par module (E43).
5. **Quiz de module** : entraînement illimité, correction et explication après envoi ; types QCM une/plusieurs réponses, vrai/faux, **numérique avec unité et tolérance** (angles en degrés « ° » compris), **appariement / glisser-déposer**, **zone cliquable sur schéma**.
6. **Calculateurs interactifs** dans les sections, non notés : loi d'Ohm, diviseur de tension, code couleur des résistances, polarisation (Partie 1) ; réactance Xc/XL, fréquence de coupure RC/RL, fréquence de résonance LC (Partie 2) ; gain d'un amplificateur (émetteur commun, AOP), transformateur (rapport, tension et courant), ondulation et condensateur de lissage (Partie 3), la résonance LC servant aussi aux oscillateurs.
7. **Examen de partie** (un par partie) : banque séparée, 70 % pour réussir, 3 tentatives, 60 min chronométrées côté serveur, mélange, sauvegarde au clic, reprise après coupure, envoi automatique, meilleure note retenue.
8. **Catalogue et inscription** : catalogue public ; inscription libre aux formations ouvertes ou par code de promotion ; e-mail vérifié ; mot de passe oublié par e-mail ; un apprenant peut suivre plusieurs formations.
9. **Certificat et badges** : certificat PDF par partie réussie (Parties 1, 2 et 3), numéro unique vérifiable sur `/verify/<uuid>/` ; badges par module terminé et par partie réussie.
10. **Espace formateur** (front, mobile) : tableau apprenants × modules de ses promotions, carnet de notes détaillé par tentative et par question, taux de réussite par question, export CSV, annonces et dates limites indicatives.
11. **Back-office Django Unfold** : comptes, promotions, codes de promotion, contenu, relecture et publication des questions (refusée si FR ou EN non relu), réglage des examens.
12. **Interface** : bilingue `/fr/` et `/en/`, patterns NetAcad, charte Ventisax déclinée « électronique », mobile d'abord.

### 2. Contraintes techniques
- **Python** le plus récent proposé par PythonAnywhere ; **Django 5.2 LTS** ; **SQLite** (un seul fichier, sauvegarde quotidienne, 1 copie gardée).
- Code **forké de school2ventisax** : gabarits serveur + **HTMX vendoré**, **JS vanilla**, CSS écrit à la main ; aucun CDN, aucun Node, aucune SPA.
- **Dépendances de production** limitées à : `django`, `django-modeltranslation`, `markdown`, `bleach`, `django-unfold` (fpdf2 retiré, E23). Toute autre dépendance demande un accord explicite. Développement : `pytest`, `pytest-django`.
- **TDD obligatoire** (skill test-driven-development) : test rouge avant chaque règle métier (dont l'unité « ° » et les nouveaux calculateurs) ; suite pytest verte, tests d'intrusion compris ; parcours Playwright MCP rejoués avant chaque déploiement.
- **PythonAnywhere gratuit** (compte `electroacadventisax`) : quota de 512 Mo, **cible < 150 Mo** (code + venv + base + médias) ; une seule web app ; pas de tâche planifiée ; internet sortant sur liste blanche ; e-mail sortant par **Gmail SMTP** seulement.
- **Poids** : < 200 Ko par page à la première visite ; CSS + JS du projet < 60 Ko (nouveaux calculateurs compris) ; schémas en SVG, images éventuelles en WebP ; pas de Pillow.
- **i18n** : `i18n_patterns` (`/fr/` par défaut, `/en/`), gettext pour l'interface, modeltranslation pour le contenu, repli sur le FR.
- **Contenu versionné** : `content/electro/` (manifeste JSON, Markdown fr/en, `questions.json` par module ; Partie 2 dans `p2/m5` à `p2/m7`, Partie 3 dans `p3/m8` à `p3/m11`, numérotation continue), importé par `import_content` (idempotent).
- **Niveau mathématique de la Partie 2** : aucun nombre complexe ; impédance par Pythagore (Z = √(R² + X²)), déphasage par tan/arctan, décibels limités à « −3 dB ≈ 70,7 % ».
- **Niveau mathématique de la Partie 3** (E33) : même règle ; gain en rapport (sans décibels), AOP par −Rf/Rin et 1 + Rf/Rin, oscillateurs par f = 1/(2π√(LC)), transformateur par Ns/Np et (Np/Ns)², ondulation ≈ I/(f·C) ; chaque énoncé de gain précise « en valeur absolue » ou « avec son signe » (E41).
- **Schémas générés** par `tools/schemas.py` (symboles CEI, version anglaise automatique), étendu aux courbes (sinusoïdes, déphasage, réponse en fréquence sur axe logarithmique, résonance) puis aux symboles et courbes de la Partie 3 (AOP, transformateur, quartz, pont de diodes, régulateur 78xx, buzzer ; tension lissée et ondulation, opposition de phase, démarrage d'oscillation) ; jamais retouchés à la main.
- **Mini-projets des Parties 2 et 3** : consignes à l'oscilloscope et au générateur basse fréquence, avec une variante « multimètre seul » (transformateur 230 V → 9 ou 12 V AC).
- **Sécurité du secteur (Partie 3, E36)** : aucun montage ni mesure côté 230 V ; transformateur moulé ou adaptateur mural seulement, mesures au secondaire, consigne de sécurité en tête de chaque mini-projet.
- **Parties non bloquantes** : les Parties 2 et 3 sont accessibles sans avoir réussi les précédentes ; leur description conseille de les suivre dans l'ordre.
- **Sécurité** : DEBUG=False et HTTPS en production, CSRF, CSP sans script en ligne, Markdown nettoyé par bleach, identifiants publics UUID, verrouillage anti force brute, limitation des inscriptions, secrets dans `.env`.
- **Livraison** : commits sur `develop`, questions relues rendues publiques, fusion dans `main` (suivie par le serveur), puis `deploy.sh` (pull, install, migrate, import, publication des questions relues, compilemessages, collectstatic, check --deploy, reload).
- **Droits** : contenu 100 % original ; le PDF de référence n'est jamais committé ni cité textuellement.

### 3. Périmètre strictement hors scope
- Reproduction du texte, des figures, des exercices ou des projets du livre *Complete Electronics Self-Teaching Guide* ; tout texte, question, logo ou asset de NetAcad/Cisco.
- **Chapitre 12 du livre (test final) et toute Partie 4**, jusqu'à nouvelle décision : l'examen de la Partie 3 tient lieu de bilan.
- Nombres complexes et calcul de décibels au-delà de −3 dB dans les Parties 2 et 3 (gain exprimé en rapport).
- Tout montage ou toute mesure côté secteur 230 V dans les mini-projets.
- Simulateur de circuits (type Packet Tracer / SPICE) et laboratoires virtuels.
- Valeurs numériques aléatoires par tentative (questions paramétrées) ; réponse libre rédigée ; correction manuelle.
- Évaluation pratique notée, saisie des mesures dans l'app, dépôt de fichiers par les apprenants.
- Verrou entre parties ; parcours séquentiel bloquant entre sections ; dates limites bloquantes.
- Annonces ou notifications par e-mail ; messagerie, forum, chat.
- Suivi en direct des examens en cours.
- SSO, connexion Google/Cisco, base partagée avec Acad Ventisax ou ventisax.
- Paiement, cours payants, Open Badges / badges exportables.
- Mode hors ligne / PWA, application mobile native.
- Captcha tiers ou tout service externe autre que Gmail SMTP.

## Guide de style de l'interface (2026-10-18)
Skill design-taste-frontend, lecture : interface produit d'une plateforme de formation, apprenants sur Android d'entrée de gamme et formateurs sur ordinateur, langage sobre et fiable. Réglages : VARIANCE 4, MOTION 3, DENSITY 5. Les règles « landing page » du skill (hero, mur de logos, bento) ne s'appliquent pas.
- **Système conservé d'Acad Ventisax** (mode « redesign, préserver ») : jetons navy/teal dans `static/acad/css/app.css`, **un seul accent (teal)**, boutons en pilule, panneaux 20px, champs et choix 14px, mode sombre par `prefers-color-scheme`. CSS écrit à la main, aucun framework, aucune police externe.
- **Marque** : « Electro Acad Ventisax » (mot « Ventisax » en teal) ; sous 520px, le logo seul ; sous 420px, le bouton « Créer un compte » de l'en-tête disparaît (présent dans les pages).
- **Icônes** : Tabler Icons 3.31.0 (MIT) uniquement, format du projet (`templates/icons/*.svg`, trait 1,75, `aria-hidden`) ; aucune icône dessinée à la main.
- **Formulaires** : `templates/includes/field.html` (libellé au-dessus, aide puis erreur en dessous, astérisque pour les champs requis) ; pages d'un seul panneau : `templates/accounts/_single_panel.html`.
- **Formateur** : sous-navigation commune `templates/progress/_trainer_nav.html` (Apprenants, Questions, Annonces, Dates limites).
- **Questions interactives** (`static/acad/js/interactions.js`, amélioration progressive) : zones cliquables posées sur le schéma en % du viewBox, toujours visibles (contour pointillé) ; appariement par listes déroulantes, étiquettes déplaçables en plus à la souris (masquées au toucher).
- **Calculateurs** (`static/acad/js/calculators.js`) : chargés seulement sur les sections qui en contiennent ; libellés traduits passés par un élément caché à attributs `data-` (aucun script en ligne).
- **Typographie** : aucun tiret cadratin ni demi-cadratin visible ; deux-points intégrés aux chaînes traduites (« Votre réponse : » / « Your answer: »).
- **Validation visuelle** : script Playwright `.playwright-mcp/shots.js` (dossier ignoré par git) sur 1280px et 360px, trois rôles, contrôles automatiques : erreurs console et CSP, débordement horizontal (`clientWidth`), boutons sur deux lignes, poids transféré. Dernier passage : 0 erreur, 0 débordement, page la plus lourde 66 Ko (tentative avec HTMX, non compressé).

### Audit graphique (2026-10-18)
Script `.playwright-mcp/audit.js` : 12 écrans, 360 et 1280 px, thèmes clair et sombre. Résultat : contraste AA sans défaut, aucun débordement, aucune erreur console, `lang` correct, toutes les images avec texte alternatif, pages de 6 à 84 Ko à la première visite (quiz avec HTMX : 84 Ko).
- **Schémas du cours** : ajustés à la largeur et liés à leur fichier pleine taille (`a.figure-zoom`, ajouté par `courses/rendering.py`) ; sur téléphone, un toucher ouvre le SVG, agrandi à deux doigts. Le défilement horizontal a été essayé puis écarté (schéma paraissant coupé). Les SVG portent `width`/`height` (dimensions intrinsèques).
- **Examen verrouillé** : modules à terminer en liste de liens numérotés avec badge « À terminer » (masqué sous 400 px), et non plus en cercles ressemblant à des choix de réponse.
- **Connexion** : « Mot de passe oublié ? » et « Créer un compte » deviennent deux cibles de 44 px sous le bouton, au lieu de deux petits liens accolés.
- **Cibles tactiles** : titre de formation du catalogue (44 px) et liens de tentatives du suivi (36 px). Exceptions assumées : le lien du pied de page (dans une phrase) et les zones des questions sur schéma, doublées par des boutons radio de 44 px.
- **Budget CSS + JS < 60 Ko** : précisé comme portant sur les fichiers du projet (48 Ko non compressés) ; HTMX vendoré (51 Ko, 16 Ko compressé), imposé par Q13 et déjà présent dans Acad Ventisax, n'y est pas compté.

- **Partie 2 (2026-10-18)** : script `.playwright-mcp/audit_p2.js` (11 écrans : fiche du catalogue, tableau de bord, module, sections à calculateur, section anglaise, mini-projet, examen, quiz et résultat de M6), 360 et 1280 px, thèmes clair et sombre : aucun défaut de contraste, aucun débordement, aucune erreur console, pages de 43 à 126 Ko à la première visite (quiz de M6 : 126 Ko). Ajustements : `.course + .course` sépare les parties sur le tableau de bord ; `.partie-desc` porte la description d'une partie ; dans les tableaux du cours, en-têtes et première colonne ne se coupent plus (le tableau défile dans son cadre) ; les calculateurs n'affichent pas deux fois la consigne ; l'aide d'une question en degrés parle d'angle et non de préfixes SI ; le tableau formateur abrège les examens en « Examen P1 / P2 » avec une légende, comme les modules ; les sources des schémas de circuit portent leur valeur à l'intérieur de la boucle. L'audit des 12 écrans de la Partie 1 reste sans régression.
- **Partie 3 (2026-10-18)** : script `.playwright-mcp/audit_p3.js` (13 écrans : fiche du catalogue, tableau de bord à trois parties, module M8, sections à calculateur gain, transformateur et ondulation, section anglaise du Colpitts, mini-projet de M11, examen, quiz et résultat de M8, tableau formateur, dates limites), 360 et 1280 px, thèmes clair et sombre : aucun défaut de contraste, aucun débordement, aucune erreur console, pages de 45 à 129 Ko à la première visite (quiz de M8 : 129 Ko). Ajustement : avec onze modules et trois examens, le tableau formateur défilait à 1280 px et coupait la colonne « Tentatives » ; les colonnes M1 à M11 portent la classe `mod` (rembourrage horizontal réduit, contenu centré) et le tableau tient en entier. Tableau de bord : chaque carte d'examen nomme sa partie (« Examen de la Partie 3 », « Part 3 exam ») et la formation n'est plus répétée au-dessus de chaque partie (`{% ifchanged %}`). Revue écran par écran : la fiche du catalogue et le tableau de bord numérotent les parties (« Partie 3 : », classe `partie-num`), puisque les descriptions renvoient aux « Parties 1 et 2 » ; le rond d'une section non lue prend la même emprise que la coche (`.section-list .dot-todo`) ; sous 400 px, le chevron des modules à terminer reste à droite quand le badge est masqué ; dans les calculateurs, les listes déroulantes occupent toute la largeur (`field-wide`) pour que « Double alternance (100 Hz) » ne soit pas tronqué. Gabarits partiels : `templates/includes/partie_heading.html` (titre numéroté d'une partie, partagé par la fiche du catalogue et le tableau de bord) et `templates/courses/_calc_labels.html` (libellés traduits des dix calculateurs, sortis de `section_detail.html`). Liste de contrôle du skill design-taste-frontend mesurée écran par écran par `.playwright-mcp/preflight_p3.js` (13 écrans, 360 et 1280 px) : zéro tiret long, aucun libellé de bouton sur deux lignes, un seul rayon de bouton (pilule), un seul accent (teal ; jaune et rouge réservés aux états), aucun champ sans libellé, aucune animation, aucun débordement ; « Ce qu'il reste à faire » répété sur le tableau de bord mène à trois examens différents, chacun dans sa carte. Exceptions inchangées : lien du pied de page et zones des questions sur schéma, doublées par des boutons radio de 44 px. L'audit de la Partie 2 reste sans régression.

## PRD

### Personas
- **Apprenant inscrit en promotion** : stagiaire du centre, sur smartphone Android d'entrée de gamme, données mobiles limitées, connexion instable ; rejoint sa promotion avec le code fourni par le formateur.
- **Apprenant libre** : visiteur qui découvre le catalogue public et s'inscrit seul à une formation ouverte ; suivi par l'admin dans le « groupe ouvert ».
- **Formateur** : intervenant du centre ; suit ses promotions (carnet de notes, annonces, dates limites), relit et publie les questions.
- **Admin** : responsable de la plateforme ; gère formations, promotions, comptes, contenu et réglages d'examen dans le back-office Unfold.
- **Vérificateur** (employeur, jury) : personne non connectée qui contrôle l'authenticité d'un certificat par son numéro.

### User Stories
Chaque story porte une étiquette : **[B]** règle métier backend (modèles, services, vues testées en pytest), **[F]** interface (gabarits, JS, style). Les [B] sont développées en TDD strict ; les [F] sont validées par les parcours Playwright MCP.

**Catalogue, inscription et compte**
- US-01 [B][F] : En tant que visiteur, je consulte le catalogue public des formations ouvertes (titre, description, parties, durée) en /fr/ ou /en/, sans être connecté.
- US-02 [B] : En tant que visiteur, je crée un compte (identifiant, e-mail, prénom, nom, mot de passe) ; le compte reste inactif tant que je n'ai pas cliqué le lien de vérification reçu par e-mail.
- US-03 [B] : En tant que plateforme, je rejette une inscription dont le champ piège est rempli, et je bloque une IP au-delà de N inscriptions par heure.
- US-04 [B] : En tant qu'admin, les comptes non vérifiés depuis plus de 7 jours sont supprimés automatiquement.
- US-05 [B] : En tant qu'apprenant connecté, je m'inscris en un clic à une formation ouverte (inscription libre, sans promotion).
- US-06 [B] : En tant qu'apprenant connecté, je saisis un code de promotion pour rejoindre cette promotion et sa formation ; un code inconnu ou désactivé est refusé.
- US-07 [B] : En tant qu'apprenant, je suis inscrit à plusieurs formations et je les retrouve toutes sur mon tableau de bord avec ma progression en %.
- US-08 [B] : En tant qu'utilisateur, je me connecte avec mon identifiant et mon mot de passe ; 5 échecs en 15 min verrouillent l'identifiant.
- US-09 [B] : En tant qu'utilisateur, je réinitialise mon mot de passe par un lien envoyé par e-mail (Gmail SMTP), valable une durée limitée, sans révéler si l'adresse existe.
- US-10 [B][F] : En tant qu'utilisateur, je change de langue à tout moment, même pendant un examen, sans perdre ma tentative.

**Lecteur de cours et pratique**
- US-11 [B][F] : En tant qu'apprenant inscrit, je navigue librement entre modules et sections grâce à un sommaire repliable ; les sections vues sont cochées ; un non-inscrit n'accède pas au contenu (il est renvoyé au catalogue).
- US-12 [B][F] : En tant qu'apprenant, je lis une section (texte, schémas SVG) confortablement sur mobile ; elle est marquée vue.
- US-13 [F] : En tant qu'apprenant, j'utilise dans les sections des calculateurs (loi d'Ohm, diviseur de tension, code couleur des résistances, polarisation) qui ne sont pas notés.
- US-14 [B][F] : En tant qu'apprenant, je consulte le mini-projet pratique de chaque module (consignes, schéma, nomenclature, tableau de mesures imprimable) et je télécharge ses annexes.

**Quiz, examen et notation**
- US-15 [B] : En tant qu'apprenant, je passe le quiz d'un module sans limite ; après envoi, je vois la correction et l'explication de chaque question.
- US-16 [B] : En tant qu'apprenant, je réponds à une question numérique en saisissant une valeur (virgule ou point, préfixes SI p n µ m k M G, unité facultative mais vérifiée si saisie) ; elle est juste si l'écart relatif est inférieur ou égal à la tolérance (2 % par défaut).
- US-17 [B][F] : En tant qu'apprenant, je réponds à une question d'appariement par glisser-déposer ou au clavier ; mon score est la part de paires justes.
- US-18 [B][F] : En tant qu'apprenant, je réponds à une question sur schéma en cliquant une zone ; c'est juste si la zone cliquée est la bonne.
- US-19 [B] : En tant qu'apprenant, je lance l'examen de partie quand tous ses modules sont terminés ; sinon je vois ce qui manque.
- US-20 [B] : En tant qu'apprenant, je passe l'examen avec un chrono serveur ; chaque réponse est sauvegardée au clic avec le temps passé sur la question.
- US-21 [B] : En tant qu'apprenant, après une coupure, je reprends mon examen avec le temps restant réel ; à l'heure limite, il est envoyé automatiquement avec les réponses déjà données.
- US-22 [B] : En tant qu'apprenant, je vois mon score global, le score par module, réussi / échoué et les tentatives restantes (sur 3).

**Certificat et badges**
- US-23 [B] : En tant qu'apprenant, je reçois un badge quand je termine un module, et un badge quand je réussis l'examen d'une partie.
- US-24 [B] : En tant qu'apprenant ayant réussi l'examen d'une partie (≥ 70 %), j'obtiens un certificat avec un numéro unique ; si mon nom complet n'est pas renseigné, on me demande de le compléter d'abord.
- US-25 [B] : En tant qu'apprenant, je télécharge mon certificat en PDF (généré à la demande, jamais stocké) ; seul son titulaire ou le personnel peut le télécharger.
- US-26 [B] : En tant que vérificateur, j'ouvre `/verify/<numéro>/` sans compte et je vois le nom, la partie, la date et la mention « valide » ; un numéro inconnu renvoie « certificat introuvable » (404).

**Formateur**
- US-27 [B][F] : En tant que formateur, je vois un tableau apprenants × modules pour mes promotions seulement (progression, meilleur score d'examen, tentatives, marqueur « en retard »).
- US-28 [B] : En tant que formateur, j'ouvre le détail d'une tentative envoyée d'un apprenant de mes promotions : chaque question, la réponse donnée, juste ou fausse, le temps passé ; une tentative en cours m'est refusée.
- US-29 [B] : En tant que formateur, je vois le taux de réussite de chaque question sur mes promotions, pour repérer les questions mal posées.
- US-30 [B] : En tant que formateur, j'exporte le carnet de notes en CSV (formules de tableur neutralisées).
- US-31 [B] : En tant que formateur, je publie une annonce pour une de mes promotions ; ses apprenants la voient sur leur tableau de bord, les autres non.
- US-32 [B] : En tant que formateur, je fixe une date limite (quiz d'un module ou examen d'une partie) pour une de mes promotions ; elle est indicative : rien n'est bloqué, mais un apprenant qui n'a pas fini à temps est marqué « en retard ».
- US-33 [B] : En tant que formateur, je relis les questions en brouillon (fr et en) dans le back-office et je les publie ; la publication est refusée si une langue n'est pas relue ou si la question est incohérente avec son type.

**Admin**
- US-34 [B] : En tant qu'admin, je gère dans le back-office Unfold les formations (dont l'indicateur « ouverte au catalogue »), les promotions, leurs formateurs et leur code (régénérable, désactivable).
- US-35 [B] : En tant qu'admin, j'importe une liste d'apprenants depuis un CSV dans une promotion (mots de passe générés).
- US-36 [B] : En tant qu'admin, je vois les apprenants libres (sans promotion) dans le « groupe ouvert » de chaque formation.
- US-37 [B] : En tant qu'admin, j'importe ou je mets à jour le contenu (cours, questions de tous types) depuis `content/electro/` avec une commande idempotente.
- US-38 [B] : En tant qu'admin, je règle un examen (seuil, tentatives, durée, questions par module) ; les valeurs NetAcad sont proposées par défaut.
- US-39 [B] : En tant qu'admin, une sauvegarde quotidienne de la base est faite automatiquement, et seule la plus récente est gardée.

**Partie 2 « Courant alternatif et filtres »**
- US-40 [B][F] : En tant qu'apprenant inscrit à la formation Électronique, je vois la Partie 2 (modules M5 Le courant alternatif, M6 Les filtres RC et RL, M7 La résonance) dans le sommaire et je la suis sans avoir réussi l'examen de la Partie 1 ; sa description me conseille de la suivre après la Partie 1.
- US-41 [B] : En tant qu'apprenant, je réponds à une question numérique en degrés (« 45° », « 45 ° », « -63,4° », virgule ou point) ; elle est juste dans la tolérance ; une autre unité saisie la rend fausse ; aucun préfixe SI n'est appliqué aux degrés dans la correction affichée (« 63,4° »).
- US-42 [F] : En tant qu'apprenant, j'utilise dans les sections de la Partie 2 trois calculateurs non notés : réactance (Xc ou XL selon f), fréquence de coupure (RC ou RL), fréquence de résonance (LC) ; utilisables au clavier, en FR et en EN.
- US-43 [B][F] : En tant qu'apprenant, je consulte le mini-projet de chaque module de la Partie 2 avec deux variantes de mesure : oscilloscope et générateur basse fréquence, ou multimètre seul avec un transformateur 230 V → 9 ou 12 V AC (consigne de sécurité en tête).
- US-44 [B] : En tant qu'apprenant ayant terminé M5, M6 et M7, je passe l'examen de la Partie 2 (mêmes règles que la Partie 1) ; s'il est réussi, j'obtiens un badge de partie et un second certificat, distinct de celui de la Partie 1, vérifiable sur `/verify/<numéro>/`.
- US-45 [B] : En tant qu'admin, j'importe la Partie 2 avec `import_content` (idempotent, deux passages = même état) ; les garde-fous du contenu vérifient p1 et p2 (fichiers FR et EN, volumes E12, schémas référencés existants).
- US-46 [B] : En tant que responsable, les 81 questions de la Partie 2, relues en FR et en EN, sont publiées par `publish_reviewed` au déploiement ; une question incohérente est signalée et reste en brouillon.
- US-47 [B][F] : En tant que formateur, mon tableau, mon carnet de notes, le taux de réussite par question et l'export CSV couvrent aussi M5 à M7 et l'examen de la Partie 2, sans changement de code.

**Partie 3 « Amplification, oscillateurs et alimentations »**
- US-48 [B][F] : En tant qu'apprenant inscrit à la formation Électronique, je vois la Partie 3 (M8 Les amplificateurs à transistor, M9 Les oscillateurs, M10 Le transformateur, M11 Les alimentations) dans le sommaire et sur mon tableau de bord, et je la suis sans avoir réussi les examens des Parties 1 et 2 ; sa description me conseille de la suivre après elles.
- US-49 [B] : En tant qu'apprenant, je réponds à une question de gain sans unité (« 10 », « -10 », « 4,7 ») ; si l'énoncé demande le gain « en valeur absolue », −10 est faux quand 10 est attendu ; s'il le demande « avec son signe », seule la valeur signée est juste ; une unité saisie (« 10 V ») rend la réponse fausse.
- US-50 [F] : En tant qu'apprenant, j'utilise dans les sections de la Partie 3 trois calculateurs non notés : gain (émetteur commun −RC/RE, AOP inverseur −Rf/Rin, AOP non inverseur 1 + Rf/Rin), transformateur (Np, Ns, Up → Us, et courant au secondaire), ondulation (I, f, C → ΔU, ou ΔU → C) ; ils s'utilisent au clavier, en FR et en EN ; en M9, le calculateur de résonance LC donne la fréquence d'un oscillateur.
- US-51 [B] : En tant qu'apprenant, je réponds dans chaque module de la Partie 3 à une question sur schéma : M8 la résistance qui fixe le gain, M9 le réseau de rétroaction, M10 l'enroulement secondaire, M11 le condensateur de lissage ; tout ou rien, comme les autres questions sur schéma.
- US-52 [B][F] : En tant qu'apprenant, je consulte le mini-projet de chaque module de la Partie 3 avec deux variantes de mesure (oscilloscope et générateur basse fréquence, ou multimètre seul) ; en M10 et M11, le mini-projet commence par la consigne de sécurité : aucun montage ni mesure côté 230 V, transformateur moulé ou adaptateur mural 230 V → 9 ou 12 V AC, mesures au secondaire seulement.
- US-53 [B] : En tant qu'apprenant ayant terminé M8, M9, M10 et M11, je passe l'examen de la Partie 3 (70 %, 3 tentatives, 60 min) ; s'il est réussi, j'obtiens un badge de partie et un troisième certificat, distinct de ceux des Parties 1 et 2, vérifiable sur `/verify/<numéro>/` ; tant qu'un module manque, je vois lequel.
- US-54 [B] : En tant qu'admin, j'importe la Partie 3 avec `import_content` (idempotent, deux passages = même état) ; les garde-fous du contenu vérifient p1, p2 et p3 (fichiers FR et EN, volumes E12, schémas référencés existants, calculateurs présents, variantes et sécurité des mini-projets, énoncés de gain précisant valeur absolue ou signe).
- US-55 [B] : En tant que responsable, les 108 questions de la Partie 3, relues en FR et en EN, sont publiées par `publish_reviewed` au déploiement ; une question incohérente est signalée et reste en brouillon.
- US-56 [B][F] : En tant que formateur, mon tableau (« Examen P3 » abrégé avec sa légende), mon carnet de notes, le taux de réussite par question, les dates limites et l'export CSV couvrent aussi M8 à M11 et l'examen de la Partie 3, sans changement de code.
- US-57 [B] : En tant que visiteur, je vois au catalogue la description de la formation mise à jour (« Du courant continu aux amplificateurs, oscillateurs et alimentations… ») et les trois parties avec leur description, en FR et en EN.

### Modélisation logique des données
`*` = champ traduit (fr/en) par modeltranslation, avec repli sur le fr. 🆕 = entité nouvelle, ✏️ = entité modifiée par rapport à school2ventisax.
Formation, Partie, Module, Section, Question, Choice, MatchPair, Attempt, Certificate et Promotion portent un `public_id` (UUID v4, unique, non modifiable) : c'est le seul identifiant exposé (URL, formulaires, ancres). Les clés entières restent internes.

| Entité | Attributs clés | Relations / contraintes |
|---|---|---|
| ✏️ **User** (personnalisé) | username, first_name, last_name, email, role ∈ {learner, trainer, admin}, email_verified, date_joined | trainer et admin donnent `is_staff` ; le champ `promotion` de school2ventisax est remplacé par Enrollment ; `is_active` = faux tant que l'e-mail n'est pas vérifié (inscription publique) ; e-mail unique quand il est renseigné |
| 🆕 **Enrollment** | enrolled_at, source ∈ {catalog, code, import, admin} | FK User (apprenant), FK Formation, FK Promotion (null = groupe ouvert) ; unique (user, formation) ; la promotion, si présente, appartient à la même formation |
| ✏️ **Promotion** | name, start_date, join_code (unique, 8 caractères sans ambiguïté), join_code_active | FK Formation ; M2M trainers (role = trainer) |
| ✏️ **Formation** | title*, slug, description*, order, is_open | 1-N Partie ; `is_open` = visible au catalogue et ouverte à l'inscription libre |
| ✏️ **Partie** | title*, description*, order, slug | FK Formation ; 1-1 Assessment (examen) |
| **Module** | title*, order, duration_hours, competence*, evaluation_note* | FK Partie ; 1-1 Assessment (quiz) |
| **Section** | title*, order, kind ∈ {content, practical}, body_md* | FK Module ; HTML rendu et nettoyé par bleach |
| **Annexe** | title*, file | FK Section (practical) |
| ✏️ **Question** | prompt*, explanation*, qtype ∈ {single, multiple, truefalse, numeric, matching, hotspot}, usage ∈ {quiz, exam}, status ∈ {draft, published}, reviewed_fr, reviewed_en, image, external_id, numeric_value, unit, tolerance_pct (2), hotspot_svg | FK Module ; publication refusée si une langue n'est pas relue ; single = 1 bonne réponse ; multiple ≥ 2 ; truefalse = 2 choix dont 1 bon ; numeric = `numeric_value` renseignée et aucun choix ; matching ≥ 2 paires ; hotspot = `hotspot_svg` + exactement 1 zone correcte |
| ✏️ **Choice** | text*, is_correct, order, shape (JSON : zone cliquable d'une question hotspot) | FK Question |
| 🆕 **MatchPair** | left*, right*, order | FK Question (matching) ; colonne de droite mélangée à chaque tentative |
| **Assessment** | kind ∈ {module_quiz, part_exam}, pass_threshold (70), max_attempts (null ; 3), duration_minutes (null ; 60), questions_per_module, shuffle | 1-1 Module (quiz) **ou** 1-1 Partie (examen) |
| **Attempt** | number, started_at, deadline, submitted_at, auto_submitted, score_pct | FK User, FK Assessment ; unique (user, assessment, number) ; au plus 1 tentative ouverte |
| ✏️ **AttemptQuestion** | order, choice_order (JSON), selected_choices (M2M Choice), answer_text, answer_json, answered_at, time_spent_s | FK Attempt, FK Question ; fige le tirage ; modifiable seulement avant la deadline et avant l'envoi ; `answer_text` = réponse numérique, `answer_json` = paires {gauche: droite} |
| **SectionView** | viewed_at | FK User, FK Section ; unique (user, section) |
| 🆕 **Announcement** | title*, body*, published_at | FK Promotion, FK User (auteur, formateur de la promotion) |
| 🆕 **Deadline** | due_at | FK Promotion, FK Assessment ; unique (promotion, assessment) |
| 🆕 **Badge** | kind ∈ {module, partie}, awarded_at | FK User, FK Module **ou** FK Partie (contrainte de cohérence) ; unique (user, module) et (user, partie) |
| 🆕 **Certificate** | public_id (numéro de vérification), issued_at, score_pct, holder_name (figé à l'émission) | FK User, FK Partie, FK Attempt (meilleure tentative) ; unique (user, partie) ; le PDF n'est jamais stocké |
| 🆕 **SignupThrottle** | ip_hash, created_at | Une ligne par inscription ; sert à la limite par IP (IP hachée, jamais stockée en clair) |
| **LoginFailure** | username, created_at | Verrouillage anti force brute |

**Règles dérivées (calculées, non stockées)**
- Module terminé = toutes ses sections vues + au moins 1 tentative de quiz envoyée (si le module a un quiz).
- Examen ouvert = apprenant inscrit à la formation + tous les modules de la partie terminés + tentatives < max.
- Score : single, truefalse, numeric, hotspot = tout ou rien ; multiple = max(0, bonnes cochées − mauvaises cochées) / nombre de bonnes ; matching = paires justes / nombre de paires.
- Numérique juste ⇔ |saisie − attendu| ≤ |attendu| × tolérance / 100 (si attendu = 0 : saisie = 0) ; une unité saisie différente de l'unité attendue rend la réponse fausse.
- Meilleure note = max(score_pct) des tentatives envoyées ; certificat émis à la première tentative réussie, mis à jour si une meilleure note suit.
- « En retard » = date limite dépassée et (quiz non envoyé, ou examen non réussi).
- Taux de réussite d'une question = moyenne des scores sur les tentatives envoyées des apprenants visibles.

**Partie 2 : aucune entité nouvelle**
| Entité | Évolution |
|---|---|
| Partie | nouveau champ traduit `description` (migration `courses/0004`, lu par l'import, affiché au catalogue et au tableau de bord) ; 2e ligne de la formation `electro` : `slug` = `p2`, `order` = 2, titre « Courant alternatif et filtres », description « à suivre après la Partie 1 » ; 1-1 Assessment `part_exam` (70 %, 3 tentatives, 60 min) |
| Module | 3 lignes, `order` 1 à 3 dans `p2`, dossiers `p2/m5`, `p2/m6`, `p2/m7` (numérotation continue des dossiers et des schémas, pour ne pas heurter `m1` à `m4`) ; chacune avec son Assessment `module_quiz` |
| Section | 20 à 22 lignes (6 à 8 par module, dont un mini-projet `practical`) |
| Question | 81 lignes (`external_id` `e-p2-m<N>-qNN`) ; `unit` accepte désormais `°` en plus de V, A, Ω, W, Hz, F, H ; aucun nouveau `qtype` |
| Badge, Certificate | inchangés : unique (user, partie) permet déjà un certificat et un badge par partie |
- Règle ajoutée : une saisie en degrés est lue sans préfixe SI (« 45° » vaut 45) ; `format_quantity(v, "°")` n'ajoute jamais de préfixe.
- Règle ajoutée : la progression d'une partie ne dépend que de ses propres modules ; aucun lien d'accès entre parties.

**Partie 3 : aucune entité nouvelle ; une migration de contraintes (E45)**
| Entité | Évolution |
|---|---|
| Formation | `electro` : `description` mise à jour (« Du courant continu aux amplificateurs, oscillateurs et alimentations… »), FR et EN |
| Partie | 3e ligne de la formation `electro` : `slug` = `p3`, `order` = 3, titre « Amplification, oscillateurs et alimentations » / « Amplifiers, oscillators and power supplies », description « à suivre après les Parties 1 et 2 » ; 1-1 Assessment `part_exam` (70 %, 3 tentatives, 60 min) |
| Module | 4 lignes, `order` 1 à 4 dans `p3`, dossiers `p3/m8` à `p3/m11` (numérotation continue des dossiers et des schémas) ; chacune avec son Assessment `module_quiz` |
| Section | 28 lignes (M8 : 8, M9 : 7, M10 : 6, M11 : 7, dont un mini-projet `practical` par module) |
| Question | 108 lignes (`external_id` `e-p3-m<N>-qNN`, 15 `quiz` et 12 `exam` par module) ; `unit` vide pour les gains et les rapports (comme β et Q), V, A, Ω, W, Hz, F, H sinon ; aucun nouveau `qtype` ; 4 questions `hotspot` dont le SVG vient de `content/electro/p3/m<N>/schemas/` |
| Badge, Certificate | inchangés : unique (user, partie) donne un badge et un certificat pour la Partie 3 |
- Règle ajoutée : un gain négatif est une valeur numérique ordinaire (|saisie − attendu| ≤ |attendu| × tolérance / 100) ; l'énoncé fixe seul si le signe est attendu.
- Règle ajoutée (TDD) : une grandeur sans unité (gain, rapport) s'affiche sans préfixe SI (`format_quantity(Decimal("0.05"), "")` donne « 0,05 », jamais « 50 m ») ; le signe moins typographique U+2212 des énoncés est lu comme « - » (« −10 » vaut -10).
- Règle ajoutée (E45) : Partie unique (formation, order) et Module unique (partie, order), en plus de Partie unique (formation, slug) ; migration `courses/0005`, seul changement de schéma de la Partie 3.
- Règle ajoutée : trois noms de calculateur de plus (`gain`, `transformer`, `ripple`) dans la liste fermée de `courses/rendering.py` ; tout autre nom reste du texte.

### Exigences non fonctionnelles
- **Performance** : TTFB < 500 ms sur PythonAnywhere pour les pages de cours ; ≤ 10 requêtes SQL par page de cours ; ≤ 20 pour le carnet de notes d'une promotion de 30 apprenants.
- **Poids** : < 200 Ko transférés à la première visite d'une page de cours ; CSS + JS < 60 Ko au total (calculateurs et interactions compris).
- **Disque** : < 150 Mo sur PythonAnywhere (code + venv + base + médias).
- **Accessibilité** : contraste AA, interactions (appariement, zone cliquable) utilisables au clavier, `lang` correct par page.
- **Fiabilité** : aucune réponse d'examen perdue lors d'un rechargement ou d'une coupure.
- **Confidentialité** : un apprenant ne voit que ses données ; un formateur, que ses promotions ; aucune IP stockée en clair.
- **Partie 2** : poids et performance identiques à la Partie 1 (< 200 Ko, ≤ 10 requêtes SQL par page de cours) ; CSS + JS du projet < 60 Ko avec les trois nouveaux calculateurs.
- **Partie 3** : mêmes budgets (< 200 Ko par page à la première visite, ≤ 10 requêtes SQL par page de cours) ; CSS + JS du projet < 60 Ko avec les six calculateurs des Parties 2 et 3 ; disque toujours < 150 Mo avec les schémas de M8 à M11.

### Écarts d'implémentation validés (backend TDD, 2026-10-18)
Décisions prises pendant l'implémentation TDD ; elles priment sur le texte ci-dessus.
1. **Fork** : code de school2ventisax repris (git archive, sans contenu « Froid », sans doc) ; ses tests sont gardés et adaptés. Deux applications créées : `catalog` (Enrollment, catalogue, inscription libre, code de promotion) et `certificates` (Badge, Certificate, PDF, vérification).
2. **`User.promotion` supprimé** au profit d'`Enrollment` (migration `accounts/0003`) : accès au contenu, visibilité des promotions, tableau de bord, import CSV et tableau formateur passent par les inscriptions. Helper de test `conftest.enroll(user, promotion)`.
3. **PDF sans dépendance** (E23) : `certificates/pdf.py`, A4 paysage, polices Helvetica standard en WinAnsi (accents français ; hors WinAnsi → « ? »), table xref vérifiée par les tests et relue par un lecteur PDF.
4. **CSP du back-office** : l'Alpine.js d'Unfold évalue ses expressions (`new Function`) ; `'unsafe-eval'` est ajouté **seulement** sous `/admin/` (réservé au personnel). Le script en ligne reste interdit partout ; le reste du site garde la CSP stricte (test `test_only_the_back_office_allows_alpine_evaluation`).
5. **Traductions dans l'admin sans onglets** : `TabbedTranslationAdmin` charge jQuery UI depuis un CDN, interdit par la CSP ; champs FR et EN affichés côte à côte (`ModelAdmin` d'Unfold + `TranslationAdmin`).
6. **Identifiants publics** : `Promotion.public_id` ajouté (migration en trois temps `accounts/0006`), utilisé dans les formulaires formateur ; code de promotion = 8 caractères sans 0/O/1/I/L (migration en trois temps `accounts/0004`).
7. **Inscription** : jeton de vérification à usage unique (il dépend de `is_active` et `email_verified`) ; champ piège `website` ; limite `SIGNUP_MAX_PER_HOUR` = 5 par IP, IP hachée en HMAC (`SignupThrottle`), en-tête de l'IP réelle configurable (`DJANGO_SIGNUP_IP_HEADER=HTTP_X_REAL_IP` sur PythonAnywhere) ; purge des comptes non vérifiés au plus une fois par heure et par processus, déclenchée par `DailyBackupMiddleware` (pas de tâche planifiée sur le plan gratuit).
8. **E-mail** : mêmes variables que le projet ventisax (`EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`) ; SMTP si le mot de passe est défini, sinon console.
9. **Notation numérique** : saisie normalisée en NFKC (signe ohm U+2126 = oméga ; micro U+00B5 = mu), unités ohm/ohms acceptées, calcul en `Decimal` (bornes exactes : 2,0 % accepté, 2,02 % refusé).
10. **Schémas SVG en ligne** : contrôlés à la publication **et** à chaque affichage (filtre `inert_svg`) ; un SVG modifié après publication et devenu actif n'est jamais rendu.
11. **Temps passé** : le navigateur envoie les secondes écoulées depuis la réponse précédente (`time_spent`) ; le serveur les additionne, borne chaque envoi à 3600 s et refuse une valeur non entière (400).
12. **Badges et certificat** : recalculés à chaque section vue (badge de module) et à chaque tentative envoyée (badge de partie, certificat) ; le certificat est relevé si une meilleure tentative suit, jamais abaissé ; nom du titulaire figé à l'émission.
13. **US-11** : un non-inscrit qui ouvre un module ou une section d'une formation ouverte est renvoyé vers sa fiche du catalogue ; formation fermée : 404.
14. **Vérification publique** : `/<langue>/verify/<numéro>/` (préfixe de langue de `i18n_patterns`).
15. **Garde-fous du contenu** (`courses/tests/test_content_files.py`) pointés vers `content/electro/` et ignorés, avec justification écrite, tant que le manifeste n'existe pas (étape Contenu).

16. **Calculateurs du cours (US-13)** : un paragraphe Markdown réduit à `[[calc:ohm]]`, `[[calc:divider]]`, `[[calc:resistor]]` ou `[[calc:bias]]` devient, **après** le nettoyage bleach, un emplacement inerte `<div class="calc" data-calc="…">` ; tout autre nom reste du texte et le balisage HTML ne peut pas forger cet emplacement.
17. **Correction lisible** : valeur attendue d'une question numérique affichée avec préfixe SI et séparateur de la langue (`assessments.scoring.format_quantity` : « 2,553 mA » / « 2.553 mA ») ; correction d'un appariement ligne par ligne (`AttemptQuestion.pair_rows` : réponse donnée, attendue, juste ou fausse).
18. **Catalogue** : chaque formation indique si l'utilisateur y est déjà inscrit (bouton « Continuer » au lieu de « S'inscrire ») ; le tableau formateur liste les tentatives envoyées de chaque apprenant (lien vers le détail, US-28) ; une promotion unique est présélectionnée dans les formulaires formateur.

19. **Contenu de la Partie 1 rédigé** (2026-10-18) : `content/electro/` contient 4 modules (8, 7, 7 et 7 sections dont un mini-projet chacun), 29 sections en FR et en EN, 108 questions (par module : 15 de quiz dont au moins 5 numériques, 1 appariement et 1 sur schéma ; 12 d'examen). Texte, exercices et schémas sont originaux : le livre de référence n'a servi que de plan (E2). Les questions sont arrivées avec `reviewed` à faux (E12) ; le responsable du projet a validé leur relecture le 2026-10-18 (E24) : elles portent désormais `reviewed` à vrai et sont publiées. Toute nouvelle question entre à nouveau avec `reviewed` à faux. Les garde-fous du contenu (`courses/tests/test_content_files.py`) s'exécutent désormais tous ; le test de publication vérifie que seules les questions relues se publient.
20. **Schémas générés** : `python tools/schemas.py` produit les 50 schémas des sections (symboles CEI, fond clair intégré pour le mode sombre) dans `static/content/electro/m<N>/`, leur version anglaise dans `static/content/electro/en/m<N>/` (libellés traduits, virgules décimales converties) et les 4 schémas des questions sur schéma dans `content/electro/p1/m<N>/schemas/`, avec les coordonnées des zones. Modifier un schéma = modifier sa fonction puis relancer le script ; ne jamais retoucher les SVG à la main.
21. **Questions numériques** : valeur attendue en unité de base (ex. `0.002553` A) ; chaque énoncé donne un exemple de saisie avec préfixe (« 2,5 mA »), car une saisie sans préfixe est lue en unité de base. Tolérance de 2 % par défaut, élargie quand la réponse est une plage physique (0,7 V d'une diode : 15 %).

22. **Déploiement initial (2026-10-18)** sur https://electroacadventisax.pythonanywhere.com/ :
    - **Code et environnement** : clone de `main` dans `~/electroschool2ventisax`, environnement virtuel `~/.virtualenvs/electro` (Python 3.13.1), fichier WSGI `/var/www/electroacadventisax_pythonanywhere_com_wsgi.py` (charge `config.settings`), fichiers statiques `/static/` → `staticfiles/` et `/media/` → `media/`.
    - **Secrets** : `.env` serveur avec droits 600 ; la clé secrète a été générée sur le serveur et les réglages e-mail téléversés depuis le `.env` local, sans transiter en clair.
    - **Compte admin** : utilisateur `admin` ; mot de passe aléatoire dans `~/admin_password.txt` (droits 600), à changer à la première connexion.
    - **Mises à jour** : `bash ~/electroschool2ventisax/deploy.sh`, puis, si l'environnement virtuel change, bouton « Reload » de l'onglet Web (toucher le fichier WSGI ne suffit pas à activer un nouvel environnement virtuel).
    - **Constats** : HTTP → HTTPS en 301 et HSTS d'un an assurés par Django ; disque utilisé : 106 Mo ; 108 questions publiées.
    - **Plan gratuit** : le site est désactivé le **18 novembre 2026** si personne ne clique « Run until 1 month from today » dans l'onglet Web ; à refaire chaque mois.
    - **Écart à E17** : aucun jeton d'API n'a été créé ; le déploiement s'est fait par la console et l'onglet Web, pour qu'aucun jeton n'apparaisse en clair dans les échanges.

23. **Partie 2 rédigée (2026-10-18)** : `content/electro/p2/` contient M5 Le courant alternatif (7 sections), M6 Les filtres RC et RL (8) et M7 La résonance (7), en FR et en EN, et 81 questions (par module : 15 de quiz et 12 d'examen, relues d'emblée selon E29). Les déphasages se saisissent et s'affichent en degrés (« 45° », jamais de préfixe SI, `assessments/scoring.py`). `Partie.description` (traduite, migration `courses/0004`) est lue par l'import et affichée au catalogue et au tableau de bord. Trois calculateurs sont ajoutés : `[[calc:reactance]]`, `[[calc:cutoff]]` et `[[calc:resonance]]`. `tools/schemas.py` produit les 40 schémas de M5 à M7 (bobine CEI, condensateur variable, écran d'oscilloscope, courbes sur axe logarithmique) et les 3 schémas des questions sur schéma, dans `content/electro/p2/m<N>/schemas/`. Garde-fous ajoutés (`courses/tests/test_content_files.py`) : trois modules p2, deux variantes de mesure et la sécurité en tête de chaque mini-projet (US-43), calculateurs présents, au moins deux déphasages en degrés, relecture validée. Chaque valeur numérique a été recalculée par sa formule (écart < 0,1 %).

24. **Partie 3 rédigée (2026-10-18)** : `content/electro/p3/` contient M8 Les amplificateurs à transistor (8 sections), M9 Les oscillateurs (7), M10 Le transformateur (6) et M11 Les alimentations (7), en FR et en EN, et 108 questions (par module : 15 de quiz et 12 d'examen, relues d'emblée selon E39). La description de la formation annonce les trois parties. Les gains et les rapports se notent sans unité ; chaque énoncé de gain précise « en valeur absolue » ou « avec son signe » (garde-fou), le signe moins typographique « − » est lu comme « - » et une grandeur sans unité s'affiche sans préfixe SI (`assessments/scoring.py`). Trois calculateurs sont ajoutés : `[[calc:gain]]`, `[[calc:transformer]]` et `[[calc:ripple]]` ; M9 réutilise `[[calc:resonance]]`. `tools/schemas.py` produit les 48 schémas de M8 à M11 (AOP, transformateur, quartz, pont de diodes, régulateur 78xx, courbes de lissage et de démarrage d'oscillation) et les 4 schémas des questions sur schéma, rangés par `question_dir()` dans `content/electro/p3/m<N>/schemas/`. Garde-fous ajoutés (`courses/tests/test_content_files.py`) : quatre modules p3 et leur nombre de sections, deux variantes de mesure et la sécurité en tête de chaque mini-projet (230 V en M10 et M11), calculateurs présents, une question sur schéma par module, import de l'examen de la Partie 3 (70 %, 3 tentatives, 60 min) et publication des 108 questions ; tests de vues dans `courses/tests/test_part_three.py`. Page des dates limites du formateur : les quiz sont listés par partie puis par module (avant, M8 s'intercalait entre M1 et M2). Chaque valeur numérique attendue est calculée par sa formule dans le script de rédaction, puis vérifiée à la main (écart < 0,1 %). CSS + JS du projet : 55 Ko.

## Definition of Done (critères stricts)
Une story n'est terminée que si **tous** les critères applicables sont vrais. Un seul critère manquant = story non terminée.

**Tests (TDD)**
1. Chaque règle [B] a été développée test d'abord : le test a été vu en échec pour la bonne raison avant le code, puis vu au vert.
2. `pytest` passe intégralement (zéro échec, zéro erreur, aucun test ignoré sans justification écrite), tests d'intrusion compris.
3. Chaque story [B] a au moins un test du cas nominal et un test de refus (droit d'accès, entrée invalide ou limite dépassée).
4. Toute vue qui expose des données d'apprenant a un test de cloisonnement (autre apprenant, formateur d'une autre promotion, anonyme).
5. Les valeurs attendues des tests sont des littéraux vérifiés à la main, jamais recalculés par le code testé.

**Code et sécurité**
6. `python manage.py check --deploy` (avec `DJANGO_DEBUG=0` et une clé de test) ne remonte aucune alerte non justifiée ; `makemigrations --check` ne détecte aucune migration manquante.
7. Aucun secret dans le dépôt ; toute nouvelle variable d'environnement est documentée dans `.env.example`, sans valeur.
8. Toute action qui modifie l'état est un POST protégé par CSRF ; aucune clé entière dans une URL ; aucun script en ligne (CSP).
9. Aucune dépendance de production hors des cinq autorisées.

**Contenu et i18n**
10. Chaque texte d'interface est traduit en EN (`makemessages` puis `compilemessages`, aucune chaîne vide) ; chaque contenu existe en FR et en EN.
11. Aucun texte, schéma ni question copié du livre de référence ou de NetAcad.

**Interface (stories [F])**
12. Le parcours est rejoué avec Playwright MCP en /fr/ et /en/, à 360 px et 1280 px de large, sans erreur dans la console.
13. Page < 200 Ko à la première visite ; interactions utilisables au clavier.

**Livraison**
14. Commit conventionnel sur `develop` ; AGENTS.md et CLAUDE.md à jour si une décision a changé ; CLAUDE.md identique à AGENTS.md (hors en-tête).
15. Après déploiement : `deploy.sh` sans erreur, disque < 150 Mo mesuré, parcours de fumée (connexion, section, quiz, examen, certificat, `/verify/`) rejoué en production.

**Contenu Partie 2**
16. Par module : 6 à 8 sections dont 1 mini-projet, 15 questions de quiz (≥ 4 numériques, ≥ 1 appariement, ≥ 1 sur schéma) et 12 d'examen, vérifié par `courses/tests/test_content_files.py`.
17. Chaque valeur numérique attendue est recalculée à la main et consignée (valeur, unité, tolérance) avant d'entrer dans `questions.json` ; aucun énoncé sans exemple de saisie avec préfixe.
18. Aucun nombre complexe ni calcul de logarithme demandé ; déphasages en degrés.
19. Tous les schémas proviennent de `tools/schemas.py` (FR et EN), aucun SVG retouché à la main ; 2 ou 3 schémas par section.
20. Chaque mini-projet porte les deux variantes (oscilloscope, multimètre seul) et une consigne de sécurité pour le transformateur.
21. Après déploiement : les 81 questions de la Partie 2 sont publiées, l'examen de la Partie 2 se lance pour un compte de test ayant terminé M5 à M7, et son certificat se vérifie sur `/verify/`.

**Contenu Partie 3**
22. Par module de M8 à M11 : 6 à 8 sections dont 1 mini-projet, 15 questions de quiz (≥ 4 numériques, ≥ 1 appariement, ≥ 1 sur schéma) et 12 d'examen, vérifié par `courses/tests/test_content_files.py` ; les sections suivent E34 et E35.
23. Chaque valeur numérique attendue est recalculée à la main par sa formule (écart < 0,1 %) et consignée (valeur, unité, tolérance) avant d'entrer dans `questions.json` ; chaque énoncé donne un exemple de saisie (avec préfixe quand l'unité en admet) ; chaque énoncé de gain précise « en valeur absolue » ou « avec son signe », vérifié par un garde-fou.
24. Aucun nombre complexe, aucun décibel au-delà de −3 dB ; gains exprimés en rapport.
25. Tous les schémas (sections et questions sur schéma) proviennent de `tools/schemas.py`, en FR et en EN, symboles CEI, aucun SVG retouché à la main ; 2 ou 3 schémas par section.
26. Chaque mini-projet porte les deux variantes (oscilloscope + générateur basse fréquence, multimètre seul) ; ceux de M10 et M11 commencent par la consigne de sécurité du secteur (E36), vérifiée par un garde-fou ; aucune consigne ne fait travailler côté 230 V.
27. Les calculateurs `gain`, `transformer` et `ripple` ont été développés test d'abord (rendu de l'emplacement, nom inconnu refusé), sont présents dans les sections prévues (E38), utilisables au clavier en FR et en EN, et le budget CSS + JS du projet reste < 60 Ko.
28. Tests de vues de la Partie 3 (`courses/tests/test_part_three.py`) : accès sans les Parties 1 et 2, examen fermé tant qu'un module manque, examen réussi → badge et certificat distinct vérifiable, cloisonnement (autre apprenant, formateur d'une autre promotion, anonyme).
29. Audit `.playwright-mcp/audit_p3.js` : 360 et 1280 px, thèmes clair et sombre, /fr/ et /en/, sans défaut de contraste, débordement ni erreur console, pages < 200 Ko ; audits des Parties 1 et 2 sans régression.
30. Après déploiement : les 108 questions de la Partie 3 sont publiées, l'examen de la Partie 3 se lance pour un compte de test ayant terminé M8 à M11, et son certificat se vérifie sur `/verify/` ; disque < 150 Mo mesuré.
