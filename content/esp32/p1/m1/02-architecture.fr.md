La carte que vous utilisez porte un **module ESP32-WROOM-32** : une petite plaque qui contient la puce ESP32, sa mémoire Flash, un quartz et une antenne imprimée. Le capot métallique protège des perturbations radio.

![Architecture du module ESP32-WROOM-32 : processeur double cœur, mémoires, périphériques, radio et gestion d'énergie](/static/content/esp32/m1/architecture.svg)

## Le processeur

L'ESP32 possède **deux cœurs** Xtensa LX6 qui tournent jusqu'à **240 MHz**. Avec l'environnement Arduino, votre programme s'exécute sur un cœur ; l'autre gère surtout le Wi-Fi et le Bluetooth. Un petit coprocesseur à très basse consommation (ULP) peut veiller pendant que les cœurs dorment.

## Trois mémoires, trois rôles

![Les trois mémoires : la Flash garde le programme sans courant, la SRAM porte les variables et s'efface à la coupure, la ROM contient le démarrage](/static/content/esp32/m1/memoires.svg)

- **Flash (4 Mo)** : elle garde votre programme même sans courant, comme une clé USB. Le téléversement écrit dedans.
- **SRAM (520 Ko)** : elle contient les variables pendant l'exécution. Elle s'efface à chaque coupure.
- **ROM (448 Ko)** : elle contient le programme de démarrage, gravé en usine. On ne peut pas la modifier.

## Les périphériques

Autour du processeur, des **périphériques** font une partie du travail à sa place :

| Périphérique | Ce qu'il fait | Module |
|---|---|---|
| GPIO | entrées et sorties numériques (0 ou 3,3 V) | M2, M3 |
| ADC | mesure une tension (18 voies, 12 bits) | M6 |
| LEDC (MLI) | règle une luminosité ou une vitesse (16 voies) | M6 |
| Touch | détecte un doigt (10 broches capacitives) | M6 |
| DAC | produit une tension (2 voies, 8 bits) | M6 |
| UART, I2C, SPI | dialoguent avec un ordinateur, un écran, un capteur | M5, M7 |
| Wi-Fi, Bluetooth | communiquent sans fil | M9 |

La **gestion d'énergie** permet enfin de mettre la puce en veille profonde, où elle ne consomme qu'une dizaine de microampères (module M8).

## À retenir

- Deux cœurs à 240 MHz, une Flash de 4 Mo pour le programme, 520 Ko de SRAM pour les variables.
- Les périphériques (GPIO, ADC, MLI, Touch, UART, I2C, SPI, Wi-Fi) sont étudiés un à un dans la formation.
