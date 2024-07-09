import random
import time

posibilidades = ("Piedra", "Papel", "Tijeras")
resultados = {
    "piedra": {"Piedra": "Empate", "Papel": "Has perdido!", "Tijeras": "Has ganado"},
    "papel": {"Piedra": "Has ganado", "Papel": "Empate", "Tijeras": "Has perdido!"},
    "tijeras": {"Piedra": "Has perdido!", "Papel": "Has ganado", "Tijeras": "Empate"}
}

ganador = False
while not ganador:
    entrada = input("Elija piedra, papel o tijeras: ")
    eleccion = entrada.lower()

    while eleccion not in ["piedra", "papel", "tijeras"]:
        eleccion = input("Elija una opción válida (piedra, papel, tijeras): ").lower()

    elecPC = random.choice(posibilidades)

    print("El rival ha jugado", end="")
    for _ in range(3):
        time.sleep(0.5)  # Pausa de 1 segundo
        print(".", end="", flush=True)  # Añade un punto sin saltar de línea

    print("\n" + elecPC)  # Esto añade una nueva línea al final del mensaje

    resultado = resultados[eleccion][elecPC]
    print(resultado)

    if resultado != "Empate":
        ganador = True
