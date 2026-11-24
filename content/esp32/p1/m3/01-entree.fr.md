Une broche réglée en **entrée** n'impose rien : elle **mesure** la tension qu'on lui présente et la traduit en 0 ou en 1. Lire un bouton semble simple ; un piège attend pourtant tous les débutants.

## Comment l'entrée décide

L'entrée compare la tension à deux seuils. Pour l'ESP32 alimenté en 3,3 V :

![Seuils d'une entrée de l'ESP32 : au-dessus de 2,5 V environ elle lit 1, en dessous de 0,8 V environ elle lit 0, entre les deux le niveau est indéterminé](/static/content/esp32/m3/seuils.svg)

- au-dessus d'environ **2,5 V** (75 % de 3,3 V), elle lit **1** (`HIGH`) ;
- en dessous d'environ **0,8 V** (25 % de 3,3 V), elle lit **0** (`LOW`) ;
- entre les deux, le résultat n'est pas garanti : un circuit bien fait n'y reste jamais.

## Le piège de l'entrée flottante

Branchons un bouton entre le 3,3 V et une entrée, et rien d'autre. Bouton appuyé, l'entrée reçoit 3,3 V : elle lit 1. Bouton relâché, l'entrée n'est plus reliée à **rien** : on dit qu'elle **flotte**.

![Une entrée reliée à un bouton seul flotte quand le bouton est relâché : son niveau est inconnu](/static/content/esp32/m3/flottant.svg)

Une entrée flottante a une résistance énorme : la moindre charge électrique, un fil voisin, la main qui approche suffit à la faire basculer. Le programme lit alors des 0 et des 1 au hasard. Ce n'est pas une panne du bouton : il manque un élément au montage, la **résistance de tirage** (section suivante).

## À retenir

- Une entrée lit 1 au-dessus de 2,5 V environ, 0 en dessous de 0,8 V environ.
- Une entrée reliée à rien flotte et lit n'importe quoi.
- Toute entrée doit avoir un niveau défini, bouton appuyé **et** relâché.
