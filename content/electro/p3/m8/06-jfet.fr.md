Le JFET, vu en Partie 1 comme interrupteur, sait aussi amplifier. Son grand atout : sa **grille ne consomme presque aucun courant**, donc l'entrée du montage ne charge pas la source.

![Amplificateur à JFET en source commune : C1 et RG de 1 MΩ sur la grille, RD de 2,2 kΩ au drain, RS de 470 Ω découplée par CS à la source](/static/content/electro/m8/jfet-ampli.svg)

## La polarisation automatique

Un JFET canal N conduit le plus quand VGS = 0 et se bloque quand VGS atteint sa tension de blocage, ici **−4 V**. Pour amplifier, on le place entre les deux, avec une grille un peu négative par rapport à la source.

L'astuce : la grille est reliée à la masse par RG (1 MΩ, aucun courant ne la traverse), et une résistance **RS** est placée dans la source. Le courant ID qui la traverse élève la source au-dessus de la masse, ce qui rend la grille négative par rapport à la source :

**VGS = −ID × RS**

![Courbe de transfert : ID vaut 8 mA à VGS = 0 et s'annule à −4 V ; le point de repos est vers −1,5 V et 3,1 mA](/static/content/electro/m8/jfet-courbe.svg)

Exemple : pour un point de repos à VGS = −1,5 V et ID ≈ 3,1 mA, on choisit RS = 1,5 V / 3,1 mA ≈ 480 Ω, soit **470 Ω** en valeur normalisée. Le drain est alors à environ 12 − 3,1 mA × 2,2 kΩ ≈ **5,1 V**.

## Le gain

Pour un JFET, on parle de **transconductance** gm : de combien de milliampères ID varie quand VGS varie de 1 V. Elle s'exprime en millisiemens (mS = mA/V) et se lit sur la fiche technique ou sur la pente de la courbe au point de repos. Avec RS découplée par CS :

**Av ≈ −gm × RD**

Avec gm = 2,5 mS et RD = 2,2 kΩ : Av ≈ −2,5 × 2,2 = **−5,5**. Comme pour l'émetteur commun, la sortie est inversée.

## JFET ou bipolaire ?

- Le **bipolaire** donne plus de gain pour un même courant.
- Le **JFET** offre une impédance d'entrée énorme (ici, celle de RG : 1 MΩ) et peu de bruit : on le trouve en tête des micros, des sondes et des appareils de mesure.

## À retenir

- Polarisation automatique : RG à la masse, VGS = −ID × RS.
- Av ≈ −gm × RD, sortie inversée.
- Atout du JFET : une entrée qui ne charge pas la source.
