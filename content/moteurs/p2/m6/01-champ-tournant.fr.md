Le moteur à courant alternatif triphasé n'a ni collecteur ni balais. Son secret : un **champ magnétique qui tourne** tout seul.

## Le champ tournant

Le stator porte trois enroulements décalés de **120°** dans l'espace, alimentés par les trois phases du réseau, elles-mêmes décalées de 120° dans le temps. Leurs trois champs s'ajoutent en un champ unique, d'intensité constante, qui **tourne** autour de l'axe du moteur.

![Trois bobines U, V, W décalées de 120°, alimentées en triphasé : leur champ total tourne](/static/content/moteurs/m6/champ.svg)

## La vitesse de synchronisme

Le champ fait un tour par période du réseau pour une **paire de pôles**. Avec p paires de pôles, il tourne p fois moins vite :

**ns = 60 × f / p**   (ns en tr/min, f en Hz)

![Vitesse de synchronisme à 50 Hz : 3 000 tr/min pour 2 pôles, 1 500 pour 4, 1 000 pour 6, 750 pour 8](/static/content/moteurs/m6/vitesses.svg)

**Exemple.** Un moteur à 4 pôles (p = 2) sur le réseau 50 Hz : ns = 60 × 50 / 2 = **1 500 tr/min**. Pour changer cette vitesse, il faut changer le nombre de pôles (moteur à plusieurs vitesses, module 9) ou la fréquence (variateur, module 11).

Pour inverser le sens du champ, donc du moteur, on **permute deux phases** (module 2).

[[calc:speed]]

## À retenir

- Trois enroulements à 120° + courants triphasés = champ tournant.
- ns = 60 × f / p ; à 50 Hz : 3 000, 1 500, 1 000, 750 tr/min.
- Permuter deux phases inverse le sens.
