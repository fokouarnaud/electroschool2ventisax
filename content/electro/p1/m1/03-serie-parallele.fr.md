Rares sont les circuits qui ne contiennent qu'une résistance. Deux assemblages de base permettent de remplacer plusieurs résistances par une seule, appelée **résistance équivalente** (Req).

## En série : les résistances s'additionnent

Des résistances sont en série quand elles sont traversées **par le même courant**, l'une après l'autre. Leur résistance équivalente est la somme :

**Req = R1 + R2 + R3**

![Trois résistances de 1 kΩ, 2,2 kΩ et 3,3 kΩ en série : Req = 6,5 kΩ](/static/content/electro/m1/serie.svg)

Avec 12 V sur les trois résistances ci-dessus, le courant vaut 12 V / 6,5 kΩ ≈ 1,85 mA. La tension se répartit ensuite : chaque résistance reçoit R × I, et la somme des trois tensions redonne 12 V.

## En parallèle : la résistance équivalente diminue

Des résistances sont en parallèle quand elles sont branchées **entre les deux mêmes points** : elles ont toutes la même tension. On additionne leurs inverses :

**1 / Req = 1 / R1 + 1 / R2**   et, pour deux résistances,   **Req = (R1 × R2) / (R1 + R2)**

![4 kΩ et 12 kΩ en parallèle : Req = 3 kΩ](/static/content/electro/m1/parallele.svg)

Exemple : 4 kΩ et 12 kΩ en parallèle donnent 48 / 16 = **3 kΩ**. La résistance équivalente est toujours **plus petite que la plus petite** des résistances : on a ouvert un chemin de plus au courant. Deux résistances égales en parallèle valent la moitié de l'une d'elles.

## Lire la valeur d'une résistance

Les petites résistances portent des anneaux de couleur : deux chiffres, puis un multiplicateur. Jaune (4), violet (7), rouge (× 100) donne 4 700 Ω, soit 4,7 kΩ.

[[calc:resistor]]

## À retenir

- Série : même courant, on additionne les résistances.
- Parallèle : même tension, Req est plus petite que la plus petite résistance.
- Deux résistances égales R en parallèle valent R / 2.
