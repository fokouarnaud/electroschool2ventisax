La **plaque signalétique** est la carte d'identité du moteur. Tout ce qu'il faut pour le raccorder, le protéger et le remplacer y figure.

![Plaque d'un moteur de 2,2 kW : 230 V triangle ou 400 V étoile, 8,3 A ou 4,8 A, 1 440 tr/min, cos φ 0,81, 50 Hz, rendement 82 %, IP55, classe F, service S1](/static/content/moteurs/m2/plaque.svg)

| Indication | Signification |
|---|---|
| 230 V Δ / 400 V Y | tensions et couplages possibles |
| 8,3 A / 4,8 A | courant nominal pour chaque tension |
| 2,2 kW | puissance **utile**, mécanique, sur l'arbre |
| 1 440 tr/min | vitesse à pleine charge (synchronisme : 1 500 tr/min) |
| cos φ 0,81 | facteur de puissance |
| η 82 % | rendement |
| IP55 | protection contre les poussières et les jets d'eau |
| classe F | classe d'isolation (155 °C au plus) |
| S1 | service continu |

## Choisir le couplage

Un enroulement de ce moteur supporte **230 V** (la plus petite des deux tensions). On choisit donc le couplage qui lui donne 230 V.

![Choix du couplage : sur un réseau 400 V on couple en étoile, sur un réseau 230 V en triangle](/static/content/moteurs/m2/tensions.svg)

Sur le réseau 400 V usuel, ce moteur se couple **en étoile** et absorbe 4,8 A. Un moteur marqué 400 V Δ / 690 V Y se couple, lui, en triangle sur ce même réseau.

## Retrouver le courant par le calcul

Le courant nominal se déduit des autres indications : I = P / (√3 × U × cos φ × η) = 2 200 / (1,732 × 400 × 0,81 × 0,82) ≈ **4,8 A**. Vérifiez-le avec le calculateur :

[[calc:motor_current]]

## À retenir

- La puissance de la plaque est la puissance utile, sur l'arbre.
- La plus petite tension de la plaque est celle d'un enroulement.
- 400 V et 230 V Δ / 400 V Y : couplage étoile.
