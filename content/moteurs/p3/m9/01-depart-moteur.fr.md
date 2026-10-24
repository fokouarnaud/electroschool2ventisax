Un **départ moteur** est l'ensemble des appareils entre le tableau et le moteur. Quatre fonctions doivent toujours y être assurées, selon les principes de l'IEC 60364 :

![Départ moteur : sectionnement par Q1, protection contre les courts-circuits par fusibles, commande par KM1, protection contre les surcharges par F1](/static/content/moteurs/m9/depart.svg)

1. **Sectionner** : séparer le départ du réseau pour la consignation (module 1) ; sectionneur ou interrupteur-sectionneur, cadenassable.
2. **Protéger contre les courts-circuits** : fusibles aM ou déclencheur magnétique d'un disjoncteur, en tête du départ.
3. **Commander** : établir et couper le courant en service ; contacteur.
4. **Protéger contre les surcharges** : relais thermique (module 7) ou déclencheur thermique d'un disjoncteur-moteur.

Un **disjoncteur-moteur** réunit à lui seul le sectionnement et les deux protections ; associé à un contacteur, il forme un départ complet et compact.

## La section des conducteurs

Le câble du moteur doit supporter son courant **sans s'échauffer** au-delà de ce que tolère son isolant, et sans trop de **chute de tension**. Le courant admissible dépend de la section, du métal, de l'isolant, du **mode de pose** (dans un conduit, sur un chemin de câbles, enterré), de la température ambiante et du nombre de câbles voisins.

![Ordre de grandeur du courant admissible du cuivre : 1,5 mm² environ 16 A, 2,5 mm² environ 21 A, 4 mm² environ 28 A, 6 mm² environ 36 A](/static/content/moteurs/m9/section.svg)

Ces valeurs ne sont qu'un ordre de grandeur : on choisit toujours la section dans les tableaux de la réglementation applicable, en appliquant ses facteurs de correction, puis on vérifie que la protection protège bien le câble. **Exemple** : pour un moteur de 4,8 A (module 2), une section de 1,5 mm² convient largement en courant ; sur une grande longueur, c'est la chute de tension qui décidera.

## À retenir

- Sectionner, protéger des courts-circuits, commander, protéger des surcharges.
- Disjoncteur-moteur + contacteur : départ complet.
- La section dépend du courant, du mode de pose et de la longueur.
