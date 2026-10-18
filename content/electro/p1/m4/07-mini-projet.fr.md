Ce mini-projet clôt la partie 1. Il se fait en atelier, avec votre formateur, et réutilise les quatre modules : diviseur de tension, LED, transistor et commutation.

## Objectif

Réaliser une veilleuse qui s'allume automatiquement quand la lumière baisse.

## Matériel

| Quantité | Composant |
|---|---|
| 1 | plaque d'essai et fils |
| 1 | pile de 9 V et son coupleur |
| 1 | photorésistance (LDR) |
| 1 | transistor NPN BC547 |
| 1 | résistance ajustable de 47 kΩ et une résistance de 1 kΩ |
| 1 | LED blanche et une résistance de 330 Ω |
| 1 | multimètre |

## Étapes

1. Mesurez la résistance de la LDR à la lumière, puis en la couvrant de la main. Notez les deux valeurs.
2. Calculez la résistance de la LED pour environ 15 mA sous 9 V, transistor saturé.
3. Montez le diviseur : ajustable de 47 kΩ en série avec 1 kΩ en haut, LDR en bas, point milieu sur la base.
4. Placez la LED et sa résistance dans le collecteur, l'émetteur à la masse.
5. Réglez l'ajustable pour que la LED s'allume quand vous couvrez la LDR.
6. Mesurez VBE et VCE dans les deux états (lumière, obscurité).

## Tableau de mesures

| État | R LDR | VBE | VCE | LED |
|---|---|---|---|---|
| Lumière | | | | éteinte |
| Obscurité | | | | allumée |

## Pour aller plus loin

Ajoutez un second transistor en cascade (section 5) pour obtenir l'effet inverse : une LED qui s'allume à la lumière.
