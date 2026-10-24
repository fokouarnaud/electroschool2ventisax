Une usine d'une certaine taille reçoit l'énergie en HTA et possède son propre **poste de transformation**.

![Poste d'usine : arrivée HTA 20 kV, sectionnement, transformateur 630 kVA, tableau général basse tension (TGBT) à 400 V et ses départs protégés](/static/content/moteurs/m3/poste.svg)

- L'**arrivée HTA** passe par un appareil de sectionnement et de protection.
- Le **transformateur** (ici 630 kVA) abaisse 20 kV en 400 V.
- Le **TGBT** (tableau général basse tension) répartit l'énergie entre des **départs**, chacun protégé par un disjoncteur : ateliers, éclairage, moteurs importants.

Chaque départ alimente à son tour des tableaux divisionnaires, plus près des machines. Les protections sont choisies pour que, en cas de défaut, **seul le disjoncteur le plus proche du défaut** déclenche : c'est la **sélectivité**. Ainsi, un court-circuit sur une machine n'arrête pas tout l'atelier.

## Le centre de commande des moteurs

Quand un atelier compte de nombreux moteurs (pompes, convoyeurs, ventilateurs), on regroupe leurs départs dans un **centre de commande des moteurs** (CCM).

![Centre de commande des moteurs : un jeu de barres vertical alimente des tiroirs, chacun équipé d'un départ moteur complet](/static/content/moteurs/m3/mcc.svg)

Un jeu de barres alimente des **tiroirs** identiques ; chacun contient un départ moteur complet : sectionnement et protection (Q), contacteur (KM), relais de surcharge (F). Un tiroir défectueux se retire et se remplace en quelques minutes, sans arrêter les autres moteurs. Tout est regroupé, repéré et accessible pour la maintenance.

## À retenir

- Poste d'usine : arrivée HTA, transformateur, TGBT, départs.
- Sélectivité : seul le disjoncteur le plus proche du défaut déclenche.
- CCM : un tiroir complet par moteur, remplaçable.
