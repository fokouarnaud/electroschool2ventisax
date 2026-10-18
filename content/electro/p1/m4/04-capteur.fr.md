Le transistor peut aussi être commandé par un **capteur** plutôt que par un interrupteur. L'exemple le plus parlant est la **photorésistance** (LDR, *light dependent resistor*), dont la résistance varie avec la lumière.

![La résistance d'une LDR chute quand l'éclairement augmente : forte dans la pénombre, faible en pleine lumière](/static/content/electro/m4/ldr-courbe.svg)

## Une résistance qui dépend de la lumière

Dans l'obscurité, une LDR courante dépasse souvent 100 kΩ ; en pleine lumière, elle descend à quelques centaines d'ohms. On ne mesure pas directement cette variation : on l'insère dans un **diviseur de tension** (module 1), qui la transforme en tension.

## La lampe qui s'allume la nuit

On place une résistance fixe R1 en haut et la LDR en bas. Le point milieu attaque la base du transistor.

![R1 de 10 kΩ en haut, LDR en bas, point milieu relié à la base ; la lampe est dans le collecteur](/static/content/electro/m4/ldr.svg)

- **En plein jour**, la LDR est faible : la tension du point milieu reste sous 0,6 V. Le transistor est bloqué, la lampe éteinte.
- **La nuit**, la LDR devient grande : la tension du point milieu monte au-dessus de 0,7 V, un courant de base s'établit et le transistor sature. La lampe s'allume.

Exemple : R1 = 10 kΩ, VCC = 9 V. Le jour, LDR = 500 Ω : la tension du diviseur vaut 9 × 0,5 / 10,5 ≈ 0,43 V, sous le seuil. La nuit, LDR = 100 kΩ : sans charge, elle monterait à 8,2 V ; en réalité la jonction base-émetteur la bloque vers 0,7 V et le surplus devient du courant de base.

## Régler le seuil

Pour choisir à quelle luminosité la lampe s'allume, on remplace R1 par une **résistance ajustable** (potentiomètre) en série avec une petite résistance fixe qui protège la base. Inverser la LDR et R1 inverse le comportement : la lampe s'allume alors à la lumière.

## À retenir

- LDR : forte résistance dans le noir, faible à la lumière.
- Le diviseur de tension transforme la variation de résistance en variation de tension.
- La base se débloque au-delà d'environ 0,7 V ; un ajustable règle le seuil.
