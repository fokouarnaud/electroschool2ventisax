Plaçons en série une résistance, une bobine et un condensateur : c'est le circuit **RLC série**. La bobine et le condensateur ont des comportements opposés, et c'est ce qui rend ce circuit remarquable.

![Circuit RLC série alimenté sous 1 V : R = 50 Ω, L = 10 mH, C = 100 nF](/static/content/electro/m7/rlc-serie.svg)

## XL et XC se compensent

Quand la fréquence augmente, XL monte et XC descend. Leurs effets sont opposés : la bobine retarde le courant, le condensateur l'avance. Dans le circuit, leurs réactances se soustraient :

**Z = √(R² + (XL − XC)²)**

![XL monte et XC descend avec la fréquence ; les deux courbes se croisent à f0 ≈ 5 kHz, où XL = XC ≈ 316 Ω](/static/content/electro/m7/xl-xc.svg)

Il existe une fréquence où **XL = XC** : les deux réactances s'annulent, il ne reste que R. C'est la **fréquence de résonance** f0.

## La formule de f0

En écrivant 2π × f × L = 1 / (2π × f × C), on obtient :

**f0 = 1 / (2π × √(L × C))**

Exemple : L = 10 mH et C = 100 nF. L × C = 0,01 × 0,000 000 1 = 10⁻⁹ ; √(10⁻⁹) ≈ 0,000 031 6. f0 = 1 / (2 × 3,14 × 0,000 031 6) ≈ **5 033 Hz**. À cette fréquence, XL = XC ≈ 316 Ω.

[[calc:resonance]]

## Ce qui se passe à la résonance

- L'impédance est **minimale** : Z = R.
- Le courant est **maximal** : I = U / R. Sous 1 V avec R = 50 Ω : I = 20 mA.
- La tension aux bornes de L et celle aux bornes de C peuvent dépasser largement celle de la source (ici 316 × 0,02 ≈ 6,3 V pour 1 V d'entrée), car elles s'annulent entre elles.
- En dessous de f0, XC domine : le circuit est **capacitif**. Au-dessus, XL domine : il est **inductif**.

## À retenir

- f0 = 1 / (2π × √(L × C)) : à f0, XL = XC.
- À la résonance série : Z = R minimale, I = U / R maximal.
