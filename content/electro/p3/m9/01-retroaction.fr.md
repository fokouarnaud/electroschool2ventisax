Un **oscillateur** fabrique un signal périodique à partir d'une simple tension continue : l'horloge d'un microcontrôleur, la porteuse d'un émetteur radio, la note d'un buzzer. En Partie 2, un circuit LC chargé oscillait, mais s'éteignait. Ici, on entretient l'oscillation.

## Une boucle fermée

Un oscillateur réunit deux blocs en boucle :

- un **amplificateur** de gain A, qui fournit l'énergie ;
- un **réseau de rétroaction** B (souvent un circuit LC ou RC), qui choisit la fréquence et renvoie une partie de la sortie vers l'entrée.

![Boucle d'un oscillateur : l'amplificateur A, puis le réseau B qui ramène une partie de la sortie à l'entrée](/static/content/electro/m9/boucle.svg)

Contrairement à la contre-réaction des amplificateurs, qui calme le montage, ici la rétroaction est **positive** : le signal renvoyé s'ajoute à celui qui existe déjà.

## Les deux conditions d'oscillation

1. **Le gain de boucle** A × B doit valoir au moins 1. Le réseau B atténue (B est plus petit que 1) ; l'amplificateur doit compenser. Exemple : un réseau qui renvoie 1/29 du signal demande A ≥ 29.
2. **La phase** : le signal doit revenir à l'entrée **en phase**, avec un déphasage total de 0° (ou 360°). Si l'amplificateur inverse (180°), le réseau doit apporter les 180° qui manquent.

Ces deux conditions ne sont réunies qu'à **une seule fréquence** : c'est la fréquence d'oscillation.

## Le démarrage

Il n'y a pas besoin de signal d'entrée. À la mise sous tension, un bruit minuscule contient toutes les fréquences. À la fréquence où la boucle est en phase, il est amplifié à chaque tour : il grandit tant que A × B est un peu **plus grand que 1**.

![Démarrage : une oscillation minuscule grandit à chaque tour, puis son amplitude se stabilise quand A × B revient à 1](/static/content/electro/m9/demarrage.svg)

L'amplitude ne grandit pas sans fin : quand le transistor approche de la saturation, son gain baisse, et A × B redescend à 1. L'amplitude se stabilise.

## À retenir

- Oscillateur = amplificateur + réseau de rétroaction, en boucle.
- Conditions : A × B ≥ 1 et retour en phase (0° ou 360°).
- Le bruit suffit au démarrage ; la saturation limite l'amplitude.
