Ce mini-projet se fait en atelier, avec votre formateur, sur n'importe quel **relais programmable 24 V**. Vous programmez successivement un auto-maintien, une temporisation et un comptage.

## Objectif

Écrire, charger et tester trois programmes ladder, et vérifier leur comportement par des mesures.

## Sécurité

- Tout le banc est en **24 V continu**, fourni par un adaptateur mural ; les sorties commandent des voyants ou des LED, jamais une charge sur le réseau.
- Câblez hors tension ; faites vérifier le câblage par le formateur avant la mise sous tension.

![Banc : relais programmable 24 V, interrupteurs sur %IX0.0 à %IX0.2, voyants sur %QX0.0 et %QX0.1](/static/content/moteurs/m12/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | relais programmable 24 V CC (toute marque) et son logiciel ou son clavier |
| 1 | adaptateur mural 230 V vers 24 V CC |
| 3 | boutons-poussoirs ou interrupteurs 24 V (dont un à ouverture pour l'arrêt) |
| 2 | voyants ou LED 24 V |
| 1 | multimètre ; oscilloscope (variante oscilloscope) ; chronomètre |

**Traduire pour votre marque** : remplacez %IX0.0, %IX0.1, %IX0.2 par les trois premières entrées de votre relais (par exemple I1, I2, I3) et %QX0.0, %QX0.1 par ses deux premières sorties (Q1, Q2).

## Les trois programmes

1. **Auto-maintien** : arrêt %IX0.0 (à ouverture), marche %IX0.1, sortie %QX0.0.
2. **TON** : %IX0.2 lance un TON de 5 s qui allume %QX0.1.
3. **CTU** : %IX0.2 incrémente un CTU de présélection 5 ; Q allume %QX0.1 ; %IX0.0 le remet à zéro.

## Variante oscilloscope

1. Voie 1 sur l'entrée %IX0.2, voie 2 sur la sortie %QX0.1 (masse au 0 V).
2. Programme TON : mesurez le retard entre le front de l'entrée et celui de la sortie ; comparez à 5 s.
3. Remplacez par un TOF de 3 s et mesurez le retard à la retombée.

## Variante multimètre seul

1. Programme d'auto-maintien : relevez au multimètre la tension de la sortie %QX0.0 après marche, puis après arrêt.
2. Programme TON : chronométrez le retard trois fois et faites la moyenne.
3. Programme CTU : comptez les appuis jusqu'à l'allumage ; vérifiez qu'un appui maintenu ne compte qu'une fois.

| Essai | Attendu | Mesuré |
|---|---|---|
| sortie après marche | 24 V | |
| retard du TON | 5 s | |
| appuis avant Q du CTU | 5 | |

## Pour conclure

Débranchez le fil du bouton d'arrêt pendant que la sortie est active : que se passe-t-il, et pourquoi est-ce voulu ?
