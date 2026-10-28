Chaque borne d'un appareil porte un **repère** gravé, et le schéma reprend ces repères. C'est grâce à eux qu'on câble et qu'on dépanne sans erreur.

## Les repères des contacts

![Repères CEI : pôles de puissance 1-2, 3-4, 5-6 ; contact à fermeture 13-14 ; contact à ouverture 21-22 ; bobine A1-A2 ; relais thermique 95-96 et 97-98](/static/content/moteurs/m2/contacts.svg)

- **Pôles de puissance** : chiffres simples, 1-2, 3-4, 5-6 (entrée impaire, sortie paire).
- **Contacts auxiliaires** : deux chiffres. Le premier est un **numéro d'ordre** (1er, 2e contact de l'appareil), le second dit la **fonction** : 3-4 pour un contact **à fermeture**, 1-2 pour un contact **à ouverture**. D'où 13-14 (premier contact, à fermeture), 21-22 (deuxième contact, à ouverture), 33-34, 43-44…
- **Bobine** : A1 et A2.
- **Relais thermique** : 95-96 (contact à ouverture qui coupe la commande) et 97-98 (contact à fermeture qui allume un voyant de défaut).

Les appareils eux-mêmes portent une lettre : **Q** pour les appareils de sectionnement et de protection de puissance, **KM** pour les contacteurs, **F** pour les protections (relais thermique, fusibles), **S** pour les boutons, **H** pour les voyants, **M** pour les moteurs.

## Ce qui se passe dans le contacteur

Dans le contacteur, chaque contact est fait de deux plots fixes, reliés à ses deux bornes, et d'un pont qui les relie quand il les recouvre. Tous les ponts sont portés par un même équipage mobile. Quand A1-A2 reçoit sa tension (24 V ici), la bobine attire l'équipage et tous les ponts coulissent ensemble : les pôles 1-2, 3-4, 5-6 et les contacts 13-14 et 43-44 se ferment, les contacts 21-22 et 31-32 s'ouvrent. Quand la bobine n'est plus alimentée, un ressort ramène l'équipage et tout revient au repos.

« À fermeture » et « à ouverture » disent donc ce que fait le contact quand la bobine est alimentée, à partir de son état au repos : c'est pourquoi un schéma montre chaque contact au repos, bobine non alimentée. Le second chiffre du repère suffit à le savoir sans ouvrir l'appareil : 3-4, ouvert au repos ; 1-2, fermé au repos. Le premier chiffre ne fait que numéroter les contacts du bloc, de 1 à 4.

[[fig:contact_marking]]

## La plaque à bornes du moteur

![Plaque à bornes : entrées U1 V1 W1 en haut, sorties W2 U2 V2 en bas, décalées d'un cran](/static/content/moteurs/m2/bornes.svg)

Un moteur triphasé a trois enroulements : U1-U2, V1-V2, W1-W2. Sur la plaque, les sorties sont **décalées** (W2 sous U1, U2 sous V1, V2 sous W1) : ce décalage permet de réaliser les couplages étoile et triangle avec de simples barrettes droites (section 5).

## Ce qui se passe sur la plaque

Chaque enroulement relie une entrée du fond à une sortie de devant, mais pas celle qui est juste en dessous : U1 est à gauche au fond, U2 au milieu devant. C'est ce décalage d'un cran qui permet de coupler le moteur avec des barrettes droites.

En **étoile**, une barrette horizontale relie W2, U2 et V2 : les trois fins d'enroulement forment le point commun, et chaque enroulement se trouve entre une phase (L1, L2 ou L3, arrivée sur U1, V1 ou W1) et ce point. Il reçoit U / √3, environ 230 V sur un réseau 400 V.

En **triangle**, trois barrettes verticales relient U1 à W2, V1 à U2 et W1 à V2 : chacune joint le début d'un enroulement à la fin d'un autre, si bien que les trois enroulements se referment en boucle. Chacun est alors placé entre deux phases et reçoit U entière, 230 V sur un réseau 230 V. Si les sorties n'étaient pas décalées (U2 sous U1), une barrette verticale relierait les deux bouts du même enroulement : elle le court-circuiterait au lieu de le coupler.

[[fig:terminal_plate]]

## À retenir

- 13-14 à fermeture, 21-22 à ouverture, A1-A2 bobine, 95-96 relais thermique.
- Q, KM, F, S, H, M : la lettre dit la fonction de l'appareil.
- Plaque à bornes : U1 V1 W1 en haut, W2 U2 V2 en bas.
