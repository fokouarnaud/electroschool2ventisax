Les composants de puissance ont besoin d'une **commande** : des impulsions au bon moment, à la bonne fréquence, avec la bonne largeur. Ce rôle revient à des circuits intégrés.

## Le 555 et la MLI

Le circuit **555** monté en **astable** produit un signal rectangulaire. Avec un potentiomètre, on règle le **rapport cyclique** : la part de la période où la sortie est à 1. C'est la **modulation de largeur d'impulsion** (MLI, ou PWM en anglais).

![Un 555 en astable, avec R1, un potentiomètre et un condensateur C, fournit le signal MLI qui commande le transistor de puissance](/static/content/moteurs/m10/555.svg)

Sur un moteur à courant continu, la **tension moyenne** vaut :

**Umoy = rapport cyclique × U**

Avec 12 V et un rapport cyclique de 25 %, le moteur voit en moyenne 3 V ; sa vitesse suit. La fréquence de découpage, de l'ordre du kilohertz ou plus, est trop rapide pour que le moteur la ressente.

## AOP et microcontrôleur

- L'**amplificateur opérationnel** compare, filtre et met en forme les mesures (courant, vitesse) ; monté en comparateur, il produit un signal tout ou rien.
- Le **microcontrôleur** génère plusieurs signaux MLI, mesure, régule et communique : c'est le cœur des variateurs modernes.

Entre la commande et le composant de puissance, un **driver** ou un **optocoupleur** fournit le courant de grille et **isole** la basse tension du circuit de puissance.

## Les décharges électrostatiques

Un corps humain peut se charger à plusieurs milliers de volts en marchant sur une moquette. La décharge, souvent imperceptible, suffit à percer la grille d'un MOSFET ou d'un IGBT.

![Protection contre les décharges : bracelet relié à la terre, tapis antistatique, sachet blindé](/static/content/moteurs/m10/esd.svg)

- Porter un **bracelet** relié à la terre et travailler sur un **tapis** antistatique.
- Garder les cartes et composants dans leur **sachet blindé** jusqu'au montage ; les tenir par les bords.
- Ne jamais toucher les broches d'un composant ni les pistes d'une carte de variateur.

## À retenir

- Un 555 en astable produit une MLI ; Umoy = rapport cyclique × U.
- Microcontrôleur et driver commandent les composants de puissance.
- Bracelet, tapis et sachet blindé contre les décharges électrostatiques.
