La **LED** (diode électroluminescente) est une diode qui émet de la lumière quand elle conduit. Elle obéit aux mêmes règles qu'une diode ordinaire, avec deux différences importantes :

- sa tension de seuil est plus élevée et dépend de la couleur : environ 1,8 V pour une LED rouge, 2,1 V pour une verte et 3 V pour une bleue ou une blanche ;
- elle supporte peu de courant : 10 à 20 mA pour une LED de signalisation classique.

![Symbole de la LED, anode et cathode, avec les seuils typiques selon la couleur](/static/content/electro/m2/led-symbole.svg)

## Toujours une résistance série

Comme toute diode passante, une LED ne limite pas son courant. Branchée seule sur une pile, elle grille en un instant. On ajoute donc une **résistance série** qui fixe le courant :

**R = (E − U_LED) / I**

![Pile de 9 V, résistance de 330 Ω et LED rouge de 2 V : environ 21 mA](/static/content/electro/m2/led-circuit.svg)

## Exemple

Une LED rouge (2 V) doit être alimentée par une pile de 9 V avec 20 mA. R = (9 − 2) / 0,02 = **350 Ω**. On choisit la valeur normalisée la plus proche, 330 Ω, ce qui donne (9 − 2) / 330 ≈ 21 mA : c'est acceptable. Si l'on veut rester sous 20 mA, on prend la valeur au-dessus, 390 Ω.

La résistance dissipe (9 − 2) × 0,021 ≈ 0,15 W : un modèle de 1/4 W convient.

## Repérer les pattes

La **patte la plus longue** est l'anode (+). Côté cathode (−), le boîtier présente souvent un **méplat**. En cas de doute, une LED montée à l'envers ne s'abîme pas sous quelques volts : elle reste simplement éteinte.

## À retenir

- Seuil d'une LED : 1,8 à 3 V selon la couleur ; courant de 10 à 20 mA.
- R = (E − U_LED) / I, puis valeur normalisée.
- Patte longue = anode.
