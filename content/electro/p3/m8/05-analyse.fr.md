Avant de brancher un générateur, on vérifie qu'un amplificateur est bien polarisé. Cette **analyse en continu** se fait en quelques minutes, au calcul puis au multimètre.

## La méthode

Pour le montage du module (12 V, R1 = 47 kΩ, R2 = 10 kΩ, RC = 3,9 kΩ, RE ≈ 1 kΩ) :

| Étape | Calcul | Résultat |
|---|---|---|
| 1. VB | 12 × 10 / 57 | 2,1 V |
| 2. VE | VB − 0,7 | 1,4 V |
| 3. IC ≈ IE | VE / RE | 1,4 mA |
| 4. VC | 12 − IC × RC | 6,5 V |
| 5. VCE | VC − VE | 5,1 V |

Au multimètre, on mesure VB, VE et VC par rapport à la masse : si l'écart avec le calcul dépasse 10 % environ, on cherche une erreur de câblage ou une résistance de mauvaise valeur.

## La droite de charge

Tous les points de fonctionnement possibles du transistor se trouvent sur une droite, la **droite de charge**, qui relie :

- le **blocage** : IC = 0, VCE = VCC = 12 V ;
- la **saturation** : VCE ≈ 0, IC sat = VCC / (RC + RE) = 12 V / 4,9 kΩ ≈ **2,45 mA**.

![Droite de charge de 2,45 mA à 12 V, avec le point de repos Q à 5,1 V et 1,4 mA, près du milieu](/static/content/electro/m8/droite.svg)

Le point de repos Q (5,1 V ; 1,4 mA) est proche du milieu : le signal pourra monter et descendre de part et d'autre sans buter.

## L'écrêtage

Si le signal de sortie devient trop grand, le transistor atteint le blocage d'un côté ou la saturation de l'autre. La sinusoïde est alors **écrêtée** : ses sommets sont aplatis et le son devient distordu.

![Tension VCE trop grande : ses sommets sont aplatis à 12 V (blocage) et ses creux près de 0 V (saturation)](/static/content/electro/m8/ecretage.svg)

Ici, VC peut descendre d'environ 4,9 V (jusqu'à VE + 0,2 V) avant la saturation. La sortie reste propre jusqu'à environ **4,9 V crête**, soit une entrée d'au plus 4,9 / 39 ≈ **0,13 V crête** avec un gain de 39.

Un point de repos trop près de la saturation ou du blocage réduit cette marge d'un côté : l'écrêtage apparaît alors dès les petits signaux, sur une seule moitié de la sinusoïde.

## À retenir

- Analyse en continu : VB, VE, IC, VC puis VCE, vérifiés au multimètre.
- Droite de charge : de IC sat = VCC / (RC + RE) à VCE = VCC.
- Un point de repos au milieu laisse la plus grande sortie sans écrêtage.
