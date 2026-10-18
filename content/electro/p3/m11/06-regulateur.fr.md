Le **régulateur intégré** remplace la Zener dès que le courant dépasse quelques dizaines de milliampères. La famille **78xx** est la plus répandue : trois pattes, une tension de sortie fixe, et presque rien à calculer.

![Régulateur 7805 : entrée Ue avec un condensateur de 330 nF, sortie 5 V avec un condensateur de 100 nF, broche de masse au milieu](/static/content/electro/m11/regulateur.svg)

## Le 78xx

- Les deux derniers chiffres donnent la tension de sortie : **7805** pour 5 V, **7809** pour 9 V, **7812** pour 12 V. La famille **79xx** fait la même chose en négatif.
- Trois broches : **entrée** (IN), **masse** (GND), **sortie** (OUT), notées en anglais sur les fiches techniques. Le brochage dépend du boîtier : vérifiez-le toujours.
- Il fournit jusqu'à environ **1 A**, et se protège contre la surchauffe et les courts-circuits.

Le fabricant conseille deux petits condensateurs placés **au plus près des broches** : environ 330 nF à l'entrée et 100 nF à la sortie. Ils évitent que le régulateur oscille.

## La tension de déchet

Un 78xx a besoin d'une marge : son entrée doit rester au moins **2 V au-dessus** de sa sortie, à tout instant, creux de l'ondulation compris. Pour un 7805, il faut donc Ue ≥ **7 V**.

Exemple : avec le lissage de la section précédente (15,6 V crête, 2,3 V d'ondulation), l'entrée descend à 13,3 V au plus bas : largement assez.

## La puissance à dissiper

Toute la tension en trop est brûlée dans le régulateur :

**P = (Ue − Us) × I**

Exemple : Ue ≈ 12 V, Us = 5 V et I = 0,5 A. P = (12 − 5) × 0,5 = **3,5 W**. Sans **radiateur**, un boîtier TO-220 ne dissipe guère plus de 1 à 2 W : il faut le fixer sur un radiateur, ou choisir une tension d'entrée plus proche de la sortie.

## L'alimentation complète

On réunit tout le module : transformateur, pont, condensateur réservoir, régulateur.

![Alimentation 5 V complète : transformateur 230 V vers 12 V, pont de diodes, condensateur de 2 200 µF, régulateur 7805 et condensateur de 100 nF en sortie](/static/content/electro/m11/alim-complete.svg)

C'est le schéma de la plupart des petites alimentations linéaires, et celui du mini-projet du module.

## À retenir

- 78xx : sortie fixe (7805 = 5 V), environ 1 A, condensateurs de 330 nF et 100 nF près des broches.
- L'entrée doit rester au moins 2 V au-dessus de la sortie.
- P = (Ue − Us) × I ; au-delà de 1 à 2 W, un radiateur est nécessaire.
