Ce mini-projet se fait en atelier, avec votre formateur. Selon le matériel disponible, suivez la variante oscilloscope ou la variante multimètre seul. Apportez votre tableau de mesures complété.

## Objectif

Mesurer un transformateur **uniquement du côté secondaire** : sa tension à vide et en charge, son rapport de transformation, et en déduire le courant du primaire par le calcul.

## Matériel

| Quantité | Composant |
|---|---|
| 1 | adaptateur secteur **fermé** 230 V vers 12 V AC (ou 9 V AC), environ 10 VA |
| 1 | résistance de 100 Ω, 2 W ou plus |
| 1 | résistance de 47 Ω, 5 W |
| 1 | petit transformateur audio de sortie (par exemple 1 kΩ vers 8 Ω) (variante oscilloscope) |
| 1 | GBF et oscilloscope à deux voies (variante oscilloscope) |
| 1 | multimètre |
| 1 | plaque d'essai et fils |

## Sécurité

- On ne travaille **jamais** côté 230 V : seul l'adaptateur fermé est branché sur le secteur. N'ouvrez jamais son boîtier, ne mesurez jamais son primaire.
- Toutes les mesures se font sur les fils du secondaire (12 V AC), adaptateur débranché pendant le câblage.
- La résistance de 47 Ω dissipe environ 3 W : elle chauffe, ne la touchez pas pendant l'essai et limitez-le à une minute.

## Variante oscilloscope

1. Faites d'abord les mesures 1 à 4 de la variante multimètre seul.
2. Branchez le GBF (sinus, 1 kHz, 2 V crête à crête) sur l'enroulement 1 kΩ du transformateur audio. Voie 1 sur cet enroulement, voie 2 sur l'enroulement 8 Ω.
3. Mesurez les deux tensions crête à crête et calculez le rapport. Comparez avec √(1 000 / 8) ≈ 11,2.
4. Inversez les deux fils de l'enroulement 8 Ω : la trace de la voie 2 passe en opposition de phase.
5. Branchez l'oscilloscope sur le secondaire de l'adaptateur, à vide : vérifiez que Ucc ≈ 2 × √2 × Ueff et que la période vaut 20 ms.

| Grandeur | Calculée | Mesurée |
|---|---|---|
| rapport audio Up / Us | 11,2 | |
| Us crête à crête (audio) | 0,18 V | |
| période du secondaire | 20 ms | |

## Variante multimètre seul

1. Adaptateur branché, sans charge : mesurez la tension du secondaire en V~. Elle dépasse souvent la valeur nominale (par exemple 13,5 V pour un modèle de 12 V).
2. Branchez la résistance de 100 Ω : mesurez Us et le courant Is (multimètre en A~, en série).
3. Remplacez-la par 47 Ω, puis mesurez à nouveau Us et Is.
4. Calculez, pour chaque charge :
   - le rapport m = Us / 230 (tension nominale du secteur) ;
   - le courant du primaire Ip = Is × Us / 230 ;
   - la chute de tension par rapport à la mesure à vide.

| Grandeur | Calculée (12 V) | Mesurée |
|---|---|---|
| Us à vide | | |
| Is sur 100 Ω | 0,12 A | |
| Is sur 47 Ω | 0,26 A | |
| Ip sur 47 Ω | 13 mA | |
| m | 0,052 | |

## Pour conclure

Expliquez pourquoi la tension du secondaire baisse quand le courant augmente, et pourquoi on calcule Ip au lieu de le mesurer.
