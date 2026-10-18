Un composant traversé par un courant transforme de l'énergie électrique, le plus souvent en chaleur. La **puissance** P, en watts (W), indique à quel rythme il le fait :

**P = U × I**

En combinant avec la loi d'Ohm, on obtient deux formes très utiles pour une résistance :

**P = R × I²**   et   **P = U² / R**

![Résistance de 100 Ω sous 10 V : I = 0,1 A et P = 1 W](/static/content/electro/m1/puissance.svg)

## Exemple

Une résistance de 100 Ω est branchée sur 10 V. Le courant vaut 10 / 100 = 0,1 A et la puissance 10 × 0,1 = **1 W**. Une résistance ordinaire de 1/4 W (0,25 W) chaufferait jusqu'à brûler : il faut ici un modèle d'au moins 2 W, car on garde toujours une marge (environ le double de la puissance calculée).

## Le carré qui change tout

Dans P = R × I², le courant est au carré : doubler le courant multiplie la puissance par quatre. C'est pourquoi un petit écart de courant peut suffire à faire chauffer un composant bien au-delà de ce qu'il supporte.

![Courbe de la puissance dissipée dans 100 Ω : 250 mW à 50 mA, 1 W à 100 mA](/static/content/electro/m1/puissance-graph.svg)

## Choisir le bon composant

Chaque composant a une **puissance maximale** indiquée par le fabricant : 0,25 W pour les petites résistances de plaque d'essai, 0,5 W ou plus pour des modèles plus gros. La pile aussi a ses limites : elle ne fournit qu'un courant raisonnable avant que sa tension ne chute.

## À retenir

- P = U × I, en watts ; 1 mW = 0,001 W.
- Pour une résistance : P = R × I² = U² / R.
- Choisissez une puissance nominale d'au moins le double de la puissance calculée.
