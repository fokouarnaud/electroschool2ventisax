Quand un courant arrive à un **nœud**, un point où plusieurs fils se rejoignent, il se partage entre les branches. Rien ne se perd : la somme des courants qui entrent dans un nœud est égale à la somme des courants qui en sortent. C'est la **loi des nœuds**.

![Courant I qui se partage en I1, I2 et I3 entre trois branches](/static/content/electro/m1/trois-branches.svg)

## Qui prend le plus de courant ?

Les branches en parallèle ont la même tension U. Chacune laisse donc passer I = U / R : **la branche la moins résistante prend le plus de courant**. Le courant préfère le chemin le plus facile, sans pour autant délaisser les autres.

Pour deux branches, le partage s'écrit directement :

**I1 = I × R2 / (R1 + R2)**   et   **I2 = I × R1 / (R1 + R2)**

Remarquez l'inversion : le courant dans R1 dépend de R2, et inversement.

![Pile de 6 V, 1 kΩ et 2 kΩ en parallèle : I = 9 mA se partage en 6 mA et 3 mA](/static/content/electro/m1/diviseur-courant.svg)

## Exemple

Une pile de 6 V alimente 1 kΩ et 2 kΩ en parallèle. On calcule chaque branche avec la loi d'Ohm : I1 = 6 / 1 = **6 mA** et I2 = 6 / 2 = **3 mA**. La pile fournit I = 6 + 3 = 9 mA. Vérification avec la formule : I1 = 9 × 2 / 3 = 6 mA.

Le calcul branche par branche est souvent le plus sûr : il évite de se tromper de résistance au numérateur.

## À retenir

- Loi des nœuds : la somme des courants entrants égale la somme des courants sortants.
- En parallèle, la branche la moins résistante prend le plus de courant.
- I1 = I × R2 / (R1 + R2) : le numérateur est l'autre résistance.
