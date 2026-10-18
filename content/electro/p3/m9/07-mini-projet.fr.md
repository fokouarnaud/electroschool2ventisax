Ce mini-projet se fait en atelier, avec votre formateur. Selon le matériel disponible, suivez la variante oscilloscope ou la variante multimètre seul. Apportez votre tableau de mesures complété.

## Objectif

Faire osciller un pont de Wien à AOP, mesurer sa fréquence et la comparer au calcul f = 1 / (2π × R × C), puis vérifier qu'il faut un gain d'au moins 3 pour qu'il démarre.

## Matériel

| Quantité | Composant |
|---|---|
| 1 | plaque d'essai et fils |
| 1 | AOP double (TL072 ou équivalent) |
| 2 | piles de 9 V et leurs coupleurs (alimentation ±9 V) |
| 2 | résistances de 10 kΩ (R) et 1 de 10 kΩ (Rin) |
| 1 | potentiomètre de 47 kΩ monté en résistance variable (Rf) |
| 2 | condensateurs film de 16 nF (ou 15 nF), et 2 de 1 µF film (variante multimètre seul) |
| 2 | résistances de 100 kΩ (variante multimètre seul) |
| 2 | LED de couleurs différentes et une résistance de 1 kΩ |
| 1 | buzzer piézo **passif** (sans oscillateur intégré) |
| 1 | oscilloscope (variante oscilloscope) |
| 1 | multimètre |

## Sécurité

- Le montage est alimenté par deux piles de 9 V : aucun branchement au 230 V n'est nécessaire dans ce mini-projet.
- Vérifiez le brochage de l'AOP (encoche, broche 1) et la polarité des piles avant de les brancher : un AOP alimenté à l'envers chauffe et se détruit.
- Débranchez une pile avant chaque modification du montage.

## Variante oscilloscope

1. Calculez f pour R = 10 kΩ et C = 16 nF (environ 995 Hz).
2. Câblez le pont de Wien de la section « Quartz et oscillateur RC », avec Rf remplacée par le potentiomètre réglé au maximum.
3. Branchez l'oscilloscope en sortie. Tournez lentement le potentiomètre : notez la valeur de Rf (mesurée à l'ohmmètre, montage débranché) à partir de laquelle l'oscillation démarre. Vérifiez qu'elle est proche de 20 kΩ (gain de 3).
4. Réglez Rf juste au-dessus du seuil pour une sinusoïde propre, puis mesurez la période et calculez f.
5. Branchez le buzzer passif en sortie à travers la résistance de 1 kΩ : vous entendez la note de 1 kHz.

| Grandeur | Calculée | Mesurée |
|---|---|---|
| Rf au démarrage | 20 kΩ | |
| T | 1,005 ms | |
| f | 995 Hz | |

## Variante multimètre seul

Sans oscilloscope, on ralentit l'oscillateur pour le voir.

1. Remplacez les deux R par 100 kΩ et les deux C par 1 µF : f = 1 / (2π × 100 000 × 0,000 001) ≈ 1,6 Hz.
2. Branchez en sortie les deux LED tête-bêche, en série avec la résistance de 1 kΩ, vers la masse : elles s'allument à tour de rôle.
3. Comptez les allumages d'une LED pendant 30 s et déduisez f (environ 48 allumages attendus).
4. Remettez R = 10 kΩ et C = 16 nF. Mesurez la tension de sortie en V~ (le multimètre donne une valeur indicative à 1 kHz) et écoutez la note au buzzer passif.

| Grandeur | Calculée | Mesurée |
|---|---|---|
| allumages en 30 s | ≈ 48 | |
| f (version lente) | 1,6 Hz | |
| Rf au démarrage | 20 kΩ | |

## Pour conclure

Expliquez pourquoi l'oscillateur ne démarre pas tant que Rf est inférieure à environ 20 kΩ, et pourquoi la sinusoïde se déforme quand on augmente trop Rf.
