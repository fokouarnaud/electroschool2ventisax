Ce mini-projet se fait en atelier, avec votre formateur. Selon le matériel disponible, suivez la variante oscilloscope ou la variante multimètre seul. Apportez votre tableau de mesures complété.

## Objectif

Mettre en évidence la résonance d'un circuit RLC série, ou, sans générateur, vérifier par la mesure qu'un RLC série alimenté à 50 Hz se comporte comme le prévoit le calcul.

## Matériel

| Quantité | Composant |
|---|---|
| 1 | plaque d'essai et fils |
| 1 | résistance de 100 Ω, 0,5 W |
| 1 | bobine de 10 mH et une bobine de 100 mH (courant admissible 100 mA ou plus) |
| 1 | condensateur non polarisé de 100 nF et un de 10 µF (film, 63 V ou plus) |
| 1 | GBF et oscilloscope à deux voies (variante oscilloscope) |
| 1 | adaptateur secteur **fermé** 230 V vers 12 V AC (transformateur, variante multimètre seul) |
| 1 | multimètre |

## Sécurité

- Seul l'adaptateur fermé est branché sur le 230 V. N'ouvrez jamais son boîtier et ne travaillez que du côté 12 V.
- Débranchez l'adaptateur ou coupez le GBF avant chaque modification du montage.
- Près de la résonance, la tension aux bornes du condensateur peut dépasser celle de la source : n'utilisez que des condensateurs de 63 V ou plus et ne touchez pas le montage sous tension.
- Toutes les pinces de masse de l'oscilloscope et du GBF vont au même point : le bas de la résistance.

## Variante oscilloscope

1. Calculez f0 pour L = 10 mH et C = 100 nF (environ 5 kHz), puis la bande passante attendue BP = R / (2π × L), soit environ 1,6 kHz avec R = 100 Ω.
2. Montez en série : GBF, condensateur, bobine, résistance de 100 Ω vers la masse. Voie 1 sur la sortie du GBF, voie 2 aux bornes de R (image du courant).
3. Réglez le GBF en sinus, 2 V crête à crête. Balayez la fréquence de 1 kHz à 20 kHz et repérez celle où Ur est maximale : c'est f0.
4. Relevez Ur pour les fréquences du tableau. Cherchez f1 et f2, où Ur vaut 0,707 × Ur max, et calculez BP = f2 − f1 et Q = f0 / BP.
5. Comparez avec le calcul. La résistance du fil de la bobine s'ajoute à R : la bande passante mesurée est souvent un peu plus large.

| f | 2 kHz | 4 kHz | f0 mesurée | 6 kHz | 10 kHz | f1 | f2 |
|---|---|---|---|---|---|---|---|
| Ucc aux bornes de R | | | | | | | |

| Grandeur | Mesurée | Calculée |
|---|---|---|
| f0 | | 5 033 Hz |
| BP | | 1 592 Hz |
| Q | | 3,2 |

## Variante multimètre seul

Sans générateur, la fréquence reste 50 Hz. On choisit L = 100 mH et C = 10 µF : f0 ≈ 159 Hz, donc à 50 Hz le circuit est **sous** sa résonance.

1. Calculez à 50 Hz : XL ≈ 31,4 Ω, XC ≈ 318 Ω, Z = √(R² + (XL − XC)²) ≈ 304 Ω.
2. Montez en série : adaptateur, résistance de 100 Ω, bobine de 100 mH, condensateur de 10 µF, multimètre en mA~.
3. Relevez le courant, puis les tensions efficaces aux bornes de l'adaptateur, de R, de L et de C.
4. Vérifiez que Ue ≈ √(Ur² + (UL − UC)²). Constatez que UC dépasse Ue.
5. Calculez la capacité qui donnerait la résonance à 50 Hz avec 100 mH : C = 1 / (4π² × 50² × 0,1) ≈ 101 µF. Expliquez pourquoi on ne l'atteint pas facilement avec des condensateurs film.

| Grandeur | Mesurée | Calculée (sous 12 V) |
|---|---|---|
| I | | 39,5 mA |
| Ur | | 3,95 V |
| UL | | 1,24 V |
| UC | | 12,6 V |

## Pour conclure

Expliquez pourquoi la tension aux bornes du condensateur peut dépasser celle de la source, et ce qui limite la hauteur du pic de résonance.
