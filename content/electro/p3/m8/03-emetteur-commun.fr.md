Le montage polarisé de la section précédente devient un amplificateur dès qu'on lui ajoute une entrée et une sortie. C'est l'**émetteur commun**, le montage amplificateur à transistor le plus répandu.

![Amplificateur à émetteur commun : C1 à l'entrée, C2 à la sortie, RE partagée en RE1 de 100 Ω et RE2 de 910 Ω, CE de 100 µF en parallèle sur RE2](/static/content/electro/m8/ec.svg)

## Les condensateurs de liaison

- **C1** amène le signal sur la base sans déranger la polarisation : il laisse passer l'alternatif et bloque le continu.
- **C2** récupère la variation de tension du collecteur et bloque les 6,5 V continus qui y règnent.
- **CE**, le condensateur de **découplage**, court-circuite RE2 pour le signal alternatif, mais pas pour le continu.

On a partagé RE en RE1 = 100 Ω et RE2 = 910 Ω : 1 010 Ω au total, le point de repos ne change presque pas. Mais pour le signal, seule RE1 reste en série dans l'émetteur.

## Le gain en tension

Le signal ajoute une petite variation ve à la base. L'émetteur la suit, donc le courant varie de ve / RE1, et ce courant traverse RC. Le gain vaut :

**Av ≈ −RC / RE1**

où RE1 est la partie **non découplée** de la résistance d'émetteur. Ici, Av ≈ −3 900 / 100 = **−39**. Avec 50 mV crête à l'entrée, la sortie fait 39 × 0,05 ≈ **1,95 V crête**.

En pratique, on mesure un peu moins, car la jonction base-émetteur ajoute sa propre petite résistance (environ 25 mV / IE, soit 18 Ω ici) à RE1.

[[calc:gain]]

## L'inversion

Pourquoi le signe moins ? Quand ve monte, IC augmente, la chute de tension dans RC augmente et la tension du collecteur **descend**. La sortie est en **opposition de phase** avec l'entrée : déphasage de 180°.

![Deux repères alignés : ve de 50 mV crête en haut, vs de 1,95 V crête en bas, qui descend quand ve monte](/static/content/electro/m8/inversion.svg)

Sans CE, toute RE (1 010 Ω) resterait dans l'émetteur : Av ≈ −3 900 / 1 010 ≈ −3,9. Découpler une partie de RE multiplie donc le gain par dix, tout en gardant la stabilité du point de repos.

## À retenir

- C1 et C2 laissent passer le signal et bloquent le continu ; CE découple une partie de RE.
- Av ≈ −RC / RE (partie non découplée).
- La sortie de l'émetteur commun est inversée.
