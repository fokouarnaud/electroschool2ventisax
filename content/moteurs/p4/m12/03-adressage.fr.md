Chaque entrée, sortie ou mémoire porte une **adresse**. La norme **IEC 61131-3** en fixe une écriture neutre, que ce module utilise partout.

## Lire une adresse

![Décomposition de %IX0.1 : % variable directe, I entrée, X bit, 0 numéro d'octet, 1 numéro de bit](/static/content/moteurs/m12/bits.svg)

- **%** : variable directement liée au matériel.
- **I** : entrée (input) ; **Q** : sortie ; **M** : mémoire interne.
- **X** : un seul bit (TOR).
- **0.1** : octet 0, bit 1. Les bits d'un octet vont de 0 à 7.

Ainsi **%IX0.0** est la première entrée, **%QX0.0** la première sortie et **%MX0.0** le premier bit de mémoire. La neuvième entrée est %IX1.0.

## Les mémoires

Un bit de mémoire **%MX** ne correspond à aucune borne : il sert à retenir un état intermédiaire (« cycle en cours », « défaut mémorisé »), comme le ferait un relais auxiliaire.

## Correspondance avec les constructeurs

Chaque constructeur a sa propre écriture. Sur votre matériel, la notice indique la correspondance :

![Correspondance : entrée 0 s'écrit %IX0.0 en IEC, I0.0 chez Siemens, %I0.0 chez Schneider ; sortie 0 : %QX0.0, Q0.0, %Q0.0 ; mémoire 0 : %MX0.0, M0.0, %M0](/static/content/moteurs/m12/adresses.svg)

Les relais programmables simples numérotent souvent leurs bornes (I1, I2… et Q1, Q2…). Gardez toujours une **table des variables** : adresse, nom (« S2_marche »), commentaire.

## Les symboles

Dans un programme, on donne à chaque adresse un **nom symbolique**. Le programme se lit alors comme le schéma de la machine : « Arret_S1 », « KM1_moteur ».

## À retenir

- %I entrée, %Q sortie, %M mémoire ; X un bit ; octet.bit.
- Table de correspondance avec la marque utilisée.
- Une table des variables avec des noms parlants.
