L'**IGBT** (transistor bipolaire à grille isolée) réunit le meilleur des deux transistors : il se **commande en tension** comme un MOSFET, et **tient de fortes tensions et de forts courants** comme un bipolaire. C'est le composant des variateurs de vitesse (module 11) et des onduleurs.

## Symbole et bornes

![Symbole de l'IGBT avec sa grille G, son collecteur C et son émetteur E ; une diode est montée en antiparallèle](/static/content/moteurs/m10/igbt.svg)

- **G** (grille) : la commande, typiquement +15 V pour conduire, 0 V ou une tension négative pour bloquer.
- **C** (collecteur) et **E** (émetteur) : le passage du courant de puissance.
- Une **diode antiparallèle**, souvent intégrée au module, laisse passer le courant de retour d'un moteur.

À l'état passant, un IGBT présente une chute d'environ **1,5 à 2 V**, presque indépendante du courant : à 20 A, il perd déjà 30 à 40 W, d'où ses gros dissipateurs.

## Modules de puissance

On trouve les IGBT en **modules** : deux IGBT forment un **bras** (l'un vers le +, l'autre vers le −), et un onduleur triphasé en compte trois. La commande est confiée à un circuit spécialisé, le **driver**, qui isole la grille de l'électronique de commande et empêche les deux IGBT d'un même bras de conduire ensemble.

## Choisir entre MOSFET, IGBT et thyristor

![Comparaison : MOSFET jusqu'à quelques centaines de volts et très rapide ; IGBT de 600 à 1 700 V pour les variateurs ; thyristor jusqu'à plusieurs kV, lent](/static/content/moteurs/m10/comparaison.svg)

## Tester un IGBT

Hors tension, condensateurs déchargés, multimètre en position diode : entre E et C, on mesure la diode antiparallèle (environ 0,4 V dans un sens, rien dans l'autre). Entre G et les autres bornes, aucune conduction : une grille en court-circuit signe un composant détruit.

## À retenir

- IGBT : commandé en tension, tient 600 à 1 700 V ; composant des variateurs.
- Chute de 1,5 à 2 V à l'état passant.
- Bras de deux IGBT ; driver obligatoire.
