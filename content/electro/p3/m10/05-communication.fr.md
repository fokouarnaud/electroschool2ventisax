En électronique de communication, le transformateur fait bien plus qu'abaisser une tension. Trois usages reviennent sans cesse.

## L'accord

Un condensateur placé sur un enroulement forme avec lui un circuit résonant : le transformateur ne transmet bien que les fréquences proches de sa résonance. Les récepteurs radio utilisent ainsi des **transformateurs FI** (fréquence intermédiaire), souvent accordés sur **455 kHz**, logés dans de petits boîtiers métalliques avec un noyau réglable.

![Transformateur accordé : un condensateur sur le primaire, un autre sur le secondaire, accord sur 455 kHz](/static/content/electro/m10/fi.svg)

Le calcul est celui de la Partie 2 : C = 1 / (4π² × f² × L). Avec un enroulement de 680 µH, il faut C = 1 / (4π² × 455 000² × 0,000 68) ≈ **180 pF** pour s'accorder sur 455 kHz.

Ces transformateurs accordés relient les étages d'un récepteur : ils transmettent la station voulue, rejettent ses voisines et adaptent les impédances d'un étage à l'autre.

## L'isolement galvanique

Le secondaire n'a **aucune liaison électrique** avec le primaire : seul le flux magnétique les relie. On parle d'**isolement galvanique**.

![Isolement galvanique : primaire relié au 230 V, secondaire relié à la masse du montage, sans aucune liaison électrique entre eux](/static/content/electro/m10/isolement.svg)

- **Sécurité** : le montage alimenté par le secondaire n'est pas relié au secteur. C'est le principe des alimentations de jouets, des sonnettes et des transformateurs de séparation des ateliers de dépannage.
- **Boucles de masse** : un transformateur placé sur une ligne audio ou téléphonique coupe le chemin des courants parasites entre deux appareils, et supprime le ronflement à 50 Hz.

## Le point milieu

Un secondaire muni d'une **prise au milieu** fournit deux tensions égales et opposées, par exemple 2 × 12 V. Reliée à la masse, cette prise permet de construire une alimentation symétrique ±12 V pour des AOP, ou un redresseur double alternance à deux diodes (voir le module suivant).

## À retenir

- Un condensateur sur un enroulement accorde le transformateur (FI de 455 kHz).
- Isolement galvanique : aucune liaison électrique entre primaire et secondaire.
- Le point milieu donne deux tensions symétriques.
