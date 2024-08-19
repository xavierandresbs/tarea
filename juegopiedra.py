
opcion_jugador = "piedra"
opcion_computadora = "tijera"

if opcion_jugador == "piedra" and opcion_computadora == "tijera":
    resultado = "¡Ganaste!"
elif opcion_jugador == "papel" and opcion_computadora == "piedra":
    resultado = "¡Ganaste!"
elif opcion_jugador == "tijera" and opcion_computadora == "papel":
    resultado = "¡Ganaste!"
elif opcion_jugador == opcion_computadora:
    resultado = "Es un empate."
else:
    resultado = "Perdiste."

print("Tu opción:", opcion_jugador)
print("Opción de la computadora:", opcion_computadora)
print("Resultado:", resultado)
