L'antenne d'un récepteur capte en même temps les signaux de toutes les stations. Pour n'en écouter qu'une, on utilise un **circuit d'accord** : un bouchon LC dont on règle la fréquence de résonance sur celle de la station.

![Antenne reliée à un bouchon formé d'une bobine de 100 µH et d'un condensateur variable d'environ 253 pF, suivi d'un amplificateur](/static/content/electro/m7/accord.svg)

## Le condensateur variable

Pour changer de station, on fait varier C à l'aide d'un **condensateur variable** (symbole barré d'une flèche) : c'est le bouton de recherche des anciens postes. Comme f0 = 1 / (2π × √(L × C)) :

- **diminuer C** fait **monter** f0 ;
- **augmenter C** (ou L) fait **descendre** f0.

## Calculer la capacité d'accord

On retourne la formule pour trouver C quand on connaît f0 et L :

**C = 1 / (4π² × f0² × L)**

Exemple : L = 100 µH et une station à 1 MHz. 4π² ≈ 39,48 ; f0² = 10¹² ; C = 1 / (39,48 × 10¹² × 0,000 1) ≈ **253 pF**.

Autre exemple : pour 100 kHz avec L = 1 mH, C ≈ 2,53 nF.

![Trois stations à 0,9, 1 et 1,1 MHz ; la courbe du circuit accordé sur 1 MHz laisse passer la station centrale et atténue les deux autres](/static/content/electro/m7/stations.svg)

## La sélectivité en pratique

Un circuit d'accord doit avoir un **Q assez élevé** pour séparer deux stations voisines, sans être trop étroit, sinon il couperait une partie du son transmis. Les récepteurs réels combinent plusieurs circuits accordés et des amplificateurs, sujets de la Partie 3.

## Ce qui se passe dans le circuit

L'antenne amène les trois stations en même temps au bouchon formé par la bobine de 100 µH et le condensateur variable. Tourner le bouton fait entrer les lames mobiles entre les lames fixes : la surface en regard grandit, C augmente et f0 descend. Lames sorties (180 pF), le circuit est accordé sur 1,19 MHz ; lames rentrées (360 pF), sur 0,839 MHz.

Réglé sur 253 pF, il résonne à 1 MHz : la station centrale passe entièrement, tandis que celles à 0,9 MHz et 1,1 MHz ne passent qu'à 12 % et 13 % (Q = 40). À 313 pF, c'est la station à 0,9 MHz qui passe, et celle à 1,1 MHz tombe à 6 %.

[[fig:lc_tuning]]

## À retenir

- Le circuit d'accord est un bouchon LC réglé sur la fréquence de la station.
- C = 1 / (4π² × f0² × L).
- Diminuer C fait monter f0.
