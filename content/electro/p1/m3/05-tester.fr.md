Un transistor douteux se vérifie en quelques secondes avec un multimètre en **mode diode** (symbole de diode sur le sélecteur). Ce mode fait passer un petit courant et affiche la tension de la jonction testée.

## Le modèle des deux diodes

Pour le test, un NPN se comporte comme deux diodes dont les anodes sont reliées à la base : une diode base-collecteur et une diode base-émetteur. Pour un PNP, les deux diodes sont retournées.

![Un NPN vu comme deux diodes : de la base vers le collecteur et de la base vers l'émetteur](/static/content/electro/m3/modele-diodes.svg)

## La procédure pour un NPN

1. Pointe rouge (+) sur la base, pointe noire (COM) sur l'émetteur : on lit environ **0,6 à 0,7 V**.
2. Pointe rouge sur la base, noire sur le collecteur : environ **0,6 à 0,7 V** aussi.
3. Inversez les pointes pour ces deux jonctions : l'appareil affiche **OL** (circuit ouvert).
4. Entre collecteur et émetteur, dans les deux sens : **OL**.

![Multimètre en mode diode, pointe rouge sur la base, pointe noire sur l'émetteur : 0,65 V](/static/content/electro/m3/test-be.svg)

## Interpréter

- Une lecture proche de **0 V** sur une jonction : elle est en court-circuit, le transistor est mort.
- **OL** dans les deux sens sur une jonction : elle est coupée.
- Si les deux jonctions conduisent avec la pointe **noire** sur la base, vous avez un PNP.

Ce test repère aussi la base d'un transistor inconnu : c'est la seule broche qui conduit vers les deux autres. La jonction base-émetteur affiche en général une tension légèrement plus élevée que la jonction base-collecteur.

## À retenir

- Mode diode : environ 0,65 V sur chaque jonction dans le bon sens, OL dans l'autre.
- Collecteur-émetteur : OL dans les deux sens.
- Près de 0 V : court-circuit ; OL partout : coupure.
