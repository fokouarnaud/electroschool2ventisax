Ce mini-projet se fait en atelier, avec votre formateur. Vous câblez un petit circuit d'après son schéma, puis vous lisez la plaque d'un vrai moteur.

## Objectif

Passer du schéma au câblage sans erreur, et exploiter une plaque signalétique.

## Sécurité

- Le circuit est alimenté en **24 V continu** par un **adaptateur mural** 230 V vers 24 V. On ne travaille jamais côté 230 V et on n'ouvre jamais l'adaptateur.
- Câblez adaptateur débranché ; faites vérifier votre câblage par le formateur avant de le brancher.
- Le moteur triphasé de la partie 2 est **débranché** et le reste : on se contente de lire sa plaque et de regarder sa plaque à bornes.

![Circuit 24 V : S1 à fermeture allume H1 ; S2 à ouverture éteint H2 quand on l'actionne](/static/content/moteurs/m2/lampes.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | adaptateur mural 230 V vers 24 V CC |
| 2 | boutons-poussoirs (un à fermeture, un à ouverture) |
| 2 | voyants ou lampes 24 V |
| 1 | bornier, fils, embouts |
| 1 | multimètre |
| 1 | moteur triphasé débranché, plaque lisible |

## Variante oscilloscope

1. Câblez le circuit et vérifiez au multimètre, hors tension, la continuité de chaque branche.
2. Mettez sous tension. Voie 1 aux bornes de H1, voie 2 aux bornes de H2.
3. Appuyez sur S1 puis sur S2 : observez sur les deux traces que les lampes changent d'état au même instant que les boutons, et notez les rebonds éventuels du contact au moment de l'appui.

## Variante multimètre seul

1. Câblez le circuit d'après le schéma, adaptateur débranché.
2. Hors tension, mesurez la résistance de S1 et de S2 au repos puis actionnés : vérifiez que S1 est bien à fermeture et S2 à ouverture.
3. Mettez sous tension et mesurez la tension aux bornes de chaque lampe, boutons au repos puis actionnés.
4. Sur le moteur débranché, relevez la plaque et indiquez le couplage à utiliser sur un réseau 400 V.

| Mesure | Attendue | Mesurée |
|---|---|---|
| S1 au repos | circuit ouvert | |
| S2 au repos | quelques ohms au plus | |
| H1, S1 actionné | 24 V | |
| H2, S2 actionné | 0 V | |
| couplage du moteur sur 400 V | | |

## Pour conclure

Expliquez pourquoi un schéma est toujours dessiné avec les contacts au repos.
