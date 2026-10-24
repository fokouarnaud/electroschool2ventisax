Couper le courant d'un radiateur et celui d'un moteur qui démarre, ce n'est pas le même travail pour les contacts. La norme **IEC 60947-4-1** classe donc les emplois en **catégories**.

![Catégories d'emploi : AC-1 charges peu inductives, AC-3 moteurs à cage coupés en marche, AC-4 inversion et à-coups, DC-1 et DC-3 en continu](/static/content/moteurs/m7/categories.svg)

- **AC-1** : charges peu inductives (chauffage, éclairage à incandescence). Le courant coupé est le courant de service ; l'arc est faible.
- **AC-3** : moteurs à cage, démarrés puis **coupés en marche**. À l'établissement, le contacteur supporte le courant de démarrage (6 à 8 In) ; à la coupure, le moteur tourne et ne prend que son courant nominal : la coupure est facile.
- **AC-4** : moteurs à cage **coupés pendant le démarrage** : inversion, marche par à-coups, freinage par contre-courant. Le contacteur coupe alors le courant de démarrage lui-même.
- **DC-1, DC-3** : leurs équivalents en courant continu, où l'arc est plus difficile à éteindre.

## Pourquoi c'est important

![Courant à couper : environ In en AC-3, environ 6 In en AC-4](/static/content/moteurs/m7/coupure.svg)

En AC-4, le contacteur coupe environ **6 fois plus de courant** qu'en AC-3 : l'arc est bien plus énergique, les contacts s'usent bien plus vite. Un même contacteur peut ainsi faire un million de manœuvres en AC-3, mais seulement quelques dizaines de milliers en AC-4. On choisit donc un contacteur **dans la catégorie de son emploi réel** : pour un moteur souvent inversé ou commandé par à-coups, on surdimensionne.

## À retenir

- AC-1 résistif, AC-3 moteur coupé lancé, AC-4 inversion et à-coups.
- AC-4 coupe environ 6 In : usure bien plus rapide.
- Le contacteur se choisit dans la catégorie de son emploi.
