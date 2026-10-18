Une diode ordinaire polarisée en inverse finit par céder si la tension devient trop forte : c'est le **claquage**, souvent destructeur. La **diode Zener** est conçue pour fonctionner justement dans cette zone, sans dommage, à une tension précise appelée **tension Zener** (Vz) : 3,3 V, 5,1 V, 12 V…

![Caractéristique d'une Zener de 5,1 V : conduction directe vers 0,7 V et conduction inverse brutale à 5,1 V](/static/content/electro/m2/zener-courbe.svg)

## Une tension qui ne bouge plus

En direct, une Zener se comporte comme une diode classique. En inverse, elle bloque jusqu'à Vz, puis conduit en maintenant une tension quasi constante à ses bornes, même si le courant varie beaucoup. C'est cette propriété qui en fait un **régulateur de tension** simple.

On la monte toujours **en inverse** : cathode du côté positif.

![Pile de 12 V, résistance série de 330 Ω, Zener de 5,1 V et charge RL en parallèle](/static/content/electro/m2/zener-regulateur.svg)

## Dimensionner la résistance série

La résistance R absorbe la différence entre la tension d'entrée et Vz, et limite le courant :

**I = (E − Vz) / R**

Exemple : E = 12 V, Vz = 5,1 V, R = 330 Ω. I = 6,9 / 330 ≈ **21 mA**. Ce courant se partage entre la Zener et la charge. Tant que la charge en prend moins de 21 mA, la Zener garde sa sortie à 5,1 V, même si la pile s'use et descend à 10 V.

Vérifiez la puissance de la Zener : à vide, elle reçoit tout le courant, soit 5,1 × 0,021 ≈ 0,11 W. Un modèle de 0,5 W laisse une marge confortable.

## À retenir

- La Zener se monte en inverse et maintient Vz à ses bornes.
- Une résistance série est obligatoire : I = (E − Vz) / R.
- Le courant de la charge doit rester inférieur à ce courant.
