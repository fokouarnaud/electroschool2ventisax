Les oscillateurs LC conviennent aux hautes fréquences, mais ils dérivent un peu avec la température et les tolérances. Deux autres familles répondent à d'autres besoins : le **quartz** pour la précision, le **réseau RC** pour les basses fréquences.

## Le quartz

Un **quartz** est une petite lame de cristal qui vibre mécaniquement quand on lui applique une tension, à une fréquence fixée par sa taille et sa coupe. Électriquement, il se comporte comme un circuit résonant au facteur de qualité immense.

![Symbole du quartz, une lame entre deux électrodes, avec Q ≈ 50 000, comparé à un circuit LC avec Q ≈ 50](/static/content/electro/m9/quartz.svg)

Avec un Q de plusieurs dizaines de milliers, la bande passante est minuscule : l'oscillateur ne peut fonctionner qu'à cette fréquence-là. On remplace simplement une partie du réseau LC d'un Colpitts par le quartz.

Exemples :

- **32 768 Hz** dans les montres : c'est 2 puissance 15. En divisant 15 fois par deux, on obtient exactement 1 impulsion par seconde.
- **16 MHz** pour cadencer un microcontrôleur.

## L'oscillateur à pont de Wien

Pour quelques hertz à quelques centaines de kilohertz, les bobines deviennent encombrantes. On utilise alors un réseau **RC** : le **pont de Wien**, avec un AOP non inverseur.

![Oscillateur à pont de Wien : R et C en série de la sortie vers l'entrée plus, R et C en parallèle de l'entrée plus vers la masse, Rf de 20 kΩ et Rin de 10 kΩ sur l'entrée moins](/static/content/electro/m9/wien.svg)

Le réseau (R et C en série, puis R et C en parallèle) n'apporte **aucun déphasage** à une seule fréquence, où il renvoie exactement **1/3** du signal :

**f = 1 / (2π × R × C)**

Avec R = 10 kΩ et C = 16 nF : f = 1 / (2π × 10 000 × 0,000 000 016) ≈ **995 Hz**, soit environ 1 kHz.

L'AOP non inverseur ne déphase pas ; il doit compenser l'atténuation de 1/3, donc avoir un gain d'au moins **3** : Av = 1 + Rf / Rin = 1 + 20 / 10 = 3. En pratique, on prend un gain légèrement supérieur pour assurer le démarrage, puis on limite l'amplitude (deux diodes en parallèle sur une partie de Rf, par exemple).

## À retenir

- Quartz : Q très élevé, fréquence très stable (32 768 Hz, 16 MHz…).
- Pont de Wien : f = 1 / (2π × R × C), le réseau renvoie 1/3 du signal.
- L'AOP du pont de Wien doit avoir un gain d'au moins 3.
