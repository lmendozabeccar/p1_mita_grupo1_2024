from VALIDACIONES.Validaciones import seguir_texto, validar_legajo
from MATRICES.matriz_calificaciones import matriz_notas, mostrar_notas
from MATRICES.Diccionario_Materias import materias_dic, agregar_materias_profesor
posicion = lambda legajo, lista: [i for i in range(len(lista)) if lista[i][0] == legajo] #Saco en que posicion de la lista está
#el respecivo legajo

def actualizar_notas_alumno():
    flag = True
    while flag == True:
        print()
        menu = "Ingrese el legajo que quiere actualizar: " #Ingresar el legajo
        legajo_actualizar = (input(menu)) #Mismo menu que arriba
        pos = validar_legajo (matriz_notas,legajo_actualizar) #Valida que el legajo exista en la matriz de notas
        while pos == -1: #No se pudo encontrar el legajo.
            print("No se pudo encontrar el legajo ingresado, por favor, volver a intentarlo.") #Pide otro.
            legajo_actualizar = (input(menu)) 
            pos = validar_legajo (matriz_notas,legajo_actualizar) #Valida nuevamente
        print()
        agregar_materias_profesor (pos) #Encontro el legajo, y va a agregar materias.
        
        menu2 = "\n1 Desea continuar actualizando alumnos. \n2 No desea continuar actualizando alumnos \nPor favor, elegir una opción: "
        lin = (input(menu2)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
        while seguir_texto(lin) == False: #Valida que variable lin sea = a 1 o 2
            lin = (input(menu2)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
            
        if int (lin) == 2: #No quiere seguir actualizando alumnos.
            flag = False
            #En caso de ingresar 1, sigue actualizando alumnos.
    return matriz_notas

def eliminar_alumno():
    print()
    flag = True
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            legajo_actualizar = int(input("Ingrese el legajo que quiere eliminar: ")) #Legajo que se quiere eliminar
            indice = posicion(legajo_actualizar, matriz_notas) #Saco en qué posicion esta el legajo en la lista
            if indice == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.") #No se pudo encontrar el legajo
            else:
                flag_2 = False #Si se pudo encontrar.

        matriz_notas.pop(indice[0]) #"indice" es una lista, entonces me fijo en la posición 0 para sacar el índice como entero, y luego borrar esa posicion
        print()
        menu = "\n1 Desea continuar eliminando alumnos. \n2 No desea continuar eliminando alumnos \nPor favor, elegir una opción: "
        lin = (input(menu)) #Mismo menú, pero modularizado.
        while seguir_texto(lin) == False: #Pregunta si quiere seguir eliminando.
            lin = (input(menu))
        print()
        if int (lin) == 2: #No quiere seguir, sale de este apartado.
            flag = False
                            #En caso de ingresar 1, sigue eliminando.
    return matriz_notas

def mostrar_calificacion_grupal ():
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

    for username in matriz_notas:
        # Convertir el -1 en un guion para cada valor de la fila
        notas_formateadas = [ "-" if valor == -1 else valor for valor in username[1]]
        # Imprimir la fila con los valores formateados
        print(f"|{username[0]:^10}||{notas_formateadas[0]:^10}||{notas_formateadas[1]:^10}||{notas_formateadas[2]:^15}||{notas_formateadas[3]:^10}||{notas_formateadas[4]:^15}|")       

        
def mostrar_calificacion_individual ():
    menu = "Ingresar el legajo del alumno del cual quiere ver la calificación: " #Legajo individual.
    legajo= input(menu) #Menú de arriba, modularizado.
    pos = validar_legajo (matriz_notas,legajo) #Valida que el legajo exista.
    while pos == -1:
        print("No se pudo encontrar el legajo ingresado, por favor, volver a intentarlo.")
        legajo= input(menu)
        pos = validar_legajo (matriz_notas,legajo) #No existe el legajo antes ingresado, pide otro y vuelve a validar.
    print()
    mostrar_notas (matriz_notas,pos)

