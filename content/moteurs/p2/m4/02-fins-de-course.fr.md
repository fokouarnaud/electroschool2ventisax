Certains appareils se manœuvrent tout seuls, sous l'effet d'une grandeur physique : une position, une température, une pression, un niveau. Ils envoient un ordre de tout ou rien.

## Le fin de course

Le **fin de course** (ou interrupteur de position) est actionné mécaniquement par la pièce mobile : une came appuie sur son galet ou sur son levier, et ses contacts basculent. Il arrête un chariot en bout de course, détecte une porte fermée, compte des passages.

![Fin de course à galet : la came de la pièce mobile appuie sur le galet ; ses contacts 13-14 et 21-22 basculent](/static/content/moteurs/m4/fin-course.svg)

Comme tout appareil de sécurité, un fin de course qui arrête un mouvement dangereux utilise un contact **à ouverture** à manœuvre positive : la came ouvre le contact par force, même si un ressort casse.

## Thermostat, pressostat, flotteur

- Le **thermostat** bascule à une température réglée (chauffage, protection de moteur).
- Le **pressostat** bascule à une pression réglée (compresseur, pompe de surpression).
- Le **flotteur** (ou interrupteur de niveau) bascule à un niveau de liquide (cuve, puisard).

Ils ont tous un **écart de commutation** (hystérésis) : ils ne basculent pas au même seuil dans les deux sens. Sans cet écart, le moteur démarrerait et s'arrêterait sans cesse autour du seuil.

![Pressostat d'un compresseur : marche quand la pression tombe à 4 bar, arrêt quand elle atteint 6 bar ; l'hystérésis vaut 2 bar](/static/content/moteurs/m4/pressostat.svg)

**Exemple.** Un pressostat réglé à 6 bar avec un écart de 2 bar démarre le compresseur à 4 bar et l'arrête à 6 bar. Plus l'écart est grand, moins le moteur démarre souvent, mais plus la pression varie.

## À retenir

- Fin de course : actionné par la pièce mobile, contacts à manœuvre positive pour la sécurité.
- Thermostat, pressostat, flotteur : tout ou rien sur un seuil.
- L'hystérésis évite les démarrages répétés.
