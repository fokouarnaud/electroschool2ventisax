Le **relais** est le petit frère du contacteur : même principe (une bobine qui attire une palette), mais des contacts prévus pour de **faibles courants**, quelques ampères. Il ne commute pas les moteurs ; il **traite les signaux** de la commande : multiplier un ordre, inverser un état, isoler deux circuits.

![Relais électromécanique : la bobine 24 V attire la palette, qui fait passer le commun du contact repos au contact travail](/static/content/moteurs/m8/relais.svg)

Son contact le plus courant est l'**inverseur** : un commun qui touche le contact **repos** quand la bobine n'est pas alimentée, et bascule sur le contact **travail** quand elle l'est.

![Contact inverseur d'un relais KA1 : commun 11, repos 12, travail 14](/static/content/moteurs/m8/inverseur.svg)

Les relais portent le repère **KA**. Leurs contacts sont numérotés comme ceux des contacteurs : 11-12-14 pour un premier inverseur (11 commun, 12 repos, 14 travail), 21-22-24 pour le deuxième.

## Pourquoi un relais

- **Isoler** : la bobine (24 V CC) et les contacts (une charge en 230 V AC, par exemple) n'ont aucun lien électrique.
- **Amplifier** : une sortie d'automate de 0,5 A commande, par un relais, un circuit plus puissant.
- **Multiplier** : un seul ordre ferme plusieurs contacts, vers plusieurs circuits.

**Exemple.** Une bobine de relais 24 V de 0,4 W absorbe I = P / U = 0,4 / 24 ≈ **17 mA** : une sortie d'automate la commande sans difficulté.

## À retenir

- Relais : faibles courants, traitement des signaux ; repère KA.
- Inverseur : 11 commun, 12 repos, 14 travail.
- Il isole, amplifie et multiplie un ordre.
