Plaçons maintenant la bobine et le condensateur **côte à côte**, en parallèle. On appelle souvent ce montage un **circuit bouchon**, car il « bouche » le passage à sa fréquence de résonance.

![Source alternative, résistance de 10 kΩ en série, puis bobine de 10 mH et condensateur de 100 nF en parallèle](/static/content/electro/m7/lc-parallele.svg)

## La même fréquence de résonance

La résonance se produit toujours quand XL = XC, donc à la même fréquence que pour le circuit série (composants idéaux) :

**f0 = 1 / (2π × √(L × C))**

Avec 10 mH et 100 nF, f0 ≈ 5 kHz ; avec 10 mH et 10 nF, f0 ≈ 15,9 kHz.

## Un comportement inversé

- **Loin de f0**, l'une des deux branches a une faible réactance (C aux hautes fréquences, L aux basses) : elle court-circuite le montage, l'impédance est faible.
- **À f0**, les courants dans L et dans C sont égaux et opposés : ils tournent entre la bobine et le condensateur sans passer par la source. Vu de l'extérieur, l'impédance est **maximale** et le courant fourni par la source est **minimal**.

![Impédance d'un bouchon de 10 mH (avec 10 Ω de pertes) et 100 nF : faible partout sauf autour de f0, où elle monte vers 10 kΩ](/static/content/electro/m7/z-parallele.svg)

C'est l'inverse du circuit série, où l'impédance est minimale à f0.

| À la résonance | Circuit série | Circuit parallèle |
|---|---|---|
| Impédance | minimale (Z = R) | maximale |
| Courant de la source | maximal | minimal |

## Ce qui se passe dans le circuit

Sur le banc ci-dessous, la vanne Rs = 10 kΩ alimente le bouchon ; le débitmètre de la ligne et le repère du volant partagent la même échelle. À f0 / 2, la bobine laisse passer presque tout : le bouchon ne vaut que 211 Ω, la tension à ses bornes tombe à 0,021 × Ve et le courant de ligne, 99,8 µA, est presque celui de Rs seule. À 2 × f0, c'est la cloche qui court-circuite le bouchon, avec le même résultat.

À f0, l'eau poussée dans la bobine revient par la cloche, puis repart : 1,58 mA vont et viennent entre L et C, tandis que la ligne ne fournit que 50,0 µA, trente fois moins, juste de quoi compenser les 10 Ω de pertes de la bobine. Le bouchon vaut alors 10 kΩ, autant que Rs : la moitié de la tension d'entrée apparaît à ses bornes (Vt ≈ 0,500 × Ve).

[[fig:lc_tank]]

## À quoi sert un bouchon ?

Alimenté à travers une résistance, un bouchon présente à ses bornes une tension **maximale à f0** et faible ailleurs. Il **sélectionne** donc une fréquence : c'est le cœur des circuits d'accord des récepteurs radio, et des oscillateurs de la Partie 3.

## À retenir

- LC parallèle : même f0 que le LC série.
- À f0, impédance maximale et courant de la source minimal.
- Alimenté à travers R, le bouchon garde la fréquence f0.
