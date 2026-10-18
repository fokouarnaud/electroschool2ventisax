Dans l'oscillateur **Armstrong**, la rétroaction passe par un petit **transformateur** : une bobine de réaction, couplée magnétiquement à la bobine du circuit accordé, renvoie le signal vers l'entrée de l'amplificateur.

![Oscillateur Armstrong : le circuit accordé L et C de 10 nF à la sortie de l'amplificateur, couplé à une bobine de réaction reliée à son entrée](/static/content/electro/m9/armstrong.svg)

## Le rôle de chaque élément

- Le **circuit accordé** (la bobine primaire L et le condensateur C) fixe la fréquence : f = 1 / (2π × √(L × C)).
- La **bobine de réaction**, enroulée sur le même support, capte une partie du champ magnétique et la renvoie à l'entrée. Son nombre de spires règle la quantité de signal renvoyée.

Exemple : L = 1 mH et C = 10 nF donnent f = 1 / (2π × √(1 mH × 10 nF)) ≈ **50,3 kHz**.

## Le sens des enroulements compte

Le transformateur peut renvoyer une tension en phase ou en opposition, selon le sens de branchement de la bobine de réaction. Sur les schémas, un **point** marque le début de chaque enroulement : deux points du même côté signifient des tensions en phase.

![Deux transformateurs : points du même côté, la sortie est en phase avec l'entrée ; points opposés, elle est en opposition](/static/content/electro/m9/points.svg)

Si l'amplificateur inverse, le transformateur doit inverser aussi pour que la boucle revienne en phase. Un Armstrong qui refuse d'osciller a souvent… sa bobine de réaction branchée à l'envers : on **inverse ses deux fils**, et il démarre.

## Où le rencontre-t-on ?

L'Armstrong est historique : c'est l'un des premiers oscillateurs à tubes, utilisé dans les premiers postes de radio. Il reste un excellent exemple pour comprendre la rétroaction, car on voit bien le chemin du signal renvoyé.

## À retenir

- Armstrong : circuit accordé LC à la sortie, bobine de réaction couplée vers l'entrée.
- f = 1 / (2π × √(L × C)).
- Les points des enroulements indiquent la phase ; inverser la bobine de réaction peut faire démarrer l'oscillation.
