L'oscillateur **Hartley** est le cousin du Colpitts : on échange les rôles. Cette fois, c'est la **bobine** qui est coupée en deux, et un seul condensateur ferme le circuit résonant.

![Oscillateur Hartley : sous l'amplificateur, un condensateur C de 2,2 nF entre deux bobines L1 et L2 de 50 µH reliées à la masse](/static/content/electro/m9/hartley.svg)

## Une bobine à prise intermédiaire

En pratique, L1 et L2 sont souvent une seule bobine munie d'une **prise** (une connexion intermédiaire) reliée à la masse. Comme pour le Colpitts, ce point milieu met les deux extrémités en opposition et le rapport L1 / L2 règle la part du signal renvoyée.

## La fréquence

Si les deux moitiés ne s'influencent pas (on néglige leur couplage), leurs inductances s'additionnent :

**L = L1 + L2**   et   **f = 1 / (2π × √((L1 + L2) × C))**

Exemple : L1 = L2 = 50 µH, C = 2,2 nF. L = 100 µH et f = 1 / (2π × √(100 µH × 2,2 nF)) ≈ **339 kHz**.

Sur une vraie bobine à prise, le couplage entre les deux moitiés augmente un peu l'inductance totale : la fréquence mesurée est alors un peu plus basse que le calcul.

## Un oscillateur facile à accorder

Le Hartley n'a qu'un condensateur : il suffit d'un **condensateur variable** pour balayer toute une gamme de fréquences, sans toucher au taux de rétroaction. C'était l'oscillateur local de nombreux récepteurs radio.

![Fréquence du Hartley selon C, avec L1 + L2 = 100 µH : environ 712 kHz à 0,5 nF, 339 kHz à 2,2 nF, 225 kHz à 5 nF](/static/content/electro/m9/hartley-courbe.svg)

Comme f varie selon 1 / √C, il faut **quadrupler** C pour diviser la fréquence par deux.

## À retenir

- Hartley : bobine coupée en deux (L1, L2, prise à la masse) et un condensateur C.
- f = 1 / (2π × √((L1 + L2) × C)), couplage négligé.
- Un seul condensateur : facile à accorder avec un condensateur variable.
