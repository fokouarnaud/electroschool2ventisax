Un circuit électrique est une **boucle fermée** : un générateur (pile, batterie, alimentation) pousse des charges électriques à travers des fils et des composants, puis les récupère. Si la boucle est ouverte, par un interrupteur ou un fil coupé, plus rien ne circule.

![Pile de 9 V, interrupteur fermé et lampe allumée, avec la flèche du courant I](/static/content/electro/m1/circuit-simple.svg)

## Trois grandeurs à ne pas confondre

- **La tension U**, en volts (V), est la « pression » électrique entre deux points. Une pile de 9 V maintient 9 V entre ses bornes. Une tension se mesure toujours **entre deux points**.
- **Le courant I**, en ampères (A), est le débit de charges qui traversent un fil. En électronique, on parle surtout de milliampères : 1 mA = 0,001 A.
- **La résistance R**, en ohms (Ω), mesure à quel point un composant s'oppose au passage du courant. 1 kΩ = 1 000 Ω et 1 MΩ = 1 000 000 Ω.

Par convention, le courant sort par la borne **+** du générateur, traverse le circuit et revient par la borne **−**. Ce sens « conventionnel » est celui de toutes les flèches de ce cours.

## Mesurer sans se tromper

Pour mesurer un courant, il faut **ouvrir le circuit** et y insérer l'ampèremètre : il se branche **en série**. Pour mesurer une tension, on pose simplement les pointes du voltmètre aux bornes du composant : il se branche **en parallèle**.

![Ampèremètre en série dans la boucle et voltmètre en parallèle sur la résistance](/static/content/electro/m1/mesures.svg)

Brancher un ampèremètre en parallèle revient à créer un court-circuit : au mieux le fusible du multimètre fond, au pire la pile chauffe. Avant chaque mesure, vérifiez le calibre et la position des cordons.

## À retenir

- Tension en volts (entre deux points), courant en ampères (dans un fil), résistance en ohms.
- Ampèremètre en série, voltmètre en parallèle.
- Un circuit ouvert ne laisse passer aucun courant.
