Une tension alternative change sans cesse : il faut donc préciser **quelle** valeur on donne. Trois valeurs servent tous les jours.

![Sinusoïde de 10 V d'amplitude : Umax = 10 V, Ucc = 20 V et Ueff ≈ 7,07 V](/static/content/electro/m5/valeurs.svg)

## Les trois valeurs

- **Valeur de crête** Umax : le sommet de la sinusoïde, mesuré depuis zéro.
- **Valeur crête à crête** Ucc : l'écart entre le sommet et le creux, **Ucc = 2 × Umax**.
- **Valeur efficace** Ueff : la tension continue qui chaufferait autant une résistance.

Pour une sinusoïde :

**Ueff = Umax / √2 ≈ 0,707 × Umax**   et   **Umax = Ueff × √2 ≈ 1,414 × Ueff**

La valeur **moyenne** d'une sinusoïde est nulle : la moitié positive compense la moitié négative. C'est pourquoi on ne l'utilise pas pour décrire l'alternatif.

## Pourquoi la valeur efficace ?

Une lampe ne « voit » que l'énergie qu'elle reçoit. Sous 12 V continus ou sous 12 V **efficaces** alternatifs, elle brille autant.

![Deux montages identiques : une lampe sous 12 V continus et une lampe sous 12 V efficaces brillent de la même façon](/static/content/electro/m5/efficace.svg)

Quand on annonce « 230 V » pour le secteur, c'est la valeur efficace. Le sommet atteint 230 × 1,414 ≈ **325 V**, et l'écart crête à crête dépasse 650 V : c'est ce sommet que doivent supporter les composants.

Un multimètre réglé en **V~** (AC) affiche la valeur efficace d'une tension sinusoïdale, à condition que la fréquence reste dans sa plage de mesure (souvent quelques centaines de hertz pour un modèle d'entrée de gamme).

## À retenir

- Ucc = 2 × Umax ; Ueff ≈ 0,707 × Umax.
- Les tensions et courants alternatifs annoncés sont des valeurs efficaces.
- 230 V efficaces correspondent à des crêtes de 325 V.
