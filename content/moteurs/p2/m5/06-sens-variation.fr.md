Le moteur à courant continu se pilote facilement : on choisit son sens par la polarité, sa vitesse par la tension.

## Inverser le sens de rotation

Pour un moteur à aimants permanents, il suffit d'**inverser la polarité** de l'induit : le courant change de sens, les forces aussi.

![Inverser le sens : avec + à gauche le moteur tourne dans le sens horaire, avec − à gauche dans le sens antihoraire](/static/content/moteurs/m5/inversion.svg)

Pour un moteur à inducteur bobiné, on inverse **soit** l'induit, **soit** l'inducteur, mais pas les deux : inverser les deux ne change rien. Dans une machine, l'inversion se fait par deux contacteurs verrouillés entre eux (module 9), ou par un **pont en H** de transistors.

## Faire varier la vitesse par MLI

Faire chuter la tension avec une résistance gaspille l'énergie en chaleur. On préfère la **modulation de largeur d'impulsion** (MLI) : un transistor relie et coupe le moteur des milliers de fois par seconde. Le moteur, par son inertie et l'inductance de son induit, ne « voit » que la **tension moyenne**.

![Tension MLI : impulsions de 12 V avec un rapport cyclique de 30 % ; la tension moyenne vaut 3,6 V](/static/content/moteurs/m5/mli.svg)

**Tension moyenne = rapport cyclique × tension d'alimentation.** Le rapport cyclique est la part du temps pendant laquelle le transistor conduit. **Exemple** : 30 % de 12 V donnent 3,6 V de tension moyenne. Les pertes restent faibles, car le transistor est soit bloqué, soit saturé (module 10).

## À retenir

- Aimants permanents : inverser la polarité inverse le sens.
- Inducteur bobiné : inverser l'induit ou l'inducteur, pas les deux.
- MLI : tension moyenne = rapport cyclique × tension.
