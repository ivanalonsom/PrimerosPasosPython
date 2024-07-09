import random


def tableroIni(palabra):
    tablero = ['_' for _ in palabra]    # for _ in palabra ese _ da igual lo que ponga
    return tablero


def actualizarTablero(palabra, tablero, letra):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            tablero[i] = letra
    return tablero


vidas = 8
victoria = False
palabras = ("sopa", "ratero", "carta", "piedra", "lomo", "cartera")

palabraElegida = random.choice(palabras)
tableroActual = tableroIni(palabraElegida)
print(" ".join(tableroActual))  # Mostrar tablero inicial

while vidas > 0 and not victoria:
    letra = input("Escriba una letra: ").lower()

    while not letra.isalpha() or len(letra) != 1:
        letra = input("Escriba una sola letra del abecedario: ").lower()

    if letra in palabraElegida:
        print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        tableroActual = actualizarTablero(palabraElegida, tableroActual, letra)
        print(" ".join(tableroActual))  # Mostrar tablero actualizado
    else:
        vidas -= 1
        print(f"La letra '{letra}' no está en la palabra. Vidas restantes: {vidas}")
        print(" ".join(tableroActual))  # Mostrar tablero actualizado

    if "_" not in tableroActual:
        victoria = True

# Salir del bucle principal: el jugador ha ganado o perdido
if victoria:
    print(f"¡Felicidades! Has ganado. La palabra era '{palabraElegida}'.")
else:
    print(f"¡Lo siento! Has perdido. La palabra era '{palabraElegida}'.")
