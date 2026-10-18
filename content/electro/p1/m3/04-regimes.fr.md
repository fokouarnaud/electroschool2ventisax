Selon le courant de base qu'on lui fournit, un transistor fonctionne dans l'un de trois **régimes**.

![Réseau de courbes IC en fonction de VCE pour trois courants de base, avec les zones de saturation, de régime linéaire et de blocage](/static/content/electro/m3/regimes.svg)

## Le blocage

Si IB = 0 (base non alimentée ou VBE inférieure à 0,6 V environ), le transistor ne conduit pas : **IC ≈ 0**. Il se comporte comme un interrupteur ouvert, et VCE ≈ VCC.

## Le régime linéaire

Pour un courant de base modéré, IC = β × IB, presque indépendamment de VCE : les courbes sont quasi horizontales. C'est le régime de l'**amplification** : une petite variation de IB produit une grande variation de IC.

## La saturation

Si l'on augmente encore IB, le circuit de collecteur ne peut plus fournir β × IB : la résistance de collecteur « prend » presque toute la tension. VCE tombe à environ **0,2 V** et IC est fixé par le reste du circuit : IC sat ≈ VCC / RC. Le transistor se comporte comme un interrupteur fermé.

## La droite de charge

Le circuit de collecteur impose une relation simple, VCE = VCC − RC × IC, qui se trace comme une droite sur le réseau de courbes. Son intersection avec la courbe du courant de base choisi donne le **point de fonctionnement** Q.

![Droite de charge de VCC = 12 V et RC = 1 kΩ, et point de repos Q à 6 V et 6 mA](/static/content/electro/m3/droite-charge.svg)

Avec VCC = 12 V et RC = 1 kΩ, la droite va de 12 mA (VCE = 0) à 12 V (IC = 0). Un point Q au milieu, vers 6 V, laisse le plus de marge pour amplifier.

## À retenir

- Blocage : IB = 0, IC = 0, interrupteur ouvert.
- Linéaire : IC = β × IB, amplification.
- Saturation : VCE ≈ 0,2 V, IC ≈ VCC / RC, interrupteur fermé.
