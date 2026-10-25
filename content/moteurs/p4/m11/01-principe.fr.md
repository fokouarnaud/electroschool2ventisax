La vitesse d'un moteur asynchrone dépend de la **fréquence** de son alimentation (module 6) : ns = 60 × f / p. Pour la faire varier, il faut donc un appareil qui fabrique une fréquence réglable : le **variateur de fréquence** (ou convertisseur de fréquence).

## Trois étages

![Variateur : le réseau 400 V 50 Hz passe par un redresseur, charge le bus continu à 540 V, puis un onduleur MLI alimente le moteur](/static/content/moteurs/m11/blocs.svg)

1. Le **redresseur** (pont de six diodes, module 10) transforme le réseau triphasé en tension continue.
2. Le **bus continu**, avec ses gros condensateurs, stocke cette tension : environ **540 V** sur un réseau 400 V.
3. L'**onduleur**, fait de six IGBT, découpe le bus continu pour recréer un triphasé dont on règle la **fréquence** et la **tension**.

**Danger** : les condensateurs du bus restent chargés plusieurs minutes après la coupure. On attend le délai indiqué sur l'appareil (souvent 5 à 15 min) et on **vérifie l'absence de tension** sur le bus avant toute intervention (module 1).

## La modulation de largeur d'impulsion

L'onduleur ne produit pas une vraie sinusoïde : il envoie des impulsions de **largeur variable**, à quelques kilohertz. Comme les enroulements du moteur sont inductifs, le **courant** lisse ces impulsions et devient presque sinusoïdal.

![Impulsions de l'onduleur dont la largeur varie ; leur moyenne, et le courant du moteur, suivent une sinusoïde](/static/content/moteurs/m11/mli.svg)

## Ce que le variateur apporte

- **Démarrage doux** : courant limité à environ 1,5 In, au lieu de 6 à 8 In en direct.
- **Vitesse réglable**, avec économies d'énergie sur les pompes et les ventilateurs.
- **Protections** intégrées du moteur (surcharge, surintensité) et du variateur.
- Inversion du sens et freinage commandés par paramètres.

## À retenir

- Redresseur, bus continu (≈ 540 V sur 400 V), onduleur à IGBT.
- La MLI fabrique un courant presque sinusoïdal de fréquence réglable.
- Bus continu dangereux plusieurs minutes après la coupure.
