La **caractéristique** d'une diode est la courbe du courant qui la traverse en fonction de la tension à ses bornes. Elle résume tout son comportement.

![Courbe courant-tension d'une diode au silicium : courant nul en inverse, puis montée brutale vers 0,7 V](/static/content/electro/m2/caracteristique.svg)

## Lire la courbe

- **En inverse** (tension négative), le courant reste quasi nul : la diode bloque.
- **En direct, sous le seuil**, le courant reste très faible.
- **Autour de 0,7 V**, la courbe se redresse brutalement : un petit supplément de tension fait grimper le courant. C'est pourquoi on considère que la tension aux bornes d'une diode passante reste à peu près constante, entre 0,6 et 0,8 V selon le courant.

Ce n'est pas une droite : une diode **ne suit pas la loi d'Ohm**. On ne calcule donc pas son courant avec U / R, mais avec le reste du circuit.

## Le calcul pratique

Dans une boucle avec une résistance, on retire le seuil de la diode puis on applique la loi d'Ohm à la résistance :

**I = (E − 0,7) / R**

Exemple : pile de 5 V, résistance de 470 Ω. I = (5 − 0,7) / 470 ≈ **9,1 mA**. Le voltmètre aux bornes de la diode affiche environ 0,7 V.

![Pile de 5 V, résistance de 470 Ω et diode passante, voltmètre aux bornes de la diode indiquant environ 0,7 V](/static/content/electro/m2/mesure.svg)

## À retenir

- La caractéristique n'est pas une droite : pas de loi d'Ohm pour la diode.
- Diode passante : environ 0,7 V à ses bornes, quel que soit le courant.
- I = (E − 0,7) / R dans une boucle avec une résistance.
