Trois courants circulent dans un transistor NPN en fonctionnement : le courant de base **IB**, le courant de collecteur **IC** et le courant d'émetteur **IE**. La loi des nœuds du module 1 s'applique : tout ce qui entre ressort par l'émetteur.

**IE = IB + IC**

![Transistor NPN avec IB entrant par la base, IC entrant par le collecteur et IE sortant par l'émetteur](/static/content/electro/m3/courants.svg)

## Le gain en courant β

Le courant de collecteur est **proportionnel** au courant de base, dans un rapport appelé **gain en courant**, noté β (bêta) ou hFE sur les fiches techniques :

**IC = β × IB**

β vaut typiquement entre 100 et 400 pour un petit transistor. Avec β = 150, un courant de base de 50 µA commande un courant de collecteur de 150 × 50 µA = **7,5 mA**.

![Droite IC en fonction de IB pour β = 150 : 50 µA donnent 7,5 mA](/static/content/electro/m3/gain.svg)

Comme IB est très petit devant IC, on considère souvent que **IE ≈ IC**. Dans l'exemple : IE = 7,5 mA + 0,05 mA = 7,55 mA.

## Un gain qui varie

β n'est pas une valeur précise : il change d'un exemplaire à l'autre du même modèle (parfois du simple au triple), avec la température et avec le courant. Les fiches techniques donnent donc une **plage**, avec une valeur minimale. Un bon montage ne doit pas dépendre de la valeur exacte de β : c'est ce que nous verrons pour la commutation au module 4.

## À retenir

- IE = IB + IC, et IE ≈ IC.
- IC = β × IB, avec β entre 100 et 400 en général.
- β varie beaucoup : calculez avec la valeur minimale de la fiche technique.
