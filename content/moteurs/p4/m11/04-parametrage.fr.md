Un variateur neuf ne connaît pas son moteur. Le **paramétrage** lui apprend le moteur, puis la façon dont la machine doit démarrer, tourner et s'arrêter. Les noms et numéros des paramètres varient selon les constructeurs ; les notions, elles, sont les mêmes partout.

## Les paramètres du moteur

On recopie la **plaque signalétique** (module 2) :

![Paramètres à saisir : tension 400 V, courant 4,8 A, fréquence 50 Hz, vitesse 1 440 tr/min, accélération 5 s, décélération 3 s, fréquences minimale 10 Hz et maximale 50 Hz](/static/content/moteurs/m11/parametres.svg)

Le courant nominal sert à régler la **protection thermique** du moteur intégrée au variateur, comme un relais thermique (module 7).

## Rampes et limites

![Rampes : accélération de 0 à 50 Hz en 5 s, marche, puis décélération en 3 s](/static/content/moteurs/m11/rampes.svg)

- **Rampe d'accélération** : temps pour passer de 0 à la fréquence nominale. Trop courte, elle provoque un défaut de **surintensité**.
- **Rampe de décélération** : temps pour revenir à 0. Trop courte avec une charge lourde, le moteur devient générateur, renvoie son énergie et fait monter le **bus continu** : défaut de **surtension**. Remède : allonger la rampe ou ajouter une **résistance de freinage**.
- **Fréquences minimale et maximale** : elles bornent la vitesse de la machine.
- **Limite de courant** : elle protège la mécanique et le variateur.

## Entrées, sorties et régulation

- **Entrées logiques** 24 V : marche avant, marche arrière, vitesses présélectionnées, réarmement.
- **Entrée analogique** 0-10 V ou 4-20 mA : consigne de vitesse venant d'un potentiomètre ou d'un automate (module 12).
- **Sorties** : relais de défaut, image de la vitesse ou du courant.
- **Régulateur PID** intégré : le variateur ajuste lui-même la vitesse pour tenir une **pression** ou un **débit** mesuré par un capteur.

Le **mode de commande** (bornier, clavier ou bus de terrain) se choisit aussi par paramètre ; on note toujours les réglages dans le dossier de la machine.

## À retenir

- D'abord la plaque du moteur, puis rampes et limites.
- Décélération trop rapide = surtension du bus ; résistance de freinage ou rampe plus longue.
- Consigne analogique, entrées 24 V et PID pour piloter la machine.
