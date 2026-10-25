Un transistor de puissance ne sert pas ici à amplifier : il sert d'**interrupteur rapide**. Il est soit **bloqué** (aucun courant), soit **saturé** (presque aucune tension à ses bornes). Rappel détaillé : [formation Électronique au catalogue](/fr/catalogue/), Partie 1, transistor en commutation.

## Bipolaire et MOSFET

- Le **transistor bipolaire** se commande par un **courant** de base ; il faut un courant de commande d'autant plus grand que la charge est forte.
- Le **MOSFET** se commande par une **tension** grille-source (souvent 10 V) ; à l'état établi, sa grille ne consomme presque rien. Il commute très vite et domine sous quelques centaines de volts.

![Un MOSFET commande un moteur 12 V ; une diode de roue libre en parallèle sur le moteur écoule son courant à chaque coupure](/static/content/moteurs/m10/mosfet.svg)

## La diode de roue libre

Un moteur ou une bobine **s'oppose** à la coupure de son courant : sans précaution, une surtension détruirait le transistor. La **diode de roue libre**, montée en inverse sur la charge, laisse ce courant s'écouler en douceur. On l'a déjà vue sur les bobines de contacteurs (module 7).

## Pourquoi la commutation dissipe peu

La puissance perdue dans le transistor vaut **P = U × I** à ses bornes :

![Bloqué : 12 V et 0 A, donc 0 W ; saturé : 0,1 V et 2 A, donc 0,2 W, alors que la charge reçoit 24 W](/static/content/moteurs/m10/pertes.svg)

Dans les deux états, l'un des deux facteurs est presque nul. Les pertes viennent surtout des **instants de commutation**, où tension et courant coexistent un bref moment : plus on commute souvent, plus on chauffe.

## À retenir

- En puissance, le transistor est un interrupteur : bloqué ou saturé.
- Bipolaire commandé en courant, MOSFET en tension.
- Diode de roue libre obligatoire sur une charge inductive.
- Pertes faibles, surtout dues aux commutations.
