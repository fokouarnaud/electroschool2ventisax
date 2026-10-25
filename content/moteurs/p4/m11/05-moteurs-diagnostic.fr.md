Un moteur standard fonctionne sur variateur, à condition de respecter quelques limites. Et quand le variateur s'arrête en défaut, son message guide le dépannage.

## Le déclassement à basse vitesse

Un moteur **autoventilé** est refroidi par le ventilateur monté sur son propre arbre. À basse vitesse, ce ventilateur souffle beaucoup moins : le moteur ne peut plus fournir son couple nominal en permanence sans surchauffer.

![Couple permanent admissible : environ 0,6 Cn à très basse vitesse pour un moteur autoventilé, contre 1 Cn avec une ventilation forcée](/static/content/moteurs/m11/declassement.svg)

Pour une machine qui tourne longtemps à basse vitesse et pleine charge (convoyeur, extrudeuse), on choisit une **ventilation forcée** (ventilateur indépendant) ou un moteur surdimensionné. Les pompes et ventilateurs, dont le couple baisse avec la vitesse, ne posent pas ce problème.

## Les autres contraintes

- **Isolation** : les fronts raides de la MLI sollicitent l'isolant des enroulements ; avec un câble long, on choisit un moteur prévu pour variateur ou on ajoute un **filtre de sortie**.
- **Roulements** : des courants parasites peuvent traverser les roulements ; mise à la terre soignée, voire roulement isolé sur les gros moteurs.
- **Survitesse** : au-delà de 50 Hz, vérifier la tenue mécanique (roulements, équilibrage, ventilateur).
- **Sonde thermique** : une sonde dans les enroulements, reliée au variateur, protège mieux qu'un calcul.

## Diagnostic des défauts

![Défauts courants : surintensité, surtension du bus, sous-tension, surchauffe, et leurs causes probables](/static/content/moteurs/m11/defauts.svg)

Démarche :

1. **Lire** le code de défaut et l'historique avant de réarmer ; noter les conditions (démarrage, freinage, charge).
2. **Interpréter** : un défaut au démarrage pointe la rampe ou le moteur ; au freinage, le bus continu ; aléatoire, le réseau ou la CEM.
3. **Vérifier hors tension** (bus déchargé, absence de tension vérifiée) : isolement du câble et du moteur **débranché du variateur**, serrage des connexions, ventilateurs.
4. **Corriger** le paramètre ou la cause, puis réarmer.

Ne jamais mesurer l'isolement d'un moteur avec le variateur raccordé : la tension d'essai détruirait l'onduleur.

## À retenir

- Autoventilé à basse vitesse : couple permanent réduit ; ventilation forcée si besoin.
- Isolation, roulements et survitesse à surveiller.
- Lire le défaut, interpréter, vérifier hors tension, corriger.
