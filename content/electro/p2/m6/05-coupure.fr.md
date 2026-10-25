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

## Ce qui se passe dans le circuit

Le même courant traverse R puis C. Chacun prend une part de la tension d'entrée à la mesure de son opposition au courant : R pour la résistance, Xc pour le condensateur. Mais ces deux tensions ne culminent pas au même instant : VR suit le courant, Vc a un quart de période de retard sur lui. Leurs amplitudes ne s'additionnent donc pas comme des nombres, elles se combinent comme les côtés d'un triangle rectangle : VR² + Vc² = Ve².

À fc / 10, Xc = 10 kΩ, dix fois R : presque toute la tension se retrouve aux bornes du condensateur (Vs ≈ 0,995 × Ve) et la résistance n'en prend que 0,0995 × Ve. À 10 × fc, Xc = 100 Ω et c'est l'inverse. À fc exactement, Xc = R : les deux parts sont égales, et comme 0,707² + 0,707² = 1, chacune vaut 0,707 × Ve, et non la moitié.

Sur le banc ci-dessous, le manomètre posé sur la vanne lit VR, celui du nœud lit Vs, et l'aiguille de crête de chaque cadran garde l'amplitude. Cherchez la fréquence où les deux crêtes se rejoignent sur le repère 0,707 : c'est fc.

[[fig:rc_cutoff]]

## Des repères d'une décade à l'autre

![Passe-bas : la sortie vaut environ 99 % de l'entrée à fc / 10, 70,7 % à fc et 10 % à 10 × fc](/static/content/electro/m6/attenuation.svg)

Pour un passe-bas RC :

- à **fc / 10**, Vs ≈ 99 % de Ve : le signal passe ;
- à **fc**, Vs ≈ 70,7 % de Ve ;
- à **10 × fc**, Vs ≈ 10 % de Ve : le signal est fortement atténué.

Pour un passe-haut, c'est l'inverse : 10 % à fc / 10 et 99 % à 10 × fc.

## À retenir

- fc = 1 / (2π × R × C) : à fc, Xc = R.
- À fc, Vs ≈ 0,707 × Ve (−3 dB).
- Une décade au-delà de fc, un passe-bas ne laisse plus passer qu'environ 10 %.
