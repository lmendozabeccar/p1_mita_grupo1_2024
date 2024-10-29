import json
from Base_de_datos.funciones_json import devolverjson, guardarjson
# Se aplica recursividad en las funciones de suma() y contar() para luego aplicarlo como tupla en la funcion mostrar_notas()
def suma(notas): 
    if len(notas) == 0:
        return 0
    else:
        return notas[0] + suma(notas[1:])
    
def contar(nota):
    if len(nota) == 0:
        return 0
    else:
        return 1 + contar(nota[1:])

def mostrar_notas (matriz_legajos_notas,legajo):
    sumas, contador = 0, 0     
    print(matriz_legajos_notas)
    #Si la suma de la lista (en la columna 2 y en su respectiva fila) son 
    #todos -1, quiere decir que no tiene ninguna nota cargada
    matriz_legajos_notas = devolverjson()
    if legajo not in matriz_legajos_notas:
        print("Para ver sus calificaciones, primero debe anotarse a una")
        return 0
    else:
        sublista_cursa = matriz_legajos_notas[legajo]["cursa"]
        sublista_notas = matriz_legajos_notas[legajo]["notas"]
        # Convertir el -1 en un guion para cada valor de la fila
        notas_formateadas = ["-" if valor == -1 else valor for valor in sublista_notas]
        for i in range(len(notas_formateadas)): 
            if notas_formateadas[i] != "-":
                sumas = suma(notas_formateadas)
                contador = contar(notas_formateadas) 
        if  sumas == 0 and contador == 0:
            print("\nNo hay notas cargadas en este legajo.")
        else:
            # Imprimir la lista con formato de f-strings
            print(f"Legajo: {legajo}")
            for cursa, nota in zip(sublista_cursa, sublista_notas): #Junta las dos sublistas de las materias cursadas con su respectiva nota en una nueva matriz
                nota = "-" if nota == -1 else nota
                print(f"Cursa {cursa}, Nota: {nota}")
                if nota != "-":
                    if nota>=0 and nota<=3:
                        print(f"Cursa {cursa}, Nota: {nota} (recursa)")
            print(f"Promedio: {sumas/contador:.2f}") #Maximo dos decimales
    return 1


