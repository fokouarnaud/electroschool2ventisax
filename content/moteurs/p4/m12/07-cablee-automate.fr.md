Passer d'une commande à relais à un automate se fait méthodiquement, en partant du schéma de commande existant.

## La démarche

![Le schéma vertical S1, S2, KM1 devient un réseau ladder : S1 sur %IX0.0, S2 sur %IX0.1, KM1 sur %QX0.0](/static/content/moteurs/m12/conversion.svg)

1. **Lister** les entrées (boutons, fins de course, capteurs, contacts de relais thermiques) et les sorties (bobines, voyants) ; leur donner une adresse et un nom dans la table des variables.
2. **Câbler** les entrées et sorties sur l'automate.
3. **Traduire** chaque branche du schéma en réseau ladder : contacts en série et en parallèle à l'identique, temporisations en blocs TON ou TOF, relais auxiliaires en bits %MX.
4. **Tester** hors puissance (contacteurs sans moteur ou disjoncteur de puissance ouvert), en simulant chaque entrée et en observant les LED.

## Le piège des contacts à ouverture

Un bouton d'arrêt est câblé **à ouverture**, comme en logique câblée. Au repos, son entrée vaut 1 ; dans le ladder, on le teste donc par un contact **à fermeture**.

![Bouton d'arrêt câblé à ouverture : %IX0.0 vaut 1 au repos et se teste par un contact à fermeture ; un fil coupé arrête la machine](/static/content/moteurs/m12/securite.svg)

C'est la **sécurité positive** : si le fil est coupé ou le bouton débranché, l'entrée passe à 0 et la machine s'arrête. Un arrêt câblé à fermeture ne se verrait pas coupé et ne pourrait plus arrêter la machine.

## Ce qui reste câblé

- L'**arrêt d'urgence** coupe directement l'alimentation des sorties ou passe par un **relais de sécurité** ou un automate de sécurité ; il n'est jamais confié au seul programme standard (module 9).
- Les **verrouillages** entre contacteurs d'inversion ou d'étoile-triangle restent câblés en plus du programme.
- Les contacts des **relais thermiques** coupent la bobine en direct, et sont aussi lus par une entrée pour signaler le défaut.

## Avantages et limites

L'automate réduit le câblage, facilite les modifications et le diagnostic (LED, état des variables en ligne). Il demande en revanche un programme sauvegardé et documenté : on garde toujours une **copie à jour** du programme avec le dossier de la machine.

## À retenir

- Lister, câbler, traduire, tester hors puissance.
- Arrêt câblé à ouverture, testé à fermeture : sécurité positive.
- Arrêt d'urgence et verrouillages restent câblés.
