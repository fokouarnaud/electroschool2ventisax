Avant les variateurs de fréquence, la vitesse variable passait par le **moteur à courant continu** (module 5). On en trouve encore sur des machines anciennes, des laminoirs, des enrouleurs et des engins de levage.

## Le principe

La vitesse d'un moteur à courant continu à excitation séparée est presque proportionnelle à sa **tension d'induit**. Un **pont de thyristors** (module 10), alimenté par le réseau, fournit cette tension ; l'**angle d'amorçage** la règle.

![Variateur à courant continu : un pont de thyristors redresse le réseau ; l'angle d'amorçage règle la tension d'induit, donc la vitesse](/static/content/moteurs/m11/pont-cc.svg)

Le variateur alimente aussi l'**inducteur** sous tension constante, et régule le courant d'induit pour limiter le couple. Une **dynamo tachymétrique** ou un codeur mesure la vitesse pour la régulation.

Les petits moteurs à aimants permanents se commandent plutôt par un **hacheur** à transistors (MLI), comme au mini-projet du module 10.

## Les quatre quadrants

![Les quatre quadrants : moteur et frein dans chaque sens de rotation](/static/content/moteurs/m11/quadrants.svg)

- Quadrants 1 et 3 : le moteur **entraîne** la charge, dans un sens ou dans l'autre.
- Quadrants 2 et 4 : le moteur **freine** la charge, qui l'entraîne (descente d'une charge, ralentissement d'un volant).

Un variateur **un quadrant** ne fait que tourner dans un sens. Un variateur **régénératif** à deux ponts tête-bêche fonctionne dans les quatre quadrants et **renvoie au réseau** l'énergie de freinage, au lieu de la brûler dans une résistance. Le principe existe aussi pour les variateurs de fréquence (redresseur actif).

## Entretien

Le moteur à courant continu demande la surveillance de ses **balais** et de son **collecteur** (module 5) ; c'est la raison principale de son remplacement par des moteurs asynchrones sur variateur de fréquence.

## À retenir

- Pont de thyristors : l'angle d'amorçage règle la tension d'induit et la vitesse.
- Quatre quadrants : moteur ou frein dans chaque sens.
- Régénératif : l'énergie de freinage retourne au réseau.
