Quand l'inducteur est bobiné, on peut le relier à l'induit de plusieurs façons. Ce raccordement, appelé **excitation**, change complètement le comportement du moteur.

## Le moteur série

L'inducteur, en **gros fil**, est en **série** avec l'induit : le même courant les traverse. Au démarrage, ce courant est fort, donc le champ aussi : le **couple de démarrage est très élevé**.

![Moteur série : l'inducteur en gros fil est en série avec l'induit ; fort couple au démarrage](/static/content/moteurs/m5/serie.svg)

Mais sa vitesse varie beaucoup avec la charge, et **à vide, il s'emballe** : il ne doit jamais tourner sans charge accrochée à lui. On le trouve dans les démarreurs d'automobile, la traction (anciens tramways, chariots) et, sous forme de **moteur universel**, dans l'outillage portatif (module 6).

## Le moteur shunt

L'inducteur, en **fil fin**, est branché en **parallèle** (en dérivation) sur l'induit : il reçoit une tension constante, donc le champ reste constant.

![Moteur shunt : l'inducteur en fil fin est en parallèle sur l'induit ; vitesse presque constante](/static/content/moteurs/m5/shunt.svg)

Sa **vitesse reste presque constante** quelle que soit la charge : machines-outils, ventilateurs, convoyeurs. Attention : si le circuit de l'inducteur se coupe pendant la marche, le champ disparaît et le moteur peut s'emballer.

## Le moteur composé

Le **moteur composé** réunit un inducteur série et un inducteur shunt : bon couple de démarrage et vitesse stable, sans risque d'emballement à vide. Il convient aux presses, aux ascenseurs, aux laminoirs.

| Excitation | Couple au démarrage | Vitesse | À vide |
|---|---|---|---|
| série | très élevé | très variable | s'emballe |
| shunt | moyen | presque constante | stable |
| composé | élevé | stable | stable |

## À retenir

- Série : fort couple au démarrage, jamais à vide.
- Shunt : vitesse presque constante.
- Composé : le meilleur des deux.
