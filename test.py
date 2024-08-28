import random

def crear(n, m):
    return [[0] * m for _ in range(n)]

def llenar(m):
    filas = len(m)
    columnas = len(m[0])
    for fil in range(filas):
        for col in range(columnas):
            num_aleatorio = random.randint(1, 10)
            m[fil][col] = num_aleatorio

def imprimir(matriz, nombres_columnas, nombres_filas):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Imprimir encabezado de columnas
    print(" " * 12, end="")  # Espacio reservado para el encabezado de las filas
    for nombre_col in nombres_columnas:
        print("{:>10}".format(nombre_col), end=" ")
    print()
    
    # Imprimir filas con nombres
    for fil in range(filas):
        print("{:>12}".format(nombres_filas[fil]), end=" ")  # Alinear los nombres de las filas a la derecha
        for col in range(columnas):
            print("{:>10}".format(matriz[fil][col]), end=" ")
        print()

# Definir nombres correctamente
nombres_columnas = ["Juan", "Manolo", "Roberto", "Octuso"]
nombres_filas = ["juan@gmail.com", "manolo@gmail.com", "roberto@gmail.com", "octuso@gmail.com"]

# Crear y llenar la matriz
matriz = crear(4, 4)
llenar(matriz)

# Imprimir la matriz con encabezados
imprimir(matriz, nombres_columnas, nombres_filas)