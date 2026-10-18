Entre deux crêtes, le condensateur se décharge dans la charge : la tension baisse d'une quantité **ΔU**, l'**ondulation résiduelle**. On la calcule simplement.

## La formule

Le condensateur fournit seul le courant I de la charge pendant presque toute la durée entre deux crêtes, soit 1 / f. La charge qu'il perd vaut I / f, et sa tension baisse de :

**ΔU ≈ I / (f × C)**

avec **f = 100 Hz** en double alternance (50 Hz en simple alternance).

![Zoom sur la tension lissée : elle oscille entre 15,6 V et environ 13,3 V, soit une ondulation ΔU d'environ 2,3 V](/static/content/electro/m11/ondulation.svg)

Exemple : I = 0,5 A et C = 2 200 µF en double alternance. ΔU ≈ 0,5 / (100 × 0,002 2) ≈ **2,3 V**. La tension varie entre 15,6 V et 13,3 V, et sa valeur moyenne est d'environ 15,6 − 2,3 / 2 ≈ **14,5 V**.

[[calc:ripple]]

## Choisir C

On part de l'ondulation acceptable et on retourne la formule :

**C ≈ I / (f × ΔU)**

Pour 0,5 A et au plus 1 V d'ondulation : C ≈ 0,5 / (100 × 1) = 0,005 F = **5 000 µF**. On prend la valeur normalisée au-dessus ou la plus proche : 4 700 µF donne ΔU ≈ 1,1 V.

![Ondulation sous 0,5 A : 1 000 µF laisse environ 5 V d'ondulation, 4 700 µF environ 1,1 V](/static/content/electro/m11/condensateurs.svg)

## Ce qu'il faut retenir du calcul

- L'ondulation **double** si le courant double.
- Elle est **divisée par deux** si l'on double la capacité.
- En **simple alternance**, f = 50 Hz : pour la même ondulation, il faut **deux fois plus** de capacité.

La formule est approchée (elle suppose que le condensateur se décharge pendant toute la période), mais elle va dans le sens de la sécurité : l'ondulation réelle est un peu plus faible.

## À retenir

- ΔU ≈ I / (f × C), avec f = 100 Hz en double alternance.
- C ≈ I / (f × ΔU) pour choisir le condensateur.
- Tension moyenne ≈ crête − ΔU / 2.
