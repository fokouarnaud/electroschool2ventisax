Un filtre ne coupe pas net : la sortie diminue progressivement. Pour le caractériser par un seul nombre, on définit sa **fréquence de coupure** fc.

![Xc diminue avec la fréquence et croise la droite R = 1 kΩ à la fréquence de coupure](/static/content/electro/m6/coupure.svg)

## Xc = R

La fréquence de coupure est celle où la réactance du condensateur égale la résistance. En écrivant 1 / (2π × f × C) = R, on obtient :

**fc = 1 / (2π × R × C)**

Exemple : R = 1 kΩ et C = 100 nF. fc = 1 / (2 × 3,14 × 1 000 × 0,000 000 1) ≈ **1 592 Hz**, soit environ 1,6 kHz.

Pour choisir un composant, retournez la formule : **R = 1 / (2π × fc × C)** ou **C = 1 / (2π × fc × R)**. Pour fc = 1 kHz avec C = 100 nF, il faut R ≈ 1 592 Ω.

[[calc:cutoff]]

## 70,7 % de l'entrée, ou −3 dB

À fc, Xc = R : Z = √(R² + R²) = R × √2. La sortie vaut alors Ve / √2 :

**À fc : Vs ≈ 0,707 × Ve**, pour un passe-bas comme pour un passe-haut.

Les électroniciens disent qu'à fc, le filtre atténue de **3 décibels (−3 dB)**. Retenez simplement : −3 dB ≈ 70,7 % de la tension d'entrée. Avec Ve = 5 V à la fréquence de coupure, Vs ≈ 3,54 V.

![Passe-bas : la sortie vaut environ 99 % de l'entrée à fc / 10, 70,7 % à fc et 10 % à 10 × fc](/static/content/electro/m6/attenuation.svg)

## Des repères d'une décade à l'autre

Pour un passe-bas RC :

- à **fc / 10**, Vs ≈ 99 % de Ve : le signal passe ;
- à **fc**, Vs ≈ 70,7 % de Ve ;
- à **10 × fc**, Vs ≈ 10 % de Ve : le signal est fortement atténué.

Pour un passe-haut, c'est l'inverse : 10 % à fc / 10 et 99 % à 10 × fc.

## À retenir

- fc = 1 / (2π × R × C) : à fc, Xc = R.
- À fc, Vs ≈ 0,707 × Ve (−3 dB).
- Une décade au-delà de fc, un passe-bas ne laisse plus passer qu'environ 10 %.
