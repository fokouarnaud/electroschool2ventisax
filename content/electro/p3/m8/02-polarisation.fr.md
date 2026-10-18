Pour amplifier un signal qui monte et qui descend, le transistor doit déjà conduire un peu au repos, en plein régime linéaire. Ce réglage au repos s'appelle la **polarisation** et fixe le **point de repos** (IC, VCE).

## Le problème de la résistance de base seule

En Partie 1, une seule résistance RB fixait le courant de base. Mais IC = β × IB, et β varie beaucoup : de 100 à 300 pour un même modèle, et il change avec la température. Avec IB = 13 µA, un transistor donne 1,3 mA, son voisin 3,9 mA : le second sature. Le montage dépend du transistor qu'on a sous la main.

## Le pont de base et la résistance d'émetteur

La solution courante utilise un **pont diviseur** R1, R2 sur la base et une **résistance d'émetteur** RE.

![Montage polarisé par pont de base : R1 de 47 kΩ et R2 de 10 kΩ fixent VB, RC de 3,9 kΩ au collecteur, RE de 1 kΩ à l'émetteur, sous 12 V](/static/content/electro/m8/pont.svg)

Le calcul se fait en quatre étapes, avec VCC = 12 V, R1 = 47 kΩ, R2 = 10 kΩ, RC = 3,9 kΩ et RE = 1 kΩ :

1. Tension de base (diviseur de tension) : VB = 12 × 10 / (47 + 10) ≈ **2,1 V**.
2. Tension d'émetteur, 0,7 V plus bas : VE ≈ 2,1 − 0,7 = **1,4 V**.
3. Courant d'émetteur : IE = VE / RE ≈ 1,4 V / 1 kΩ = **1,4 mA**, et IC ≈ IE.
4. Tension collecteur-émetteur : VCE = VCC − IC × (RC + RE) ≈ 12 − 1,4 mA × 4,9 kΩ ≈ **5,1 V**.

β n'apparaît dans aucune de ces lignes : le point de repos ne dépend plus du transistor.

![IC en fonction de β : avec RB seule, IC grimpe jusqu'à la saturation ; avec le pont et RE, il reste près de 1,3 à 1,4 mA](/static/content/electro/m8/beta.svg)

## Pourquoi ça marche

Si IC augmente (transistor plus « fort », ou chaleur), VE = IE × RE augmente aussi. Comme VB est tenue par le pont, VBE diminue, ce qui freine le courant de base : le montage se corrige tout seul. C'est une **contre-réaction**.

Pour que VB reste bien fixée, le courant du pont doit être grand devant IB. Règle pratique : **R2 ≤ β × RE / 10**. Ici, avec β = 100 : 10 kΩ ≤ 100 × 1 kΩ / 10 = 10 kΩ, la règle est tenue.

## À retenir

- La polarisation fixe le point de repos (IC, VCE) au milieu de la plage utile.
- Pont de base + RE : VB par le diviseur, VE = VB − 0,7 V, IC ≈ VE / RE.
- Le point de repos ne dépend presque plus de β.
