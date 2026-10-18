Le **pont de diodes** (ou pont de Graetz) utilise quatre diodes pour récupérer **les deux alternances** : c'est le redressement **double alternance**.

![Pont de quatre diodes en losange : l'alternatif arrive en haut et en bas, la charge R est branchée entre le + à droite et le − à gauche](/static/content/electro/m11/pont.svg)

## Comment il fonctionne

- Pendant l'alternance positive, le courant passe par une diode vers la borne **+**, traverse la charge, puis revient par la diode opposée.
- Pendant l'alternance négative, ce sont les **deux autres** diodes qui conduisent, et le courant traverse la charge **dans le même sens**.

À chaque instant, le courant traverse **deux diodes** en série. La chute de tension est donc d'environ 2 × 0,7 = **1,4 V** :

**Umax sortie ≈ Ueff × √2 − 1,4 V**

Avec 12 V efficaces : 17 − 1,4 ≈ **15,6 V** crête.

![Redressement double alternance : les deux alternances ressortent positives, 15,6 V crête, et la tension se répète tous les 10 ms](/static/content/electro/m11/double.svg)

## Une fréquence doublée

La tension redressée a maintenant **deux bosses par période** du secteur : elle se répète toutes les 10 ms, soit à **100 Hz**. Pour le filtre, c'est un grand avantage : les creux sont deux fois plus courts, donc deux fois plus faciles à combler.

## Choisir les diodes

Chaque diode doit supporter :

- le **courant** moyen de la charge (une diode de la famille 1N4001 à 1N4007 supporte 1 A) ;
- la **tension inverse** quand elle bloque, environ égale à la tension crête (17 V ici). On prend de la marge : une 1N4001 tient 50 V.

On trouve aussi des ponts tout faits, en un seul boîtier à quatre pattes marquées **~**, **~**, **+** et **−**.

Une autre solution existe : un transformateur à point milieu (module précédent) et deux diodes seulement. Elle donne aussi la double alternance, avec une seule chute de diode, mais demande un secondaire deux fois plus long.

## À retenir

- Pont de quatre diodes : les deux alternances passent, deux diodes conduisent à la fois.
- Umax sortie ≈ Ueff × √2 − 1,4 V.
- Ondulation à 100 Hz au lieu de 50 Hz.
