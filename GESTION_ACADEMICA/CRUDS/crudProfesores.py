from VALIDACIONES.Validaciones import seguir_texto, validar_legajo, validar_num
from MATRICES.matriz_calificaciones import matriz_notas, mostrar_notas
from MATRICES.Diccionario_Materias import agregar_materias

posicion = lambda legajo, lista: [i for i in range(len(lista)) if lista[i][0] == legajo] #Saco en que posicion de la lista está el respecivo legajo

def matriz_a_usar(matriz_notas_register):
    if matriz_notas_register == []:
        return matriz_notas
    else:
        return matriz_notas_register
        
def actualizar_notas_alumno(matriz_notas_register): #Matriz notas proveniente del registro
    matriz_notas_usar = matriz_a_usar(matriz_notas_register)
    print()
    flag = True
    menu = "Ingrese el legajo que quiere actualizar: " #Ingresar el legajo
    menu2 = "\n1 Desea continuar actualizando alumnos. \n2 No desea continuar actualizando alumnos \nPor favor, elegir una opción: "
    while flag == True:
        print()
        flag_2 = True
        while flag_2 == True:
            legajo_actualizar = input(menu) #Mismo menu que arriba
            while validar_num(legajo_actualizar) == False:
                legajo_actualizar = input(menu)
            indice = posicion(int(legajo_actualizar), matriz_notas_usar) #Valida que el legajo exista en la matriz de notas
            if indice == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.") #No se pudo encontrar el legajo
            else:
                flag_2 = False #Si se pudo encontrar.
        print()
        
        agregar_materias(matriz_notas_usar, indice[0]) #Encontro el legajo, y va a agregar materias.
        
        lin = (input(menu2)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
        while seguir_texto(lin) == False: #Valida que variable lin sea = a 1 o 2
            lin = (input(menu2)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
            
        if int (lin) == 2: #No quiere seguir actualizando alumnos.
            flag = False
            #En caso de ingresar 1, sigue actualizando alumnos.
    return matriz_notas_usar

def eliminar_alumno(matriz_notas_register):
    matriz_notas_usar = matriz_a_usar(matriz_notas_register)
    print()
    flag = True
    menu = "Ingrese el legajo que quiere eliminar: " #Ingresar el legajo
    menu2 = "\n1 Desea continuar eliminando alumnos. \n2 No desea continuar eliminando alumnos \nPor favor, elegir una opción: "
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            legajo_eliminar = input(menu) #Legajo que se quiere eliminar
            while validar_num(legajo_eliminar) == False:
                legajo_eliminar = input(menu)
            indice = posicion(int(legajo_eliminar), matriz_notas_usar) #Saco en qué posicion esta el legajo en la lista
            if indice == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.") #No se pudo encontrar el legajo
            else:
                flag_2 = False #Si se pudo encontrar.

        matriz_notas_usar.pop(indice[0]) #"indice" es una lista, entonces me fijo en la posición 0 para sacar el índice como entero, y luego borrar esa posicion
        print()
        lin = (input(menu2)) #Mismo menú, pero modularizado.
        while seguir_texto(lin) == False: #Pregunta si quiere seguir eliminando.
            lin = (input(menu2))
        print()
        if int (lin) == 2: #No quiere seguir, sale de este apartado.
            flag = False
                            #En caso de ingresar 1, sigue eliminando.
    return matriz_notas_usar

def mostrar_calificacion_grupal (matriz_notas_register):
    matriz_notas_usar = matriz_a_usar(matriz_notas_register)
    print()        
    # Asignación para poder mostrar las listas con encabezados.
    username = "Legajo"
    algebra = "Álgebra"
    sistemas = "Sistemas"
    desarrollo = "Desarrollo"
    ingles = "Inglés"
    programacion = "Programación"

    # Imprimir la lista con formato de f-strings
    print("Lista de las notas de alumnos ya registrados en el sistema.")
    print(f"|{username:^10}||{algebra:^10}||{sistemas:^10}||{desarrollo:^15}||{ingles:^10}||{programacion:^15}|")  # Mostrar encabezados, con restricciones.

    for username in matriz_notas_usar:
        # Convertir el -1 en un guion para cada valor de la fila
        notas_formateadas = [ "-" if valor == -1 else valor for valor in username[1]]
        # Imprimir la fila con los valores formateados
        print(f"|{username[0]:^10}||{notas_formateadas[0]:^10}||{notas_formateadas[1]:^10}||{notas_formateadas[2]:^15}||{notas_formateadas[3]:^10}||{notas_formateadas[4]:^15}|")       

        
def mostrar_calificacion_individual (matriz_notas_register):
    matriz_notas_usar = matriz_a_usar(matriz_notas_register)
    menu = "Ingresar el legajo del alumno del cual quiere ver la calificación: " #Legajo individual.
    legajo= input(menu) #Menú de arriba, modularizado.
    while validar_num(legajo) == False:
        legajo = input(menu)
    pos = validar_legajo (matriz_notas_usar,int(legajo)) #Valida que el legajo exista.
    while pos == -1:
        print("No se pudo encontrar el legajo ingresado, por favor, volver a intentarlo.")
        legajo= input(menu)
        while validar_num(legajo) == False:
            legajo = input(menu)
        pos = validar_legajo (matriz_notas_usar,int(legajo)) #No existe el legajo antes ingresado, pide otro y vuelve a validar.
    print()
    mostrar_notas (matriz_notas_usar,pos)

