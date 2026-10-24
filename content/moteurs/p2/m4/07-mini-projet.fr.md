Ce mini-projet se fait en atelier, avec votre formateur. Vous raccordez un vrai capteur industriel et vous mesurez sa portée selon le métal détecté.

## Objectif

Raccorder un capteur inductif PNP 3 fils, vérifier sa sortie et mesurer sa distance de détection sur plusieurs métaux.

## Sécurité

- Tout le montage est en **24 V continu**, fourni par un **adaptateur mural** 230 V vers 24 V. On ne travaille jamais côté 230 V.
- Câblez adaptateur débranché ; une erreur entre brun et bleu peut détruire le capteur.

![Banc du mini-projet : alimentation 24 V, capteur inductif PNP, sortie noire reliée à une LED et sa résistance de 1 kΩ](/static/content/moteurs/m4/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | adaptateur mural 230 V vers 24 V CC |
| 1 | capteur inductif PNP 3 fils, sn = 8 mm (M18) |
| 1 | LED et résistance de 1 kΩ (ou voyant 24 V) |
| 4 | plaquettes d'acier, d'inox, d'aluminium et de cuivre |
| 1 | réglet ou pied à coulisse |
| 1 | multimètre |

## Variante oscilloscope

1. Câblez : brun au +24 V, bleu au 0 V, noir vers la LED et sa résistance, retour au 0 V.
2. Voie 1 de l'oscilloscope sur la sortie noire. Passez rapidement une plaquette d'acier devant le capteur : observez les fronts de la sortie.
3. Faites tourner un disque muni d'une vis devant le capteur : mesurez la fréquence des impulsions et déduisez-en la vitesse de rotation.

## Variante multimètre seul

1. Même câblage. Multimètre en V continu entre la sortie noire et le 0 V.
2. Approchez lentement la plaquette d'acier : notez la distance à laquelle la sortie passe à 24 V.
3. Éloignez-la : notez la distance à laquelle la sortie retombe (hystérésis).
4. Recommencez avec l'inox, l'aluminium et le cuivre.

| Métal | Distance attendue | Distance mesurée |
|---|---|---|
| acier | 8 mm | |
| inox | 5,6 mm | |
| aluminium | 3,2 mm | |
| cuivre | 2,4 mm | |

## Pour conclure

Calculez, pour chaque métal, le facteur de correction mesuré (distance mesurée / distance mesurée sur l'acier) et comparez-le aux valeurs du cours.
