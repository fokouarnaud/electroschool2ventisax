Le **moteur asynchrone à cage** est de loin le moteur le plus répandu dans l'industrie : robuste, simple, sans contact glissant.

## Le rotor à cage

Son rotor est une **cage d'écureuil** : des barres d'aluminium (ou de cuivre) logées dans un empilage de tôles, reliées à chaque bout par un anneau de court-circuit. Aucune borne, aucun fil vers l'extérieur.

![Rotor à cage d'écureuil : barres d'aluminium reliées à chaque bout par un anneau de court-circuit](/static/content/moteurs/m6/cage.svg)

Le champ tournant du stator balaie les barres et y **induit** des courants. Ces courants, dans le champ, subissent des forces de Laplace : le rotor est entraîné dans le sens du champ.

## Le glissement

Si le rotor tournait exactement à la vitesse du champ, les barres ne seraient plus balayées : plus de courant, plus de couple. Le rotor tourne donc toujours **un peu moins vite** que le champ : il est **asynchrone**. L'écart relatif est le **glissement** :

**g = (ns − n) / ns**

**Exemple.** ns = 1 500 tr/min, n = 1 440 tr/min : g = 60 / 1 500 = 0,04, soit **4 %**. À pleine charge, le glissement vaut en général 2 à 6 %.

## Le couple selon la vitesse

![Couple du moteur asynchrone en fonction de la vitesse : couple de démarrage, couple maximal vers 1 230 tr/min, point nominal près de 1 440 tr/min](/static/content/moteurs/m6/couple.svg)

Au démarrage, le moteur absorbe **5 à 8 fois son courant nominal** et fournit un couple voisin de son couple nominal. Il accélère, passe par son **couple maximal**, puis se stabilise là où son couple égale celui de la charge, près du synchronisme. Si la charge augmente, il ralentit un peu, le glissement augmente et le couple aussi.

## À retenir

- Rotor à cage : barres en court-circuit, aucune connexion.
- g = (ns − n) / ns ; 2 à 6 % en charge.
- Démarrage direct : 5 à 8 fois le courant nominal.
