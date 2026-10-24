Ce mini-projet se fait en atelier, avec votre formateur. Vous câblez le circuit de commande le plus courant de l'industrie, le marche-arrêt avec auto-maintien, sur un vrai contacteur, en très basse tension.

## Objectif

Câbler un contacteur à bobine 24 V avec boutons marche et arrêt et auto-maintien, lui faire commuter un moteur 12 V, mesurer ses tensions d'appel et de retombée, et observer l'effet de l'antiparasitage.

## Sécurité

- La commande est en **24 V continu** (adaptateur mural 230 V vers 24 V), la puissance en **12 V continu** : rien ne dépasse 24 V et on ne travaille jamais côté 230 V.
- Câblez tout circuit débranché ; faites vérifier le câblage avant la mise sous tension.

![Banc : commande 24 V avec arrêt S1, marche S2, contact d'auto-maintien 13-14 et bobine KM1 ; le pôle de KM1 commute un moteur 12 V](/static/content/moteurs/m7/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | contacteur à bobine 24 V CC avec un contact auxiliaire 13-14 |
| 2 | boutons-poussoirs (arrêt à ouverture, marche à fermeture) |
| 1 | adaptateur 230 V vers 24 V CC et alimentation réglable 0 à 24 V |
| 1 | moteur 12 V à courant continu et son alimentation 12 V |
| 1 | diode 1N4007 (antiparasitage) |
| 1 | multimètre ; oscilloscope (variante oscilloscope) |

## Variante oscilloscope

1. Câblez la commande et la puissance comme le schéma ; vérifiez marche, auto-maintien et arrêt.
2. Voie 1 de l'oscilloscope aux bornes de la bobine, sans diode. Appuyez sur arrêt : observez la pointe de tension à la coupure.
3. Ajoutez la diode en inverse sur la bobine (cathode sur A1) et recommencez : la pointe disparaît.

## Variante multimètre seul

1. Câblez et vérifiez le fonctionnement (marche, auto-maintien, arrêt).
2. Mesurez le courant de la bobine en marche (multimètre en série).
3. Alimentez la bobine par l'alimentation réglable : montez lentement la tension et notez la **tension d'appel** (fermeture), puis descendez-la et notez la **tension de retombée**.

| Grandeur | Attendue | Mesurée |
|---|---|---|
| tension d'appel | ≤ 85 % de 24 V, soit ≤ 20,4 V | |
| tension de retombée | nettement plus basse | |
| courant de bobine (bobine de 3 W) | environ 125 mA | |

## Pour conclure

Expliquez pourquoi le moteur ne redémarre pas seul quand on rebranche l'alimentation après l'avoir coupée en marche.
