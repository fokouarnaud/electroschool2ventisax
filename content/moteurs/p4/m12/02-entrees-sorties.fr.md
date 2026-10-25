Les entrées et sorties **TOR** (tout ou rien) ne connaissent que deux états : 0 ou 1. En industrie, elles fonctionnent presque toujours en **24 V continu**.

## Les entrées

![Câblage des entrées : S1 (arrêt, à ouverture) sur %IX0.0, S2 (marche, à fermeture) sur %IX0.1, capteur PNP B1 sur %IX0.2, tous alimentés par le +24 V](/static/content/moteurs/m12/entrees.svg)

- Un contact fermé amène le **+24 V** sur la borne d'entrée : l'automate lit **1**. Contact ouvert : il lit **0**.
- Un **capteur PNP** 3 fils (module 4) se raccorde directement : brun au +24 V, bleu au 0 V, noir sur l'entrée. Ce type d'entrée est dit **« sink »** ou à logique positive.
- Une **LED** par entrée, sur l'automate, montre l'état lu : premier outil de dépannage.

## Les sorties

![Câblage des sorties : %QX0.0 alimente la bobine du contacteur KM1, %QX0.1 le voyant H1, avec retour au 0 V](/static/content/moteurs/m12/sorties.svg)

Deux technologies :

| | Sortie à **relais** | Sortie à **transistor** |
|---|---|---|
| tension | continu ou alternatif | continu seulement (24 V) |
| courant | 2 à 8 A | 0,5 A environ |
| vitesse | lente, usure mécanique | rapide, sans usure |

Une sortie ne commande **jamais un moteur directement** : elle alimente la bobine d'un contacteur, qui commute la puissance. Sur une bobine en continu, on ajoute une **diode de roue libre** (module 7).

## Entrées analogiques

Pour une température, une pression ou une consigne de vitesse, on utilise des **entrées analogiques** (0-10 V ou 4-20 mA), converties en nombre. Ce module se limite au TOR.

## À retenir

- TOR en 24 V : contact fermé = 1.
- Capteur PNP directement sur une entrée ; LED d'état pour dépanner.
- Sortie à relais ou à transistor ; la puissance passe toujours par un contacteur.
