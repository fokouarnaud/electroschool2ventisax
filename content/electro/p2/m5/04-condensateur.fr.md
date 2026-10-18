En continu, un condensateur chargé bloque le courant (Partie 1, module 1). En alternatif, la tension change sans cesse : le condensateur se charge, se décharge et se recharge dans l'autre sens. Un courant circule donc en permanence dans le circuit.

![Source de 10 V efficaces, ampèremètre et condensateur de 1 µF : un courant alternatif circule](/static/content/electro/m5/c-circuit.svg)

## La réactance capacitive

Le condensateur s'oppose plus ou moins au passage de l'alternatif. Cette opposition s'appelle la **réactance capacitive** Xc, en ohms :

**Xc = 1 / (2π × f × C)**   (f en hertz, C en farads)

Exemple : C = 1 µF à 50 Hz. Xc = 1 / (2 × 3,14 × 50 × 0,000 001) ≈ **3 183 Ω**, soit environ 3,18 kΩ. À 1 kHz, la même capacité ne présente plus que **159 Ω**.

![Courbe de Xc pour 1 µF : très grande aux basses fréquences, elle diminue quand la fréquence augmente](/static/content/electro/m5/xc-courbe.svg)

Retenez le sens de variation : **quand f augmente, Xc diminue**. Si la fréquence double, Xc est divisée par deux. En continu (f = 0), Xc devient infinie : on retrouve le condensateur qui bloque.

La réactance s'utilise comme une résistance dans la loi d'Ohm : **Ieff = Ueff / Xc**. Sous 10 V efficaces à 50 Hz, le condensateur de 1 µF laisse passer 10 / 3 183 ≈ 3,14 mA.

[[calc:reactance]]

## Le courant en avance

Le courant est maximal quand la tension change le plus vite, c'est-à-dire quand elle passe par zéro. Résultat : dans un condensateur, **le courant est en avance d'un quart de période (90°) sur la tension**.

![Dans un condensateur, la courbe du courant atteint son maximum un quart de période avant celle de la tension](/static/content/electro/m5/c-phase.svg)

## À retenir

- Xc = 1 / (2π × f × C) ; Xc diminue quand f ou C augmente.
- Ieff = Ueff / Xc.
- Dans un condensateur, i est en avance de 90° sur u.
- En alternatif, n'utilisez que des condensateurs **non polarisés** (céramique, film) : un condensateur électrochimique branché à l'envers peut chauffer et éclater.
