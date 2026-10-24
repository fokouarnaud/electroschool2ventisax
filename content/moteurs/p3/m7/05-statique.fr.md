Le **contacteur statique** fait le même travail qu'un contacteur, mais sans pièce mobile : des **thyristors** (ou des triacs) remplacent les contacts.

![Contacteur statique : deux thyristors tête-bêche par phase, commandés par un signal 24 V isolé, montés sur un dissipateur](/static/content/moteurs/m7/statique.svg)

Par phase, deux thyristors montés **tête-bêche** laissent passer chacun une alternance. Un petit signal de commande (souvent 24 V), isolé par un optocoupleur, les fait conduire. Le fonctionnement des thyristors est détaillé au module 10.

## Avantages et limites

- **Aucune usure mécanique** : des millions de manœuvres, à cadence très élevée (fours, résistances commandées en permanence).
- **Silencieux** et sans arc ; commutation possible au passage par zéro (module 8).
- Mais les semi-conducteurs ont une **chute de tension** d'environ 1,5 V en conduction : ils **chauffent**.

![Échauffement : environ 1,5 W par ampère et par phase, soit 45 W à 10 A et 112,5 W à 25 A en triphasé](/static/content/moteurs/m7/dissipation.svg)

**Exemple.** À 10 A sur trois phases : P ≈ 1,5 × 10 × 3 = **45 W**, qu'il faut évacuer par un **dissipateur** bien ventilé. Un contacteur électromécanique de même calibre ne dissipe que quelques watts.

- En cas de défaut, un semi-conducteur claque souvent **en court-circuit** : le contacteur statique ne sépare pas, il faut toujours un appareil de sectionnement en amont.

## À retenir

- Thyristors tête-bêche à la place des contacts : aucune usure.
- Environ 1,5 W par ampère et par phase : dissipateur obligatoire.
- Ne sépare jamais : sectionneur en amont.
