Échangeons la résistance et le condensateur : le condensateur passe en série, la résistance va vers la masse, et la sortie est prise **aux bornes de la résistance**. On obtient un **passe-haut RC**.

![Filtre passe-haut : entrée Ve, condensateur de 100 nF en série, résistance de 1 kΩ vers la masse, sortie Vs aux bornes de la résistance](/static/content/electro/m6/passe-haut.svg)

## Le comportement inverse du passe-bas

Le rapport de sortie devient :

**Vs / Ve = R / Z = R / √(R² + Xc²)**

- **Aux basses fréquences**, Xc est très grande : le condensateur bloque presque tout, **Vs tend vers 0**. En continu, Vs = 0 : le passe-haut supprime la composante continue.
- **Aux hautes fréquences**, Xc devient petite : le condensateur se comporte presque comme un fil, **Vs ≈ Ve**.

![Réponse d'un passe-haut RC de 1 kΩ et 100 nF : Vs / Ve part de 0, vaut 0,707 vers 1,6 kHz et atteint 1 aux hautes fréquences](/static/content/electro/m6/passe-haut-courbe.svg)

## Des usages courants

- **Condensateur de liaison** : transmettre un signal audio d'un étage à l'autre en bloquant la tension continue de polarisation.
- Supprimer un ronflement grave (50 Hz) sur un signal plus aigu.
- Ne garder que les variations rapides d'un signal.

## Comment s'en souvenir

Demandez-vous où se trouve le condensateur par rapport à la sortie :

- condensateur **vers la masse**, en travers de la sortie : il court-circuite les hautes fréquences, c'est un **passe-bas** ;
- condensateur **en série**, sur le chemin du signal : il bloque les basses fréquences, c'est un **passe-haut**.

## À retenir

- Passe-haut RC : C en série, sortie aux bornes de R.
- Basses fréquences (et continu) : Vs → 0 ; hautes fréquences : Vs ≈ Ve.
- Vs / Ve = R / √(R² + Xc²).
