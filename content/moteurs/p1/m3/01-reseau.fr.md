L'énergie qui fait tourner un moteur d'usine a souvent parcouru des centaines de kilomètres. Elle change plusieurs fois de tension en chemin.

![De la centrale à l'usine : production, transport à 400 kV, poste source, distribution à 20 kV, poste HTA/BT, 400 V à l'usine](/static/content/moteurs/m3/chaine.svg)

1. La **centrale** produit, par exemple à 20 kV.
2. Un transformateur élève la tension pour le **transport** à très haute tension (225 ou 400 kV).
3. Le **poste source** l'abaisse pour la **distribution** en HTA, souvent 20 kV.
4. Un **poste HTA/BT**, au bout d'une rue ou dans l'usine elle-même, l'abaisse à **400 V entre phases** (230 V entre phase et neutre) : c'est la tension des moteurs.

## Pourquoi monter en tension ?

Pour une même puissance, le courant est d'autant plus faible que la tension est élevée : en triphasé, I = P / (√3 × U). Or les pertes dans les câbles valent **3 × R × I²** : elles varient comme le carré du courant.

![Pertes en ligne pour transporter 100 kW avec 0,1 Ω par conducteur : 6,25 kW à 400 V, 2,5 W à 20 kV](/static/content/moteurs/m3/pertes-ligne.svg)

**Exemple.** Transporter 100 kW sur une ligne de 0,1 Ω par conducteur :

- à 400 V : I = 100 000 / (1,732 × 400) = 144 A, pertes = 3 × 0,1 × 144² ≈ **6,25 kW** ;
- à 20 kV : I = 2,89 A, pertes = 3 × 0,1 × 2,89² ≈ **2,5 W**.

La tension 50 fois plus élevée divise les pertes par 50² = 2 500. C'est pour cela qu'on transporte en haute tension et qu'on n'abaisse qu'au plus près des utilisateurs.

## À retenir

- Production, transport (THT), distribution (HTA), puis 400 V au poste HTA/BT.
- I = P / (√3 × U) ; pertes = 3 × R × I².
- Multiplier la tension par k divise les pertes par k².
