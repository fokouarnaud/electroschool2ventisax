Ce mini-projet se fait en atelier, avec votre formateur. Vous appliquez la consignation complète sur un petit banc en très basse tension.

## Objectif

Consigner un banc 24 V, vérifier l'absence de tension dans les règles, puis le déconsigner.

## Sécurité

- Tout le banc fonctionne en **24 V continu**, fourni par un **adaptateur mural** 230 V vers 24 V. Seul l'adaptateur est branché sur le secteur : on n'ouvre jamais son boîtier et on ne travaille jamais côté 230 V.
- Même en 24 V, on applique la méthode complète : c'est elle que vous devrez appliquer demain sur un moteur en 400 V.
- Câblez toujours adaptateur débranché.

![Banc de consignation 24 V : adaptateur, sectionneur cadenassable, étiquette et lampe](/static/content/moteurs/m1/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | adaptateur mural 230 V vers 24 V CC, 1 A |
| 1 | interrupteur-sectionneur cadenassable (ou interrupteur à clé) |
| 1 | lampe ou voyant 24 V |
| 1 | cadenas personnel et une étiquette de consignation |
| 1 | multimètre (et un VAT si l'atelier en possède un) |
| 1 | pile de 9 V servant de source connue |

## Variante oscilloscope

1. Câblez adaptateur, sectionneur et lampe. Branchez la voie 1 de l'oscilloscope aux bornes de la lampe.
2. Observez la tension (une droite à 24 V). Ouvrez le sectionneur : la trace tombe à 0 V. Mesurez combien de temps la tension met à disparaître.
3. Appliquez les étapes : séparer, condamner (cadenas et étiquette remplie), identifier la lampe, vérifier l'absence de tension avec le multimètre testé sur la pile avant et après.

## Variante multimètre seul

1. Même câblage. Mesurez la tension aux bornes de la lampe, sectionneur fermé.
2. Ouvrez le sectionneur, posez cadenas et étiquette.
3. Testez le multimètre sur la pile de 9 V, mesurez aux bornes de la lampe, puis testez-le de nouveau sur la pile.
4. Déconsignez dans l'ordre inverse et vérifiez que la lampe se rallume.

| Mesure | Attendue | Mesurée |
|---|---|---|
| tension lampe, sectionneur fermé | 24 V | |
| tension pile (essai avant) | 9 V | |
| tension lampe, consigné | 0 V | |
| tension pile (essai après) | 9 V | |

## Pour conclure

Expliquez pourquoi l'essai du multimètre sur la pile, après la mesure, est indispensable.
