Ce mini-projet se fait en atelier, avec votre formateur. Selon le matériel disponible, suivez la variante oscilloscope ou la variante multimètre seul. Apportez votre tableau de mesures complété.

## Objectif

Monter un filtre passe-bas RC, relever sa réponse et vérifier la fréquence de coupure calculée.

## Matériel

| Quantité | Composant |
|---|---|
| 1 | plaque d'essai et fils |
| 1 | résistance de 1 kΩ et une de 10 kΩ, 0,25 W |
| 3 | condensateurs non polarisés (film, 63 V ou plus) : 100 nF, 330 nF, 1 µF |
| 1 | GBF et oscilloscope à deux voies (variante oscilloscope) |
| 1 | adaptateur secteur **fermé** 230 V vers 12 V AC (transformateur, variante multimètre seul) |
| 1 | multimètre |
| 1 | calculatrice avec √ et tan⁻¹ |

## Sécurité

- Seul l'adaptateur fermé est branché sur le 230 V. N'ouvrez jamais son boîtier et ne travaillez que du côté 12 V.
- Débranchez l'adaptateur ou coupez le GBF avant chaque modification du montage.
- Uniquement des condensateurs non polarisés.
- Toutes les pinces de masse de l'oscilloscope et du GBF vont au même point : le bas du condensateur.

## Variante oscilloscope

1. Calculez fc pour R = 1 kΩ et C = 100 nF (environ 1,6 kHz).
2. Montez le passe-bas : GBF, résistance en série, condensateur vers la masse. Voie 1 sur l'entrée, voie 2 sur la sortie (aux bornes de C).
3. Réglez le GBF en sinus, 4 V crête à crête. Pour chaque fréquence du tableau, mesurez Ucc en entrée et en sortie, puis le décalage Δt entre les deux courbes.
4. Calculez Vs / Ve et φ = 360° × Δt / T. Comparez avec les valeurs attendues.
5. Tracez Vs / Ve en fonction de la fréquence et repérez la fréquence où le rapport vaut 0,707.

| f | Ucc entrée | Ucc sortie | Vs / Ve | Vs / Ve attendu | Δt | φ | φ attendu |
|---|---|---|---|---|---|---|---|
| 160 Hz | | | | 0,995 | | | 5,7° |
| 500 Hz | | | | 0,954 | | | 17,4° |
| 1,6 kHz | | | | 0,705 | | | 45° |
| 5 kHz | | | | 0,303 | | | 72,3° |
| 16 kHz | | | | 0,099 | | | 84,3° |

## Variante multimètre seul

La fréquence de l'adaptateur est fixe (50 Hz) : on change donc C pour placer 50 Hz avant, sur ou après la fréquence de coupure.

1. Montez : adaptateur, résistance de 10 kΩ en série, condensateur vers l'autre borne de l'adaptateur.
2. Pour chaque condensateur, calculez fc = 1 / (2π × 10 000 × C).
3. Mesurez en V~ la tension d'entrée Ue, la tension Ur aux bornes de R et la tension Uc aux bornes de C (la sortie du passe-bas).
4. Calculez Uc / Ue et vérifiez que √(Ur² + Uc²) ≈ Ue.

| C | fc | Ue | Ur | Uc | Uc / Ue | Uc / Ue attendu |
|---|---|---|---|---|---|---|
| 100 nF | 159 Hz | | | | | 0,954 |
| 330 nF | 48 Hz | | | | | 0,694 |
| 1 µF | 16 Hz | | | | | 0,303 |

## Pour conclure

Expliquez pourquoi Ur + Uc dépasse Ue, et indiquez pour quel montage 50 Hz se trouve le plus près de la fréquence de coupure.
