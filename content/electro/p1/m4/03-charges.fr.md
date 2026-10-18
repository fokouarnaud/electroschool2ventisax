La méthode de la section précédente s'applique à toutes les charges. Deux cas reviennent sans cesse : la LED et le relais.

## Commander une LED

Une sortie logique de 5 V ne doit pas alimenter directement une LED puissante ou plusieurs LED. On place la LED et sa résistance série dans le collecteur, alimentées par VCC.

![Commande 5 V, RB = 4,7 kΩ, LED et résistance de 330 Ω dans le collecteur, VCC = 9 V](/static/content/electro/m4/led-transistor.svg)

Exemple : VCC = 9 V, LED rouge de 2 V, transistor saturé (0,2 V). La résistance de la LED reçoit 9 − 2 − 0,2 = 6,8 V : avec 330 Ω, le courant vaut 6,8 / 330 ≈ **20,6 mA**. Côté base, avec β min = 100, il faut au moins 0,21 mA. Avec 4,7 kΩ : IB = 4,3 / 4,7 ≈ 0,91 mA, soit plus de quatre fois le minimum. La saturation est franche.

## Commander un relais

Un **relais** est un interrupteur mécanique actionné par une bobine. Il permet de commander un appareil sur le secteur, isolé du circuit électronique. La bobine consomme plusieurs dizaines de milliampères : un transistor la commande sans difficulté.

![Transistor commandant la bobine d'un relais de 12 V, avec une diode de roue libre en parallèle sur la bobine](/static/content/electro/m4/relais.svg)

## La diode de roue libre

Une bobine s'oppose aux variations brusques de courant. Quand le transistor se bloque, elle produit une **surtension** de plusieurs dizaines, voire centaines de volts, qui peut détruire le transistor. Une **diode de roue libre**, montée en parallèle sur la bobine et **en inverse** (cathode côté +VCC), offre un chemin à ce courant et protège le transistor. Elle ne conduit qu'au moment de la coupure.

Cette protection est obligatoire pour toute charge inductive : relais, moteur, électroaimant, électrovanne.

## À retenir

- La LED et sa résistance se placent dans le collecteur ; la tension de la résistance vaut VCC − U_LED − 0,2.
- Un relais isole le circuit électronique de la charge commandée.
- Diode de roue libre en inverse sur toute bobine commandée par un transistor.
