Deux phénomènes accompagnent chaque manœuvre d'un contacteur : l'**arc** entre ses contacts de puissance, et la **surtension** de sa bobine à la coupure.

## L'extinction de l'arc

Quand les contacts s'ouvrent sous charge, le courant continue de passer un instant dans l'air ionisé : c'est l'arc. Il use les contacts et doit être éteint vite.

![Extinction de l'arc : il s'allonge entre les contacts qui s'ouvrent, puis se fractionne et refroidit dans les plaques de la chambre de coupure](/static/content/moteurs/m7/arc.svg)

Le contacteur l'**allonge** (double coupure, soufflage magnétique) et le **fractionne** dans les plaques métalliques d'une **chambre de coupure**, qui le refroidissent. En alternatif, l'arc s'éteint au passage naturel du courant par zéro, cent fois par seconde à 50 Hz ; en continu, ce passage n'existe pas, c'est pourquoi la coupure en continu est plus difficile.

## La surtension de la bobine

Une bobine stocke de l'énergie magnétique. Quand on coupe son courant brutalement, cette énergie produit une **surtension** de plusieurs centaines de volts, qui perturbe l'électronique voisine (automates, capteurs) et use le contact qui commande la bobine.

![Antiparasitage d'une bobine : diode en parallèle en courant continu, circuit RC ou varistance en alternatif](/static/content/moteurs/m7/antiparasite.svg)

On place donc en parallèle sur la bobine un **module d'antiparasitage** :

- en courant continu, une **diode** (de roue libre), montée en inverse : très efficace, mais elle ralentit un peu l'ouverture ;
- en alternatif, un **circuit RC** ou une **varistance**, qui absorbent la pointe de tension.

Sur les bobines commandées par un automate, l'antiparasitage est indispensable.

## À retenir

- Arc allongé et fractionné dans la chambre de coupure.
- Couper du continu est plus difficile : pas de passage par zéro.
- Bobine : diode en continu, RC ou varistance en alternatif.
