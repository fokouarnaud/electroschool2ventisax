Échangeons la résistance et le condensateur : le condensateur passe en série, la résistance va vers la masse, et la sortie est prise **aux bornes de la résistance**. On obtient un **passe-haut RC**.

![Filtre passe-haut : entrée Ve, condensateur de 100 nF en série, résistance de 1 kΩ vers la masse, sortie Vs aux bornes de la résistance](/static/content/electro/m6/passe-haut.svg)

## Le comportement inverse du passe-bas

Le rapport de sortie devient :

**Vs / Ve = R / Z = R / √(R² + Xc²)**

- **Aux basses fréquences**, Xc est très grande : le condensateur bloque presque tout, **Vs tend vers 0**. En continu, Vs = 0 : le passe-haut supprime la composante continue.
- **Aux hautes fréquences**, Xc devient petite : le condensateur se comporte presque comme un fil, **Vs ≈ Ve**.

## Ce qui se passe dans le circuit

Le condensateur est maintenant sur le chemin du signal. Aucun électron ne traverse son isolant : chaque électron qui arrive sur une armature en repousse un autre hors de l'armature d'en face. Un courant circule donc dans la résistance tant que le condensateur se charge ou se décharge, et il s'arrête dès que le condensateur est chargé.

- **À basse fréquence**, chaque alternance dure longtemps : le condensateur a le temps de se charger presque jusqu'à la tension d'entrée. Xc est grande, le courant reste faible et la résistance ne voit presque aucune tension : **Vs tend vers 0**. En continu, une fois le condensateur chargé, plus aucun courant ne circule : Vs = 0.
- **À haute fréquence**, le courant change de sens avant que le condensateur ait pu se charger : sa tension reste presque nulle. Xc est petite, le courant est fort et presque toute la tension d'entrée se retrouve aux bornes de la résistance : **Vs ≈ Ve**.

L'eau aide à le voir. Le piston pousse l'eau dans un sens puis dans l'autre (Ve), contre la membrane d'une cloche placée en série (C). Aucune goutte ne traverse la membrane, mais en se tendant elle chasse le même volume d'eau de l'autre côté, vers une vanne étranglée qui se vide dans le bac (R vers la masse). Le manomètre lit la pression avant la vanne, comme Vs se lit aux bornes de R. Lentement, la membrane suit tout le mouvement du piston et sa tige monte et descend de toute sa course : le débit dans la vanne reste faible et l'aiguille reste près de zéro. Ce faible débit est le plus fort quand le piston passe au milieu de sa course, presque un quart de période avant son point haut : l'aiguille est en avance sur le piston. Vite, la membrane bouge à peine : l'eau va et vient dans la vanne à plein débit et l'aiguille suit le piston. À la fréquence de coupure fc = 1 / (2π·R·C) ≈ 1,6 kHz, Xc = R : l'aiguille atteint 0,707 de sa course, avec une avance de 45°.

[[fig:rc_highpass]]

## Lire la courbe de réponse

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
