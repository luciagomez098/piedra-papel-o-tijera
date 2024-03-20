import random

def juego_ppt(jugador1, jugador2):
    """
    Función que simula una partida de Piedra, Papel y Tijera.
    Retorna 0 si hay empate, 1 si gana jugador1, 2 si gana jugador2.
    """
    if jugador1 == jugador2:
        return 0
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        return 1
    else:
        return 2

opciones = ["piedra", "papel", "tijera"]

# Simular una partida
jugador1 = random.choice(opciones)
jugador2 = random.choice(opciones)

print("Jugador 1 elige:", jugador1)
print("Jugador 2 elige:", jugador2)

resultado = juego_ppt(jugador1, jugador2)

if resultado == 0:
    print("Empate!")
elif resultado == 1:
    print("¡Jugador 1 gana!")
else:
    print("¡Jugador 2 gana!")