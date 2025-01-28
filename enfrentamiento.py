import random

nombre1 = input("Por favor ingresa tu nombre jugador 1: ")
nombre2 = input("Por favor ingresa tu nombre jugador 2: ")

ac = input("Por favor para lanzar el dado presiona enter jugador 1: ")
if ac == "":
    lanzamientoJugador1 = random.randint(1, 6)
    print(f" {nombre1} sacaste {lanzamientoJugador1}")

ac = input("Por favor para lanzar el dado presiona enter jugador 2: ")
if ac == "":
    lanzamientoJugador2 = random.randint(1, 6)
    print(f" {nombre2} sacaste {lanzamientoJugador2}")

if lanzamientoJugador1 > lanzamientoJugador2:
    print(f"El ganador es {nombre1}")
elif lanzamientoJugador2 > lanzamientoJugador1:
    print(f"El ganador es {nombre2}")
elif lanzamientoJugador1 == lanzamientoJugador2:
    print(f" {nombre1} y {nombre2} empataron")