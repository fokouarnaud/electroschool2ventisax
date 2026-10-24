Ce mini-projet se fait en atelier, avec votre formateur. Vous câblez une inversion verrouillée, puis un démarrage étoile-triangle **figuré** par des lampes, en très basse tension.

## Objectif

Vérifier qu'un verrouillage électrique empêche toute fermeture simultanée, et observer la séquence d'un démarrage étoile-triangle avec sa temporisation.

## Sécurité

- Tout le banc est en **24 V continu** pour la commande et en **12 V** pour les lampes et le moteur, fournis par des **adaptateurs muraux**. On ne travaille jamais côté 230/400 V : le démarrage étoile-triangle est seulement **figuré** par des lampes.
- Câblez débranché ; faites vérifier le câblage par le formateur avant chaque mise sous tension.

![Banc : trois relais 24 V figurent KM1 (ligne), KM2 (étoile) et KM3 (triangle) ; trois lampes 12 V montrent la séquence ; KT1 temporise le passage étoile vers triangle](/static/content/moteurs/m9/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | adaptateur mural 230 V vers 24 V CC et alimentation 12 V |
| 3 | relais ou contacteurs à bobine 24 V, avec contacts 13-14 et 21-22 |
| 1 | relais temporisé 24 V au travail |
| 3 | boutons-poussoirs (arrêt, avant, arrière) |
| 3 | lampes 12 V ; un moteur 12 V à courant continu (inversion) |
| 1 | multimètre ; oscilloscope (variante oscilloscope) |

## Variante oscilloscope

1. Câblez l'étoile-triangle figuré : KM1 et KM2 s'enclenchent ensemble, KT1 coupe KM2 puis enclenche KM3.
2. Voie 1 sur la lampe H2 (étoile), voie 2 sur la lampe H3 (triangle). Mesurez le délai étoile → triangle et le **temps mort** entre l'extinction de H2 et l'allumage de H3 : il ne doit jamais être négatif (chevauchement = court-circuit sur un vrai moteur).

## Variante multimètre seul

1. Câblez l'inversion d'un moteur 12 V avec KM1 (avant) et KM2 (arrière), avec le verrouillage électrique (21-22 de l'un dans la bobine de l'autre).
2. Appuyez sur avant puis, sans arrêter, sur arrière : vérifiez que KM2 ne s'enclenche pas.
3. Retirez un fil du verrouillage (moteur débranché !) : constatez au multimètre que les deux bobines peuvent alors être alimentées. Remettez le fil.
4. Câblez l'étoile-triangle figuré et chronométrez le délai réglé sur KT1.

| Essai | Attendu | Observé |
|---|---|---|
| avant puis arrière sans arrêt | KM2 reste ouvert | |
| délai étoile → triangle (KT1 sur 3 s) | 3 s | |
| H2 et H3 allumées ensemble | jamais | |

## Pour conclure

Expliquez pourquoi on ajoute un verrouillage mécanique alors que le verrouillage électrique fonctionne.
