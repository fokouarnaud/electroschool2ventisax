Un circuit résonant ne répond pas qu'à f0 : il laisse aussi passer les fréquences voisines. Deux grandeurs mesurent cette largeur : la **bande passante** et le **facteur de qualité** Q.

![Courbe I / Imax autour de 5 kHz : elle reste au-dessus de 0,707 entre f1 et f2, soit une bande passante d'environ 796 Hz](/static/content/electro/m7/bande.svg)

## La bande passante

On reprend le seuil des filtres : 0,707 du maximum, soit −3 dB. Les deux fréquences où le courant vaut 0,707 × Imax s'appellent f1 (en dessous de f0) et f2 (au-dessus). La **bande passante** est l'écart entre elles :

**BP = f2 − f1**

Exemple : f1 = 9,5 kHz et f2 = 10,5 kHz donnent BP = 1 kHz.

## Le facteur de qualité Q

Q compare la fréquence de résonance à la bande passante :

**Q = f0 / BP**   donc   **BP = f0 / Q**

Pour un circuit RLC série, Q se calcule aussi à partir des composants : **Q = XL / R**, avec XL prise à f0.

Exemple du circuit de ce module : L = 10 mH, C = 100 nF, R = 50 Ω. À f0 ≈ 5 033 Hz, XL ≈ 316 Ω, donc Q ≈ 316 / 50 ≈ **6,3**, et BP ≈ 5 033 / 6,3 ≈ **796 Hz**. On trouve f1 ≈ 4,65 kHz et f2 ≈ 5,45 kHz.

![Deux courbes normalisées : Q ≈ 6,3 donne un pic étroit, Q ≈ 1,6 un pic large](/static/content/electro/m7/q.svg)

## Sélectif ou large

- **Q élevé** (R faible) : bande passante étroite, le circuit est **sélectif**. Il distingue deux fréquences proches, comme deux stations de radio.
- **Q faible** (R élevée) : bande passante large, le circuit accepte toute une plage de fréquences.

À la résonance, la tension aux bornes de L ou de C vaut **Q fois** la tension de la source : avec Q = 20 et 1 V en entrée, 20 V apparaissent aux bornes du condensateur. Choisissez des composants qui le supportent.

## Ce qui se passe dans le circuit

Ramenées à leur maximum, les deux courbes culminent ensemble à 1, à f0 : seule leur largeur diffère. Avec R = 50 Ω, le courant tombe à 0,707 × Imax dès que XL − XC atteint ±50 Ω, car Z vaut alors R × √2 : c'est à f1 ≈ 4,65 kHz et f2 ≈ 5,45 kHz, d'où BP ≈ 796 Hz et Q = 5 033 / 796 ≈ 6,3. Avec R = 200 Ω, il faut que XL − XC atteigne ±200 Ω, ce qui n'arrive qu'à 3,69 kHz et 6,87 kHz : BP ≈ 3,18 kHz et Q ≈ 1,6.

Placez le portique sur f1 : la plume teal touche la ligne 0,707, tandis que la plume grise est encore à 0,970. Le circuit de Q élevé a déjà perdu près d'un tiers de son courant quand l'autre répond presque pleinement : c'est ce qui le rend sélectif.

[[fig:rlc_bandwidth]]

## À retenir

- BP = f2 − f1, mesurée à 0,707 × Imax.
- Q = f0 / BP ; en RLC série, Q = XL / R à f0.
- Q élevé : circuit sélectif et surtensions importantes sur L et C.
