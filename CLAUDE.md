# CLAUDE.md : Electro Acad Ventisax

> Les instructions du projet sont dans **AGENTS.md**, qui est la source de vérité. En cas de divergence, AGENTS.md prime.
> Ce fichier en reprend le contenu pour Claude Code.

Plateforme de formation et d'évaluation en ligne inspirée des principes d'interface de Cisco NetAcad, forkée d'Acad Ventisax (dépôt `school2ventisax`). Première formation : électronique, Partie 1.
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
| E22 | Dépôt et disque ? | GitHub `fokouarnaud/electroschool2ventisax` ; `develop` → `main` (suivi par le serveur) ; < 150 Mo de disque ; 1 sauvegarde SQLite quotidienne |

## GOALS

### 1. Objectifs fonctionnels prioritaires
1. **Lecteur de cours** : Formation → Partie → Module → Section, sommaire repliable, sections vues cochées, barre de progression par module et par partie.
2. **Contenu Partie 1 « Électronique DC et semi-conducteurs »** : 4 modules originaux (révision DC, diode, transistor, transistor en commutation), rédigés en FR et traduits en EN, avec schémas SVG et 1 mini-projet pratique par module.
3. **Quiz de module** : entraînement illimité, correction et explication après envoi ; types QCM une/plusieurs réponses, vrai/faux, **numérique avec unité et tolérance**, **appariement / glisser-déposer**, **zone cliquable sur schéma**.
4. **Calculateurs interactifs** dans les sections (loi d'Ohm, diviseur de tension, code couleur des résistances, polarisation), non notés.
5. **Examen de partie** : banque séparée, 70 % pour réussir, 3 tentatives, 60 min chronométrées côté serveur, mélange, sauvegarde au clic, reprise après coupure, envoi automatique, meilleure note retenue.
6. **Catalogue et inscription** : catalogue public ; inscription libre aux formations ouvertes ou par code de promotion ; e-mail vérifié ; mot de passe oublié par e-mail ; un apprenant peut suivre plusieurs formations.
7. **Certificat et badges** : certificat PDF par partie réussie, numéro unique vérifiable sur `/verify/<uuid>/` ; badges par module terminé et par partie réussie.
8. **Espace formateur** (front, mobile) : tableau apprenants × modules de ses promotions, carnet de notes détaillé par tentative et par question, taux de réussite par question, export CSV, annonces et dates limites indicatives.
9. **Back-office Django Unfold** : comptes, promotions, codes de promotion, contenu, relecture et publication des questions (refusée si FR ou EN non relu), réglage des examens.
10. **Interface** : bilingue `/fr/` et `/en/`, patterns NetAcad, charte Ventisax déclinée « électronique », mobile d'abord.

### 2. Contraintes techniques
- **Python** le plus récent proposé par PythonAnywhere ; **Django 5.2 LTS** ; **SQLite** (un seul fichier, sauvegarde quotidienne, 1 copie gardée).
- Code **forké de school2ventisax** : gabarits serveur + **HTMX vendoré**, **JS vanilla**, CSS écrit à la main ; aucun CDN, aucun Node, aucune SPA.
- **Dépendances de production** limitées à : `django`, `django-modeltranslation`, `markdown`, `bleach`, `django-unfold` (fpdf2 retiré, E23). Toute autre dépendance demande un accord explicite. Développement : `pytest`, `pytest-django`.
- **TDD obligatoire** (skill test-driven-development) : test rouge avant chaque règle métier ; suite pytest verte, tests d'intrusion compris ; parcours Playwright MCP rejoués avant chaque déploiement.
- **PythonAnywhere gratuit** (compte `electroacadventisax`) : quota de 512 Mo, **cible < 150 Mo** (code + venv + base + médias) ; une seule web app ; pas de tâche planifiée ; internet sortant sur liste blanche ; e-mail sortant par **Gmail SMTP** seulement.
- **Poids** : < 200 Ko par page à la première visite ; schémas en SVG, images éventuelles en WebP ; pas de Pillow.
- **i18n** : `i18n_patterns` (`/fr/` par défaut, `/en/`), gettext pour l'interface, modeltranslation pour le contenu, repli sur le FR.
- **Contenu versionné** : `content/electro/` (manifeste JSON + Markdown fr/en + `questions.json`), importé par `import_content` (idempotent).
- **Sécurité** : DEBUG=False et HTTPS en production, CSRF, CSP sans script en ligne, Markdown nettoyé par bleach, identifiants publics UUID, verrouillage anti force brute, limitation des inscriptions, secrets dans `.env`.
- **Déploiement par Claude** : jeton d'API PythonAnywhere créé via Playwright MCP, puis `deploy.sh` (pull, install, migrate, compilemessages, collectstatic, check --deploy, reload) ; branche `main` suivie par le serveur, développement sur `develop`.
- **Droits** : contenu 100 % original ; le PDF de référence n'est jamais committé ni cité textuellement.

### 3. Périmètre strictement hors scope (v1)
- Reproduction du texte, des figures ou des projets du livre *Complete Electronics Self-Teaching Guide* ; tout texte, question, logo ou asset de NetAcad/Cisco.
- Parties 2 et suivantes (chapitres 5 et au-delà du livre : AC, filtres, résonance, amplificateurs, oscillateurs, transformateur…).
- Simulateur de circuits (type Packet Tracer / SPICE) et laboratoires virtuels.
- Valeurs numériques aléatoires par tentative (questions paramétrées) ; réponse libre rédigée ; correction manuelle.
- Évaluation pratique notée, saisie des mesures dans l'app, dépôt de fichiers par les apprenants.
- Dates limites bloquantes ; annonces ou notifications par e-mail ; messagerie, forum, chat.
- Suivi en direct des examens en cours.
- SSO, connexion Google/Cisco, base partagée avec Acad Ventisax ou ventisax.
- Paiement, cours payants, Open Badges / badges exportables.
- Mode hors ligne / PWA, application mobile native.
- Parcours séquentiel bloquant entre sections.
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

### Modélisation logique des données
`*` = champ traduit (fr/en) par modeltranslation, avec repli sur le fr. 🆕 = entité nouvelle, ✏️ = entité modifiée par rapport à school2ventisax.
Formation, Partie, Module, Section, Question, Choice, MatchPair, Attempt, Certificate et Promotion portent un `public_id` (UUID v4, unique, non modifiable) : c'est le seul identifiant exposé (URL, formulaires, ancres). Les clés entières restent internes.

| Entité | Attributs clés | Relations / contraintes |
|---|---|---|
| ✏️ **User** (personnalisé) | username, first_name, last_name, email, role ∈ {learner, trainer, admin}, email_verified, date_joined | trainer et admin donnent `is_staff` ; le champ `promotion` de school2ventisax est remplacé par Enrollment ; `is_active` = faux tant que l'e-mail n'est pas vérifié (inscription publique) ; e-mail unique quand il est renseigné |
| 🆕 **Enrollment** | enrolled_at, source ∈ {catalog, code, import, admin} | FK User (apprenant), FK Formation, FK Promotion (null = groupe ouvert) ; unique (user, formation) ; la promotion, si présente, appartient à la même formation |
| ✏️ **Promotion** | name, start_date, join_code (unique, 8 caractères sans ambiguïté), join_code_active | FK Formation ; M2M trainers (role = trainer) |
| ✏️ **Formation** | title*, slug, description*, order, is_open | 1-N Partie ; `is_open` = visible au catalogue et ouverte à l'inscription libre |
| **Partie** | title*, order, slug | FK Formation ; 1-1 Assessment (examen) |
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

### Exigences non fonctionnelles
- **Performance** : TTFB < 500 ms sur PythonAnywhere pour les pages de cours ; ≤ 10 requêtes SQL par page de cours ; ≤ 20 pour le carnet de notes d'une promotion de 30 apprenants.
- **Poids** : < 200 Ko transférés à la première visite d'une page de cours ; CSS + JS < 60 Ko au total (calculateurs et interactions compris).
- **Disque** : < 150 Mo sur PythonAnywhere (code + venv + base + médias).
- **Accessibilité** : contraste AA, interactions (appariement, zone cliquable) utilisables au clavier, `lang` correct par page.
- **Fiabilité** : aucune réponse d'examen perdue lors d'un rechargement ou d'une coupure.
- **Confidentialité** : un apprenant ne voit que ses données ; un formateur, que ses promotions ; aucune IP stockée en clair.

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
