Une LED peut être reliée à une broche de deux façons. Les deux fonctionnent ; elles n'allument pas la LED avec le même niveau.

## Logique directe : la broche est une source

La LED et sa résistance vont de la broche à la masse. Au niveau haut, la broche fournit le courant : **`HIGH` allume**.

![Logique directe (source) : la LED va de la broche à la masse ; HIGH l'allume, le courant sort de la broche](/static/content/esp32/m2/source.svg)

## Logique inversée : la broche est un puits

La LED et sa résistance vont du 3,3 V à la broche. Au niveau bas, la broche absorbe le courant : **`LOW` allume** ; au niveau haut, les deux bornes sont à 3,3 V et aucun courant ne passe.

![Logique inversée (puits) : la LED va du 3,3 V à la broche ; LOW l'allume, le courant entre dans la broche](/static/content/esp32/m2/puits.svg)

## Écrire un programme lisible

En logique inversée, `digitalWrite(LED_PIN, LOW)` pour allumer surprend le lecteur. On nomme donc les deux états une fois pour toutes :

```cpp
// En logique inversée, LOW allume et HIGH éteint
const uint8_t LED_ON = LOW;
const uint8_t LED_OFF = HIGH;
```

Le reste du programme écrit `digitalWrite(LED_PIN, LED_ON)` : si le câblage change, on ne modifie que ces deux lignes.

## Quand choisir le puits ?

- Beaucoup de modules du commerce (relais, LED intégrées de certaines cartes) sont câblés en logique inversée : leur entrée s'active au niveau bas.
- Au démarrage, une broche reste un court instant en entrée, sans tension imposée : une LED en puits reste alors éteinte.

## À retenir

- Source : LED vers la masse, `HIGH` allume.
- Puits : LED vers le 3,3 V, `LOW` allume.
- Nommez `LED_ON` et `LED_OFF` pour que le programme se lise sans schéma.
