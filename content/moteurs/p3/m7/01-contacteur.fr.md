Le **contacteur** est l'interrupteur télécommandé des moteurs : une petite puissance (sa bobine, souvent en 24 V) commande l'ouverture et la fermeture d'un circuit de puissance (le moteur, en 400 V).

## Sa constitution

![Constitution d'un contacteur : circuit magnétique avec sa bobine, armature mobile, ressort de rappel et contacts principaux](/static/content/moteurs/m7/constitution.svg)

- Le **circuit magnétique** fixe porte la **bobine**. Alimentée, elle attire l'**armature mobile**.
- L'armature entraîne les **contacts principaux** (ou pôles), qui se ferment.
- Quand la bobine n'est plus alimentée, un **ressort de rappel** ramène l'armature et ouvre les contacts.

Le contacteur est donc **monostable** : il ne reste fermé que tant que sa bobine est alimentée. Une coupure de courant le fait retomber, ce qui protège contre les redémarrages inattendus.

## Le même appareil dans trois rôles

![Symbole du contacteur KM1 : bobine A1-A2, trois pôles de puissance 1-2, 3-4, 5-6, contacts auxiliaires 13-14 et 21-22](/static/content/moteurs/m7/symbole.svg)

Sur les schémas, le contacteur apparaît à plusieurs endroits, toujours avec le même repère (KM1) :

- sa **bobine** A1-A2 dans le schéma de commande ;
- ses **pôles de puissance** 1-2, 3-4, 5-6 dans le schéma de puissance ;
- ses **contacts auxiliaires** (13-14 à fermeture, 21-22 à ouverture) dans le schéma de commande : auto-maintien, verrouillages, signalisation.

La bobine se ferme correctement entre **85 % et 110 %** de sa tension assignée Uc : une tension de commande trop basse fait « coller » mal le contacteur, qui vibre et chauffe.

## À retenir

- Bobine qui attire une armature ; ressort qui la rappelle.
- Monostable : sans courant, le contacteur s'ouvre.
- Un repère, trois places : bobine, pôles, auxiliaires.
