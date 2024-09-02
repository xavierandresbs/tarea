import random

# Estructura de Datos: Tuplas, Listas y Diccionarios
opciones = ("piedra", "papel", "tijera")  # Tupla: Las opciones del juego no cambian.
resultados = []  # Lista: Para almacenar los resultados de cada ronda.
estadisticas = {  # Diccionario: Para llevar la cuenta de las victorias, derrotas y empates.
    "ganaste": 0,
    "perdiste": 0,
    "empate": 0
}

# Función que determina el ganador.
def determinar_ganador(opcion_jugador, opcion_computadora):
    if opcion_jugador == opcion_computadora:
        estadisticas["empate"] += 1
        return "Es un empate."
    elif (opcion_jugador == "piedra" and opcion_computadora == "tijera") or \
         (opcion_jugador == "papel" and opcion_computadora == "piedra") or \
         (opcion_jugador == "tijera" and opcion_computadora == "papel"):
        estadisticas["ganaste"] += 1
        return "¡Ganaste!"
    else:
        estadisticas["perdiste"] += 1
        return "Perdiste."

# Función para mostrar las estadísticas del juego.
def mostrar_estadisticas():
    print("\n--- Estadísticas del juego ---")
    print(f"Victorias: {estadisticas['ganaste']}")
    print(f"Derrotas: {estadisticas['perdiste']}")
    print(f"Empates: {estadisticas['empate']}")
    print("------------------------------\n")

# Función principal del juego.
def jugar():
    jugando = True
    
    while jugando:
        opcion_jugador = input("Elige piedra, papel o tijera: ").lower()
        
        if opcion_jugador not in opciones:
            print("Opción inválida, intenta nuevamente.")
            continue
        
        opcion_computadora = random.choice(opciones)
        resultado = determinar_ganador(opcion_jugador, opcion_computadora)
        resultados.append((opcion_jugador, opcion_computadora, resultado))  # Almacenando el resultado como una tupla.
        
        print(f"Tu opción: {opcion_jugador}")
        print(f"Opción de la computadora: {opcion_computadora}")
        print(f"Resultado: {resultado}")
        
        mostrar_estadisticas()
        
        seguir_jugando = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if seguir_jugando != "s":
            jugando = False
    
    # Mostrar todos los resultados al final.
    print("\n--- Resultados Finales ---")
    for ronda, (jugador, computadora, resultado) in enumerate(resultados, start=1):
        print(f"Ronda {ronda}: Tú elegiste {jugador}, la computadora eligió {computadora}. Resultado: {resultado}")
    print("--------------------------\n")

# Ejecución de la Función principal para iniciar el juego.
jugar()
