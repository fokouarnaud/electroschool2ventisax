Un **compteur** compte des **fronts montants** : chaque passage de 0 à 1 de son entrée. Il sert à compter des pièces, des cycles, des tours.

## Le CTU : compteur

![Bloc CTU : capteur %IX0.3 sur CU, remise à zéro %IX0.4 sur R, présélection PV = 10, sortie Q vers %QX0.2](/static/content/moteurs/m12/ctu.svg)

- **CU** : chaque front montant ajoute 1 à la valeur courante **CV**.
- **PV** : la présélection. Quand CV ≥ PV, la sortie **Q passe à 1**.
- **R** : la remise à zéro ; CV repart de 0 et Q retombe.

Un capteur qui reste à 1 devant une pièce immobile ne compte qu'**une** fois : seul le front compte.

![Comptage : chaque passage du capteur ajoute 1 ; à la troisième pièce (PV = 3), Q passe à 1 et y reste](/static/content/moteurs/m12/comptage.svg)

## Le CTD : décompteur

- **CD** : chaque front montant retire 1 à CV.
- **LD** (load) : charge la présélection PV dans CV.
- **Q passe à 1 quand CV ≤ 0**.

Exemple : un magasin de 20 pièces. LD charge 20 ; chaque pièce prélevée décompte ; à 0, Q allume le voyant « magasin vide ».

## Limites

- Une impulsion plus courte qu'un **temps de cycle** peut être manquée : pour des pièces très rapides ou un codeur, on utilise une **entrée de comptage rapide**.
- Selon l'automate, la valeur d'un compteur est perdue ou conservée à la coupure (variable **rémanente**) : on vérifie ce point pour un compteur de production.

## À retenir

- CTU : compte les fronts sur CU ; Q quand CV ≥ PV ; R remet à 0.
- CTD : décompte sur CD ; LD charge PV ; Q quand CV ≤ 0.
- Fronts, pas niveaux ; compteur rapide pour les signaux brefs.
