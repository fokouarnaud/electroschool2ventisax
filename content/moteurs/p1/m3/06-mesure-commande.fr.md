Deux petits transformateurs rendent de grands services dans une armoire : le transformateur de courant, pour mesurer, et le transformateur de commande, pour alimenter les circuits de commande en sécurité.

## Le transformateur de courant (TC)

On ne fait pas passer 200 A dans un ampèremètre de tableau. Le **transformateur de courant** a pour primaire le conducteur lui-même, qui traverse un tore ; son secondaire délivre un courant **proportionnel** et normalisé, en général **5 A** (ou 1 A) pour le courant primaire assigné.

![Transformateur de courant 200/5 A : le conducteur traverse le tore, le secondaire alimente un ampèremètre 5 A](/static/content/moteurs/m3/tc.svg)

Un TC 200/5 A divise le courant par 40. **Exemple** : l'ampèremètre lit 3,5 A ; le courant dans le conducteur vaut 3,5 × 200 / 5 = **140 A**.

**Règle de sécurité :** on ne laisse **jamais** le secondaire d'un TC ouvert quand le primaire est parcouru par un courant. Le TC tenterait d'imposer son courant dans une résistance infinie : une tension très élevée apparaîtrait à ses bornes. Avant de débrancher l'ampèremètre, on court-circuite le secondaire (bornier de court-circuitage prévu à cet effet).

On utilise aussi des **transformateurs de tension** (TT) pour mesurer les tensions HTA avec des appareils prévus pour 100 V.

## Le transformateur de commande

Les circuits de commande (boutons, bobines, voyants) sont alimentés par un **transformateur de commande** 400 V / 24 V (ou 230 V / 24 V), protégé par un fusible.

![Transformateur de commande 400 V / 24 V : il isole le circuit de commande du réseau et l'alimente en très basse tension](/static/content/moteurs/m3/commande-24v.svg)

Il apporte deux choses : l'**isolement** du réseau (primaire et secondaire ne sont pas reliés électriquement) et une **très basse tension** qui protège l'opérateur qui touche un bouton. Sa puissance se choisit d'après les bobines qu'il alimente, en tenant compte de leur appel au moment de la fermeture.

## À retenir

- TC 200/5 A : courant réel = courant lu × 200 / 5.
- Secondaire d'un TC jamais ouvert en service.
- Transformateur de commande : isolement et TBT pour la commande.
