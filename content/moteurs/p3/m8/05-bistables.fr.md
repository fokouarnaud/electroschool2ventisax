Le relais ordinaire est **monostable** : il retombe dès qu'on coupe sa bobine. Les relais **bistables** gardent leur état **sans courant** : ils ont une mémoire.

## Le télérupteur

Chaque **impulsion** sur la bobine du télérupteur fait **changer d'état** son contact : une impulsion ferme, la suivante ouvre, et ainsi de suite. Entre deux impulsions, la bobine n'est pas alimentée.

![Télérupteur : chaque impulsion sur la bobine fait changer l'état du contact, qui reste ensuite dans sa position](/static/content/moteurs/m8/telerupteur.svg)

**Usage classique** : l'éclairage d'un long couloir commandé par plusieurs boutons-poussoirs, tous **en parallèle** : n'importe lequel allume ou éteint. On ajoute autant de boutons qu'on veut avec seulement deux fils.

## Le relais à deux bobines

Un relais bistable à deux bobines a une bobine d'**enclenchement** (S, set) et une bobine de **déclenchement** (R, reset). Une impulsion sur S le ferme, une impulsion sur R l'ouvre ; il reste dans son état sans consommer.

![Relais bistable à deux bobines : une impulsion sur S enclenche, une impulsion sur R déclenche ; l'état est mémorisé sans courant](/static/content/moteurs/m8/bistable.svg)

## Attention à la sécurité

Un bistable **garde son état après une coupure de courant** : au retour de la tension, la sortie peut se retrouver active. Pour commander un moteur, on lui préfère donc le contacteur avec auto-maintien, qui **retombe** à la coupure et évite tout redémarrage inattendu. Les bistables conviennent à l'éclairage, à la signalisation, aux mémoires d'état.

## À retenir

- Télérupteur : chaque impulsion change l'état.
- Bistable à deux bobines : S enclenche, R déclenche.
- Mémoire conservée à la coupure : jamais pour démarrer un moteur.
