Le multimètre donne une valeur efficace ; il ne montre pas la forme du signal. Pour voir une tension évoluer dans le temps, on utilise un **oscilloscope**, et pour produire une sinusoïde réglable, un **générateur basse fréquence** (GBF).

![Écran d'oscilloscope quadrillé : la sinusoïde occupe 4 divisions crête à crête et une période dure 5 divisions](/static/content/electro/m5/ecran.svg)

## Le générateur basse fréquence

Un GBF se règle avec trois commandes : la **forme** (sinus, carré, triangle), la **fréquence** (de quelques hertz à plusieurs centaines de kilohertz) et l'**amplitude**. Il se branche comme une source : une borne de signal et une borne de masse.

## Lire l'écran de l'oscilloscope

L'écran est quadrillé en **divisions** (souvent 10 en largeur et 8 en hauteur).

- Le réglage vertical, en **volts par division** (V/div), donne l'échelle des tensions.
- La **base de temps**, en secondes par division (ms/div, µs/div), donne l'échelle du temps.

Exemple de l'écran ci-dessus, à 2 V/div et 1 ms/div :

- la sinusoïde occupe 4 divisions crête à crête : Ucc = 4 × 2 = **8 V**, donc Umax = 4 V ;
- une période dure 5 divisions : T = 5 × 1 ms = **5 ms**, donc f = 1 / 0,005 = **200 Hz**.

Choisissez des calibres qui font tenir une ou deux périodes sur la largeur et occuper au moins la moitié de la hauteur : la lecture est plus précise.

## Le banc de mesure

![Le GBF alimente le circuit ; la voie 1 de l'oscilloscope observe l'entrée, la voie 2 la sortie, toutes les masses reliées](/static/content/electro/m5/banc.svg)

Avec deux voies, on compare l'entrée (voie 1) et la sortie (voie 2) d'un circuit. Attention : sur la plupart des appareils, **les masses du GBF et des deux voies sont reliées entre elles** (et souvent à la terre). Toutes les pinces de masse doivent donc aller **au même point** du circuit ; en placer une ailleurs court-circuite une partie du montage.

## À retenir

- Ucc = nombre de divisions verticales × V/div.
- T = nombre de divisions horizontales × base de temps ; f = 1 / T.
- Toutes les masses au même point.
