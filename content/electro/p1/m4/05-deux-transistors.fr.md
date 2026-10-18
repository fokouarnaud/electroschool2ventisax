Quand un seul transistor ne suffit pas, on en associe deux. Deux montages sont à connaître.

## Le Darlington : multiplier le gain

L'émetteur du premier transistor alimente directement la base du second, et les deux collecteurs sont reliés. Le courant de sortie du premier devient le courant de base du second : les gains se **multiplient**.

**β total ≈ β1 × β2**

![Montage Darlington : l'émetteur du premier transistor attaque la base du second, collecteurs reliés](/static/content/electro/m4/darlington.svg)

Avec deux transistors de gain 100, le gain total atteint environ 10 000 : un courant de base de 50 µA suffit alors à commander 500 mA. Le Darlington sert à piloter des charges lourdes (moteurs, rubans de LED) depuis un signal très faible.

Il a deux contreparties :

- la tension base-émetteur totale double, environ **1,4 V** (deux jonctions en série) ;
- saturé, sa tension collecteur-émetteur reste vers **0,7 à 1 V**, plus que celle d'un transistor seul : il chauffe davantage.

On trouve aussi des Darlington tout faits dans un seul boîtier (TIP120, par exemple).

## Deux étages en cascade : inverser la commande

Dans le second montage, le collecteur du premier transistor commande la base du second. Quand le premier conduit, il ramène son collecteur vers 0 V et prive le second de courant de base : le second se bloque. Quand le premier est bloqué, le second sature.

![Deux étages : le collecteur du premier transistor commande la base du second, qui allume la lampe](/static/content/electro/m4/cascade.svg)

Ce montage **inverse** la logique. Avec le capteur de lumière de la section précédente, il permet par exemple d'allumer une lampe au jour plutôt qu'à la nuit sans réorganiser le diviseur.

## À retenir

- Darlington : β total ≈ β1 × β2, VBE ≈ 1,4 V, VCE sat plus élevé.
- Deux étages en cascade : le second fait l'inverse du premier.
- Choisissez le montage selon le besoin : plus de gain, ou une logique inversée.
