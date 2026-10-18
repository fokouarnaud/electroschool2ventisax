Après le lissage, la tension ondule encore et change avec la charge et le secteur. Pour une tension vraiment fixe, il faut la **réguler**. La solution la plus simple, déjà vue en Partie 1 (module « La diode »), est la **diode Zener**.

![Régulateur à Zener : Ue de 15 V, résistance série Rs de 200 Ω, Zener de 9,1 V et charge R de 455 Ω en parallèle](/static/content/electro/m11/zener.svg)

## Rappel du principe

Une Zener branchée **en inverse** maintient à ses bornes une tension presque constante, sa tension Zener Uz, tant qu'un courant suffisant la traverse. La résistance série **Rs** absorbe l'écart entre la tension d'entrée et Uz.

## Dimensionner Rs

Le courant de Rs se partage entre la Zener (Iz) et la charge (I) :

**Rs = (Ue − Uz) / (Iz + I)**

Exemple : Ue = 15 V, Uz = 9,1 V, une charge de 20 mA et 10 mA réservés à la Zener. Rs = (15 − 9,1) / 0,03 ≈ 197 Ω, soit **200 Ω**.

## Vérifier les puissances

Le cas le plus dur pour la Zener est **sans charge** : tout le courant de Rs passe par elle.

- Iz max = (15 − 9,1) / 200 ≈ 29,5 mA, et Pz = 9,1 × 0,029 5 ≈ **0,27 W** : on prend une Zener de 0,5 W.
- Dans Rs : P = (15 − 9,1)² / 200 ≈ 0,17 W : une résistance de 0,25 W suffit, 0,5 W est plus confortable.

## La limite basse

La régulation ne tient que si l'entrée reste assez haute. Avec la charge de 20 mA (455 Ω), il faut au minimum Ue = Uz + Rs × I = 9,1 + 200 × 0,02 ≈ **13,1 V**. En dessous, la Zener ne conduit plus et la sortie suit l'entrée.

![Sortie en fonction de l'entrée : elle monte avec Ue jusqu'à environ 13,1 V, puis reste fixée à 9,1 V](/static/content/electro/m11/zener-courbe.svg)

Avec un condensateur de lissage, c'est le **creux** de l'ondulation qui doit rester au-dessus de cette limite.

## Les limites de la Zener

Le régulateur à Zener gaspille du courant en permanence et ne convient qu'aux faibles courants (quelques dizaines de milliampères). Pour plus, on utilise un régulateur intégré, section suivante.

## À retenir

- Rs = (Ue − Uz) / (Iz + I).
- Vérifier la puissance de la Zener à vide : Pz = Uz × Iz max.
- L'entrée doit rester au-dessus de Uz + Rs × I.
