Les **détecteurs de proximité** détectent un objet **sans le toucher** : pas d'usure, pas de rebond, des milliers de détections par seconde possibles.

## Inductif ou capacitif

- Le **capteur inductif** crée un champ magnétique alternatif à sa face avant ; une pièce **métallique** qui s'en approche le perturbe et le capteur bascule. Il ne voit que les métaux.
- Le **capteur capacitif** réagit à tout objet qui modifie la capacité devant sa face : métal, mais aussi bois, plastique, liquide, grain. On l'utilise pour détecter un niveau à travers la paroi d'une cuve en plastique.

![Capteur inductif M18 devant une cible en acier ; il bascule quand la cible entre dans sa portée nominale sn = 8 mm](/static/content/moteurs/m4/inductif.svg)

La **portée nominale sn** est donnée pour une cible en acier. Pour d'autres métaux, on la multiplie par un **facteur de correction** : environ 0,7 pour l'inox, 0,4 pour l'aluminium, 0,3 pour le cuivre. **Exemple** : un capteur de sn = 8 mm détecte de l'aluminium à 8 × 0,4 ≈ 3,2 mm.

## Le raccordement en 3 fils

Les capteurs courants ont **trois fils** : **brun** au +24 V, **bleu** au 0 V, **noir** pour la sortie.

![Capteur 3 fils : en PNP, la sortie noire fournit le +24 V à la charge reliée au 0 V ; en NPN, la charge est reliée au +24 V et la sortie la ramène au 0 V](/static/content/moteurs/m4/pnp-npn.svg)

- **PNP** : quand l'objet est détecté, la sortie **fournit** le +24 V à la charge, branchée entre la sortie et le 0 V. C'est la sortie la plus répandue en Europe et sur les automates.
- **NPN** : la sortie **ramène** la charge au 0 V ; la charge est branchée entre le +24 V et la sortie.

Un capteur PNP branché sur une entrée prévue pour du NPN ne fonctionne pas : on vérifie toujours la plaque du capteur et la documentation de l'entrée.

## À retenir

- Inductif : métaux seulement ; capacitif : presque tout.
- sn est donnée pour l'acier ; facteur de correction pour les autres métaux.
- Brun +24 V, bleu 0 V, noir sortie ; PNP fournit le +24 V.
