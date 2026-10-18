Concevoir un oscillateur LC simple tient en quatre étapes. Le dépanner demande surtout de la méthode.

![Quatre étapes : choisir f, choisir L et calculer C, vérifier le gain de boucle et la phase, mesurer et ajuster](/static/content/electro/m9/procedure.svg)

## Concevoir

1. **Choisir la fréquence** f voulue.
2. **Choisir L** parmi les valeurs disponibles, puis **calculer C** : C = 1 / (4π² × f² × L).
3. **Vérifier la boucle** : l'amplificateur doit avoir assez de gain pour compenser le réseau (A × B ≥ 1), et la phase doit revenir à 0°.
4. **Mesurer et ajuster** : les composants ont des tolérances (souvent 5 à 10 %), on retouche C ou L.

Exemple : on veut 100 kHz avec une bobine de 100 µH. C = 1 / (4π² × 100 000² × 0,000 1) ≈ **25,3 nF**. Pour un Colpitts, c'est Céq : avec C1 = C2, chacun vaut le double, environ 51 nF. Avec deux condensateurs normalisés de 47 nF, Céq = 23,5 nF et f ≈ 104 kHz, assez proche.

[[calc:resonance]]

## Mesurer la fréquence

À l'oscilloscope, on lit la période sur l'écran puis f = 1 / T. Un fréquencemètre (ou la fonction Hz de certains multimètres) donne directement la valeur.

![Écran d'oscilloscope : une période occupe 4 divisions à 0,25 ms par division, soit T = 1 ms et f = 1 kHz](/static/content/electro/m9/ecran.svg)

## Dépanner : la liste de contrôle

Quand un oscillateur ne démarre pas, on vérifie dans l'ordre :

1. **L'alimentation** : la tension est-elle présente sur le montage ?
2. **La polarisation** : sans oscillation, le transistor est-il bien en régime linéaire (VCE vers la moitié de VCC) ?
3. **La phase** : le réseau est-il bien câblé ? Pour un Armstrong, la bobine de réaction est-elle dans le bon sens ?
4. **Le gain** : est-il suffisant ? Une charge trop lourde branchée en sortie peut faire chuter A × B sous 1.
5. **La fréquence** : si l'oscillateur fonctionne mais à la mauvaise fréquence, on contrôle les valeurs de L et de C.

Une sonde d'oscilloscope ajoute elle aussi une petite capacité : brancher la mesure peut décaler la fréquence d'un oscillateur LC, voire l'arrêter. On mesure de préférence en sortie d'un étage tampon.

## À retenir

- C = 1 / (4π² × f² × L) ; ajuster après mesure.
- Dépannage : alimentation, polarisation, phase, gain, puis valeurs de L et C.
- La sonde de mesure peut perturber l'oscillateur.
