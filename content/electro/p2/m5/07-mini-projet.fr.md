Ce mini-projet se fait en atelier, avec votre formateur. Selon le matériel disponible, suivez la variante oscilloscope ou la variante multimètre seul. Apportez votre tableau de mesures complété.

## Objectif

Mesurer les valeurs d'une tension sinusoïdale, puis vérifier par la mesure la réactance d'un condensateur et son évolution avec la fréquence ou la capacité.

## Matériel

| Quantité | Composant |
|---|---|
| 1 | plaque d'essai et fils |
| 2 | condensateurs **non polarisés** (film) de 1 µF, tension de service 63 V ou plus |
| 2 | condensateurs non polarisés (film) de 2,2 µF, 63 V ou plus |
| 1 | résistance de 10 Ω, 0,25 W |
| 1 | GBF et oscilloscope à deux voies (variante oscilloscope) |
| 1 | adaptateur secteur **fermé** 230 V vers 12 V AC (transformateur, variante multimètre seul) |
| 1 | multimètre |

## Sécurité

- Seul l'adaptateur fermé est branché sur le 230 V. N'ouvrez jamais son boîtier et ne travaillez que du côté 12 V.
- Débranchez l'adaptateur ou coupez le GBF avant chaque modification du montage.
- N'utilisez jamais de condensateur électrochimique (polarisé) en alternatif.
- Un ampèremètre se place toujours en série, jamais directement sur une source.
- Toutes les pinces de masse de l'oscilloscope et du GBF vont au même point du circuit.

## Variante oscilloscope

1. Réglez le GBF : sinus, 1 kHz, 4 V crête à crête. Observez-le sur la voie 1 et mesurez Ucc, Umax et T ; calculez f.
2. Montez en série : sortie du GBF, condensateur de 1 µF, résistance de 10 Ω vers la masse. La voie 2 mesure la tension aux bornes de la résistance de 10 Ω.
3. Le courant vaut Imax = Umax(voie 2) / 10. Comme la résistance est petite devant Xc, presque toute la tension est aux bornes du condensateur : Xc ≈ Umax(voie 1) / Imax.
4. Comparez avec Xc = 1 / (2π × f × C), soit 159 Ω à 1 kHz.
5. Recommencez à 500 Hz puis à 2 kHz. Comment varie Xc ?

| f | Umax voie 1 | Umax voie 2 | Imax | Xc mesurée | Xc calculée |
|---|---|---|---|---|---|
| 500 Hz | | | | | 318 Ω |
| 1 kHz | | | | | 159 Ω |
| 2 kHz | | | | | 80 Ω |

## Variante multimètre seul

1. Mesurez la tension efficace de l'adaptateur à vide, en V~. Calculez Umax = Ueff × 1,414. (Un adaptateur de 12 V affiche souvent un peu plus à vide.)
2. Branchez en série : adaptateur, multimètre en mA~, condensateur de 2,2 µF. Relevez le courant efficace.
3. Mesurez au multimètre en V~ la tension efficace aux bornes du condensateur.
4. Calculez Xc = Ueff / Ieff et comparez avec 1 / (2π × 50 × 0,000 002 2) ≈ 1 447 Ω.
5. Placez le second condensateur de 2,2 µF en parallèle sur le premier (4,4 µF). Que deviennent le courant et Xc ?

| Montage | U efficace | I efficace | Xc mesurée | Xc calculée |
|---|---|---|---|---|
| Adaptateur à vide | | - | - | - |
| 2,2 µF | | | | 1 447 Ω |
| 2 × 2,2 µF en parallèle | | | | 723 Ω |

## Pour conclure

Écrivez en une phrase comment Xc varie avec la fréquence et avec la capacité, et ce qui explique les écarts entre mesure et calcul (tolérance des condensateurs, précision des appareils).
