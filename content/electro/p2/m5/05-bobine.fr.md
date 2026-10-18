Une **bobine** (ou inductance) est un fil enroulé, souvent autour d'un noyau. Son inductance L se mesure en henrys (H) ; on rencontre surtout des millihenrys (mH) et des microhenrys (µH). En continu, une bobine idéale n'est qu'un fil : elle laisse passer le courant sans opposition.

![Source de 10 V efficaces, ampèremètre et bobine de 100 mH](/static/content/electro/m5/l-circuit.svg)

## La réactance inductive

En alternatif, la bobine crée un champ magnétique qui s'oppose à toute variation du courant. Cette opposition est la **réactance inductive** XL, en ohms :

**XL = 2π × f × L**   (f en hertz, L en henrys)

Exemple : L = 100 mH. À 50 Hz, XL = 2 × 3,14 × 50 × 0,1 ≈ **31,4 Ω**. À 1 kHz, XL ≈ **628 Ω**.

![Droite de XL pour 100 mH : 31,4 Ω à 50 Hz, 314 Ω à 500 Hz, elle monte avec la fréquence](/static/content/electro/m5/xl-courbe.svg)

C'est l'inverse du condensateur : **quand f augmente, XL augmente**. Sous 10 V efficaces à 1 kHz, la bobine de 100 mH laisse passer 10 / 628 ≈ 15,9 mA.

[[calc:reactance]]

## Le courant en retard

La bobine freine les changements de courant : le courant atteint son maximum **un quart de période après** la tension. Dans une bobine, **le courant est en retard de 90° sur la tension**.

![Dans une bobine, la courbe du courant atteint son maximum un quart de période après celle de la tension](/static/content/electro/m5/l-phase.svg)

Une bobine réelle possède aussi la résistance de son fil, mesurable à l'ohmmètre. Elle reste en général petite devant XL aux fréquences d'usage.

## À retenir

- XL = 2π × f × L ; XL augmente avec f et avec L.
- En continu, une bobine idéale se comporte comme un fil.
- Dans une bobine, i est en retard de 90° sur u.
