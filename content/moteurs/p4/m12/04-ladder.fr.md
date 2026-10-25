Le **ladder** (langage à contacts, LD) dessine le programme comme un schéma électrique couché : deux **rails** verticaux et, entre eux, des **réseaux** horizontaux. Le « courant » logique circule de gauche à droite.

## Les éléments

- **Contact à fermeture** `-| |-` : passant quand le bit lu vaut 1.
- **Contact à ouverture** `-|/|-` : passant quand le bit lu vaut 0.
- **Bobine** `-( )-` : elle écrit 1 dans son bit quand le réseau est passant, 0 sinon.
- Contacts **en série** : fonction ET ; contacts **en parallèle** : fonction OU (module 8).

## La marche-arrêt avec auto-maintien

![Réseau de marche-arrêt : contact %IX0.0 (arrêt), puis %IX0.1 (marche) doublé en parallèle par le contact %QX0.0, puis bobine %QX0.0](/static/content/moteurs/m12/maintien.svg)

- L'arrêt S1 est câblé **à ouverture** : au repos, %IX0.0 vaut 1. Dans le programme, on le teste donc par un contact **à fermeture**.
- Un appui sur marche (%IX0.1 = 1) rend le réseau passant : %QX0.0 passe à 1.
- Le contact **%QX0.0**, en parallèle sur la marche, maintient le réseau quand on relâche : c'est l'**auto-maintien**, comme le 13-14 d'un contacteur (module 9).
- Un appui sur arrêt fait passer %IX0.0 à 0 : le réseau s'ouvre, la sortie retombe.

## Les bobines SET et RESET

![Bobine S : %IX0.1 met %QX0.0 à 1 ; bobine R : %IX0.0 le remet à 0](/static/content/moteurs/m12/set-reset.svg)

Une bobine **S** (SET) met son bit à 1 et l'y laisse, même quand le réseau redevient non passant. Une bobine **R** (RESET) le remet à 0. On obtient le même effet qu'un auto-maintien. Si les deux réseaux sont vrais en même temps, c'est le **dernier** dans le programme qui l'emporte : on place le RESET après le SET pour que l'arrêt soit prioritaire.

## Règles de lecture

- Une sortie ne doit être écrite par une bobine **qu'à un seul endroit** du programme (sauf couples SET et RESET).
- Les réseaux s'exécutent de **haut en bas**, dans l'ordre du cycle.

## À retenir

- Contact à fermeture : vrai si le bit vaut 1 ; à ouverture : vrai si le bit vaut 0.
- Série = ET ; parallèle = OU.
- Auto-maintien : contact de la sortie en parallèle sur la marche ; ou SET et RESET.
