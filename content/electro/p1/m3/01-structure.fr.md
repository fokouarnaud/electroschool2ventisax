Le **transistor bipolaire** est formé de trois couches de silicium dopé, empilées : soit N-P-N, soit P-N-P. Chaque couche a sa broche :

- l'**émetteur** (E), qui émet les porteurs de charge ;
- la **base** (B), couche centrale très fine, qui sert de commande ;
- le **collecteur** (C), qui recueille l'essentiel du courant.

On peut le voir comme deux jonctions PN dos à dos, mais avec une base si mince qu'un petit courant de base suffit à laisser passer un grand courant entre collecteur et émetteur. C'est tout l'intérêt du transistor : **un petit courant en commande un grand**.

## NPN et PNP

Le symbole porte une flèche sur l'émetteur, qui indique le sens du courant dans la jonction base-émetteur :

- pour un **NPN**, la flèche sort : le courant entre par la base et le collecteur et sort par l'émetteur ;
- pour un **PNP**, la flèche entre : tout est inversé, l'émetteur va vers le +.

![Symbole du transistor NPN, base à gauche, collecteur en haut, émetteur en bas avec la flèche vers l'extérieur](/static/content/electro/m3/npn.svg)

![Symbole du transistor PNP, avec la flèche de l'émetteur vers l'intérieur](/static/content/electro/m3/pnp.svg)

Un moyen mnémotechnique : pour le NPN, la flèche « **N**e **P**énètre **N**on » pas, elle sort.

## Les boîtiers

Les petits transistors courants (BC547, 2N2222 pour des NPN ; BC557, 2N2907 pour des PNP) sont en boîtier plastique à trois pattes. L'ordre des broches **change d'un modèle à l'autre** : consultez toujours la fiche technique (datasheet) avant de câbler.

## À retenir

- Trois broches : base (commande), collecteur, émetteur.
- NPN : flèche sortante ; PNP : flèche entrante.
- L'ordre des pattes dépend du modèle : lisez la fiche technique.
