À l'autre bout de la chaîne de commande, les **actionneurs** transforment un ordre électrique en action physique.

## L'électrovanne

Une **électrovanne** ouvre ou ferme le passage d'un fluide (air comprimé, eau, gaz). Sa bobine, alimentée, attire un noyau mobile qui libère le passage ; un ressort le referme quand la bobine n'est plus alimentée.

![Électrovanne : la bobine 24 V alimentée attire le noyau qui ouvre le passage du fluide ; symbole YV1](/static/content/moteurs/m4/electrovanne.svg)

Sur le schéma, sa bobine porte le repère **YV**. On choisit sa tension (souvent 24 V), son état au repos (**normalement fermée** ou normalement ouverte) et le fluide qu'elle supporte. Les électrovannes pilotent les vérins pneumatiques des machines.

## Le moteur pas à pas

Un **moteur pas à pas** tourne d'un angle fixe, un **pas**, à chaque impulsion reçue. Un moteur courant fait **200 pas par tour**, soit 360 / 200 = **1,8° par pas**.

![Moteur pas à pas : 200 pas par tour, 1,8° par impulsion ; la position est connue sans capteur](/static/content/moteurs/m4/pas-a-pas.svg)

**Exemple.** Pour tourner d'un quart de tour (90°), il faut 90 / 1,8 = **50 impulsions**. Comme chaque impulsion donne un pas, la position est connue **sans capteur**, tant que le moteur ne « saute » pas de pas sous une charge trop forte. On l'utilise sur les imprimantes 3D, les petites machines à commande numérique, les vannes motorisées.

## Le servomoteur

Le **servomoteur** est un moteur associé à un capteur de position (codeur) et à un variateur qui corrige en permanence l'écart entre la position voulue et la position mesurée : c'est une **boucle fermée**. Plus précis et plus rapide qu'un pas à pas, il équipe les robots et les machines-outils.

## À retenir

- Électrovanne : bobine YV, normalement fermée ou ouverte.
- Pas à pas : 200 pas par tour, 1,8° par pas, position sans capteur.
- Servomoteur : boucle fermée avec un codeur.
