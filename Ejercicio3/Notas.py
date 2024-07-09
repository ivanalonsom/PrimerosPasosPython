"""
PROGRAMA LEE SECUENCIA DE NOTAS INTRODUCIDAS POR TECLADO (PUEDE TENER DECIMALES). SI VALOR<0 PROGRAMA FINALIZA.
INFORMAR DE NºAPROBADOS, SUSPENSOS Y NOTA MEDIA
"""

listaNotas = []
calif = 0
numAprobados = 0
numTotal = 0
sumaNotas = 0

while calif >= 0:
    calif = float(input("Introduzca una nueva calificación: ") )
    if calif>=0:
        listaNotas.append(calif)
        numTotal += 1
        sumaNotas += calif

    if calif>=5:
        numAprobados += 1


print("El número de aprobados ha sido:", numAprobados, "\nEl de suspensos:", (numTotal-numAprobados),
      "\nLa nota media de la clase ha sido de ", (sumaNotas/numTotal))
