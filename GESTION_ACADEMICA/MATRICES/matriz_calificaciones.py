from random import randint
aleatorio = lambda: randint(1, 10)
encabezado_calificaciones = [
    ["Legajos", "Algebra", "Programación", "Análisis", "Sistemas", "Desarrollo web"]
]

def llenar_matriz(lista):
    for i in range(10):
        lista.append([1000+i, aleatorio(), aleatorio(), aleatorio(), aleatorio(), aleatorio()])
    return lista
