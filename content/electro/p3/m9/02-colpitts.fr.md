L'oscillateur **Colpitts** est l'un des plus utilisés jusqu'à quelques dizaines de mégahertz. Son réseau de rétroaction est un circuit LC dont le condensateur est coupé en deux.

![Oscillateur Colpitts : sous l'amplificateur, une bobine L de 100 µH entre deux condensateurs C1 et C2 de 10 nF reliés à la masse](/static/content/electro/m9/colpitts.svg)

## Le diviseur capacitif

Les condensateurs C1 et C2 sont en série dans la boucle du circuit résonant, avec leur point commun à la masse. Ils jouent deux rôles :

- avec L, ils fixent la **fréquence** ;
- ils forment un **diviseur** : le rapport C1 / C2 fixe la part du signal renvoyée à l'amplificateur. Le point milieu à la masse fait que les deux extrémités du circuit LC sont en opposition : le réseau apporte les 180° que l'amplificateur inverseur n'a pas.

## La fréquence

Deux condensateurs en série valent un seul condensateur **Céq** plus petit :

**Céq = C1 × C2 / (C1 + C2)**

![Deux condensateurs de 10 nF en série équivalent à un seul de 5 nF](/static/content/electro/m9/ceq.svg)

On reprend alors la formule de la résonance de la Partie 2 :

**f = 1 / (2π × √(L × Céq))**

Exemple : L = 100 µH, C1 = C2 = 10 nF. Céq = 10 × 10 / 20 = 5 nF, et f = 1 / (2π × √(100 µH × 5 nF)) ≈ **225 kHz**.

Pour retrouver ce résultat, saisissez L et Céq (et non C1 ou C2) dans le calculateur :

[[calc:resonance]]

## Régler la fréquence

On change la fréquence en changeant L (bobine à noyau réglable) ou les condensateurs. Pour garder le même taux de rétroaction, on modifie C1 et C2 ensemble, ou on ajoute un petit condensateur variable en parallèle sur L.

## À retenir

- Colpitts : bobine L et diviseur capacitif C1, C2 dont le point milieu est à la masse.
- Céq = C1 × C2 / (C1 + C2) ; f = 1 / (2π × √(L × Céq)).
- Le rapport C1 / C2 règle la part du signal renvoyée.
