Choisir un contacteur, c'est lire ses caractéristiques et les comparer au besoin.

![Données d'un contacteur : 9 A et 4 kW en AC-3 sous 400 V, Ith 25 A en AC-1, bobine 24 V CC, un contact à fermeture et un à ouverture, un million de manœuvres](/static/content/moteurs/m7/choix.svg)

1. **La catégorie et le courant** : pour un moteur, on lit le courant (ou la puissance) en **AC-3** à la tension du réseau. **Exemple** : un moteur de 4 kW sous 400 V absorbe environ 7,9 A ; un contacteur de **9 A en AC-3** convient. Pour de l'inversion ou des à-coups, on choisit en AC-4, donc plus gros.
2. **La tension de la bobine** : celle du circuit de commande (24 V CC le plus souvent) ; une bobine 230 V AC branchée sur 24 V ne se fermera jamais, une bobine 24 V branchée sur 230 V brûle.
3. **Les contacts auxiliaires** nécessaires (auto-maintien, verrouillage, signalisation), intégrés ou ajoutés en bloc.
4. **La durée de vie** électrique (nombre de manœuvres) au regard de la cadence de la machine.

Le **courant thermique Ith** (en AC-1) est le courant que le contacteur supporte en permanence sur une charge résistive ; il ne sert pas à choisir pour un moteur.

## Encadré : les tailles NEMA

Les documents américains désignent les contacteurs par des **tailles NEMA** (00, 0, 1, 2…), chacune couvrant une plage de puissances. La norme CEI, elle, raisonne par **catégorie et courant**. Les deux ne se convertissent qu'approximativement :

![Comparaison indicative : taille NEMA 00 vers 9 A, taille 0 vers 18 A, taille 1 vers 27 A, taille 2 vers 45 A en AC-3](/static/content/moteurs/m7/nema.svg)

Dans cette formation et sur le matériel CEI, on choisit toujours par le **courant AC-3** ; la taille NEMA ne sert qu'à lire une documentation américaine.

## À retenir

- Moteur : courant en AC-3 à la tension du réseau.
- Bobine : tension du circuit de commande.
- NEMA ne sert qu'à lire une documentation américaine.
