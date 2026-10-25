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

## Ce qui se passe dans le circuit

Le courant est le même dans R et dans C. Aux bornes de R, la tension suit le courant au même instant. Aux bornes de C, elle suit la charge accumulée : elle culmine un quart de période (90°) après le courant, au moment où celui-ci s'annule et cesse de charger le condensateur.

Le courant est en avance de φ = arctan(Xc / R) sur Ve. La sortie d'un passe-bas, prise sur C, est donc en retard de 90° − φ sur l'entrée. À fc / 10, Xc = 10 kΩ : φ ≈ 84,3° et la sortie ne retarde que de 5,7°, presque en phase. À fc, Xc = R : φ = 45° et le retard vaut aussi 45°, soit Δt = T / 8. À 10 × fc, φ ≈ 5,7° et le retard approche 90° (84,3°).

Sur le traceur ci-dessous, la voie 1 enregistre Ve et la voie 2 enregistre Vs. Mettez en pause et comptez les graduations sous l'accolade : chacune vaut 45°. Le relevé donne Δt / T, puis le retard 360° × Δt / T. Avec Xc = 577 Ω, le courant avance de 30° et la sortie retarde de 60°.

[[fig:rc_phase]]

## À retenir

- φ = 360° × Δt / T à l'oscilloscope.
- φ = arctan(Xc / R) dans un RC série.
- À la fréquence de coupure, le déphasage vaut 45°.
