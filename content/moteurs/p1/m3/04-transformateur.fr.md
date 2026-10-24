Le principe du transformateur (deux enroulements sur un noyau, Us / Up = Ns / Np) est vu dans la formation Électronique. Ici, on s'intéresse au **transformateur de distribution** qui alimente une usine.

## La plaque du transformateur

![Plaque d'un transformateur de distribution : 630 kVA, 50 Hz, 20 kV / 410 V, 18,2 A / 887 A, couplage Dyn11, tension de court-circuit 4 %, pertes à vide 1 kW, pertes en charge 6,5 kW](/static/content/moteurs/m3/plaque-transfo.svg)

- **Puissance assignée en kVA** : c'est une puissance apparente, car le transformateur chauffe selon le courant, quel que soit le cos φ de la charge.
- **Tensions** : 20 kV au primaire, 410 V à vide au secondaire (un peu plus que 400 V, pour compenser la chute de tension en charge).
- **Courants assignés** : I = S / (√3 × U). Au secondaire : 630 000 / (1,732 × 410) ≈ **887 A**.
- **Couplage** : Dyn11 (section 5).
- **Tension de court-circuit ucc** : 4 % ; elle fixe le courant de court-circuit au secondaire, environ 887 / 0,04 ≈ 22 kA.

## Pertes et rendement

Un transformateur a deux sortes de pertes : les **pertes fer**, dans le noyau, constantes dès qu'il est sous tension (pertes à vide), et les **pertes cuivre**, dans les enroulements, qui croissent comme le carré de la charge.

![Rendement du transformateur de 630 kVA selon sa charge : toujours supérieur à 98 %, maximal vers 40 % de charge](/static/content/moteurs/m3/rendement.svg)

Le rendement est maximal quand les deux pertes sont égales. Ici : 1 kW = 6,5 kW × x², soit x ≈ 0,39 : vers **40 % de charge**. Un transformateur surdimensionné, presque toujours à vide, gaspille ses pertes fer ; un transformateur surchargé chauffe et vieillit vite.

Pour un rapport de transformation, utilisez le calculateur :

[[calc:transformer]]

## À retenir

- Puissance en kVA ; I = S / (√3 × U).
- Pertes fer constantes, pertes cuivre en carré de la charge.
- Rendement maximal quand pertes fer = pertes cuivre.
