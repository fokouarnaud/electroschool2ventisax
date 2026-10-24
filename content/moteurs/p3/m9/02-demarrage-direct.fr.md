Le **démarrage direct** branche le moteur d'un coup sur la pleine tension du réseau. C'est le plus simple et le plus répandu : schéma de puissance du module 2, commande marche-arrêt avec auto-maintien.

## Commander depuis plusieurs postes

Une machine longue peut avoir plusieurs postes de commande. La règle découle de la logique câblée (module 8) :

![Commande depuis deux postes : les arrêts S1 et S3 en série, les marches S2 et S4 en parallèle avec le contact d'auto-maintien KM1](/static/content/moteurs/m9/postes.svg)

- les boutons d'**arrêt** se câblent **en série** : n'importe lequel coupe la bobine ;
- les boutons de **marche** se câblent **en parallèle**, avec le contact d'**auto-maintien** : n'importe lequel la ferme.

## Le courant de démarrage

![Courant d'un démarrage direct : environ 7 fois le courant nominal pendant l'accélération, puis le courant de marche](/static/content/moteurs/m9/courant-direct.svg)

Pendant l'accélération, le moteur absorbe **6 à 8 fois son courant nominal**. **Exemple** : un moteur de 10 A appelle environ 70 A pendant une à quelques secondes. Ce pic provoque une **chute de tension** sur la ligne (les lampes du même réseau baissent), et un à-coup mécanique sur la machine (courroies, engrenages).

Le démarrage direct convient donc aux moteurs de **petite et moyenne puissance**, sur un réseau qui supporte cet appel, et aux machines qui acceptent un démarrage brusque. Au-delà, on démarre sous tension réduite (section suivante) ou par un variateur (module 11).

## À retenir

- Arrêts en série, marches en parallèle avec l'auto-maintien.
- Démarrage direct : 6 à 8 fois In, à-coup mécanique.
- Pour les petites et moyennes puissances.
