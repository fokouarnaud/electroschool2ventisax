Le **schéma de liaison à la terre** (SLT) dit comment sont reliés à la terre, d'une part le neutre du transformateur, d'autre part les masses de l'installation. Il est noté par deux lettres : la première concerne le neutre (T : relié à la terre, I : isolé), la seconde les masses (T : reliées à une terre, N : reliées au neutre). Les principes sont fixés par la norme internationale IEC 60364.

## Schéma TT

Le neutre est relié à la terre au poste du distributeur, les masses à une prise de terre propre à l'installation. Un défaut fait circuler un courant faible à travers les deux prises de terre : il ne suffit pas à faire déclencher un disjoncteur, c'est le **DDR qui coupe au premier défaut**. C'est le schéma le plus répandu chez les particuliers et dans les petits ateliers.

![Schéma TT : neutre et masses reliés à deux prises de terre distinctes ; le DDR coupe au premier défaut](/static/content/moteurs/m1/tt.svg)

## Schéma TN

Les masses sont reliées au neutre, lui-même relié à la terre. Un défaut d'isolement devient un **court-circuit phase-neutre** : le courant est fort, et le disjoncteur ou le fusible coupe au premier défaut. En TN-C, neutre et protection partagent un même conducteur, le **PEN** ; en TN-S, ils sont séparés (N et PE). On le rencontre dans les usines qui ont leur propre transformateur.

![Schéma TN : les masses sont reliées au neutre par le conducteur PEN ; un défaut devient un court-circuit et le disjoncteur coupe](/static/content/moteurs/m1/tn.svg)

## Schéma IT

Le neutre est isolé de la terre (ou relié par une forte impédance). Un premier défaut ne fait circuler qu'un courant minuscule : on **ne coupe pas**, un **contrôleur permanent d'isolement** le signale et l'équipe de maintenance le recherche. Un second défaut sur une autre phase, lui, doit couper. On le choisit quand une coupure serait dangereuse ou coûteuse : bloc opératoire, process continu.

![Schéma IT : neutre isolé ; le premier défaut est signalé par le contrôleur d'isolement, pas coupé](/static/content/moteurs/m1/it.svg)

## À retenir

- TT : DDR, coupure au premier défaut.
- TN : le défaut est un court-circuit, le disjoncteur coupe au premier défaut.
- IT : premier défaut signalé, continuité de service.
