Le JFET présenté au module 3 peut lui aussi servir d'interrupteur. Sa grande différence avec le bipolaire est sa commande : une **tension** sur la grille, et presque aucun courant.

![JFET canal N : LED et résistance de 470 Ω dans le drain, VDD = 9 V ; l'interrupteur K relie la grille à une tension de −5 V](/static/content/electro/m4/jfet-interrupteur.svg)

## Les deux états

- **Grille reliée à la source** (VGS = 0) : le canal est ouvert, le JFET conduit. La LED s'allume.
- **Grille portée sous VGS(off)** (par exemple −5 V pour un JFET dont VGS(off) vaut −3 V) : le canal est pincé, le JFET est bloqué. La LED s'éteint.

Attention au sens : un JFET canal N **conduit au repos** et il faut une tension négative pour le bloquer. C'est l'inverse d'un NPN, bloqué tant qu'on ne lui envoie pas de courant de base.

![ID en fonction de VGS : le JFET conduit à VGS = 0 et se bloque en dessous de VGS(off) = −3 V](/static/content/electro/m4/jfet-blocage.svg)

## Une marge pour bloquer

VGS(off) varie d'un exemplaire à l'autre : la fiche technique indique une plage, par exemple de −0,5 V à −6 V. Pour garantir le blocage, la tension de grille doit être plus négative que la pire valeur de la plage.

## Quand préférer le JFET ?

- Quand le circuit de commande ne peut fournir **aucun courant** : la grille ne consomme presque rien.
- Pour **commuter des signaux** faibles, par exemple aiguiller un signal audio, car le canal se comporte comme une simple résistance quand il conduit.

Pour des charges de forte puissance, on lui préfère aujourd'hui le transistor MOSFET, que vous découvrirez dans une partie ultérieure.

## À retenir

- JFET canal N : conduit à VGS = 0, bloqué sous VGS(off).
- Il faut une tension de grille négative pour le bloquer.
- Commande sans courant : idéal pour commuter de petits signaux.
