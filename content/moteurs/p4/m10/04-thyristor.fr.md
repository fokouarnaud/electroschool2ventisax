Le **thyristor** est une diode qu'on **commande à l'allumage**. Il bloque dans les deux sens tant qu'on ne l'a pas amorcé ; une impulsion de courant sur sa **gâchette** le rend conducteur de l'anode vers la cathode.

![Symbole du thyristor : anode A, cathode K et gâchette G ; une impulsion sur G le fait conduire, il s'éteint quand son courant s'annule](/static/content/moteurs/m10/thyristor.svg)

## Il ne s'éteint pas seul

Une fois amorcé, le thyristor **reste conducteur** même si l'impulsion de gâchette disparaît. Il ne s'éteint que lorsque son courant passe sous une petite valeur, le **courant de maintien**. En alternatif, cela arrive naturellement à chaque passage par zéro : c'est pourquoi le thyristor règne sur les montages alimentés par le réseau à 50 Hz.

## Le redressement commandé

En retardant l'amorçage d'un angle **α** après le début de chaque alternance, on ne laisse passer qu'une partie de l'onde : la **tension moyenne** baisse quand α augmente.

![Thyristor amorcé à α = 60° : seule la fin de chaque alternance positive atteint la charge](/static/content/moteurs/m10/angle.svg)

- α = 0° : le thyristor se comporte comme une diode, tension moyenne maximale.
- α = 90° : la moitié de chaque alternance positive, tension moyenne divisée par deux.
- α proche de 180° : presque plus rien.

Un **pont de thyristors** sert ainsi à régler la tension d'induit d'un moteur à courant continu (module 11) ou à charger des batteries.

## Le tester

Thyristor débranché, multimètre en ohmmètre : entre A et K, très grande résistance dans les deux sens ; entre G et K, une jonction comme une diode. Un thyristor « franc » entre A et K est en court-circuit.

## À retenir

- Thyristor : amorcé par la gâchette, éteint quand son courant s'annule.
- En alternatif, il s'éteint seul à chaque passage par zéro.
- Retarder l'amorçage (angle α) réduit la tension moyenne.
