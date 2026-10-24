Ce mini-projet se fait en atelier, avec votre formateur. Vous mesurez un petit moteur 12 V à courant continu et vous vérifiez l'équation U = E + R × I.

## Objectif

Mesurer la résistance d'induit, le courant à vide et en charge, calculer la force contre-électromotrice et inverser le sens de rotation.

## Sécurité

- Le banc est alimenté en **12 V continu** par une alimentation de laboratoire ou un **adaptateur mural** 230 V vers 12 V. Aucun élément ne dépasse 24 V et on ne travaille jamais côté 230 V.
- Fixez le moteur sur la table : il saute quand il démarre. Ne bloquez jamais l'arbre plus de quelques secondes : le courant de démarrage le ferait chauffer.

![Banc du mini-projet : alimentation 12 V, ampèremètre en série et voltmètre aux bornes du moteur](/static/content/moteurs/m5/banc.svg)

## Matériel

| Quantité | Élément |
|---|---|
| 1 | moteur 12 V à courant continu, à aimants permanents, environ 10 W |
| 1 | alimentation 12 V réglable, 2 A |
| 1 | multimètre (et un second si possible) |
| 1 | inverseur à deux circuits |
| 1 | tachymètre optique (facultatif) |
| 1 | oscilloscope et module MLI 12 V (variante oscilloscope) |

## Variante oscilloscope

1. Faites d'abord les mesures 1 à 4 de la variante multimètre seul.
2. Alimentez le moteur par le module MLI. Voie 1 aux bornes du moteur.
3. Réglez trois rapports cycliques (25 %, 50 %, 75 %) : mesurez sur l'écran la tension moyenne et notez la vitesse.

## Variante multimètre seul

1. Moteur débranché, mesurez la résistance d'induit R à l'ohmmètre ; tournez légèrement l'arbre entre trois mesures et gardez la plus petite.
2. Alimentez en 12 V à vide : mesurez U et I.
3. Freinez légèrement l'arbre (doigt protégé, ou petite charge) : mesurez U et I.
4. Calculez E = U − R × I dans les deux cas.
5. Inversez la polarité avec l'inverseur : vérifiez que le sens change.

| Grandeur | Calculée (R = 1,5 Ω) | Mesurée |
|---|---|---|
| E à vide (I = 0,3 A) | 11,55 V | |
| E en charge (I = 2 A) | 9 V | |
| courant de démarrage U / R | 8 A | |

## Pour conclure

Expliquez pourquoi E baisse quand on freine le moteur, et pourquoi le courant augmente.
