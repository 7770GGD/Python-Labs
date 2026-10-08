#Piedra, papel o tijera
print("Juguemos piedra, papel o tijera")

jugador_1 = input("Jugador 1, ingrese su elección (piedra, papel o tijera): ").lower()
jugador_2 = input("Jugador 2, ingrese su elección (piedra, papel o tijera): ").lower()

if jugador_1 == jugador_2:
    print("Es un empate")
elif (jugador_1 == "piedra" and jugador_2 == "tijera") or (jugador_1 == "papel" and jugador_2 == "piedra") or (jugador_1 == "tijera" and jugador_2 == "papel"):
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana")


repeat = input("¿Desea jugar otra vez? (si/no): ").lower()
while repeat == "si":
    jugador_1 = input("Jugador 1, ingrese su elección (piedra, papel o tijera): ").lower()
    jugador_2 = input("Jugador 2, ingrese su elección (piedra, papel o tijera): ").lower()

    if jugador_1 == jugador_2:
        print("Es un empate")
    elif (jugador_1 == "piedra" and jugador_2 == "tijera") or (jugador_1 == "papel" and jugador_2 == "piedra") or (jugador_1 == "tijera" and jugador_2 == "papel"):
        print("Jugador 1 gana")
    else:
        print("Jugador 2 gana")

    repeat = input("¿Desea jugar otra vez? (si/no): ").lower()
