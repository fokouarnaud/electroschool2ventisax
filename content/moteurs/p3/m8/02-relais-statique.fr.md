Le **relais statique** (en anglais SSR) remplace la bobine et les contacts par de l'électronique.

![Relais statique : la commande 24 V allume une diode dans un optocoupleur, qui commande un triac branché sur la charge](/static/content/moteurs/m8/ssr.svg)

- Côté commande, le signal allume une petite **diode lumineuse** dans un **optocoupleur** : l'isolement entre commande et charge est assuré par la lumière.
- Côté charge, un **triac** (ou deux thyristors) conduit tant que la commande est présente.

Sans pièce mobile, il ne s'use pas, ne fait aucun bruit, ne rebondit pas et commute très vite : il convient aux commutations fréquentes (régulation de température d'un four, par exemple).

## La commutation au zéro de tension

La plupart des relais statiques pour charges résistives **attendent le passage de la tension par zéro** pour commuter. En coupant ou en établissant le courant quand la tension est nulle, ils évitent les pointes de courant et les parasites.

![Commutation au zéro : l'ordre arrive en pleine alternance, le relais attend le passage par zéro suivant pour fermer](/static/content/moteurs/m8/zero.svg)

À 50 Hz, la tension passe par zéro toutes les **10 ms** : la commutation est retardée de 10 ms au plus.

## Ses limites

Comme le contacteur statique (module 7), il présente une **chute de tension** d'environ 1 à 1,5 V en conduction et **chauffe** : il se monte sur un dissipateur au-delà de quelques ampères. Il laisse passer un petit **courant de fuite** à l'état bloqué : une petite lampe peut rester faiblement allumée. Et il claque souvent en court-circuit : on ne l'utilise jamais pour séparer.

## À retenir

- Optocoupleur + triac : isolement par la lumière, aucune usure.
- Zéro de tension : commutation retardée de 10 ms au plus à 50 Hz.
- Chute de tension, chaleur et courant de fuite.
