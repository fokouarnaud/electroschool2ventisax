D'autres principes permettent de détecter plus loin, ou des objets que les capteurs inductifs ne voient pas.

## Les cellules photoélectriques

Un émetteur envoie un faisceau de lumière (souvent infrarouge) ; un récepteur détecte sa présence ou son absence. Trois montages :

![Trois montages de cellule photoélectrique : barrage avec émetteur et récepteur séparés, reflex avec réflecteur, proximité avec renvoi par l'objet](/static/content/moteurs/m4/photo.svg)

- **barrage** : émetteur et récepteur face à face ; l'objet coupe le faisceau. Portée la plus grande, jusqu'à des dizaines de mètres.
- **reflex** : émetteur et récepteur dans le même boîtier, face à un **réflecteur** ; l'objet coupe le faisceau aller-retour.
- **proximité** (ou diffus) : c'est l'objet lui-même qui renvoie la lumière ; portée plus courte, qui dépend de la couleur de l'objet.

## Les capteurs à effet Hall

Un capteur à **effet Hall** détecte un **champ magnétique** : un aimant fixé sur la pièce mobile le fait basculer. On le trouve sur les vérins (position du piston), dans les moteurs sans balais et dans les capteurs de vitesse.

## Les capteurs à ultrasons

Le capteur émet une salve d'ultrasons et mesure le **temps** que met l'écho à revenir. Le son parcourt l'aller et le retour à environ 340 m/s dans l'air : la distance vaut **d = v × t / 2**.

![Capteur à ultrasons : l'onde part vers l'objet et revient ; la distance vaut v × t / 2](/static/content/moteurs/m4/ultrasons.svg)

**Exemple.** L'écho revient après 5 ms : d = 340 × 0,005 / 2 = **0,85 m**. Les ultrasons détectent les objets transparents, les liquides et les matières en vrac, quelle que soit leur couleur : on les utilise pour mesurer le niveau d'une cuve.

## À retenir

- Barrage, reflex, proximité : de la plus longue à la plus courte portée.
- Effet Hall : détection d'un aimant.
- Ultrasons : d = v × t / 2, avec v ≈ 340 m/s.
