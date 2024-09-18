matriz_notas = [
    [1000,[-1,-1,-1,-1,-1]],
    [1001,[-1,-1,-1,-1,-1]],
    [1002,[-1,-1,-1,-1,-1]],
    [1003,[-1,-1,-1,-1,-1]],
    [1004,[-1,-1,-1,-1,-1]],
    [1005,[-1,-1,-1,-1,-1]],
    [1006,[-1,-1,-1,-1,-1]],
    [1007,[-1,-1,-1,-1,-1]],
    [1008,[-1,-1,-1,-1,-1]],
    [1009,[-1,-1,-1,-1,-1]]    
]

#Primer columna, lista de legajos.
#Segunda columna, lista de lista 
    #La cual tiene 5 posiciones, todo vale -1.
    #Cada materia tiene su posicion, de acuerdo al diccionario.
    
def mostrar_notas (lista,posicion):
    suma,cont = 0,0
    # Asignación para poder mostrar las listas con encabezados.
    username = "Legajo"
    algebra = "Álgebra"
    sistemas = "Sistemas"
    desarrollo = "Desarrollo"
    ingles = "Inglés"
    programacion = "Programación"

    # Elige la sublista en la posición deseada, por ejemplo, la segunda fila (índice 1)
    sublista = lista[posicion]

    # Convertir el -1 en un guion para cada valor de la fila
    notas_formateadas = ["-" if valor == -1 or valor== -2 else valor for valor in sublista[1]]
    for i in range (len (notas_formateadas)): 
        if notas_formateadas[i] != "-":
            suma += notas_formateadas[i]
            cont += 1
    if suma == 0 or cont == 0:
        print()
        print("No hay notas cargadas en este legajo.")
    else:
        # Imprimir la lista con formato de f-strings
        print()
        print("Listado de notas:")
        print(f"|{username:^10}||{algebra:^10}||{sistemas:^10}||{desarrollo:^15}||{ingles:^10}||{programacion:^15}|")  # Mostrar encabezados, con restricciones.

        promedio = suma / cont
        # Imprimir la fila con los valores formateados
        print(f"|{sublista[0]:^10}||{notas_formateadas[0]:^10}||{notas_formateadas[1]:^10}||{notas_formateadas[2]:^15}||{notas_formateadas[3]:^10}||{notas_formateadas[4]:^15}|")
        print()
        print(f"El usuario cursó {cont} materias y obtuvo un promedio de {promedio:.2f}") #Hasta 2 dígitos    