Un moteur dont l'isolation se dégrade peut mettre sa **carcasse** sous tension : c'est un **défaut d'isolement**. Celui qui touche alors la carcasse subit un **contact indirect** : il touche une pièce qui n'aurait jamais dû être sous tension. Deux mesures complémentaires le protègent : la mise à la terre des masses et la coupure automatique.

## Relier les masses à la terre

Toutes les parties métalliques accessibles (carcasses de moteurs, armoires, goulottes) sont reliées au **conducteur de protection PE** (vert et jaune), lui-même relié à la prise de terre. En cas de défaut, le courant trouve un chemin facile vers la terre au lieu de passer par une personne.

![Défaut d'isolement : la phase touche la carcasse du moteur ; le conducteur PE ramène le courant de défaut vers la prise de terre](/static/content/moteurs/m1/defaut.svg)

La terre seule ne suffit pas : tant que le défaut dure, la carcasse reste à une tension dangereuse par rapport au sol. Il faut **couper** l'alimentation, et vite.

## Le dispositif différentiel résiduel (DDR)

Le DDR surveille la différence entre le courant qui part par la phase et celui qui revient par le neutre. Sans défaut, les deux sont égaux. Si une partie du courant s'échappe vers la terre (par le PE ou par une personne), la différence apparaît et le DDR coupe.

![Principe du DDR : le tore compare le courant aller I1 et le courant retour I2 ; si l'écart atteint 30 mA, le déclencheur coupe](/static/content/moteurs/m1/ddr.svg)

- Un DDR de **30 mA** (haute sensibilité) protège les personnes, y compris contre un contact direct accidentel.
- Un DDR de 300 mA protège plutôt les installations contre l'incendie.
- On le teste régulièrement avec son bouton « test ».

**Exemple.** I1 = 10 A et I2 = 9,97 A : l'écart vaut 30 mA, un DDR 30 mA déclenche. Le courant de la charge (10 A) n'intervient pas : seul l'écart compte.

## À retenir

- Défaut d'isolement : la carcasse passe sous tension ; on parle de contact indirect.
- Masses reliées au PE + coupure automatique.
- Le DDR 30 mA coupe dès que 30 mA s'échappent du circuit.
