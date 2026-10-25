Ce mini-projet se fait en atelier, avec votre formateur. Vous préparez **sur papier** le paramétrage d'un variateur pour un vrai moteur, puis vous reproduisez des rampes sur une maquette 12 V.

## Objectif

Passer de la plaque signalétique d'un moteur à une fiche de paramétrage complète et justifiée, et visualiser une rampe d'accélération.

## Sécurité

- On ne raccorde **aucun variateur triphasé** : le paramétrage se fait sur papier, à partir de la plaque d'un moteur **débranché**.
- La maquette de rampe utilise le module MLI 12 V du module 10, alimenté par un adaptateur mural ; aucune tension au-delà de 24 V.
- Si un variateur réel est présent à l'atelier, on ne l'ouvre pas : son bus continu reste dangereux après la coupure.

![Fiche de paramétrage : tension, courant, fréquence et vitesse du moteur, rampes d'accélération et de décélération](/static/content/moteurs/m11/tableau.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | moteur asynchrone débranché, avec sa plaque lisible |
| 1 | fiche de paramétrage vierge et la notice d'un variateur (papier ou PDF) |
| 1 | module MLI 12 V, moteur 12 V et alimentation 12 V (module 10) |
| 1 | multimètre ; oscilloscope (variante oscilloscope) |
| 1 | chronomètre |

## Variante oscilloscope

1. Remplissez la fiche à partir de la plaque : tension, courant, fréquence, vitesse ; calculez le glissement nominal.
2. Choisissez les rampes (5 s et 3 s) et les fréquences minimale et maximale ; justifiez chaque choix.
3. Sur la maquette, sonde sur la sortie MLI : tournez lentement le potentiomètre pendant 5 s et observez l'élargissement progressif des impulsions, image d'une rampe.

## Variante multimètre seul

1. Remplissez et justifiez la fiche comme ci-dessus.
2. Sur la maquette, relevez la tension moyenne du moteur toutes les secondes pendant que vous montez le potentiomètre en 5 s ; tracez la rampe obtenue.
3. Calculez la tension que fournirait le variateur à 25 Hz selon la loi U/f.

| Grandeur | Plaque | Paramètre retenu | Justification |
|---|---|---|---|
| tension | | | |
| courant | | | |
| vitesse | | | |
| rampe d'accélération | | 5 s | |

## Pour conclure

Expliquez ce qui se passerait avec une rampe de décélération de 0,5 s sur une machine à forte inertie.
