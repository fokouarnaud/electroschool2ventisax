Un variateur mal installé tombe en défaut, perturbe les appareils voisins ou abîme le moteur. Les règles suivent les principes de l'IEC 60364 et les notices du constructeur.

## La chaîne d'installation

![De l'amont vers le moteur : sectionneur et fusibles, inductance de ligne, variateur, câble blindé, moteur, avec une terre commune](/static/content/moteurs/m11/installation.svg)

- **Sectionnement et protection** en amont : interrupteur-sectionneur cadenassable et fusibles ou disjoncteur du calibre indiqué par la notice.
- **Inductance de ligne** (selon le cas) : elle réduit les harmoniques renvoyés au réseau et protège le redresseur.
- **Pas de contacteur entre variateur et moteur** pour commander la marche : on démarre et on arrête par les entrées du variateur. Un contacteur aval ne s'ouvre qu'à variateur arrêté.
- **Contacteur de contournement** (bypass) : il permet de faire tourner le moteur directement sur le réseau si le variateur est en panne ; il est verrouillé avec le contacteur de sortie du variateur pour ne jamais renvoyer le réseau dans l'onduleur.

## Compatibilité électromagnétique

La MLI découpe des centaines de volts en quelques fractions de microseconde : le câble moteur rayonne des parasites.

![Câble moteur blindé, blindage repris à 360° aux deux bouts ; câbles de puissance et de commande séparés d'au moins 30 cm](/static/content/moteurs/m11/cem.svg)

- Câble moteur **blindé**, blindage relié à la masse **sur toute sa circonférence** aux deux extrémités (colliers, presse-étoupes CEM).
- Câbles de **puissance** et de **commande** séparés d'au moins 30 cm ; croisements à angle droit.
- **Filtre CEM** d'entrée, intégré ou ajouté.
- Liaisons de terre **courtes et larges**, sur une plaque de montage métallique non peinte.

## Ventilation

Un variateur perd environ 2 à 3 % de la puissance qu'il transmet : 300 W pour un moteur de 11 kW. On respecte les distances libres au-dessus et au-dessous, et on dimensionne la ventilation de l'armoire.

## À retenir

- Sectionner et protéger en amont ; ne pas commander la marche par un contacteur aval.
- Câble blindé repris à 360°, puissance et commande séparées, terre courte.
- Prévoir l'évacuation des pertes de chaleur.
