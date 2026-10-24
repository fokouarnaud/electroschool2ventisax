Un équipement de moteur se décrit avec **deux schémas développés** séparés, dessinés verticalement : l'énergie et les ordres circulent de haut en bas.

## Le schéma de puissance

![Schéma de puissance : L1 L2 L3, sectionneur Q1, contacteur KM1, relais thermique F1, moteur M1](/static/content/moteurs/m2/puissance.svg)

De haut en bas : le réseau triphasé L1 L2 L3, le **sectionneur Q1** qui sépare l'équipement pour la consignation, les pôles du **contacteur KM1** qui établissent et coupent le courant du moteur, le **relais thermique F1** qui surveille la surcharge, et le **moteur M1**. Le pointillé horizontal relie les trois pôles d'un même appareil : ils bougent ensemble.

## Le schéma de commande

![Schéma de commande : fusible F2, contact 95-96 de F1, bouton arrêt S1, bouton marche S2 doublé par le contact 13-14 de KM1, bobine KM1](/static/content/moteurs/m2/commande.svg)

Il est alimenté en très basse tension (ici 24 V). On le lit comme un chemin : le courant ne parvient à la bobine KM1 que si **tous** les contacts en série sont fermés.

1. Au repos, S2 (marche) est ouvert : la bobine n'est pas alimentée, le moteur est arrêté.
2. On appuie sur **S2** : la bobine KM1 est alimentée, le contacteur se ferme, le moteur démarre.
3. Le contact **13-14 de KM1**, en parallèle sur S2, se ferme en même temps : quand on relâche S2, la bobine reste alimentée par ce contact. C'est l'**auto-maintien**.
4. On appuie sur **S1** (arrêt, à ouverture) : le chemin est coupé, KM1 retombe, son contact 13-14 s'ouvre, le moteur s'arrête et ne redémarre pas seul.
5. En cas de surcharge, le contact **95-96 de F1** s'ouvre et produit le même effet.

## À retenir

- Puissance et commande sont deux schémas distincts, lus de haut en bas.
- Un même appareil (KM1) apparaît dans les deux : pôles en puissance, bobine et contacts en commande.
- L'auto-maintien : un contact 13-14 du contacteur en parallèle sur le bouton marche.
