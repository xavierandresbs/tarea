Piedra, Papel o Tijera - Juego en Python

Este proyecto implementa el clásico juego de "Piedra, Papel o Tijera" utilizando el lenguaje de programación Python. El objetivo del juego es competir contra la computadora, seleccionando una de las tres opciones: piedra, papel o tijera, para determinar el ganador de cada ronda.

Objetivo del Programa

El objetivo principal del programa es permitir al usuario jugar múltiples rondas del juego "Piedra, Papel o Tijera" contra la computadora. El programa almacena los resultados de cada ronda, mostrando estadísticas de las victorias, derrotas y empates, además de un resumen final al terminar el juego.

Principales Funcionalidades

1. Elección del Jugador y la Computadora
   - El usuario elige entre "piedra", "papel" o "tijera".
   - La computadora elige aleatoriamente una opción utilizando el módulo `random`.

2. Determinación del Ganador
   - Se compara la elección del jugador con la de la computadora utilizando estructuras condicionales (`if`, `elif`, `else`).
   - El resultado puede ser una victoria, derrota o empate.

3. Almacenamiento de Resultados
   - Los resultados de cada ronda (la elección del jugador, la elección de la computadora, y el resultado) se almacenan en una lista como tuplas.
   - Un diccionario se utiliza para llevar el conteo de las victorias, derrotas y empates.

4. Estadísticas del Juego
   - Después de cada ronda, el programa muestra las estadísticas actuales, incluyendo el número de victorias, derrotas y empates.

5. Control de Flujo y Repetición
   - El juego se repite en un bucle `while` hasta que el usuario decida dejar de jugar.
   - El usuario puede optar por jugar otra ronda o terminar el juego en cualquier momento.

6. Resumen Final
   - Al final del juego, se muestra un resumen de todas las rondas jugadas, detallando las elecciones y resultados de cada una.

Cómo Ejecutar el Programa

1. Requisitos Previos: Asegúrate de tener Python instalado en tu sistema.
2. Ejecución:
   - Guarda el código en un archivo con la extensión `.py`.
   - Abre una terminal y navega hasta el directorio donde guardaste el archivo.
   - Ejecuta el archivo con el siguiente comando:
     ```bash
     python piedra_papel_tijera.py
     ```

Tecnologías Utilizadas

- Python 3.x
- Módulo random: Utilizado para la selección aleatoria de la opción de la computadora.
