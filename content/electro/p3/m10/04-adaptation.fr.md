Un transformateur ne change pas seulement les tensions et les courants : il change aussi la façon dont une charge est « vue » depuis le primaire. On s'en sert pour **adapter** une charge à une source.

## L'impédance ramenée au primaire

Une charge Zs branchée au secondaire se comporte, vue du primaire, comme une impédance :

**Zp = Zs × (Np / Ns)²**

Le rapport des spires intervient **au carré** : il agit une fois sur la tension, une fois sur le courant.

![Amplificateur relié au primaire d'un transformateur 10 pour 1, dont le secondaire alimente un haut-parleur de 8 Ω](/static/content/electro/m10/adaptation.svg)

Exemple : un haut-parleur de 8 Ω derrière un transformateur de rapport Np / Ns = 10. Zp = 8 × 10² = **800 Ω**.

![Vu du primaire, le haut-parleur de 8 Ω se comporte comme une résistance de 800 Ω](/static/content/electro/m10/equivalent.svg)

## Pourquoi adapter ?

Une source transmet le plus de puissance à sa charge quand l'impédance de la charge **égale** sa propre impédance interne. Un étage à transistor ou à tube qui a besoin d'environ 800 Ω de charge ne pourrait presque rien fournir à un haut-parleur de 8 Ω branché en direct : le transformateur règle ce désaccord.

## Choisir le rapport

On part de la relation à l'envers :

**Np / Ns = √(Zp / Zs)**

Exemple : pour qu'une charge de 4 Ω paraisse valoir 1 kΩ, Np / Ns = √(1 000 / 4) = √250 ≈ **15,8**.

On retrouve ces transformateurs d'adaptation dans les postes de radio à transistors, les amplis à tubes, les lignes de sonorisation et les antennes (adaptation entre un câble de 75 Ω et une antenne de 300 Ω, par exemple : rapport de spires √4 = 2).

## À retenir

- Zp = Zs × (Np / Ns)² : le rapport des spires agit au carré.
- Le transfert de puissance est maximal quand les impédances sont égales.
- Np / Ns = √(Zp / Zs).
