On dit qu'une diode est **polarisée** selon la façon dont on lui applique la tension.

## Polarisation directe

L'anode est reliée au côté **+** et la cathode au côté **−**. Dès que la tension dépasse le seuil (environ 0,7 V pour le silicium), la diode conduit : elle se comporte presque comme un fil, avec une chute de tension d'environ 0,7 V à ses bornes. La lampe s'allume.

![Diode passante : pile de 6 V, diode dans le sens direct et lampe allumée](/static/content/electro/m2/directe.svg)

Attention : une diode passante ne limite pas le courant. Dans un vrai montage, une résistance ou la charge elle-même doit fixer ce courant, sinon la diode chauffe et se détruit.

## Polarisation inverse

On retourne la diode : la cathode est côté **+**. La zone de déplétion s'élargit et la diode est **bloquée** : le courant est pratiquement nul (quelques microampères au plus pour une diode au silicium). La lampe reste éteinte, et presque toute la tension de la pile se retrouve aux bornes de la diode.

![Diode bloquée : même montage avec la diode retournée, courant nul, lampe éteinte](/static/content/electro/m2/inverse.svg)

## Un outil de protection

Cette propriété sert tous les jours : une diode en série à l'entrée d'un appareil le protège d'une pile branchée à l'envers. Le prix à payer est la chute de 0,7 V quand tout est branché correctement.

## À retenir

- Directe : anode au +, la diode conduit avec environ 0,7 V à ses bornes.
- Inverse : cathode au +, la diode bloque.
- Une diode passante ne limite pas le courant : prévoyez une résistance.
