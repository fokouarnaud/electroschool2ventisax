Un filtre ne change pas seulement l'amplitude du signal : il le **décale dans le temps**. Ce décalage, exprimé en degrés, s'appelle le **déphasage** φ (phi). Une période complète vaut 360°.

![Entrée ve et sortie vs d'un passe-bas à fc : la sortie atteint son maximum Δt = 0,125 ms après l'entrée, pour T = 1 ms](/static/content/electro/m6/dephasage.svg)

## Mesurer un déphasage à l'oscilloscope

On affiche l'entrée sur la voie 1 et la sortie sur la voie 2, puis on mesure le décalage Δt entre deux points homologues (deux maximums, ou deux passages par zéro en montant) :

**φ = 360° × Δt / T**

Exemple : Δt = 0,125 ms et T = 1 ms. φ = 360 × 0,125 / 1 = **45°**. Avec Δt = 0,1 ms et T = 1 ms, φ = 36°.

## Calculer un déphasage

Dans un circuit RC série, le triangle des impédances donne directement l'angle entre le courant et la tension d'entrée :

**tan φ = Xc / R**   donc   **φ = arctan(Xc / R)**

![Triangle avec R = 1 kΩ et Xc = 577 Ω : tan φ = 0,577 et φ ≈ 30°](/static/content/electro/m6/triangle-phi.svg)

Exemples :

- R = Xc (c'est-à-dire à fc) : φ = arctan 1 = **45°** ;
- R = 1 kΩ et Xc = 577 Ω : φ = arctan 0,577 ≈ **30°** ;
- R = 2 kΩ et Xc = 1 kΩ : φ = arctan 0,5 ≈ **26,6°**.

Dans un RC série, le courant est **en avance** sur la tension d'entrée (le condensateur tire le courant en avant). La sortie d'un passe-bas, prise sur C, est en retard sur l'entrée ; celle d'un passe-haut, prise sur R, est en avance.

## À retenir

- φ = 360° × Δt / T à l'oscilloscope.
- φ = arctan(Xc / R) dans un RC série.
- À la fréquence de coupure, le déphasage vaut 45°.
