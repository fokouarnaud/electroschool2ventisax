Plaçons en série une résistance R et un condensateur de réactance Xc. Le courant est le même partout dans la boucle. Mais la tension aux bornes de R est en phase avec ce courant, alors que celle du condensateur est décalée de 90°. Les deux tensions n'atteignent donc pas leur maximum en même temps.

![Circuit RC série sous 10 V avec R = Xc = 1 kΩ : Ur ≈ 7,07 V, Uc ≈ 7,07 V et I ≈ 7,07 mA](/static/content/electro/m6/rc-serie.svg)

## L'impédance

L'opposition totale du circuit au courant alternatif s'appelle l'**impédance** Z, en ohms. Comme R et Xc agissent à 90° l'une de l'autre, elles se combinent comme les côtés d'un triangle rectangle :

**Z = √(R² + Xc²)**   puis   **Ieff = Ueff / Z**

![Triangle des impédances : R horizontale, Xc verticale, Z sur l'hypoténuse, φ = 45° quand R = Xc](/static/content/electro/m6/triangle-z.svg)

Exemple : R = 1 kΩ et Xc = 1 kΩ, sous 10 V efficaces.

- Z = √(1 000² + 1 000²) ≈ **1 414 Ω**, et non 2 000 Ω.
- I = 10 / 1 414 ≈ **7,07 mA**.
- Ur = R × I ≈ 7,07 V et Uc = Xc × I ≈ 7,07 V.

## Les tensions ne s'additionnent pas simplement

7,07 V + 7,07 V font 14,14 V, plus que les 10 V de la source ! Ce n'est pas une erreur : les deux tensions sont décalées dans le temps. Les valeurs efficaces se combinent elles aussi par Pythagore :

**Ue = √(Ur² + Uc²)**   : √(7,07² + 7,07²) ≈ 10 V.

Au multimètre, vous mesurerez donc Ur + Uc supérieur à Ue : c'est normal dans un circuit RC.

## À retenir

- Z = √(R² + Xc²) ; I = U / Z.
- En RC série, Ue = √(Ur² + Uc²) et non Ur + Uc.
