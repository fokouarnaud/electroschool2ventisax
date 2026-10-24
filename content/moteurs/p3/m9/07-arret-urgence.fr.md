Toute machine qui présente un danger porte un ou plusieurs **arrêts d'urgence**. Leurs règles viennent de la norme **IEC 60204-1** (équipement électrique des machines).

## L'arrêt d'urgence

![Arrêt d'urgence : bouton coup de poing rouge à ouverture et à accrochage, en tête du circuit de commande ; réarmer ne redémarre pas](/static/content/moteurs/m9/au.svg)

- Un bouton **coup de poing rouge** sur fond **jaune**, facile à atteindre et à frapper.
- Un contact **à ouverture** à manœuvre positive, en **tête** du circuit de commande : son action coupe tout, même si un fil se coupe (la coupure du fil fait le même effet que l'appui).
- **À accrochage** : il reste enfoncé jusqu'à un **réarmement** volontaire (en tournant ou en tirant).
- **Réarmer ne redémarre pas** : après le réarmement, il faut un nouvel ordre de marche. Grâce à l'auto-maintien, le contacteur est retombé et la machine attend.

Plusieurs arrêts d'urgence se câblent **en série** (logique NON-OU, module 8). Sur les machines dangereuses, la fonction passe par un **relais de sécurité** qui surveille ses propres contacts et le câblage. L'arrêt d'urgence ne remplace jamais la consignation pour une intervention (module 1).

## Le commutateur manuel-0-auto

Une pompe, un compresseur peuvent marcher seuls (commandés par un pressostat, un flotteur, un automate) ou à la main pour un essai. Un **sélecteur à trois positions** choisit le mode.

![Commande manuel-0-auto d'une pompe : en manuel, le bouton S2 commande KM1 ; en auto, le pressostat ; en 0, rien](/static/content/moteurs/m9/manuel-auto.svg)

- **Manuel** : le contact 13-14 du sélecteur alimente le bouton de marche ; l'opérateur commande.
- **0** : aucun ordre ne passe ; position de repos et d'intervention.
- **Auto** : le contact 23-24 alimente le pressostat ; il démarre et arrête la pompe seul.

Les protections (relais thermique, arrêt d'urgence) restent en série **dans tous les modes**.

## À retenir

- Arrêt d'urgence : rouge sur jaune, à ouverture, à accrochage, en tête de la commande.
- Réarmer ne redémarre pas.
- Manuel-0-auto : un sélecteur, les protections toujours en série.
