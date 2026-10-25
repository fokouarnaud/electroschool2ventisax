Ce mini-projet se fait en atelier, avec votre formateur. Vous réglez la vitesse d'un moteur 12 V par MLI, puis la luminosité d'une lampe 12 V par un gradateur à triac.

## Objectif

Relier le rapport cyclique à la tension moyenne et à la vitesse, puis observer l'effet de l'angle d'amorçage d'un triac.

## Sécurité

- Tout le banc reste en **très basse tension** : 12 V continu pour la MLI, 12 V alternatif pour le gradateur, jamais au-delà de 24 V.
- Le 12 V alternatif vient d'un **transformateur moulé** ou d'un adaptateur mural 230 V vers 12 V AC : on ne touche jamais au côté 230 V, on ne mesure qu'au secondaire.
- Le dissipateur du module peut chauffer ; câblez hors tension.

![Banc : alimentation 12 V, module MLI et moteur 12 V ; transformateur moulé 12 V AC, gradateur à triac et lampe 12 V](/static/content/moteurs/m10/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | alimentation 12 V continu (adaptateur mural) |
| 1 | module MLI 12 V à MOSFET ou IGBT, avec potentiomètre |
| 1 | moteur 12 V à courant continu |
| 1 | transformateur moulé 230 V vers 12 V AC |
| 1 | module gradateur à triac basse tension et une lampe 12 V à incandescence |
| 1 | multimètre ; oscilloscope et GBF (variante oscilloscope) |

## Variante oscilloscope

1. Sonde sur la sortie du module MLI (masse au 0 V). Réglez le potentiomètre pour un rapport cyclique de 25 %, 50 % puis 75 % ; relevez la fréquence de découpage.
2. Pour chaque réglage, mesurez la tension moyenne au multimètre et comparez-la à rapport cyclique × 12 V.
3. Sur le gradateur, observez la tension aux bornes de la lampe (sonde différentielle ou transformateur d'isolement, jamais côté 230 V) : repérez l'angle d'amorçage pour trois positions du bouton.

## Variante multimètre seul

1. Mesurez la tension moyenne aux bornes du moteur pour cinq positions du potentiomètre.
2. Comptez les tours de l'arbre (repère adhésif) sur 10 s ou estimez la vitesse ; tracez vitesse en fonction de la tension.
3. Sur le gradateur, mesurez la tension efficace aux bornes de la lampe pour trois positions et notez la luminosité.

| Réglage | Rapport cyclique | Umoy calculée | Umoy mesurée | Vitesse |
|---|---|---|---|---|
| 1 | 25 % | 3 V | | |
| 2 | 50 % | 6 V | | |
| 3 | 75 % | 9 V | | |

## Pour conclure

Expliquez pourquoi le transistor du module MLI chauffe peu alors qu'il commande tout le courant du moteur.
