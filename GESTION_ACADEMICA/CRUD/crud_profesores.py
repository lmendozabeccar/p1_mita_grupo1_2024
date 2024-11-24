from VALIDACIONES.validaciones import validar_num, validacion_dig, validar_nota
from OPERACIONES.promedios import mostrar_notas
from BASE_DE_DATOS.funciones_json import devolverjson, guardarjson
    
def menu_actualizar_notas(): 
    """
    pre: no recibe ningun dato, se lo llama desde una opcion del profesor.
    pos: no retorna nada, actualiza las notas en otra funcion (en diccionario materias), y las guarda en otra
    funcion (guardarjson)
    """

    diccionario_notas = devolverjson()
    legajos = diccionario_notas.keys()
    legajos_formateados = ", ".join(str(legajo) for legajo in legajos) # Se junta las claves en una cadena separada por comas
    print(f"\nLegajos de alumnos inscriptos a alguna/s materia: {legajos_formateados}")
    flag = True
    menu_legajo = "\nIngrese el legajo del cual quiere agregar/actualizar notas: " 
    menu_agregar_notas = "\n1 Desea continuar agregando notas. \n2 No desea continuar agregando notas. \nPor favor, elegir una opción: "
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            legajo_actualizar = input(menu_legajo) #Ingresar el legajo
            while validar_num(legajo_actualizar) == False:
                legajo_actualizar = input(menu_legajo)
            if legajo_actualizar not in diccionario_notas: #Valida que el legajo exista en el diccionario de notas
                print("No se ha podido encontrar ese legajo, ingrese otro.")
            else:
                flag_2 = False #Si se pudo encontrar el legajo.
        
        diccionario_notas_act = actualizar_notas(diccionario_notas, legajo_actualizar) #Encontro el legajo, y va a actualizar las materias
        guardarjson(diccionario_notas_act) #Guarda las notas actualizadas en el archivo JSON
        
        lin = (input(menu_agregar_notas)) #Menu2, si desea continuar actualizando alumnos
        while validacion_dig(lin,2) == False: #Valida que variable lin sea = a 1 o 2
            lin = (input(menu_agregar_notas)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
            
        if int (lin) == 2: #No quiere seguir actualizando alumnos.
            flag = False
            #En caso de ingresar 1, sigue actualizando alumnos.
    return True

def actualizar_notas(matriz_legajos_notas, legajo):
    """
    pre: recibe la matriz de notas y el legajo el cual que quiere actualizar.
    pos: retorna la matriz de notas, pero actualizadas por el profesor.
    """
    flag = True
    cursa_sublista = matriz_legajos_notas[legajo]["cursa"]
    dic_materias_inscriptas = {}
    contador = 1
    materias_formateadas = ""
    print()
    for materia in cursa_sublista: #Preparo qué materias mostrar segun a qué materias está inscripto el alumno
        materias_formateadas += f"{contador}. {materia}\n"
        dic_materias_inscriptas[contador] = materia #Creo un nuevo diccionario según que cursa el alumno
        contador += 1 
        
    menu_nota = materias_formateadas + "Por favor, elegir un número de acuerdo a su materia: "
    menu_agregar_nota = "¿Desea agregar la nota de otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: "
    menu_calificacion = "Ingresar nota de la respectiva materia: "
    while flag == True:
        materia = input(menu_nota)
        while validacion_dig(materia, 10)== False: #Valida que sea un numero del 1 al 10
            materia = input(menu_nota)

        materia_nombre = dic_materias_inscriptas.get(int(materia)) #Busca el valor asociado a la clave materia, en el diccionario (y devuelve el respectivo valor)
        if materia_nombre in cursa_sublista:
                calificacion = input(menu_calificacion)
                while validar_nota(calificacion) == False:
                    calificacion = input(menu_calificacion)
                
                posicion = cursa_sublista.index(materia_nombre) # .index() me devuelve en qué posicion está el elemento en la lista
                matriz_legajos_notas[legajo]["notas"][posicion] = int(calificacion)
                print(f"\nLa materia {materia_nombre} fue agregada con una calificación de {calificacion}.\n") #Aviso al usuario.
                # Preguntar si el usuario desea agregar otra materia
                continuar = input(menu_agregar_nota)
                while validacion_dig(continuar, 2)== False: #Valida que ingrese 1 o 2.
                    continuar = input(menu_agregar_nota)
                if int(continuar) == 2:
                    flag = False                  #Ingresa 2, sale del apartado y vuelve atras.
        else:
            print("El alumno no cursa esa materia")
    return matriz_legajos_notas


def eliminar_alumno():
    """
    pre: no recibe ningun dato, se lo llama desde el apartado de profesores.
    pos: no retorna nada, se encarga de eliminar al alumno elegido por el profesor."""

    matriz_legajos_notas = devolverjson()
    legajos = matriz_legajos_notas.keys()
    legajos_formateados = ", ".join(str(legajo) for legajo in legajos) # Se junta las claves en una cadena separada por comas
    print(f"\nLegajos existentes: {legajos_formateados}")
    flag = True
    menu_legajo_eliminar = "\nIngrese el legajo que quiere eliminar: " #Ingresar el legajo
    menu_continuar = "\n1 Desea continuar eliminando alumnos. \n2 No desea continuar eliminando alumnos \nPor favor, elegir una opción: "
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            legajo_eliminar = input(menu_legajo_eliminar) #Mismo menu que arriba
            while validar_num(legajo_eliminar) == False:
                legajo_eliminar = input(menu_legajo_eliminar)
            try:
                matriz_legajos_notas.pop(legajo_eliminar)
            except KeyError: #En caso de que el legajo no exista en la matriz de alumnos
                print(f"\nError: El legajo {legajo_eliminar} no existe en la base de datos.")
            else:
                guardarjson(matriz_legajos_notas)
                print("\nBase de datos de alumnos actualizada")
                flag_2 = False
        lin = (input(menu_continuar)) 
        while validacion_dig(lin,2) == False: #Pregunta si quiere seguir eliminando.
            lin = (input(menu_continuar))
        if int (lin) == 2 or len(matriz_legajos_notas) == 0: # Si no quiere seguir o el diccionario se quedó sin legajos, sale de este apartado.
            flag = False
                            #En caso de ingresar 1, sigue eliminando.
    return True

def mostrar_calificacion_grupal ():
    """
    pre: no recibe ningun dato, se lo llama desde el apartado de profesores.
    pos: muestra las calificaciones de los alumnos inscriptos en sus respectivas materias.
    """       
    # Imprimir la lista con formato de f-strings
    matriz_legajos_notas = devolverjson()
    for legajo, info in matriz_legajos_notas.items(): #Se obtienen dos elementos por separado, la llave "legajo" y una lista de tuplas con dos elementos: "cursa" y "notas"
        print(f"\nEl legajo: {legajo}")
        for cursa, nota in zip(info["cursa"], info["notas"]): #Zip JUNTA la materia cursada con su RESPECTIVA nota (junta las dos sublistas)
            if nota == -1:
                print(f"El alumno cursa la materia {cursa}, pero aún no tiene una nota cargada.")
            else:
                print(f"El alumno cursa la materia {cursa} y obtuvo una nota de: {nota}")
    print("\nVolviendo al menú principal...")
    return True
        
def mostrar_calificacion_individual ():
    """
    pre: no recibe ningun dato, se lo llama desde el apartado de profesores.
    pos: muestra las notas de un alumno en particular, elegido por el profesor por legajo (esto lo hace a traves
    de la funcion mostrar_notas)
    """
    flag = False
    matriz_legajos_notas = devolverjson()
    legajos = matriz_legajos_notas.keys()
    legajos_formateados = ", ".join(str(legajo) for legajo in legajos) # Se junta las claves en una cadena separada por comas
    print(f"\nLegajos de alumnos inscriptos a alguna/s materia: {legajos_formateados}")
    menu_legajo = "\nIngresar el legajo del alumno el cual quiere ver la calificación: "
    legajo= input(menu_legajo) #Menú de arriba, modularizado.
    while validar_num(legajo) == False:
        legajo = input(menu_legajo)
    if legajo in matriz_legajos_notas:
        flag = True
    while flag == False:
        print("\nNo se pudo encontrar el legajo ingresado, por favor, volver a intentarlo.")
        legajo= input(menu_legajo)
        while validar_num(legajo) == False:
            legajo = input(menu_legajo)
        if legajo in matriz_legajos_notas:
            flag = True #No existe el legajo antes ingresado, pide otro y vuelve a validar.

    mostrar_notas(matriz_legajos_notas,legajo,"profesor")
    return True