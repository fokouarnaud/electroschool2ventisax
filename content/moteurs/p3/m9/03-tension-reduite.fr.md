Pour réduire l'appel de courant au démarrage, on alimente d'abord le moteur sous une **tension réduite**, puis sous la pleine tension.

## Le démarrage étoile-triangle

Le moteur doit être prévu pour fonctionner **en triangle** sur le réseau (par exemple 400 V Δ / 690 V Y sur un réseau 400 V) et avoir ses **six bornes** accessibles. On démarre en **étoile** : chaque enroulement ne reçoit que 400 / √3 = 231 V. Puis une temporisation passe en **triangle**.

![Démarreur étoile-triangle : KM1 alimente le moteur, KM2 forme le point étoile au démarrage, puis KM3 couple les enroulements en triangle](/static/content/moteurs/m9/etoile-triangle.svg)

1. **KM1** (ligne) et **KM2** (étoile) se ferment : le moteur démarre en étoile.
2. Après quelques secondes (temporisation au travail, module 8), **KM2** s'ouvre puis **KM3** (triangle) se ferme.
3. KM2 et KM3 sont **verrouillés** entre eux : leur fermeture simultanée serait un court-circuit.

En étoile, le **courant** de ligne et le **couple** de démarrage sont tous deux **divisés par 3** par rapport au démarrage direct. Le moteur doit donc pouvoir démarrer sa charge avec un tiers de son couple : ventilateurs, pompes centrifuges, machines démarrées à vide. Vérifiez avec le calculateur :

[[calc:stardelta]]

![Courant de démarrage : environ 7 In en direct, environ 2,3 In en étoile-triangle, environ 3 In avec un démarreur progressif réglé](/static/content/moteurs/m9/courants.svg)

## Autres procédés

- **Résistances statoriques** : des résistances en série avec le moteur absorbent une partie de la tension, puis sont court-circuitées.
- **Démarreur progressif** : des thyristors (module 10) font monter la tension **progressivement** selon une rampe réglable. Pas d'à-coup, courant limité à une valeur choisie (souvent 3 à 4 In), arrêt progressif possible pour les pompes (pas de coup de bélier). C'est aujourd'hui la solution la plus courante quand un variateur n'est pas nécessaire.

## À retenir

- Étoile-triangle : courant et couple divisés par 3 ; moteur prévu pour le triangle.
- KM2 et KM3 verrouillés entre eux.
- Démarreur progressif : rampe de tension par thyristors.
