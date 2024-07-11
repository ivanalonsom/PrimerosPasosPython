"""
CREA UN 3 EN RAYA MOSTRANDO TABLERO. PC DEBERÁ SER EL RIVAL
"""

import random
import time


def conversor_letra_num(col):
    return {'a': 1, 'b': 2, 'c': 3}[col]


def obtener_columna():
    colUsu = input("Elija una columna para colocar su ficha (a,b,c) : ")
    while colUsu not in ('a', 'b', 'c'):
        colUsu = input("Por favor, elija únicamente a, b o c: ")
    return colUsu


def obtener_fila():
    filaUsu = input("Elija una fila para colocar su ficha (1,2,3): ")
    while filaUsu not in ('1', '2', '3'):
        filaUsu = input("Por favor, elija únicamente 1, 2 o 3: ")
    return int(filaUsu)


def obtener_posicion_valida(tablero):
    while True:
        colUsu = obtener_columna()
        numCol = conversor_letra_num(colUsu)

        filaUsu = obtener_fila()

        if tablero[filaUsu][numCol] == " ":
            return filaUsu, numCol
        else:
            print("Posición ocupada. Introduzca otros valores:")


def imprimir_tablero(tablero):
    # Imprimir la primera fila sin separador
    print("  ".join(tablero[0]))  # Imprime la primera fila sin separadores


    # Imprimir las demás filas con separador
    for fila in tablero[1:]:
        print(fila[0], " | ".join(fila[1:]))  # Imprime la primera columna sin separadores
        print("   ", end="")
        print("-" * 7)


# Crear el tablero inicial
tablero = [[" " for x in range(4)] for x in range(4)]
# Lo del paréntesis interno me genera un salto de linea 4 veces: [' ',' ',' ', ' ']
# y lo del paréntesis externo lo cuadriplica: [[' ', ' ', ' '], [' ', ' ', ' '],[' ', ' ', ' '], [' ', ' ', ' ']]
tablero[0][1] = 'a'
tablero[0][2] = 'b'
tablero[0][3] = 'c'
tablero[1][0] = '1'
tablero[2][0] = '2'
tablero[3][0] = '3'

ganador = False
movimientos = 3

# Bucle principal del juego
while not ganador and movimientos > 0:
    imprimir_tablero(tablero)
    filaUsu, numCol = obtener_posicion_valida(tablero)

    # Suponemos que el jugador usa 'X' y la computadora usa 'O'
    tablero[filaUsu][numCol] = 'X'

    # Simula el movimiento del oponente si hay movimientos restantes
    print("Le toca a tu oponente", end="")
    for x in range(3):
        print('.', end="")
        time.sleep(0.3)

    while True:
        filaPC = random.randint(1, 3)
        colPC = random.randint(1, 3)
        if tablero[filaPC][colPC] == " ":
            tablero[filaPC][colPC] = 'O'
            break

    movimientos -= 1

print("Fin del juego")
imprimir_tablero(tablero)
