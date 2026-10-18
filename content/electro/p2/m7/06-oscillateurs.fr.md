Un circuit LC ne se contente pas de répondre à une fréquence : chargé une seule fois, il se met à **osciller tout seul** à sa fréquence de résonance. C'est le principe des oscillateurs, étudiés dans la Partie 3.

![Deux états d'un circuit LC : le condensateur chargé stocke l'énergie électrique, puis la bobine parcourue par le courant maximal stocke l'énergie magnétique](/static/content/electro/m7/echange.svg)

## Un échange d'énergie

Chargeons un condensateur, puis relions-le à une bobine :

1. Le condensateur se décharge dans la bobine. Son **énergie électrique** passe dans le champ magnétique de la bobine : quand il est vide, le courant est maximal et toute l'énergie est **magnétique**.
2. La bobine s'oppose à la baisse du courant : elle continue de le pousser et recharge le condensateur **dans l'autre sens**.
3. Le cycle recommence dans l'autre sens, puis encore, à la fréquence f0 = 1 / (2π × √(L × C)).

On peut comparer ce va-et-vient à une balançoire : l'énergie passe de la hauteur (le condensateur) à la vitesse (la bobine) et inversement.

## Des oscillations qui s'éteignent

Dans un circuit réel, le fil de la bobine et les connexions ont une résistance qui transforme une partie de l'énergie en chaleur à chaque aller-retour. L'oscillation garde sa fréquence, mais son amplitude diminue : c'est une **oscillation amortie**.

![Oscillation amortie : la sinusoïde garde sa période mais son amplitude décroît, suivant une enveloppe qui tend vers zéro](/static/content/electro/m7/amortie.svg)

Plus le facteur Q est élevé (pertes faibles), plus l'oscillation dure longtemps.

## Entretenir l'oscillation

Pour obtenir une sinusoïde permanente, il faut **rendre au circuit l'énergie perdue** à chaque cycle, au bon moment, comme on pousse une balançoire au bon instant. Ce rôle est confié à un **amplificateur** (un transistor) qui réinjecte une partie du signal : on obtient un **oscillateur**. Les amplificateurs et les oscillateurs font l'objet de la Partie 3.

## À retenir

- Dans un LC, l'énergie passe du condensateur à la bobine et revient, à la fréquence f0.
- Les pertes amortissent l'oscillation.
- Un oscillateur compense ces pertes avec un amplificateur.
