Ce mini-projet se fait en atelier, avec votre formateur, sur un moteur asynchrone triphasé **débranché**. On ne le met jamais sous tension pendant ce mini-projet.

## Objectif

Relever la plaque, calculer vitesse de synchronisme, glissement, courant et couple, puis contrôler les enroulements à l'ohmmètre.

## Sécurité

- Le moteur est **débranché** de tout réseau et le reste ; son câble d'alimentation est retiré ou consigné par le formateur.
- On mesure seulement des **résistances**, à l'ohmmètre (quelques volts). Aucun mégohmmètre, aucune mesure au-delà de 24 V, aucun travail côté 230/400 V.
- Les mesures à l'oscilloscope se font sur la tension d'un petit moteur 12 V utilisé comme génératrice, jamais sur le moteur triphasé.

![Ohmmètre branché entre U1 et U2 d'un moteur débranché, barrettes retirées](/static/content/moteurs/m6/releve.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | moteur asynchrone triphasé débranché, plaque lisible |
| 1 | multimètre (fonction ohmmètre) |
| 1 | tournevis et clé pour la boîte à bornes |
| 1 | petit moteur 12 V à courant continu et oscilloscope (variante oscilloscope) |

## Variante oscilloscope

1. Faites d'abord les relevés 1 à 3 de la variante multimètre seul.
2. Faites tourner à la main l'arbre d'un petit moteur 12 V à courant continu utilisé comme génératrice ; voie 1 à ses bornes.
3. Observez que la tension produite augmente avec la vitesse : c'est la force contre-électromotrice du module 5.

## Variante multimètre seul

1. Relevez la plaque : puissance, tensions, courants, vitesse, cos φ, rendement, classe, IP.
2. Calculez ns, le glissement g, le couple C = P / ω et, sur 400 V, le courant par la formule du module 2.
3. Ouvrez la boîte à bornes, retirez les barrettes et notez leur position.
4. Mesurez U1-U2, V1-V2, W1-W2, puis entre U1 et V1 (doit être infini, barrettes retirées).
5. Remettez les barrettes dans le couplage étoile et refermez.

| Grandeur | Exemple (2,2 kW, 1 440 tr/min, 4 pôles) | Votre moteur |
|---|---|---|
| ns | 1 500 tr/min | |
| glissement | 4 % | |
| couple utile | 14,6 N·m | |
| U1-U2, V1-V2, W1-W2 | trois valeurs égales | |
| U1-V1 sans barrettes | infini | |

## Pour conclure

Expliquez ce que signalerait une résistance V1-V2 deux fois plus faible que les deux autres.
