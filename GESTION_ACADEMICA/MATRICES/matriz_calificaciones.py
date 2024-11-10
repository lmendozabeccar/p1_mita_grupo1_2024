import json
from Base_de_datos.funciones_json import devolverjson, guardarjson
from VALIDACIONES.Validaciones import validacion_dig
from VALIDACIONES.test_main import aprobado_desaprobado

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

def mostrar_notas (matriz_legajos_notas,legajo,tipo_usuario):
    """
    pre: recibe la matriz de notas, con el respectivo legajo a mostrar.
    pos: muestra todas las notas agregadas del alumno, con su respectiva materia y su promedio final.
    """

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
            print(f"\nLegajo número: {legajo}")
            for cursa, nota in zip(sublista_cursa, sublista_notas): #Junta las dos sublistas de las materias cursadas con su respectiva nota en una nueva matriz
                nota = "-" if nota == -1 else nota
                print(f"Cursa la materia {cursa} y obtuviste una nota de: {nota}")
            print(f"El promedio del alumno fue de: {sumas/contador:.2f}") #Maximo dos decimales
            
            if tipo_usuario == "alumno":
                materias = int 
                materias = 0
                while len(sublista_cursa)>materias:
                    try:
                        assert (aprobado_desaprobado(sublista_notas[materias])) == True, "En caso que el alumno deba recursar" #El string es el mensaje de error si el assert falla
                    except AssertionError:  
                        print(f"Lamentablemente, debes recursar la materia",sublista_cursa[materias])
                        menu_recursa = "\n1 Desea cursar nuevamente la materia.\n2 Desea abandonar la materia. \nPor favor, elegir una opción: "
                        
                        recursa = input(menu_recursa)
                        while validacion_dig (recursa, 2)==False: #Valida que sea un numero del 1 al 10
                            recursa = input(menu_recursa)
                            
                        indice = matriz_legajos_notas[legajo]['cursa'].index(sublista_cursa[materias]) #Devuelve en que posición esta el elemento en la lista
                        if recursa == "1":
                            print("\nBuena suerte para el próximo cuatrimestre.")
                            matriz_legajos_notas[legajo]["notas"][indice] = -1 #Se le asigna -1 como nota no cargada
                            guardarjson(matriz_legajos_notas)
                            
                        elif recursa == "2":                            
                            matriz_legajos_notas[legajo]['cursa'].pop(indice)
                            matriz_legajos_notas[legajo]['notas'].pop(indice) #Se elimina la materia con su respectiva nota
                            guardarjson(matriz_legajos_notas)
                            print("\nAbandonaste la materia.")
                            materias -= 1                      
                    finally:
                        materias = int(materias) + 1
                        
    print("\nVolviendo al menú principal...")          
    return matriz_legajos_notas

