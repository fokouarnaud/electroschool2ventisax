Presque tous les montages électroniques veulent une tension **continue** et stable. Le secteur fournit de l'alternatif. Une **alimentation** fait le lien, en quatre étapes.

![Chaîne d'une alimentation : transformateur, redresseur, filtre, régulateur puis charge, avec sous chaque bloc la forme de la tension](/static/content/electro/m11/chaine.svg)

1. Le **transformateur** abaisse le 230 V et isole le montage du secteur (module précédent).
2. Le **redresseur** (des diodes) ne laisse passer le courant que dans un sens.
3. Le **filtre** (un condensateur) comble les creux de la tension redressée.
4. Le **régulateur** maintient une tension fixe, quelle que soit la charge.

## Rappel : la diode redresse

En Partie 1 (module « La diode »), une diode seule redressait déjà l'alternatif : elle conduit quand son anode est plus positive que sa cathode, et bloque dans l'autre sens. C'est le redressement **simple alternance**.

## Les valeurs à connaître

Un transformateur est toujours désigné par sa tension **efficace**. La diode, elle, voit la tension **crête** :

**Umax = Ueff × √2**

Avec un secondaire de 12 V efficaces : Umax = 12 × 1,414 ≈ **17 V**. Après la diode (environ 0,7 V de seuil), la sortie atteint 17 − 0,7 ≈ **16,3 V** crête.

![Redressement simple alternance : l'entrée de 17 V crête en gris, la sortie de 16,3 V crête en vert, seules les alternances positives passent](/static/content/electro/m11/simple.svg)

## Le défaut de la simple alternance

Une alternance sur deux est perdue. La tension de sortie retombe à zéro pendant 10 ms à chaque période de 20 ms : il faudra un gros condensateur pour combler ces trous, et l'ondulation restera à **50 Hz**. Le pont de diodes, section suivante, fait mieux.

## À retenir

- Alimentation : transformateur, redresseur, filtre, régulateur.
- Umax = Ueff × √2 ; une diode retire environ 0,7 V.
- La simple alternance perd une alternance sur deux.
