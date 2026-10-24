Un **démarreur** réunit ce qu'il faut pour mettre un moteur en marche, l'arrêter et le protéger contre les surcharges.

## Le démarreur manuel

![Démarreur manuel : un disjoncteur-moteur Q1 à bouton rotatif alimente directement le moteur](/static/content/moteurs/m2/manuel.svg)

Le plus simple est un **disjoncteur-moteur** : un seul appareil qui sectionne, protège contre les courts-circuits (déclencheur magnétique) et contre les surcharges (déclencheur thermique réglable). On le manœuvre à la main, par un bouton rotatif ou deux poussoirs. Il convient aux petites machines commandées sur place : touret, pompe d'appoint.

Sa limite : il ne peut pas être commandé à distance, ni par un automate, ni par un capteur, et il ne coupe pas tout seul après une coupure de courant si on ne l'a pas prévu.

## Le démarreur télécommandé

![Démarreur télécommandé : disjoncteur, contacteur, relais thermique, moteur ; le contacteur est piloté à distance par des boutons](/static/content/moteurs/m2/telecommande.svg)

On sépare alors les fonctions : un **disjoncteur** (ou des fusibles) protège contre les courts-circuits, un **contacteur** commandé par sa bobine établit et coupe le courant, un **relais thermique** surveille la surcharge. La bobine peut être pilotée de n'importe où : boutons, fin de course, automate.

Avantage décisif pour la sécurité : après une coupure de courant, le contacteur retombe et **le moteur ne redémarre pas seul** au retour de la tension (l'auto-maintien est perdu). Il faut un nouvel appui sur marche.

## À retenir

- Disjoncteur-moteur : démarreur manuel tout-en-un.
- Démarreur télécommandé : disjoncteur, contacteur, relais thermique.
- Le contacteur retombe à la coupure : pas de redémarrage intempestif.
