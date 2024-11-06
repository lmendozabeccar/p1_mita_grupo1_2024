import json
from Base_de_datos.funciones_json import devolverjson

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
    
def contar(notas):
    """
    pre: recibe la nota que tuvo el alumno.
    pos: se encarga de contar cada nota, para despues hacer el promedio.
    """
    if len(notas) == 0:
        return 0
    else:
        return 1 + contar(notas[1:])

def mostrar_notas (matriz_legajos_notas,legajo):
    """
    pre: recibe la matriz de notas, con el respectivo legajo a mostrar.
    pos: muestra todas las notas agregadas del alumno, con su respectiva materia y su promedio final.
    """
    recursa = True
    sumas, contador = 0, 0     
    matriz_legajos_notas = devolverjson()
    if legajo not in matriz_legajos_notas:
        print("\nPara ver sus calificaciones, primero debe anotarse a una")
        return 0
    else:
        sublista_cursa = matriz_legajos_notas[legajo]["cursa"]
        sublista_notas = matriz_legajos_notas[legajo]["notas"]
        # Convertir el -1 en un guion para cada valor de la fila
        notas_formateadas = ["-" if valor == -1 else valor for valor in sublista_notas]
        notas_sin_guion = [num for num in notas_formateadas if str(num).isnumeric() == True]
        sumas = suma(notas_sin_guion)
        contador = contar(notas_sin_guion) 
        if  sumas == 0 and contador == 0:
            print("\nNo hay notas cargadas en este legajo.")
        else:
            # Imprimir la lista con formato de f-strings
            print(f"\nLegajo: {legajo}")
            for cursa, nota in zip(sublista_cursa, sublista_notas): #Junta las dos sublistas de las materias cursadas con su respectiva nota en una nueva matriz
                nota = "-" if nota == -1 else nota
                print(f"Cursa {cursa}, Nota: {nota}")
                if nota != "-":
                    if nota>=0 and nota<=3:
                        recursa = False
                        print(f"\nCursa {cursa}, Nota: {nota} (RECURSA)")
            print(f"\nPromedio: {sumas/contador:.2f}") #Maximo dos decimales

