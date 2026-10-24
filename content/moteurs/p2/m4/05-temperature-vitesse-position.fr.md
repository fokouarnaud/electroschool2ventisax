Les capteurs de la section précédente disent **oui ou non**. D'autres mesurent une **valeur** : une température, une vitesse, une position.

## Mesurer une température

La **sonde Pt100** est un fil de platine dont la résistance vaut **100 Ω à 0 °C** et augmente d'environ **0,385 Ω par degré** : R ≈ 100 × (1 + 0,00385 × T).

![Sonde Pt100 : résistance de 100 Ω à 0 °C, 138,5 Ω à 100 °C, droite presque parfaite](/static/content/moteurs/m4/pt100.svg)

**Exemple.** On mesure 119,25 Ω : T = (119,25 / 100 − 1) / 0,00385 = **50 °C**. Les **thermocouples** (deux métaux soudés qui produisent une petite tension) mesurent des températures plus élevées. Dans les enroulements des moteurs, on trouve aussi des **sondes CTP**, qui changent brusquement de résistance à une température donnée et commandent un relais de protection.

## Mesurer une vitesse et une position

Le **codeur incrémental** est un disque à fentes monté sur l'arbre ; un faisceau lumineux traversant les fentes produit une **impulsion par fente**.

![Codeur incrémental : le disque à fentes coupe un faisceau ; chaque fente produit une impulsion](/static/content/moteurs/m4/codeur.svg)

Avec N impulsions par tour : vitesse (tr/s) = impulsions par seconde / N. **Exemple** : un codeur de 500 impulsions par tour délivre 1 000 impulsions en une seconde : 1 000 / 500 = 2 tr/s, soit **120 tr/min**. En comptant les impulsions depuis une position de référence, on connaît aussi la position. Un **codeur absolu** donne directement la position par un code numérique, même après une coupure de courant.

Pour une simple surveillance de rotation, une **dynamo tachymétrique** donne une tension proportionnelle à la vitesse.

## À retenir

- Pt100 : 100 Ω à 0 °C, + 0,385 Ω par degré.
- Codeur : vitesse = impulsions par seconde / impulsions par tour.
- Codeur absolu : position conservée après une coupure.
