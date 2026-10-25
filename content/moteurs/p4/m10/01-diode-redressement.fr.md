L'électronique de puissance commute l'énergie d'un moteur au lieu de la dissiper. Tout commence par la **diode** : elle laisse passer le courant de l'anode vers la cathode et le bloque dans l'autre sens. Ce module en fait un rappel rapide ; pour le détail, voyez la [formation Électronique au catalogue](/fr/catalogue/), Partie 1.

## Le pont de diodes monophasé

Quatre diodes montées en **pont** redressent les deux alternances : pendant l'une, deux diodes conduisent ; pendant l'autre, ce sont les deux autres. La charge reçoit un courant toujours de même sens.

![Pont de quatre diodes alimenté par une source alternative ; la charge est branchée entre les deux sorties du pont](/static/content/moteurs/m10/pont.svg)

La tension obtenue est **continue mais ondulée** : elle remonte deux fois par période. Un condensateur de lissage la rend presque constante.

## Le pont triphasé

Dans un variateur ou un chargeur industriel, on redresse le réseau triphasé avec **six diodes**. La tension continue obtenue vaut environ :

**Udc ≈ 1,35 × U** (U : tension entre phases)

Sur un réseau 400 V : 1,35 × 400 ≈ **540 V**. L'ondulation est faible, car six « bosses » se succèdent à chaque période.

![Tension en sortie d'un pont triphasé : six bosses par période, autour de 540 V sur un réseau 400 V](/static/content/moteurs/m10/triphase.svg)

## Choisir une diode de puissance

Deux valeurs comptent : le **courant moyen** qu'elle supporte et la **tension inverse** maximale qu'elle tient à l'état bloqué. On prend une marge confortable sur les deux, et on la monte sur un **dissipateur** : une diode de puissance chute environ 1 V, soit 10 W perdus à 10 A.

## À retenir

- Pont de 4 diodes : redressement des deux alternances.
- Pont triphasé de 6 diodes : Udc ≈ 1,35 × U, soit environ 540 V sur 400 V.
- Choisir une diode par son courant moyen et sa tension inverse, avec un dissipateur.
