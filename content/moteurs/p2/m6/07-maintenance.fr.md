Le moteur asynchrone est robuste, mais il n'est pas éternel. Ses ennemis : la **chaleur**, l'**humidité**, la **poussière** et les **vibrations**.

## La maintenance préventive

- **Nettoyer** les ailettes et la grille du ventilateur : un moteur encrassé se refroidit mal.
- **Écouter et toucher** (avec le dos de la main, moteur arrêté) : un bruit de roulement ou une chauffe anormale annoncent une panne.
- **Graisser** les roulements qui le demandent, avec la graisse et la quantité indiquées : trop de graisse fait chauffer.
- **Resserrer** les connexions et vérifier le presse-étoupe.
- Contrôler les **vibrations** et l'alignement.

## Contrôler les enroulements

Moteur **consigné et débranché**, barrettes retirées, on mesure à l'ohmmètre la résistance de chaque enroulement : U1-U2, V1-V2, W1-W2.

![Les trois enroulements U1-U2, V1-V2, W1-W2 d'un moteur débranché doivent présenter la même résistance, ici environ 2,7 Ω](/static/content/moteurs/m6/resistances.svg)

Les trois valeurs doivent être **égales à quelques % près**. Une valeur nettement plus faible signale des spires en court-circuit ; une valeur infinie, un enroulement coupé. L'**isolement** des enroulements par rapport à la carcasse se mesure avec un appareil spécial sous tension élevée (mégohmmètre) : c'est un travail réservé à un technicien habilité, jamais fait dans cette formation.

## Dépanner un moteur qui ne démarre pas

On procède du plus simple au plus compliqué, de l'alimentation vers le moteur :

![Démarche de dépannage : tension aux bornes, protection déclenchée, résistances des enroulements, isolement et roulements](/static/content/moteurs/m6/diagnostic.svg)

1. La tension arrive-t-elle aux bornes, sur les **trois** phases ? Un moteur qui n'a que deux phases ne démarre pas et grogne : c'est la **marche en monophasé**, qui le détruit en quelques minutes si la protection ne coupe pas.
2. La protection a-t-elle déclenché ? Pourquoi (surcharge, blocage, mauvais réglage) ?
3. Les enroulements sont-ils sains (résistances égales) ?
4. L'arbre tourne-t-il librement à la main ? Sinon : roulements ou machine entraînée.

## À retenir

- Chaleur, humidité, poussière, vibrations : les quatre ennemis.
- Trois résistances d'enroulement égales à quelques % près.
- Marche sur deux phases : le moteur grogne et brûle ; la protection doit couper.
