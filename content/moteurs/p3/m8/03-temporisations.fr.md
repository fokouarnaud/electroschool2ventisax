Un **relais temporisé** (repère **KT**) introduit un retard réglable entre un ordre et l'action de son contact. Deux fonctions de base : le retard à la fermeture (temporisation **au travail**) et le retard à l'ouverture (temporisation **au repos**).

## La temporisation au travail

Le contact se ferme **t secondes après** l'alimentation de la bobine ; il s'ouvre immédiatement quand on coupe la bobine. Si la bobine est coupée avant la fin du délai, le contact ne se ferme jamais.

![Temporisation au travail : la bobine est alimentée à 0, le contact se ferme au bout du délai t et s'ouvre dès la coupure](/static/content/moteurs/m8/ton.svg)

**Usages** : passage d'étoile en triangle après le démarrage (module 9), démarrage décalé de plusieurs moteurs pour ne pas appeler leurs courants en même temps, alarme qui ne se déclenche qu'après une durée minimale.

## La temporisation au repos

Le contact se ferme **immédiatement** à la commande et ne s'ouvre que **t secondes après** la fin de la commande.

![Temporisation au repos : le contact se ferme dès la commande et s'ouvre seulement le délai t après la coupure de la commande](/static/content/moteurs/m8/tof.svg)

**Usages** : ventilateur qui continue de tourner après l'arrêt d'un moteur pour le refroidir, éclairage d'escalier, pompe qui vide un circuit après l'arrêt.

## Symboles et réglage

Sur le schéma, le contact temporisé porte un petit **demi-cercle** sur sa tige, qui indique le sens du retard ; sa bobine est marquée d'une croix ou d'une case grisée selon la fonction. Le délai se règle par une molette, avec une **gamme** (0,1 à 1 s, 1 à 10 s, 1 à 10 min…) choisie d'abord.

## À retenir

- Au travail : retard à la fermeture.
- Au repos : retard à l'ouverture.
- On choisit la gamme, puis on règle le délai.
