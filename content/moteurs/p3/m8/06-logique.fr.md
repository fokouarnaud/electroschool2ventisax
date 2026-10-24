Avec des contacts, on réalise des **fonctions logiques** : c'est la **logique câblée**, l'ancêtre de l'automate (module 12). On note 1 un contact actionné ou une lampe allumée, 0 sinon.

## ET, OU, NON

![Fonction ET : deux contacts A et B en série ; la lampe ne s'allume que si A et B sont actionnés](/static/content/moteurs/m8/et.svg)

- **ET** : contacts **en série**. La lampe s'allume si A **et** B sont actionnés. Exemple : une presse qui ne descend que si l'opérateur appuie sur deux boutons à la fois, une main sur chacun (commande bimanuelle).

![Fonction OU : deux contacts A et B en parallèle ; la lampe s'allume si A ou B est actionné](/static/content/moteurs/m8/ou.svg)

- **OU** : contacts **en parallèle**. La lampe s'allume si A **ou** B (ou les deux) est actionné. Exemple : plusieurs boutons de marche d'un même moteur (module 9).

![Fonction NON : un contact à ouverture ; la lampe est allumée tant que A n'est pas actionné](/static/content/moteurs/m8/non.svg)

- **NON** : un contact **à ouverture**. La lampe est allumée tant que A n'est **pas** actionné.

## Tables de vérité

| A | B | ET | OU | NON-ET | NON-OU |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

- **NON-ET** (NAND) : deux contacts **à ouverture en parallèle** ; la lampe ne s'éteint que si A et B sont actionnés tous les deux.
- **NON-OU** (NOR) : deux contacts **à ouverture en série** ; la lampe s'éteint dès que A ou B est actionné. C'est la logique des **arrêts** : plusieurs boutons d'arrêt en série, chacun peut tout arrêter.

## À retenir

- Série = ET, parallèle = OU, contact à ouverture = NON.
- Arrêts en série (NON-OU), marches en parallèle (OU).
- La table de vérité donne la sortie pour chaque combinaison.
