Un moteur peut être détruit de deux façons : par un **court-circuit** (courant énorme, en une fraction de seconde) ou par une **surcharge** (courant un peu trop fort, mais pendant des minutes, qui cuit les isolants). On le protège contre les deux.

## Contre les courts-circuits

Des **fusibles** de type aM (accompagnement moteur, qui laissent passer le courant de démarrage) ou le déclencheur **magnétique** d'un disjoncteur-moteur coupent le court-circuit en quelques millisecondes.

## Contre les surcharges : le relais thermique

Le **relais thermique** (ou relais de surcharge) mesure en permanence le courant de chaque phase. Si le courant dépasse son **réglage** assez longtemps, il ouvre son contact 95-96, placé dans la commande : le contacteur retombe. Il réagit d'autant plus vite que la surcharge est forte ; il détecte aussi la perte d'une phase.

![Courbes de déclenchement : la classe 10 déclenche en moins de 10 s à 7,2 fois le réglage, la classe 20 en moins de 20 s](/static/content/moteurs/m7/declenchement.svg)

La **classe de déclenchement** dit en combien de temps il coupe à 7,2 fois son réglage (le courant d'un moteur bloqué) : **classe 10**, en moins de 10 s, pour les démarrages normaux ; **classe 20**, en moins de 20 s, pour les démarrages longs (grosse inertie : ventilateur, broyeur), sans quoi le relais déclencherait pendant chaque démarrage.

## Le réglage

![Réglage du relais thermique : la molette est réglée sur 4,8 A, le courant nominal lu sur la plaque du moteur, dans une plage de 4 à 6 A](/static/content/moteurs/m7/reglage.svg)

On règle le relais sur le **courant nominal du moteur** lu sur sa plaque, pour la tension du réseau (4,8 A pour le moteur du module 2 couplé en étoile sur 400 V), sans ajouter de marge. On choisit un relais dont la plage encadre ce courant. Le calculateur ci-dessous retrouve ce courant à partir de la plaque :

[[calc:motor_current]]

Après un déclenchement, on cherche la cause (moteur bloqué, phase coupée, charge trop forte) **avant** de réarmer.

## À retenir

- Courts-circuits : fusibles aM ou magnétique ; surcharges : relais thermique.
- Classe 10 normale, classe 20 pour les démarrages longs.
- Réglage = courant de plaque, sans marge.
