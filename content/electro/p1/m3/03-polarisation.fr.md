**Polariser** un transistor, c'est lui fournir les tensions et les courants qui le placent dans l'état voulu. Le montage le plus simple utilise une résistance de base RB reliée à une tension de commande VBB.

![Polarisation par résistance de base : VBB = 5 V, RB = 100 kΩ, RC = 1 kΩ, VCC = 12 V](/static/content/electro/m3/polarisation.svg)

## Calculer le courant de base

La jonction base-émetteur est une diode passante : elle garde environ **0,7 V** à ses bornes. La résistance RB reçoit donc VBB − 0,7, et la loi d'Ohm donne :

**IB = (VBB − 0,7) / RB**

Exemple : VBB = 5 V et RB = 100 kΩ. IB = 4,3 V / 100 kΩ = **43 µA**.

## En déduire le courant de collecteur

Avec β = 100 : IC = 100 × 43 µA = **4,3 mA**. La résistance de collecteur RC = 1 kΩ reçoit alors RC × IC = 4,3 V, et il reste entre collecteur et émetteur :

**VCE = VCC − RC × IC = 12 − 4,3 = 7,7 V**

Si ce calcul donnait un VCE négatif, le transistor ne pourrait pas fournir le courant demandé : il serait saturé (section suivante).

[[calc:bias]]

## Vérifier par la mesure

Deux ampèremètres permettent de mesurer IB et IC en même temps. Leur rapport donne le β réel de l'exemplaire testé.

![Même montage avec un ampèremètre dans la base et un autre dans le collecteur](/static/content/electro/m3/polarisation-mesures.svg)

## À retenir

- VBE ≈ 0,7 V : IB = (VBB − 0,7) / RB.
- IC = β × IB, puis VCE = VCC − RC × IC.
- β réel = IC mesuré / IB mesuré.
