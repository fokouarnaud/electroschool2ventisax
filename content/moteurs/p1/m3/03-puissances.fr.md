Un moteur absorbe deux sortes de puissance. La **puissance active P** (en kW) se transforme réellement en travail mécanique et en chaleur. La **puissance réactive Q** (en kvar) sert à magnétiser le moteur : elle va et vient entre le réseau et le moteur sans être consommée, mais elle fait circuler du courant. Le réseau doit fournir la **puissance apparente S** (en kVA).

## Le triangle des puissances

Les trois puissances forment un triangle rectangle : S² = P² + Q². L'angle φ entre P et S donne le **facteur de puissance** cos φ = P / S.

![Triangle des puissances : P active à l'horizontale, Q réactive à la verticale, S apparente en hypoténuse, angle φ entre P et S](/static/content/moteurs/m3/triangle.svg)

En triphasé : **P = √3 × U × I × cos φ**, **Q = √3 × U × I × sin φ**, **S = √3 × U × I**.

**Exemple.** Une installation absorbe 100 kW avec cos φ = 0,8. S = P / cos φ = 125 kVA et Q = √(125² − 100²) = 75 kvar.

## Pertes et compensation

Un mauvais cos φ fait circuler plus de courant pour la même puissance utile : les câbles et le transformateur chauffent davantage, et le distributeur facture souvent l'énergie réactive. On installe alors des **condensateurs** qui fournissent eux-mêmes une partie de la puissance réactive : c'est la **compensation**.

![Compensation : avec des condensateurs, Q passe de 75 kvar à 33 kvar pour 100 kW, et cos φ de 0,8 à 0,95](/static/content/moteurs/m3/compensation.svg)

La puissance réactive à installer vaut : **Qc = P × (tan φ1 − tan φ2)**, où φ1 est l'angle avant compensation et φ2 l'angle visé.

**Exemple.** P = 100 kW, cos φ1 = 0,8 (tan φ1 = 0,75), cos φ2 = 0,95 (tan φ2 = 0,329) : Qc = 100 × (0,75 − 0,329) ≈ **42 kvar**. Après compensation, Q ne vaut plus que 33 kvar et S tombe de 125 à 105 kVA.

## À retenir

- S² = P² + Q² ; cos φ = P / S.
- P = √3 × U × I × cos φ en triphasé.
- Compensation : Qc = P × (tan φ1 − tan φ2).
