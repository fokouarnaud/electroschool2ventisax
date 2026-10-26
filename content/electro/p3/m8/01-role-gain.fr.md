Un micro produit quelques millivolts, une antenne encore moins. Pour faire bouger la membrane d'un haut-parleur ou attaquer l'entrée d'un convertisseur, il faut un signal bien plus grand. C'est le travail de l'**amplificateur** : il reproduit la forme du signal d'entrée, en plus grand.

![Schéma-bloc : un petit signal de 50 mV crête entre dans le triangle A, l'alimentation arrive par le haut, un signal de 2 V crête sort](/static/content/electro/m8/bloc.svg)

## D'où vient l'énergie ?

L'amplificateur ne crée pas d'énergie. Il puise dans son **alimentation** (une pile, une alimentation 12 V) et s'en sert pour fabriquer une copie agrandie du signal. Le transistor joue le rôle d'un robinet : un petit courant de base commande un grand courant de collecteur, fourni par l'alimentation.

## Le gain

Le **gain** dit combien de fois le signal est agrandi. On le note A, sans unité :

- gain en tension : **Av = vs / ve** ;
- gain en courant : **Ai = is / ie** ;
- gain en puissance : **Ap = Av × Ai**.

Exemple : 50 mV crête à l'entrée, 2 V crête à la sortie. Av = 2 / 0,05 = **40**. Si, en plus, le courant est multiplié par 25, la puissance l'est par 40 × 25 = 1 000.

![Les deux signaux sur le même repère : ve, minuscule, et vs, quarante fois plus grande](/static/content/electro/m8/signaux.svg)

On compare des valeurs de même nature : crête avec crête, ou efficace avec efficace. Le rapport reste le même.

## Le signe du gain

Certains montages rendent une sortie **inversée** : quand l'entrée monte, la sortie descend. Leur gain est négatif, par exemple Av = −39. Le signe dit seulement que la sortie est en opposition de phase ; la **valeur absolue** (39) dit de combien le signal est agrandi. Dans les exercices, lisez bien si l'on vous demande le gain « en valeur absolue » ou « avec son signe ».

## Ce qui se passe dans le circuit

Sur le banc ci-dessous, le micro fournit 50 mV crête : sa membrane bouge à peine. L'amplificateur en fait une copie quarante fois plus grande, 2 V crête, et la membrane du haut-parleur, dessinée à la même échelle, bouge quarante fois plus. L'énergie de ce grand mouvement vient de la batterie, pas du micro : le micro ne fait que commander, comme la main qui tourne un robinet.

Les deux galvanomètres ont des échelles dans le rapport 40 : avec Av = 40, leurs aiguilles battent ensemble. Avec Av = −39, la sortie ne vaut plus que 1,95 V crête et elle est inversée : quand l'aiguille d'entrée part d'un côté, celle de sortie part de l'autre.

[[fig:amp_gain]]

## À retenir

- Un amplificateur agrandit un signal en puisant l'énergie dans son alimentation.
- Av = vs / ve, sans unité ; Ap = Av × Ai.
- Un gain négatif indique une sortie inversée.
