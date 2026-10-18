Au module précédent, le transistor amplifiait. Ici, on n'utilise que ses deux régimes extrêmes : **bloqué** et **saturé**. Il devient alors un **interrupteur commandé** : un petit courant de base allume ou éteint une charge qui consomme beaucoup plus.

![Transistor NPN : la lampe est dans le collecteur, l'interrupteur K et RB commandent la base](/static/content/electro/m4/interrupteur.svg)

## Les deux états

- **Bloqué** : aucun courant de base. Le transistor ne conduit pas, IC = 0 et toute la tension VCC se retrouve entre collecteur et émetteur. La lampe est éteinte, comme avec un interrupteur ouvert.
- **Saturé** : courant de base suffisant. VCE tombe vers 0,2 V et la lampe reçoit presque toute la tension. Elle s'allume, comme avec un interrupteur fermé.

![Comparaison bloqué et saturé : interrupteur ouvert et lampe éteinte, interrupteur fermé et lampe allumée](/static/content/electro/m4/bloque-sature.svg)

## Pourquoi ne pas rester entre les deux ?

Dans les deux états extrêmes, le transistor chauffe peu : bloqué, il n'est traversé par aucun courant ; saturé, la tension à ses bornes est très faible. Or la puissance qu'il dissipe vaut VCE × IC. En régime linéaire, VCE et IC sont tous les deux importants et le transistor chauffe : une commutation doit donc être **franche**, sans s'attarder entre les deux.

Exemple : une lampe de 9 V, 100 mA. Saturé, le transistor dissipe 0,2 × 0,1 = 0,02 W. À mi-chemin, avec 4,5 V et 50 mA, il dissiperait 0,225 W, plus de dix fois plus.

## Pourquoi un transistor plutôt qu'un vrai interrupteur ?

Parce que la commande peut venir d'un circuit qui ne fournit que quelques milliampères : une sortie de microcontrôleur, un capteur, une porte logique. Le transistor fait le lien entre ce signal faible et une charge gourmande.

## À retenir

- Commutation : bloqué (interrupteur ouvert) ou saturé (interrupteur fermé).
- Saturé, VCE ≈ 0,2 V : le transistor chauffe peu.
- Évitez le régime intermédiaire, qui fait chauffer le transistor.
