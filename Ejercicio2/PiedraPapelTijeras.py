"""
CREA EL JUEGO, DEBE INFORMARSE DE RESULTADO Y SI ES EMPATE REPETIR
"""
import random
import time

posibilidades = ("Piedra", "Papel", "Tijeras")

ganador = False
while not ganador:
    entrada = input("Elija piedra, papel o tijeras: ")
    eleccion = entrada.lower()

    while eleccion != "piedra" and eleccion != "papel" and eleccion != "tijeras":
        eleccion = input("Elija una opción válida (piedra, papel, tijeras): ")

    elecPC = random.choice(posibilidades)

    print("El rival ha jugado", end="")
    for _ in range(3):
        time.sleep(0.5)  # Pausa de 1 segundo
        print(".", end="", flush=True)  # Añade un punto sin saltar de línea

    print("\n" + elecPC)  # Esto añade una nueva línea al final del mensaje

    if eleccion == "piedra":
        if elecPC == "Piedra":
            print("Empate")
        if elecPC == "Papel":
            print("Has perdido!")
            ganador = True
        if elecPC == "Tijeras":
            print("Has ganado")
            ganador = True

    if eleccion == "papel":
        if elecPC == "Papel":
            print("Empate")
        if elecPC == "Tijeras":
            print("Has perdido!")
            ganador = True
        if elecPC == "Piedra":
            print("Has ganado")
            ganador = True

    if eleccion == "tijeras":
        if elecPC == "Tijeras":
            print("Empate")
        if elecPC == "Piedra":
            print("Has perdido!")
            ganador = True
        if elecPC == "Papel":
            print("Has ganado")
            ganador = True
