Baisser seulement la fréquence ne suffit pas : la réactance des enroulements baisserait aussi, le courant monterait et le moteur saturerait. Le variateur baisse donc la **tension en même temps** que la fréquence.

## La loi U/f

En gardant le rapport **U / f constant**, on garde le **flux** magnétique du moteur constant, donc son **couple** disponible. Pour un moteur 400 V 50 Hz : U / f = 400 / 50 = **8 V/Hz**.

![Loi U/f : 200 V à 25 Hz, 400 V à 50 Hz ; au-delà de 50 Hz, la tension plafonne à 400 V](/static/content/moteurs/m11/uf.svg)

- À 25 Hz, le variateur fournit 8 × 25 = **200 V**.
- Au-dessus de 50 Hz, la tension ne peut plus monter : le flux diminue, le couple aussi. C'est le **défluxage**, utilisable avec prudence pour dépasser un peu la vitesse nominale.
- Aux très basses vitesses, un réglage de **compensation** (« boost ») ajoute un peu de tension pour vaincre la résistance des enroulements.

## Toute la courbe se décale

![Courbes couple-vitesse à 25 Hz et à 50 Hz : même allure, même couple maximal, décalées en vitesse](/static/content/moteurs/m11/courbes.svg)

À chaque fréquence, le moteur garde sa courbe couple-vitesse, décalée : il fonctionne toujours près de sa vitesse de synchronisme, avec un **glissement** faible. Calculez la vitesse de synchronisme et le glissement pour une fréquence donnée :

[[calc:speed]]

## Le contrôle vectoriel

La loi U/f suffit aux pompes et aux ventilateurs. Pour un convoyeur, un levage ou une machine qui démarre en charge, on choisit le **contrôle vectoriel** : le variateur calcule en permanence l'état magnétique du moteur à partir de ses courants et sépare la part qui crée le flux de celle qui crée le couple. Résultat : couple élevé dès les basses vitesses, vitesse précise malgré les variations de charge.

Le contrôle vectoriel demande de bien saisir la **plaque signalétique** et, souvent, de lancer un **autoréglage** : le variateur mesure lui-même les caractéristiques du moteur à l'arrêt.

## À retenir

- U / f constant : flux et couple constants ; 8 V/Hz pour un moteur 400 V 50 Hz.
- Au-delà de 50 Hz, défluxage : le couple diminue.
- Contrôle vectoriel : couple élevé à basse vitesse ; plaque et autoréglage indispensables.
