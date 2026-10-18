Ce mini-projet se fait en atelier, avec votre formateur. Selon le matériel disponible, suivez la variante oscilloscope ou la variante multimètre seul. Apportez votre tableau de mesures complété.

## Objectif

Construire l'alimentation 5 V du module à partir d'un adaptateur 12 V AC, et mesurer chaque étape : redressement, lissage, ondulation et régulation.

## Matériel

| Quantité | Composant |
|---|---|
| 1 | adaptateur secteur **fermé** 230 V vers 12 V AC, 10 VA environ |
| 4 | diodes 1N4001 (ou un pont redresseur 1 A) |
| 1 | condensateur électrolytique de 2 200 µF, 25 V ou plus |
| 1 | régulateur 7805 en boîtier TO-220 et un petit radiateur |
| 1 | condensateur de 330 nF et 1 de 100 nF |
| 1 | résistance de 100 Ω, 1 W, et 1 de 47 Ω, 1 W |
| 1 | LED et sa résistance de 330 Ω (témoin) |
| 1 | oscilloscope (variante oscilloscope) |
| 1 | multimètre |
| 1 | plaque d'essai et fils de section suffisante |

## Sécurité

- Seul l'adaptateur **fermé** est branché sur le 230 V. N'ouvrez jamais son boîtier et ne travaillez que du côté 12 V.
- Débranchez l'adaptateur avant chaque modification, et attendez que le condensateur se décharge (la LED témoin s'éteint).
- Respectez la polarité du condensateur de 2 200 µF : monté à l'envers, il peut éclater. Ne vous penchez pas au-dessus à la mise sous tension.
- Le régulateur et les résistances chauffent : ne les touchez pas en fonctionnement.

## Variante oscilloscope

1. Montez le pont seul, chargé par 100 Ω. À l'oscilloscope, observez la double alternance : 15,6 V crête environ et une période de 10 ms.
2. Ajoutez le condensateur de 2 200 µF. Mesurez la tension crête et l'ondulation ΔU (couplage AC de la voie pour agrandir l'ondulation). Calculez ΔU ≈ I / (100 × 0,002 2) avec I ≈ 15 V / 100 Ω = 0,15 A.
3. Ajoutez le 7805, ses deux condensateurs et le radiateur, puis la LED témoin. Chargez la sortie par 100 Ω, puis par 47 Ω : la sortie reste à 5 V et l'ondulation disparaît.

| Grandeur | Calculée | Mesurée |
|---|---|---|
| crête après le pont | 15,6 V | |
| ΔU avec 2 200 µF, 0,15 A | 0,68 V | |
| sortie du 7805 sur 100 Ω | 5,0 V | |
| sortie du 7805 sur 47 Ω | 5,0 V | |

## Variante multimètre seul

1. Pont seul, chargé par 100 Ω : mesurez la tension en V continu. Le multimètre affiche la valeur **moyenne**, environ 0,64 × 15,6 ≈ 9,9 V.
2. Ajoutez le condensateur : la tension continue monte vers 15 V. Débranchez la charge : elle atteint la tension crête, environ 15,6 V.
3. Avec la charge, passez le multimètre en V~ : la plupart des appareils affichent alors une valeur liée à l'ondulation (vérifiez avec votre formateur que le vôtre bloque bien le continu dans ce calibre).
4. Ajoutez le régulateur et mesurez la sortie à vide, sur 100 Ω puis sur 47 Ω. Calculez la puissance dissipée dans le 7805 : P = (Ue − 5) × I.

| Grandeur | Calculée | Mesurée |
|---|---|---|
| pont seul, valeur moyenne | 9,9 V | |
| avec C, à vide | 15,6 V | |
| sortie sur 47 Ω | 5,0 V | |
| P dans le 7805 sur 47 Ω | ≈ 1 W | |

## Pour conclure

Expliquez pourquoi la tension à vide après le condensateur dépasse 12 V, et pourquoi le régulateur chauffe davantage avec la charge de 47 Ω.
