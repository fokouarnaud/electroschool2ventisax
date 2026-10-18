Un vrai transformateur chauffe un peu : une partie de la puissance absorbée au primaire n'arrive jamais au secondaire.

## Le bilan de puissance

- **Pp** : puissance absorbée au primaire.
- **Ps** : puissance fournie au secondaire, Ps = Us × Is pour une charge résistive.
- **Pertes** : Pp − Ps, transformées en chaleur.

Le **rendement** compare ce qui sort à ce qui entre :

**η = Ps / Pp**

![Bilan : 14 W entrent au primaire, 12 W sortent au secondaire, 2 W de pertes fer et cuivre ; rendement d'environ 86 %](/static/content/electro/m10/bilan.svg)

Exemple : un transformateur fournit 12 V et 1 A, soit Ps = 12 W, et absorbe Pp = 14 W. η = 12 / 14 ≈ **86 %**. Les 2 W restants chauffent le transformateur.

## D'où viennent les pertes ?

- **Pertes cuivre** : le fil des enroulements a une résistance ; le courant y dissipe R × I². Elles augmentent avec la charge.
- **Pertes fer** : le noyau s'aimante et se désaimante 50 fois par seconde, et des courants parasites (courants de Foucault) circulent dans le fer. On réduit ces courants en empilant des **tôles minces isolées** : c'est le noyau feuilleté. Ces pertes existent même à vide.

Les gros transformateurs dépassent 95 % de rendement ; les petits modèles de quelques watts sont plutôt vers 70 à 85 %.

## La puissance apparente, en VA

La plaque d'un transformateur indique sa puissance en **voltampères** (VA), le produit de la tension et du courant qu'il peut fournir sans trop chauffer. On en déduit le courant maximal du secondaire :

**Is max = puissance (VA) / Us**

![Plaque signalétique : primaire 230 V 50 Hz, secondaire 12 V 1 A, puissance 12 VA](/static/content/electro/m10/plaque.svg)

Exemple : un modèle de 18 VA avec un secondaire de 9 V supporte Is max = 18 / 9 = **2 A**. Au-delà, il chauffe trop et sa tension s'effondre.

## À retenir

- η = Ps / Pp ; les pertes (fer et cuivre) chauffent le transformateur.
- Le noyau feuilleté limite les pertes fer.
- Is max = puissance en VA / Us.
