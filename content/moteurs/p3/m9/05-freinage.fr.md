Un moteur coupé s'arrête en roue libre, parfois en plusieurs dizaines de secondes. Pour l'arrêter vite, ou pour **maintenir** la charge à l'arrêt, on le freine.

## Le freinage électrique

- **Par contre-courant** : on inverse deux phases pendant que le moteur tourne encore ; le champ tourne alors en sens contraire et freine très énergiquement. Un détecteur de vitesse nulle coupe l'alimentation juste à l'arrêt, sinon le moteur repartirait dans l'autre sens. Courant très élevé, contacteurs en AC-4.
- **Par injection de courant continu** : on coupe le moteur du réseau, puis on envoie du courant **continu** dans deux phases. Le stator crée alors un champ **fixe** ; le rotor qui tourne dedans est freiné, sans usure mécanique.

![Freinage par injection : moteur coupé, injection de courant continu, champ fixe, rotor freiné](/static/content/moteurs/m9/injection.svg)

Le freinage électrique arrête le moteur, mais **ne le maintient pas** à l'arrêt : une charge suspendue redescendrait.

## Le frein électromécanique

Pour maintenir une charge (levage, translation, machine qui ne doit pas tourner à l'arrêt), on monte sur l'arbre un **frein à manque de courant** : des **ressorts** serrent un disque ; une **bobine**, alimentée en même temps que le moteur, desserre le frein.

![Frein électromécanique à manque de courant : les ressorts serrent le disque, la bobine alimentée le desserre ; sans courant, le frein serre](/static/content/moteurs/m9/frein.svg)

Son principe est une règle de sécurité : **sans courant, le frein serre**. Une coupure de courant ou un fil coupé arrête et maintient la charge, au lieu de la laisser tomber. Ses garnitures s'usent : on contrôle régulièrement l'entrefer et le couple de freinage.

## À retenir

- Contre-courant : énergique, coupure à vitesse nulle obligatoire.
- Injection de CC : champ fixe, sans usure, sans maintien.
- Frein à manque de courant : sans courant, il serre.
