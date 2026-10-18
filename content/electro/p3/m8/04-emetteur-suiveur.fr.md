Dans l'**émetteur suiveur** (ou collecteur commun), le collecteur va directement à l'alimentation et la sortie est prise sur l'**émetteur**. Ce montage n'agrandit pas la tension, mais il rend un autre service, très précieux.

![Émetteur suiveur : R1 et R2 de 10 kΩ sur la base, collecteur relié au +12 V, RE de 1 kΩ à l'émetteur, sortie par C2 sur l'émetteur](/static/content/electro/m8/suiveur.svg)

## Un gain proche de 1

L'émetteur reste toujours environ 0,7 V sous la base. Si la base monte de 1 V, l'émetteur monte de 1 V : la sortie **suit** l'entrée. Le gain en tension vaut presque 1 (en pratique 0,98 ou 0,99), et la sortie n'est **pas inversée**.

Avec R1 = R2 = 10 kΩ sous 12 V : VB = 6 V, VE ≈ 5,3 V et IE ≈ 5,3 V / 1 kΩ = 5,3 mA.

![Tension de base et tension d'émetteur : même sinusoïde, même amplitude, l'émetteur décalé de 0,7 V vers le bas](/static/content/electro/m8/suiveur-signaux.svg)

## À quoi sert un gain de 1 ?

Le suiveur a un **grand gain en courant** (environ β). Vu de l'entrée, une résistance RE dans l'émetteur paraît β fois plus grande :

**Ze ≈ β × RE**

Avec β = 100 et RE = 1 kΩ, l'entrée du transistor présente environ 100 kΩ, alors que la sortie peut fournir plusieurs milliampères. (Le pont R1, R2 de 5 kΩ en parallèle abaisse ici l'impédance d'entrée du montage complet ; on choisit des résistances de pont plus grandes quand elle compte.)

Le suiveur sert donc d'**adaptateur** ou de **tampon** (buffer) :

- une source fragile (un capteur, un étage à forte impédance de sortie) n'est presque pas chargée ;
- une charge gourmande (un câble, un petit haut-parleur, une LED) est alimentée par le transistor, pas par la source.

## Comparer les deux montages

| Montage | Gain en tension | Sortie | Usage |
|---|---|---|---|
| Émetteur commun | élevé (ex. −39) | inversée | agrandir la tension |
| Émetteur suiveur | ≈ 1 | non inversée | tampon, attaquer une charge |

On les associe souvent : un émetteur commun pour le gain, suivi d'un émetteur suiveur pour attaquer la charge.

## À retenir

- Sortie sur l'émetteur, collecteur à l'alimentation : Av ≈ 1, sans inversion.
- Impédance d'entrée élevée (≈ β × RE), impédance de sortie faible.
- Le suiveur sert de tampon entre une source fragile et une charge.
