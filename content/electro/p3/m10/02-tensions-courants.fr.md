Un transformateur change la tension, mais il ne crée pas d'énergie. Si la tension baisse, le courant doit augmenter d'autant.

## Abaisseur ou élévateur

- **Ns < Np** : la tension baisse, c'est un **abaisseur** (230 V vers 12 V).
- **Ns > Np** : la tension monte, c'est un **élévateur** (12 V vers 230 V dans un convertisseur pour voiture, ou la haute tension d'un allume-gaz).

![Deux symboles : à gauche un primaire plus long que le secondaire, abaisseur ; à droite un secondaire plus long, élévateur](/static/content/electro/m10/types.svg)

## Les courants

Pour un transformateur idéal, la puissance entrée au primaire ressort au secondaire : Up × Ip = Us × Is. Le rapport des courants est donc **l'inverse** de celui des tensions :

**Is / Ip = Np / Ns**

Le côté basse tension est le côté **fort courant**, et inversement. C'est pourquoi le fil du secondaire d'un abaisseur est plus gros que celui du primaire.

![Abaisseur 230 V vers 12 V chargé par 12 Ω : le secondaire fournit 1 A, le primaire n'absorbe qu'environ 52 mA](/static/content/electro/m10/abaisseur.svg)

Exemple : 230 V vers 12 V, avec une charge de 12 Ω au secondaire.

1. Courant secondaire : Is = 12 V / 12 Ω = **1 A**.
2. Courant primaire : Ip = Is × Us / Up = 1 × 12 / 230 ≈ **52 mA**, soit environ 19 fois moins.

Le transformateur ne « pousse » pas de courant tout seul : c'est la **charge** du secondaire qui fixe Is, et le primaire s'adapte. Sans charge, le primaire n'absorbe qu'un tout petit courant à vide.

[[calc:transformer]]

## À retenir

- Ns < Np : abaisseur ; Ns > Np : élévateur.
- Us / Up = Ns / Np et Is / Ip = Np / Ns.
- La charge fixe le courant du secondaire ; le primaire suit.
