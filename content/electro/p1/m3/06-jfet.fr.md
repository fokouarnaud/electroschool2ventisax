Le **transistor à effet de champ à jonction** (JFET) commande lui aussi un courant, mais d'une autre manière : ce n'est pas un courant qui le pilote, c'est une **tension**. Ses trois broches portent d'autres noms :

- le **drain** (D), par où entre le courant ;
- la **source** (S), par où il sort ;
- la **grille** (G), l'électrode de commande.

![Symbole du JFET canal N : grille à gauche avec la flèche vers l'intérieur, drain en haut, source en bas](/static/content/electro/m3/jfet.svg)

## Comment il fonctionne

Entre drain et source, le courant traverse un **canal** de silicium (de type N pour un JFET canal N). La grille forme une jonction avec ce canal. En rendant la grille négative par rapport à la source, on élargit une zone isolante qui **rétrécit le canal** : le courant de drain diminue.

- À **VGS = 0**, le canal est grand ouvert : le courant est maximal, noté **IDSS**.
- À **VGS = VGS(off)** (par exemple −4 V), le canal est complètement pincé : le JFET est **bloqué**.

![Courbe ID en fonction de VGS : IDSS = 10 mA à VGS = 0, courant nul à VGS(off) = −4 V](/static/content/electro/m3/jfet-courbe.svg)

## Ce qui change par rapport au bipolaire

- La grille, polarisée en inverse, ne consomme **presque aucun courant** : le JFET ne charge pas le circuit qui le commande.
- Il conduit **par défaut** (à VGS = 0) et il faut une tension négative pour le bloquer, alors qu'un bipolaire est bloqué par défaut.
- Comme β pour le bipolaire, IDSS et VGS(off) varient beaucoup d'un exemplaire à l'autre.

## À retenir

- JFET : drain, source, grille ; commande en tension.
- Canal N : conduit à VGS = 0 (IDSS), bloqué à VGS(off) négative.
- Courant de grille quasi nul.
