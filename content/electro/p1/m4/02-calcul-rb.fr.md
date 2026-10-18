Pour qu'un transistor sature à coup sûr, il faut lui fournir **assez** de courant de base, même avec l'exemplaire au gain le plus faible. La méthode tient en quatre étapes.

![Commande 5 V, RB à calculer, charge de 100 Ω dans le collecteur, VCC = 9 V](/static/content/electro/m4/calcul-rb.svg)

## La méthode

1. **Courant de saturation** de la charge : IC sat = (VCC − 0,2) / RC.
2. **Courant de base minimal** avec le gain minimal de la fiche technique : IB min = IC sat / β min.
3. **Marge de sécurité** : on prend IB = 2 × IB min (certains concepteurs vont jusqu'à 5 ou 10 fois).
4. **Résistance de base** : RB = (Ve − 0,7) / IB, puis valeur normalisée **inférieure**.

## Exemple

VCC = 9 V, charge RC = 100 Ω, commande Ve = 5 V, β min = 100.

1. IC sat = (9 − 0,2) / 100 = **88 mA**.
2. IB min = 88 mA / 100 = 0,88 mA.
3. IB = 2 × 0,88 = **1,76 mA**.
4. RB = (5 − 0,7) / 1,76 mA ≈ **2,44 kΩ**, donc 2,2 kΩ en valeur normalisée.

On prend la valeur inférieure parce qu'une résistance plus petite donne **plus** de courant de base, donc une saturation encore plus sûre.

![IC en fonction de IB : le courant plafonne à 88 mA à partir de 880 µA, la marge double ce courant de base](/static/content/electro/m4/saturation-courbe.svg)

## Et si l'on exagère ?

Au-delà de la saturation, augmenter IB ne fait plus monter IC : la courbe plafonne. Un excès de courant de base ne sert à rien et charge inutilement le circuit de commande. Vérifiez aussi que celui-ci peut fournir IB : une sortie de microcontrôleur supporte en général une vingtaine de milliampères au plus.

## À retenir

- IC sat = (VCC − 0,2) / RC ; IB min = IC sat / β min.
- Marge : IB = 2 × IB min au moins.
- RB = (Ve − 0,7) / IB, puis valeur normalisée inférieure.
