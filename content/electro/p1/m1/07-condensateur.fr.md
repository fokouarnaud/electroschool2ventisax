Un **interrupteur** fermé se comporte comme un fil (résistance quasi nulle) ; ouvert, comme une coupure (résistance quasi infinie). Un **condensateur**, lui, est formé de deux armatures séparées par un isolant : il stocke des charges, et sa capacité C se mesure en farads (F). En pratique on rencontre des microfarads (µF) et des nanofarads (nF).

![Pile de 10 V, interrupteur K, résistance de 10 kΩ et condensateur de 100 µF en série](/static/content/electro/m1/rc-circuit.svg)

## La charge à travers une résistance

À la fermeture de l'interrupteur, le condensateur vide se comporte d'abord comme un fil : le courant est maximal, E / R. Puis la tension Uc à ses bornes monte et le courant diminue. Quand Uc atteint la tension de la pile, le courant s'annule : **en régime établi, un condensateur bloque le courant continu**.

La vitesse de charge dépend de la **constante de temps** :

**τ = R × C**   (en secondes, avec R en ohms et C en farads)

Avec 10 kΩ et 100 µF : τ = 10 000 × 0,000 1 = **1 s**.

![Courbe de charge : Uc atteint 63 % de E au bout de τ = 1 s et presque 100 % au bout de 5 s](/static/content/electro/m1/rc-courbe.svg)

## Les repères à connaître

- Au bout de **τ**, le condensateur est chargé à environ **63 %**.
- Au bout de **5 τ**, on le considère comme chargé (plus de 99 %).

La décharge suit la même logique dans l'autre sens. On utilise ces circuits RC pour créer des temporisations, filtrer des parasites ou retarder l'allumage d'un montage.

## À retenir

- Interrupteur fermé : fil ; ouvert : coupure.
- En continu, un condensateur chargé ne laisse plus passer de courant.
- τ = R × C ; 63 % au bout de τ, chargé au bout de 5 τ.
