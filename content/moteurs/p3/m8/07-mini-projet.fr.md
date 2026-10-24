Ce mini-projet se fait en atelier, avec votre formateur. Vous réglez un relais temporisé et vous réalisez des fonctions logiques avec deux relais, en très basse tension.

## Objectif

Vérifier les temporisations au travail et au repos, puis câbler les fonctions ET et OU avec des boutons, deux relais et des voyants.

## Sécurité

- Tout le banc est en **24 V continu**, fourni par un **adaptateur mural** 230 V vers 24 V. On ne travaille jamais côté 230 V.
- Câblez adaptateur débranché ; vérifiez le brochage des relais sur leur notice avant de câbler.

![Banc : alimentation 24 V, relais KA1 et KA2, relais temporisé KT1, boutons S1 et S2, voyants H1 et H2](/static/content/moteurs/m8/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | adaptateur mural 230 V vers 24 V CC |
| 2 | relais 24 V à contact inverseur, sur embase |
| 1 | relais temporisé multifonction 24 V |
| 2 | boutons-poussoirs à fermeture |
| 2 | voyants 24 V |
| 1 | chronomètre (ou téléphone) ; multimètre ; oscilloscope (variante oscilloscope) |

## Variante oscilloscope

1. Réglez KT1 en temporisation au travail, 2 s. Voie 1 sur sa bobine, voie 2 sur la sortie de son contact (vers H1).
2. Appuyez sur S1 : mesurez sur l'écran le retard entre les deux voies.
3. Passez en fonction clignotant : mesurez la période et le rapport entre temps allumé et temps éteint.

## Variante multimètre seul

1. Réglez KT1 en temporisation au travail, 5 s : chronométrez le retard entre l'appui et l'allumage de H1, cinq fois, et faites la moyenne.
2. Passez en temporisation au repos, 5 s : chronométrez le retard entre le relâchement et l'extinction.
3. Câblez S1 et S2 commandant KA1 et KA2 ; leurs contacts 11-14 **en série** vers H1 (fonction ET), **en parallèle** vers H2 (fonction OU). Remplissez la table de vérité.

| S1 | S2 | H1 (ET) attendu | H2 (OU) attendu | H1, H2 observés |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | |
| 0 | 1 | 0 | 1 | |
| 1 | 0 | 0 | 1 | |
| 1 | 1 | 1 | 1 | |

## Pour conclure

Comparez le retard mesuré au réglage : quel écart, en pourcentage ? Pourquoi refaire la mesure plusieurs fois ?
