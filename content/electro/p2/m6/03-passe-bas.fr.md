Un **filtre** laisse passer certaines fréquences et en atténue d'autres. Le plus simple est le **passe-bas RC** : une résistance en série, puis un condensateur vers la masse. La sortie Vs est prise **aux bornes du condensateur**.

![Filtre passe-bas : entrée Ve, résistance de 1 kΩ en série, condensateur de 100 nF vers la masse, sortie Vs aux bornes du condensateur](/static/content/electro/m6/passe-bas.svg)

## Un diviseur de tension qui dépend de la fréquence

Le montage ressemble au diviseur de tension de la Partie 1, avec Xc à la place de la seconde résistance. Le rapport de sortie vaut :

**Vs / Ve = Xc / Z = Xc / √(R² + Xc²)**

- **Aux basses fréquences**, Xc est très grande devant R : presque toute la tension se retrouve aux bornes du condensateur, **Vs ≈ Ve**.
- **Aux hautes fréquences**, Xc devient petite : le condensateur court-circuite la sortie, **Vs tend vers 0**.

## Ce qui se passe dans le circuit

En alternatif, les électrons ne font pas le tour du circuit : ils vont et viennent sur place, et la fréquence compte combien de fois par seconde ils changent de sens. Aucun électron ne traverse l'isolant du condensateur : il se charge dans un sens, puis dans l'autre.

- **À basse fréquence**, chaque alternance dure longtemps : le condensateur a le temps de se charger presque jusqu'à la tension d'entrée. Xc est grande, le courant reste faible et la résistance ne fait chuter presque aucune tension. La tension aux bornes du condensateur suit l'entrée : **Vs ≈ Ve**.
- **À haute fréquence**, le courant change de sens avant que le condensateur ait pu se charger : sa tension reste presque nulle. Xc est petite, le courant est fort et presque toute la tension d'entrée tombe dans la résistance : **Vs tend vers 0**.

L'eau aide à le voir. Le piston pousse l'eau dans un sens puis dans l'autre (Ve), la vanne étranglée, placée en série, freine le débit (R) et le soufflet, posé dans le bac et branché en dérivation après la vanne, se gonfle sous la pression (C vers la masse). Le manomètre lit la pression dans le soufflet, comme Vs se lit aux bornes du condensateur. Lentement, le soufflet a le temps de se gonfler et de se dégonfler en entier : l'aiguille suit le piston. Vite, l'eau ne fait qu'aller et venir dans la vanne, le soufflet bouge à peine : l'aiguille reste près de zéro et prend du retard sur le piston. À la fréquence de coupure fc = 1 / (2π·R·C) ≈ 1,6 kHz, Xc = R : l'aiguille n'atteint plus que 0,707 de sa course, avec un retard de 45°.

[[fig:rc_lowpass]]

## Lire la courbe de réponse

![Réponse d'un passe-bas RC de 1 kΩ et 100 nF : Vs / Ve vaut 1 aux basses fréquences, 0,707 vers 1,6 kHz puis chute](/static/content/electro/m6/passe-bas-courbe.svg)

L'axe horizontal est **logarithmique** : chaque graduation multiplie la fréquence par 10 (10 Hz, 100 Hz, 1 kHz…). Cela permet de voir d'un coup d'œil un large domaine de fréquences. La zone où Vs ≈ Ve s'appelle la **bande passante** du filtre.

## Des usages courants

- Supprimer un bruit aigu (souffle) sur un signal audio.
- Lisser une tension qui ondule.
- Ne garder que les variations lentes d'un capteur.

## À retenir

- Passe-bas RC : sortie aux bornes de C.
- Basses fréquences : Vs ≈ Ve ; hautes fréquences : Vs → 0.
- Vs / Ve = Xc / √(R² + Xc²).
