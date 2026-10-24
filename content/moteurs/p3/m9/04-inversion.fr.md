Un convoyeur, un pont roulant, une porte motorisée doivent tourner dans les deux sens. On inverse un moteur triphasé en **permutant deux phases** (module 2) : il faut donc deux contacteurs.

![Inversion : KM1 alimente le moteur pour le sens avant ; KM2, pour le sens arrière, permute les phases L1 et L3](/static/content/moteurs/m9/inversion-puissance.svg)

**KM1** alimente le moteur dans le sens avant, **KM2** dans le sens arrière avec deux phases permutées. Si KM1 et KM2 se fermaient en même temps, deux phases seraient reliées directement : **court-circuit**. Il faut donc les **verrouiller**.

## Les deux verrouillages

![Verrouillage électrique : un contact à ouverture de KM2 dans la branche de la bobine KM1, et un contact à ouverture de KM1 dans celle de KM2](/static/content/moteurs/m9/verrouillage.svg)

- **Verrouillage électrique** : un contact à ouverture (21-22) de KM2 est placé en série avec la bobine de KM1, et réciproquement. Tant que l'un est fermé, l'autre ne peut pas être alimenté.
- **Verrouillage mécanique** : un dispositif mécanique, monté entre les deux contacteurs, empêche physiquement leur fermeture simultanée, même si un contact se soude.

On met **toujours les deux**. Pour passer d'un sens à l'autre, on appuie d'abord sur arrêt ; certains schémas l'imposent, d'autres permettent l'inversion directe au prix d'un fort courant (catégorie AC-4, module 7).

## La marche par à-coups

En **marche par à-coups**, le moteur ne tourne que tant qu'on appuie sur le bouton : pas d'auto-maintien. On l'utilise pour positionner une pièce, un pont, une broche. Un bouton à double contact (à ouverture dans la branche d'auto-maintien, à fermeture vers la bobine) permet d'avoir marche normale et à-coups sur le même circuit. Les à-coups répétés usent vite les contacteurs : on les choisit en AC-4.

## À retenir

- Inversion : deux contacteurs, deux phases permutées.
- Toujours deux verrouillages : électrique et mécanique.
- À-coups : pas d'auto-maintien ; contacteurs en AC-4.
