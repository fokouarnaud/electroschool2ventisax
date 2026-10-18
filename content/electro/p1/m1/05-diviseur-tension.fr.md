Deux résistances en série partagent la tension du générateur. En prenant la tension au point milieu, on obtient une tension plus faible, choisie par le rapport des résistances : c'est le **diviseur de tension**, l'un des montages les plus utilisés en électronique.

![Diviseur de tension : R1 = 10 kΩ en haut, R2 = 4,7 kΩ en bas, Vs prise au point milieu](/static/content/electro/m1/diviseur.svg)

## La formule

Le même courant traverse R1 et R2. La tension de sortie, prise aux bornes de R2, vaut :

**Vs = Ve × R2 / (R1 + R2)**

Exemple : Ve = 12 V, R1 = 10 kΩ et R2 = 4,7 kΩ. Vs = 12 × 4,7 / 14,7 ≈ **3,84 V**. Si R1 = R2, la sortie vaut exactement la moitié de l'entrée.

[[calc:divider]]

## Attention à la charge

La formule suppose que rien ne consomme de courant à la sortie. Si l'on branche une résistance de charge RL sur Vs, elle se retrouve en parallèle avec R2 et la tension baisse.

![Diviseur de deux résistances de 10 kΩ chargé par RL = 10 kΩ : Vs passe de 6 V à 4 V](/static/content/electro/m1/diviseur-charge.svg)

Avec R1 = R2 = RL = 10 kΩ sous 12 V : à vide, Vs = 6 V. Chargé, R2 et RL en parallèle valent 5 kΩ, et Vs = 12 × 5 / 15 = **4 V**. Règle pratique : pour que la charge perturbe peu le diviseur, elle doit être au moins dix fois plus grande que R2.

## À retenir

- Vs = Ve × R2 / (R1 + R2), avec Vs prise aux bornes de R2.
- Une charge en sortie se met en parallèle avec R2 et fait baisser Vs.
- Charge au moins dix fois plus grande que R2 pour rester précis.
