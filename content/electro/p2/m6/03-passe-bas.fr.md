Un **filtre** laisse passer certaines fréquences et en atténue d'autres. Le plus simple est le **passe-bas RC** : une résistance en série, puis un condensateur vers la masse. La sortie Vs est prise **aux bornes du condensateur**.

![Filtre passe-bas : entrée Ve, résistance de 1 kΩ en série, condensateur de 100 nF vers la masse, sortie Vs aux bornes du condensateur](/static/content/electro/m6/passe-bas.svg)

## Un diviseur de tension qui dépend de la fréquence

Le montage ressemble au diviseur de tension de la Partie 1, avec Xc à la place de la seconde résistance. Le rapport de sortie vaut :

**Vs / Ve = Xc / Z = Xc / √(R² + Xc²)**

- **Aux basses fréquences**, Xc est très grande devant R : presque toute la tension se retrouve aux bornes du condensateur, **Vs ≈ Ve**.
- **Aux hautes fréquences**, Xc devient petite : le condensateur court-circuite la sortie, **Vs tend vers 0**.

![Réponse d'un passe-bas RC de 1 kΩ et 100 nF : Vs / Ve vaut 1 aux basses fréquences, 0,707 vers 1,6 kHz puis chute](/static/content/electro/m6/passe-bas-courbe.svg)

## Lire la courbe de réponse

L'axe horizontal est **logarithmique** : chaque graduation multiplie la fréquence par 10 (10 Hz, 100 Hz, 1 kHz…). Cela permet de voir d'un coup d'œil un large domaine de fréquences. La zone où Vs ≈ Ve s'appelle la **bande passante** du filtre.

## Des usages courants

- Supprimer un bruit aigu (souffle) sur un signal audio.
- Lisser une tension qui ondule.
- Ne garder que les variations lentes d'un capteur.

## À retenir

- Passe-bas RC : sortie aux bornes de C.
- Basses fréquences : Vs ≈ Ve ; hautes fréquences : Vs → 0.
- Vs / Ve = Xc / √(R² + Xc²).
