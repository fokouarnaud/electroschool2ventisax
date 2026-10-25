Un **automate programmable** (API, ou PLC en anglais) remplace les relais, temporisations et compteurs câblés par un **programme**. Pour changer le fonctionnement d'une machine, on modifie le programme au lieu de recâbler l'armoire.

## Structure

![Automate : unité centrale avec sa mémoire, cartes d'entrées reliées aux capteurs et boutons, cartes de sorties reliées aux bobines et voyants, alimentation 24 V et communication](/static/content/moteurs/m12/structure.svg)

- L'**alimentation**, le plus souvent 24 V continu.
- L'**unité centrale** (CPU) et sa **mémoire** : elle exécute le programme et garde les variables.
- Les **entrées** : elles lisent l'état des boutons, capteurs et contacts.
- Les **sorties** : elles commandent bobines de contacteurs, voyants, électrovannes.
- La **communication** : programmation depuis un ordinateur, échanges avec un pupitre, un variateur (module 11) ou un autre automate.

Du petit **relais programmable** à quelques entrées jusqu'à l'automate modulaire de centaines d'entrées, le principe reste le même.

## Le cycle

L'automate ne traite pas ses entrées au fil de l'eau : il travaille par **cycles** répétés sans fin.

![Cycle : lire toutes les entrées, exécuter le programme, écrire toutes les sorties, puis recommencer](/static/content/moteurs/m12/cycle.svg)

1. **Lire** toutes les entrées et figer leur état dans une image mémoire.
2. **Exécuter** le programme du début à la fin, avec cette image.
3. **Écrire** toutes les sorties d'un coup.

Un tour complet est le **temps de cycle**, de l'ordre de quelques millisecondes. Conséquences : une impulsion plus courte qu'un cycle peut passer inaperçue, et une sortie modifiée deux fois dans le programme ne prend que la **dernière** valeur.

## À retenir

- Le programme remplace la logique câblée.
- Alimentation, unité centrale, entrées, sorties, communication.
- Cycle : lire les entrées, exécuter, écrire les sorties ; quelques ms.
