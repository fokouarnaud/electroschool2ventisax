La norme IEC 61131-3 définit trois blocs de temporisation. Chacun a une entrée **IN**, une durée **PT** (preset time, écrite par exemple `T#5s`), une sortie **Q** et un temps écoulé **ET**.

## Le TON : retard à la montée

![Bloc TON : contact %IX0.2 sur IN, PT = T#5s, sortie Q vers la bobine %QX0.1](/static/content/moteurs/m12/ton.svg)

Quand **IN passe à 1**, le bloc compte ; après PT, **Q passe à 1**. Si IN retombe avant la fin, le comptage repart de zéro. Quand IN retombe, Q retombe aussitôt. C'est l'équivalent du **relais temporisé au travail** (module 8) : passage étoile-triangle, démarrage différé d'un convoyeur.

## Le TOF : retard à la retombée

Q passe à 1 **dès que IN passe à 1**. Quand IN retombe, Q reste à 1 **pendant PT**, puis retombe. C'est le **relais temporisé au repos** : ventilateur qui continue de tourner après l'arrêt d'un moteur, éclairage d'escalier.

## Le TP : impulsion

Un front montant sur IN produit sur Q une **impulsion de durée PT**, quelle que soit la durée d'appui. Pratique pour un coup de klaxon de 2 s avant le démarrage d'une machine.

![Chronogrammes : TON retarde la montée de Q, TOF retarde sa descente, TP donne une impulsion de durée fixe](/static/content/moteurs/m12/chronos.svg)

## Exemple : étoile-triangle

Le passage étoile-triangle du module 9 devient : %QX0.0 (ligne) et %QX0.1 (étoile) à la marche ; un TON de 5 s lancé par %QX0.0 ; quand il est écoulé, %QX0.1 retombe et %QX0.2 (triangle) monte, avec un contact à ouverture de %QX0.1 en série pour le verrouillage. Le verrouillage **électrique** entre contacteurs reste câblé : on ne confie pas une sécurité au seul programme.

## À retenir

- TON : Q monte PT après IN ; TOF : Q retombe PT après IN ; TP : impulsion de PT.
- Durée écrite T#5s, T#500ms.
- Les verrouillages de sécurité restent câblés.
