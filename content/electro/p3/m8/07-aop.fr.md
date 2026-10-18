L'**amplificateur opérationnel** (AOP) est un circuit intégré qui contient des dizaines de transistors déjà polarisés. On ne s'occupe plus de points de repos : deux résistances suffisent pour fixer un gain précis.

## Un gain énorme, que l'on maîtrise

L'AOP a deux entrées, **−** (inverseuse) et **+** (non inverseuse), et une sortie. Il amplifie la différence entre ses entrées avec un gain énorme, de l'ordre de 100 000. Utilisé tel quel, il sature au moindre écart.

On ramène donc une partie de la sortie sur l'entrée − : c'est la **contre-réaction**. L'AOP ajuste alors sa sortie pour que ses deux entrées restent presque à la même tension, et le gain ne dépend plus que des résistances.

## Le montage inverseur

Le signal arrive sur l'entrée − par Rin ; Rf relie la sortie à l'entrée − ; l'entrée + est à la masse.

**Av = −Rf / Rin**

![AOP inverseur : Rin de 10 kΩ en entrée, Rf de 47 kΩ de la sortie vers l'entrée moins, entrée plus à la masse](/static/content/electro/m8/aop-inverseur.svg)

Avec Rin = 10 kΩ et Rf = 47 kΩ : Av = −47 / 10 = **−4,7**. Une entrée de 0,5 V donne −2,35 V.

## Le montage non inverseur

Le signal arrive sur l'entrée + ; Rf va de la sortie à l'entrée −, et Rin de l'entrée − à la masse.

**Av = 1 + Rf / Rin**

![AOP non inverseur : le signal sur l'entrée plus, Rf de 47 kΩ de la sortie vers l'entrée moins, Rin de 10 kΩ de l'entrée moins vers la masse](/static/content/electro/m8/aop-non-inverseur.svg)

Avec les mêmes résistances : Av = 1 + 4,7 = **5,7**, sans inversion. Si Rf = 0 (fil direct) et sans Rin, Av = 1 : c'est le **suiveur** à AOP, un tampon parfait.

[[calc:gain]]

## La limite : l'alimentation

La sortie ne peut pas dépasser les tensions d'alimentation. Alimenté en ±12 V, un AOP courant sort au plus environ ±10,5 V. Avec un gain de −4,7, une entrée de 3 V demanderait −14,1 V : la sortie **sature** vers −10,5 V et le signal est écrêté.

## À retenir

- Inverseur : Av = −Rf / Rin. Non inverseur : Av = 1 + Rf / Rin.
- La contre-réaction rend le gain précis : il ne dépend que des résistances.
- La sortie reste limitée par l'alimentation.
