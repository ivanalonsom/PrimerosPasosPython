"""
REALIZA UN PROGRAMA QUE PERMITA INTRODUCIR UNA PALABRA O FRASE Y DECIR SI ES O NO PALÍNDROMO
"""

entrada = input("Introduzca una palabra/frase: ")

entradaFormat = entrada.lower().replace(" ", "")

lista = []

for x in reversed(entradaFormat):
    lista.append(x)


entradaInvert = ''.join(lista)          # Este método me permite concatenar Strings


if entradaFormat == entradaInvert:
    print("Es un palíndromo")
else:
    print("No es palíndromo")
