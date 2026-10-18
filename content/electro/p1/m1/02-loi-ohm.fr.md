La loi d'Ohm relie les trois grandeurs de la section précédente. Pour une résistance, la tension à ses bornes est proportionnelle au courant qui la traverse :

**U = R × I**   donc   **I = U / R**   et   **R = U / I**

Travaillez toujours avec des unités cohérentes : volts, ampères et ohms, ou bien volts, milliampères et kilohms (le produit kΩ × mA donne directement des volts).

![Résistance de 4,7 kΩ alimentée sous 12 V, courant I à calculer](/static/content/electro/m1/ohm-circuit.svg)

## Exemple

Une résistance de 4,7 kΩ est branchée sur 12 V. Le courant vaut I = 12 / 4 700 = 0,002 55 A, soit **2,55 mA**. Avec les unités « électroniques » : 12 V / 4,7 kΩ = 2,55 mA, sans aucune conversion.

## Une droite qui révèle la résistance

Si l'on trace la tension en fonction du courant pour une résistance, on obtient une droite qui passe par l'origine. Plus la résistance est grande, plus la droite est raide : pour le même courant, il faut plus de tension.

![Droites U en fonction de I pour 1 kΩ et 2 kΩ ; la plus raide correspond à 2 kΩ](/static/content/electro/m1/ohm-graph.svg)

Un composant dont la courbe n'est pas une droite (une diode, une lampe à filament) ne suit pas la loi d'Ohm sur toute sa plage : on ne peut alors pas lui attribuer une résistance unique.

Essayez le calculateur : renseignez deux grandeurs, la troisième s'affiche.

[[calc:ohm]]

## À retenir

- U = R × I : retenez cette forme, les deux autres s'en déduisent.
- V, mA et kΩ vont ensemble sans conversion.
- La caractéristique d'une résistance est une droite passant par l'origine.
