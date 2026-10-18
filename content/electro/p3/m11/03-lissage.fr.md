La tension redressée est toujours positive, mais elle n'est pas continue : elle monte et retombe à zéro cent fois par seconde. Un **condensateur réservoir** la lisse.

![Montage de lissage : la sortie du pont alimente un condensateur C de 2 200 µF en parallèle sur la charge R d'environ 31 Ω](/static/content/electro/m11/lissage-circuit.svg)

## Charge et décharge

On place un gros condensateur électrolytique **en parallèle sur la charge**, juste après le pont :

1. Près de chaque crête, la tension redressée dépasse celle du condensateur : les diodes conduisent et **rechargent** C jusqu'à la crête.
2. Entre deux crêtes, la tension redressée redescend sous celle du condensateur : les diodes se bloquent, et c'est **C qui alimente la charge**. Il se décharge lentement.

![Tension lissée : elle suit les crêtes puis descend en pente douce jusqu'à la crête suivante, au lieu de retomber à zéro comme la tension redressée seule](/static/content/electro/m11/lissage-courbe.svg)

La tension de sortie ne retombe plus à zéro : elle reste proche de la **tension crête**, avec une petite **ondulation** en dents de scie, étudiée à la section suivante.

## Attention à la tension à vide

Sans charge, le condensateur ne se décharge pas : il reste à la **tension crête**. Un adaptateur de 12 V efficaces donne donc environ **15,6 V continus** après le pont et le condensateur, et non 12 V. Les composants qui suivent doivent le supporter.

## Choisir le condensateur

- **Capacité** : plusieurs centaines à plusieurs milliers de microfarads, selon le courant (section suivante).
- **Tension de service** : au-dessus de la tension crête, avec de la marge ; pour 15,6 V, on prend **25 V**.
- **Polarité** : le condensateur électrolytique est polarisé. Sa borne **−** (repérée par une bande) va au **−** du pont. Monté à l'envers, il chauffe et peut éclater.

Les diodes, elles, ne conduisent plus que pendant de brèves pointes, près des crêtes : leur courant de crête est bien plus grand que le courant moyen de la charge.

## À retenir

- Le condensateur se charge aux crêtes et alimente la charge entre deux crêtes.
- À vide, la sortie vaut la tension crête (15,6 V pour 12 V efficaces).
- Tension de service au-dessus de la crête, et polarité respectée.
