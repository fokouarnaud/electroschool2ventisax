Ce mini-projet se fait en atelier, avec votre formateur. Selon le matériel disponible, suivez la variante oscilloscope ou la variante multimètre seul. Apportez votre tableau de mesures complété.

## Objectif

Monter l'amplificateur à émetteur commun du module, vérifier son point de repos, puis mesurer son gain en tension et le comparer au calcul (Av ≈ −RC / RE1 = −39).

## Matériel

| Quantité | Composant |
|---|---|
| 1 | plaque d'essai et fils |
| 1 | transistor NPN d'usage courant (BC547 ou 2N2222) |
| 1 | résistance de chaque valeur : 47 kΩ, 10 kΩ, 3,9 kΩ, 910 Ω, 100 Ω |
| 2 | condensateurs de 10 µF (C1, C2) et 1 de 100 µF (CE), 25 V ou plus |
| 1 | alimentation continue 12 V de laboratoire, ou bloc secteur fermé 12 V continu |
| 1 | GBF et oscilloscope à deux voies (variante oscilloscope) |
| 1 | adaptateur secteur **fermé** 230 V vers 9 V AC et deux résistances de 100 kΩ et 1 kΩ (variante multimètre seul) |
| 1 | multimètre |

## Sécurité

- Seuls les blocs fermés (alimentation 12 V, adaptateur 9 V AC) sont branchés sur le 230 V. N'ouvrez jamais leur boîtier et ne travaillez que du côté basse tension.
- Coupez l'alimentation avant chaque modification du montage.
- Respectez la polarité des condensateurs chimiques (bande « − » vers la tension la plus basse) : inversé, un condensateur chauffe et peut éclater.

## Variante oscilloscope

1. Câblez le montage du schéma de la section « Le gain de l'émetteur commun ». Sans signal d'entrée, mesurez VB, VE et VC au multimètre et comparez au calcul (2,1 V ; 1,4 V ; 6,5 V).
2. Réglez le GBF en sinus, 1 kHz, 100 mV crête à crête. Voie 1 sur l'entrée ve (avant C1), voie 2 sur la sortie vs (après C2), masses communes.
3. Relevez les amplitudes crête à crête et calculez |Av| = vs / ve. Observez l'opposition de phase.
4. Débranchez CE et mesurez à nouveau : le gain doit tomber vers 3,9.
5. Remettez CE et augmentez ve jusqu'à voir l'écrêtage. Notez l'amplitude d'entrée où il apparaît.

| Mesure | Calculée | Mesurée |
|---|---|---|
| VB | 2,1 V | |
| VE | 1,4 V | |
| VC | 6,5 V | |
| ve crête à crête | 100 mV | |
| vs crête à crête | 3,9 V | |
| abs(Av) avec CE | 39 | |
| abs(Av) sans CE | 3,9 | |

## Variante multimètre seul

Sans générateur, le signal vient de l'adaptateur 9 V AC, réduit par un diviseur.

1. Câblez le montage et vérifiez VB, VE et VC comme dans la variante oscilloscope.
2. Branchez l'adaptateur sur un diviseur : 100 kΩ en série, puis 1 kΩ vers la masse. À vide, la tension aux bornes du 1 kΩ vaut environ 9 × 1 / 101 ≈ 89 mV efficaces ; elle baisse un peu une fois l'amplificateur branché, d'où la mesure de ve.
3. Reliez ce point à C1. Mesurez en V~ (ou mV~) la tension ve sur la base côté C1, puis vs après C2.
4. Calculez abs(Av) = vs / ve avec les valeurs efficaces, et comparez à 39. Le multimètre ne montre pas l'inversion : notez-la d'après le cours.

| Mesure | Calculée | Mesurée |
|---|---|---|
| ve efficace | ≈ 89 mV à vide | |
| vs efficace | 39 × ve | |
| abs(Av) | 39 | |

## Pour conclure

Expliquez pourquoi le gain mesuré est un peu inférieur à 39, et pourquoi il chute quand on retire CE.
