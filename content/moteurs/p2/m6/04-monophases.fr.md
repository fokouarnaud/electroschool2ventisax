Une seule phase ne crée pas de champ tournant : un enroulement alimenté en monophasé produit un champ qui **pulse**, sans sens de rotation. Un moteur monophasé à cage ne démarre donc pas seul : il lui faut un artifice de démarrage.

## Le moteur à condensateur

On ajoute un **enroulement auxiliaire**, décalé dans l'espace, en série avec un **condensateur**. Le condensateur décale le courant de cet enroulement : les deux enroulements créent ensemble un champ qui tourne, assez pour démarrer.

![Moteur monophasé à condensateur : enroulement principal entre L et N, enroulement auxiliaire en série avec un condensateur de 8 µF](/static/content/moteurs/m6/monophase.svg)

C'est le moteur des pompes, compresseurs de réfrigérateur, ventilateurs, petites machines d'atelier en 230 V. Si le condensateur est défaillant, le moteur grogne mais ne démarre pas (ou démarre seulement si on lance l'arbre à la main, ce qu'on ne fait jamais). On inverse son sens en inversant les connexions de **l'un** des deux enroulements.

## Le moteur à bague de déphasage

Une **spire de cuivre en court-circuit** entoure une partie de chaque pôle ; elle retarde le flux dans cette partie et crée un faible champ tournant.

![Moteur à bague de déphasage : une spire de cuivre sur une partie du pôle retarde le flux et fait démarrer le rotor](/static/content/moteurs/m6/bague.svg)

Simple et bon marché, mais de faible couple et de faible rendement : petits ventilateurs, pompes de lave-linge, hottes.

## Le moteur universel

C'est un moteur **série à collecteur** (module 5) qui fonctionne aussi bien en continu qu'en alternatif, puisque courant et champ s'inversent ensemble. Très rapide et léger : perceuses, meuleuses, aspirateurs. Ses balais s'usent.

## À retenir

- Monophasé : pas de champ tournant sans artifice.
- Moteur à condensateur : enroulement auxiliaire + condensateur.
- Universel : moteur série à collecteur, en alternatif.
