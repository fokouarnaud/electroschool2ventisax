Une bobine peut remplacer le condensateur dans un filtre. Sa réactance XL varie dans l'autre sens que Xc : elle **augmente** avec la fréquence. Les rôles s'inversent donc.

![Filtre passe-bas RL : bobine de 10 mH en série, résistance de 100 Ω vers la masse, sortie Vs aux bornes de la résistance](/static/content/electro/m6/rl-passe-bas.svg)

## Passe-bas et passe-haut RL

Avec la bobine **en série** et la sortie **aux bornes de R** :

- aux basses fréquences, XL est petite : la bobine laisse passer, Vs ≈ Ve ;
- aux hautes fréquences, XL devient grande : la bobine bloque, Vs → 0.

C'est un **passe-bas**. Si l'on prend la sortie **aux bornes de la bobine**, on obtient au contraire un **passe-haut**.

| Filtre | En série | Sortie aux bornes de |
|---|---|---|
| Passe-bas RC | R | C |
| Passe-haut RC | C | R |
| Passe-bas RL | L | R |
| Passe-haut RL | R | L |

## Impédance, coupure et déphasage

Les formules suivent le même modèle que pour le RC, avec XL :

- **Z = √(R² + XL²)** ;
- **fc = R / (2π × L)** : à fc, XL = R et Vs ≈ 0,707 × Ve ;
- **φ = arctan(XL / R)** ; dans un RL série, le courant est **en retard** sur la tension d'entrée.

Exemple : R = 100 Ω et L = 10 mH. fc = 100 / (2 × 3,14 × 0,01) ≈ **1 592 Hz**. Avec R = 220 Ω et la même bobine, fc ≈ 3 501 Hz.

![Réponse du passe-bas RL de 100 Ω et 10 mH : Vs / Ve vaut 1 aux basses fréquences et 0,707 vers 1,6 kHz](/static/content/electro/m6/rl-courbe.svg)

## RC ou RL ?

Aux fréquences audio, les condensateurs sont petits, bon marché et précis : on préfère le RC. Les bobines servent plutôt quand les courants sont forts (filtres d'alimentation, filtres d'enceintes) ou aux hautes fréquences (radio).

## À retenir

- XL augmente avec f : bobine en série et sortie sur R donnent un passe-bas.
- fc = R / (2π × L).
- Dans un RL série, le courant est en retard sur la tension.
