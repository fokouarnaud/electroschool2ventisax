Le **triac** équivaut à deux thyristors montés tête-bêche dans un seul boîtier, avec une seule gâchette. Une impulsion le fait conduire **dans les deux sens** : il commande directement un courant alternatif.

![Symbole du triac : bornes A2 et A1, gâchette G ; il conduit dans les deux sens](/static/content/moteurs/m10/triac.svg)

## Le gradateur

Le **gradateur** règle la puissance d'une charge alternative en retardant l'amorçage du triac à chaque alternance, positive comme négative. On l'emploie pour l'éclairage, le chauffage et les petits moteurs universels (perceuse, ventilateur).

![Gradateur amorcé à 90° : la lampe reçoit la seconde moitié de chaque alternance, positive et négative](/static/content/moteurs/m10/gradateur.svg)

Pour une charge **résistive**, un amorçage à 90° transmet environ la **moitié de la puissance**. Le circuit de déclenchement le plus simple est un réseau résistance-condensateur et un **diac**, qui envoie une impulsion quand la tension du condensateur atteint une trentaine de volts ; un potentiomètre règle l'angle.

## Précautions

- Un gradateur à angle de phase produit des **harmoniques** et des parasites : on lui ajoute un filtre.
- Une charge **inductive** (moteur, transformateur) demande un réseau d'aide à la commutation (un **snubber** RC) et parfois un triac plus robuste.
- Un **moteur asynchrone** ne se règle pas en vitesse par un gradateur : sa vitesse dépend de la fréquence (module 6). Le gradateur sert au mieux de **démarreur progressif** (module 9).

## Le relais statique

Un relais statique (module 8) contient un triac ou deux thyristors, commandés au **zéro de tension** : ils ne font que du tout ou rien, sans réglage d'angle.

## À retenir

- Triac : conduit dans les deux sens après une impulsion de gâchette.
- Gradateur : retarder l'amorçage réduit la puissance ; 90° donne environ la moitié sur une charge résistive.
- Pas de variation de vitesse d'un asynchrone par gradateur : il faut un variateur de fréquence.
