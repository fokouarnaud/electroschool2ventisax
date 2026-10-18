Faisons varier la fréquence du générateur en gardant la même tension, et mesurons le courant du circuit RLC série. On obtient sa **courbe de réponse**.

![Courant dans le RLC série sous 1 V : faible aux basses et aux hautes fréquences, il culmine à 20 mA à f0 ≈ 5 kHz](/static/content/electro/m7/courbe-i.svg)

## Une courbe en cloche

- **Loin en dessous de f0**, XC est grande : le courant est faible.
- **À f0**, XL et XC s'annulent : le courant atteint son maximum Imax = U / R.
- **Loin au-dessus de f0**, XL est grande : le courant redevient faible.

En pratique, on observe souvent la tension aux bornes de R plutôt que le courant : comme Ur = R × I, elle a exactement la même forme, et l'oscilloscope la mesure directement.

## L'effet de la résistance

Seule R limite le courant à la résonance. Que se passe-t-il si on l'augmente ?

![Deux courbes : avec R = 50 Ω, le pic monte à 20 mA et reste étroit ; avec R = 200 Ω, il ne dépasse pas 5 mA et s'étale](/static/content/electro/m7/courbe-r.svg)

- Le pic **s'abaisse** : Imax = U / R diminue (5 mA au lieu de 20 mA sous 1 V).
- Le pic **s'élargit** : le circuit répond à une plage de fréquences plus large.
- La fréquence de résonance **ne change pas** : f0 ne dépend que de L et de C.

Toute perte compte comme une résistance : la résistance du fil de la bobine, celle de la source, celle de la charge.

## À retenir

- La courbe de réponse d'un RLC série est en cloche, centrée sur f0.
- Augmenter R abaisse et élargit le pic sans déplacer f0.
