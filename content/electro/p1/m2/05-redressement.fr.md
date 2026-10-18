Le secteur et les transformateurs fournissent une **tension alternative** : elle change de sens plusieurs dizaines de fois par seconde (50 fois au Cameroun). Or la plupart des circuits électroniques ont besoin de courant continu. La diode, qui ne laisse passer le courant que dans un sens, est l'outil idéal pour **redresser** cette tension.

![Source alternative de 12 V, diode et résistance de charge : redressement simple alternance](/static/content/electro/m2/simple-alternance.svg)

## Le redressement simple alternance

Avec une seule diode en série, seules les alternances positives traversent la charge. Pendant les alternances négatives, la diode est bloquée et la tension de sortie est nulle. La sortie est donc une suite de « bosses », toutes du même côté.

![Tension d'entrée sinusoïdale et tension redressée : seules les alternances positives passent, diminuées de 0,7 V](/static/content/electro/m2/redresse-courbe.svg)

Remarquez que chaque bosse est un peu plus basse que l'entrée : la diode passante « prend » ses 0,7 V au passage. Avec une crête de 12 V, la sortie culmine vers 11,3 V.

## Vers une tension continue

Cette tension ne change plus de signe, mais elle est loin d'être constante. Deux améliorations sont courantes :

- le **pont de diodes** (quatre diodes) redresse aussi les alternances négatives : on parle de redressement double alternance ;
- un **condensateur de filtrage** placé en parallèle sur la charge se charge à chaque crête et comble les creux, comme vu au module 1.

## À retenir

- Une diode seule ne garde que les alternances positives : redressement simple alternance.
- La crête de sortie est diminuée d'environ 0,7 V.
- Pont de diodes et condensateur de filtrage rapprochent la sortie d'une tension continue.
