from VALIDACIONES.Validaciones import seguir_texto, validar_num
from MATRICES.matriz_calificaciones import mostrar_notas
from MATRICES.Diccionario_Materias import actualizar_notas

posicion = lambda legajo, lista: [i for i in range(len(lista)) if lista[i][0] == legajo] #Saco en que posicion de la lista está el respecivo legajo

def actualizar_notas_alumno(matriz_legajos_notas): #Matriz notas proveniente del registro
    print()
    legajos = matriz_legajos_notas.keys()
    legajos_formateados = ", ".join(str(legajo) for legajo in legajos) # Se junta las claves en una cadena separada por comas
    print(f"Legajos inscriptos: {legajos_formateados}")
    flag = True
    menu_legajo = "Ingrese el legajo del cual quiere agregar/actualizar notas: " #Ingresar el legajo
    menu_agregar_notas = "\n1 Desea continuar agregando notas. \n2 No desea continuar agregando notas. \nPor favor, elegir una opción: "
    while flag == True:
        print()
        flag_2 = True
        while flag_2 == True:
            legajo_actualizar = input(menu_legajo) #Mismo menu que arriba
            while validar_num(legajo_actualizar) == False:
                legajo_actualizar = input(menu_legajo)
            if int(legajo_actualizar) not in matriz_legajos_notas: #Valida que el legajo exista en la matriz de notas
                print("No se ha podido encontrar ese legajo, ingrese otro.") #No se pudo encontrar el legajo
            else:
                flag_2 = False #Si se pudo encontrar.
        print()
        
        matriz_legajos_notas_act = actualizar_notas(matriz_legajos_notas, legajo_actualizar) #Encontro el legajo, y va a actualizar las materias
        matriz_legajos_notas = matriz_legajos_notas_act
        
        lin = (input(menu_agregar_notas)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
        while seguir_texto(lin) == False: #Valida que variable lin sea = a 1 o 2
            lin = (input(menu_agregar_notas)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
            
        if int (lin) == 2: #No quiere seguir actualizando alumnos.
            flag = False
            #En caso de ingresar 1, sigue actualizando alumnos.
    return matriz_legajos_notas

def eliminar_alumno(matriz_alumnos, matriz_legajos_notas):
    print()
    legajos_formateados = ", ".join(str(subfila[0]) for subfila in matriz_alumnos) # Se junta las claves en una cadena separada por comas
    print(f"Legajos existentes: {legajos_formateados}")
    flag = True
    menu_legajo_eliminar = "Ingrese el legajo que quiere eliminar: " #Ingresar el legajo
    menu_continuar = "\n1 Desea continuar eliminando alumnos. \n2 No desea continuar eliminando alumnos \nPor favor, elegir una opción: "
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            if len(matriz_alumnos) == 0: #Si no hay alumnos en la matriz, no se puede eliminar
                print("No hay alumnos en la base de datos.")
                flag_2 = False
            legajo_eliminar = input(menu_legajo_eliminar) #Mismo menu que arriba
            while validar_num(legajo_eliminar) == False:
                legajo_eliminar = input(menu_legajo_eliminar)
            try: #Manejo de excepciones por si la clave no existe en el diccionario
                indice = posicion(int(legajo_eliminar), matriz_alumnos) #Saco la posición del legajo en la lista de alumnos dentro de una lista
                matriz_alumnos.pop(indice[0]) #como "indice" es una lista, entonces me fijo en la posición 0 para sacar el índice como entero, y luego borrar esa posicion
                if int(legajo_eliminar) in matriz_legajos_notas:
                    matriz_legajos_notas.pop(int(legajo_eliminar))
            except KeyError: #En caso de que el legajo no exista en la matriz de alumnos
                print(f"Error: El legajo {legajo_eliminar} no existe en la base de datos.")
            except IndexError: 
                print(f"Error: El legajo {legajo_eliminar} no existe en la base de datos.")
            else:
                print("Base de datos de alumnos actualizada")
                flag_2 = False
        print()
        lin = (input(menu_continuar)) #Mismo menú, pero modularizado.
        while seguir_texto(lin) == False: #Pregunta si quiere seguir eliminando.
            lin = (input(menu_continuar))
        print()
        if int (lin) == 2: #No quiere seguir, sale de este apartado.
            flag = False
                            #En caso de ingresar 1, sigue eliminando.
    return matriz_alumnos, matriz_legajos_notas

def mostrar_calificacion_grupal (matriz_legajos_notas):
    print()        
    # Imprimir la lista con formato de f-strings
    for legajo, info in matriz_legajos_notas.items(): #Se obtienen dos elementos por separado, la llave "legajo" y una lista de tuplas con dos elementos: "cursa" y "notas"
        print("-"*26)
        print(f"Legajo: {legajo}")
        for cursa, nota in zip(info["cursa"], info["notas"]): #Zip JUNTA la materia cursada con su RESPECTIVA nota (junta las dos sublistas)
            nota = "-" if nota == -1 else nota
            print(f"Cursa {cursa}, Nota: {nota}")
        
def mostrar_calificacion_individual (matriz_legajos_notas):
    print()
    flag = 0
    legajos = matriz_legajos_notas.keys()
    legajos_formateados = ", ".join(str(legajo) for legajo in legajos) # Se junta las claves en una cadena separada por comas
    print(f"Legajos inscriptos: {legajos_formateados}")
    menu_legajo = "Ingresar el legajo del alumno del cual quiere ver la calificación: " #Legajo individual.
    legajo= input(menu_legajo) #Menú de arriba, modularizado.
    while validar_num(legajo) == False:
        legajo = input(menu_legajo)
    if int(legajo) in matriz_legajos_notas:
        flag = 1
    while flag == 0:
        print("No se pudo encontrar el legajo ingresado, por favor, volver a intentarlo.")
        legajo= input(menu_legajo)
        while validar_num(legajo) == False:
            legajo = input(menu_legajo)
        if int(legajo) in matriz_legajos_notas:
            flag = 1 #No existe el legajo antes ingresado, pide otro y vuelve a validar.
    print()
    mostrar_notas(matriz_legajos_notas, legajo)