La vitesse d'un moteur asynchrone dépend du nombre de pôles (module 6) : ns = 60 × f / p. Pour obtenir **deux vitesses** sans variateur, on change le nombre de pôles.

## Le moteur Dahlander

Le moteur **Dahlander** possède un seul enroulement par phase, dont on change le couplage pour diviser le nombre de pôles par deux : les deux vitesses sont dans un **rapport de 1 à 2**.

![Moteur Dahlander : petite vitesse en triangle, réseau sur 1U 1V 1W ; grande vitesse en double étoile, réseau sur 2U 2V 2W et 1U 1V 1W reliées](/static/content/moteurs/m9/dahlander.svg)

- **Petite vitesse** (par exemple 8 pôles, 750 tr/min à 50 Hz) : le réseau arrive sur 1U, 1V, 1W ; enroulements en triangle.
- **Grande vitesse** (4 pôles, 1 500 tr/min) : le réseau arrive sur 2U, 2V, 2W ; les bornes 1U, 1V, 1W sont **reliées entre elles** (double étoile).

Il faut donc **trois contacteurs** : KM1 pour la petite vitesse, KM2 (réseau sur 2U 2V 2W) et KM3 (étoile sur 1U 1V 1W) pour la grande.

![Moteur à deux vitesses : KM1 pour la petite vitesse, KM2 et KM3 pour la grande, verrouillés entre eux](/static/content/moteurs/m9/deux-vitesses.svg)

Les contacteurs de petite et de grande vitesse sont **verrouillés** électriquement et mécaniquement : leur fermeture simultanée serait un court-circuit. Pour des vitesses dans un autre rapport (1 000 et 1 500 tr/min, par exemple), on utilise un moteur à **deux enroulements séparés**.

## Le moteur à rotor bobiné

Le moteur à rotor bobiné (module 6) démarre avec des résistances rotoriques retirées par étapes, par des contacteurs commandés par temporisation ; il peut aussi tourner un peu plus lentement en laissant une partie des résistances, au prix de pertes. Ces solutions sont aujourd'hui souvent remplacées par un **variateur de fréquence** (module 11), qui donne toutes les vitesses.

## À retenir

- Dahlander : deux vitesses dans le rapport 1 à 2.
- Petite vitesse en triangle, grande vitesse en double étoile.
- Contacteurs des deux vitesses toujours verrouillés.
