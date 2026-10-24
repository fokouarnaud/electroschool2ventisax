Quand l'induit tourne dans le champ, ses conducteurs coupent les lignes de champ : une tension y est **induite**, comme dans une dynamo. Cette tension s'oppose à la tension d'alimentation : c'est la **force contre-électromotrice** E (fcém). Elle est proportionnelle à la vitesse.

## L'équation de l'induit

La tension appliquée U se partage entre la fcém E et la chute de tension dans la résistance R de l'induit :

**U = E + R × I**   donc   **I = (U − E) / R**

![Modèle de l'induit : la source U alimente la résistance R en série avec la fcém E ; U = E + R × I](/static/content/moteurs/m5/fcem.svg)

**Exemple.** Un moteur 12 V a une résistance d'induit R = 1,5 Ω et absorbe I = 2 A en marche. E = U − R × I = 12 − 1,5 × 2 = **9 V**. La puissance convertie en puissance mécanique vaut E × I = 9 × 2 = 18 W.

## Le courant de démarrage

À l'arrêt, le moteur ne tourne pas : E = 0. Le courant de démarrage vaut donc I = U / R, sans rien pour le limiter.

**Exemple.** Le même moteur au démarrage : I = 12 / 1,5 = **8 A**, quatre fois son courant de marche. Puis, à mesure qu'il prend de la vitesse, E augmente et le courant baisse.

![Courant de démarrage : il part de plusieurs fois le courant nominal et diminue quand le moteur prend de la vitesse](/static/content/moteurs/m5/demarrage.svg)

Pour les gros moteurs, ce courant serait destructeur : on limite la tension au démarrage (résistances, ou variateur qui monte progressivement la tension).

## La vitesse

Comme E est proportionnelle à la vitesse, à flux constant : **n est à peu près proportionnelle à U − R × I**. On règle donc la vitesse d'un moteur à courant continu en réglant **la tension d'induit**.

## À retenir

- U = E + R × I ; E proportionnelle à la vitesse.
- Au démarrage, E = 0 : I = U / R, courant élevé.
- La vitesse se règle par la tension d'induit.
