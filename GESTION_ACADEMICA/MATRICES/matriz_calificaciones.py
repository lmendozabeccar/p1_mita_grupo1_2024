import json
from Base_de_datos.funciones_json import devolverjson
from VALIDACIONES.Validaciones import validacion_dig
# Se aplica recursividad en las funciones de suma() y contar() para luego aplicarlo como tupla en la funcion mostrar_notas()
def suma(notas): 
    """
    pre: recibe la nota que tuvo el alumno 
    pos: se encarga de sumar las notas del alumno.
    """
    if len(notas) == 0:
        return 0
    else:
        return notas[0] + suma(notas[1:])
    
def contar(nota):
    """
    pre: recibe la nota que tuvo el alumno.
    pos: se encarga de contar cada nota, para despues hacer el promedio.
    """
    if len(nota) == 0:
        return 0
    else:
        return 1 + contar(nota[1:])

def mostrar_notas (matriz_legajos_notas,legajo,tipo_usuario):
    """
    pre: recibe la matriz de notas, con el respectivo legajo a mostrar.
    pos: muestra todas las notas agregadas del alumno, con su respectiva materia y su promedio final.
    """
    print()
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
                print(f"Cursa la materia {cursa}, y obtuviste una nota de: {nota}")
            print(f"El promedio del alumno fue de: {sumas/contador:.2f}") #Maximo dos decimales
            if tipo_usuario == "alumno":
                i=0
                while len(sublista_cursa)>i:
                    if sublista_notas[i]<=3:
                        print()
                        print(f"Lamentablemente, debes recursar la materia",sublista_cursa[i])
                        menu_recursa = "\n1 Desea cursar nuevamente la materia.\n2 Desea abandonar la materia. \nPor favor, elegir una opción: "
                        recursa = input(menu_recursa)
                        while validacion_dig (recursa, 2)==False: #Valida que sea un numero del 1 al 10
                            recursa = input(menu_recursa)
                        indice = matriz_legajos_notas[legajo]['cursa'].index(sublista_cursa[i])
                        if recursa == "1":
                            print("Buena suerte para el próximo cuatrimestre.")
                            matriz_legajos_notas[legajo]["notas"][indice] = -1

                        elif recursa == "2":                            
                            matriz_legajos_notas[legajo]['cursa'].pop(indice)
                            matriz_legajos_notas[legajo]['notas'].pop(indice)
                            print("Abandonaste la materia.")
                            
                            i -= 1                      
                        else:
                                print("No existe")
                    i += 1
    return matriz_legajos_notas