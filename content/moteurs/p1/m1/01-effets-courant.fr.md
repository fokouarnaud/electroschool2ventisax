Le corps humain conduit le courant. Ce qui blesse, ce n'est pas la tension elle-même mais le **courant qui traverse le corps**, sa durée et son chemin. La tension, elle, décide de ce courant à travers la résistance du corps.

## Des seuils très bas

En alternatif 50 Hz, quelques milliampères suffisent à produire des effets graves. Les valeurs ci-dessous sont des ordres de grandeur pour un adulte et un contact de quelques secondes : elles varient d'une personne à l'autre.

![Seuils indicatifs : perception vers 0,5 mA, non-lâcher vers 10 mA, arrêt respiratoire vers 30 mA, fibrillation vers 75 mA](/static/content/moteurs/m1/seuils.svg)

- **0,5 mA** : on sent un picotement.
- **10 mA** : les muscles de la main se contractent, on ne peut plus lâcher le conducteur.
- **30 mA** : la respiration peut s'arrêter. C'est la valeur retenue pour les dispositifs différentiels qui protègent les personnes.
- **75 mA et plus** : risque de fibrillation du cœur, mortelle sans secours rapide.

La durée compte autant que l'intensité : plus le contact dure, plus le seuil dangereux baisse. Le chemin aussi : un courant qui traverse le thorax (main à main, main à pieds) est le plus dangereux.

## Calculer le courant traversant le corps

On applique la loi d'Ohm au corps : I = U / R. La résistance du corps entre une main et les pieds vaut de l'ordre de 1 000 Ω pour une peau humide, davantage pour une peau sèche, beaucoup moins en cas de plaie.

![Contact direct avec une phase à 230 V : le courant traverse la main, le corps et les pieds, puis revient par le sol](/static/content/moteurs/m1/corps.svg)

**Exemple.** Une personne touche une phase à 230 V, pieds nus sur un sol humide (R ≈ 1 000 Ω). I = 230 / 1 000 = 0,23 A, soit **230 mA** : bien au-delà du seuil de fibrillation. À 24 V, dans les mêmes conditions, I = 24 / 1 000 = 24 mA : encore désagréable, mais en dessous du seuil d'arrêt respiratoire, et en pratique la peau sèche réduit ce courant à quelques milliampères. C'est pourquoi tous les montages de cette formation se câblent en **très basse tension, 24 V au plus**.

## À retenir

- C'est le courant qui tue : 30 mA peuvent arrêter la respiration.
- I = U / R avec R ≈ 1 000 Ω pour un corps humide.
- Durée et chemin aggravent le danger ; travailler hors tension reste la première protection.
