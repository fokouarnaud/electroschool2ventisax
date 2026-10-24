Ce mini-projet se fait en atelier, avec votre formateur. Vous mesurez un transformateur uniquement du côté secondaire et vous en déduisez son rendement et sa chute de tension.

## Objectif

Mesurer à vide et en charge la tension et le courant du secondaire d'un petit transformateur, et calculer la puissance apparente, la chute de tension et le courant du primaire.

## Sécurité

- On ne travaille **jamais côté 230 V** : seul un **adaptateur moulé** ou un **transformateur moulé** 230 V vers 12 V AC est branché sur le secteur. N'ouvrez jamais son boîtier et ne mesurez jamais son primaire.
- Toutes les mesures se font au secondaire (12 V AC), adaptateur débranché pendant le câblage.
- La résistance de charge chauffe : ne la touchez pas pendant l'essai et limitez-le à une minute.
- Aucun montage de ce module ne dépasse 24 V.

![Banc du mini-projet : adaptateur moulé 230 V vers 12 V AC, charge résistive, ampèremètre et voltmètre au secondaire](/static/content/moteurs/m3/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | adaptateur moulé 230 V vers 12 V AC, environ 12 VA |
| 1 | résistance de 22 Ω, 10 W |
| 1 | résistance de 47 Ω, 5 W |
| 1 | multimètre (et un second si possible) |
| 1 | oscilloscope (variante oscilloscope) |
| 1 | bornier et fils |

## Variante oscilloscope

1. Faites d'abord les mesures 1 à 3 de la variante multimètre seul.
2. Branchez l'oscilloscope sur le secondaire à vide : mesurez la tension crête et vérifiez que Ueff ≈ Ucrête / √2 et que la période vaut 20 ms (50 Hz).
3. Branchez la charge de 22 Ω et observez que la sinusoïde reste propre, un peu plus petite.

| Grandeur | Calculée | Mesurée |
|---|---|---|
| période | 20 ms | |
| tension crête à vide (12 V eff) | 17 V | |

## Variante multimètre seul

1. Mesurez la tension du secondaire à vide (V~). Elle dépasse souvent 12 V, par exemple 13,5 V.
2. Branchez la charge de 47 Ω : mesurez Us et Is (multimètre en A~, en série).
3. Remplacez-la par 22 Ω, puis mesurez de nouveau Us et Is.
4. Calculez pour chaque charge : la puissance apparente S = Us × Is, la chute de tension par rapport au fonctionnement à vide (en %), et le courant du primaire Ip ≈ Is × Us / 230.

| Grandeur | Calculée (12 V) | Mesurée |
|---|---|---|
| Is sur 47 Ω | 0,26 A | |
| Is sur 22 Ω | 0,55 A | |
| S sur 22 Ω | 6,5 VA | |
| Ip sur 22 Ω | 29 mA | |

## Pour conclure

Expliquez pourquoi la tension du secondaire baisse quand le courant augmente, et pourquoi on calcule le courant du primaire au lieu de le mesurer.
