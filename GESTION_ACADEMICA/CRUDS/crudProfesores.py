import json
from VALIDACIONES.Validaciones import seguir_texto, validar_num
from MATRICES.matriz_calificaciones import mostrar_notas
from MATRICES.Diccionario_Materias import actualizar_notas
from Base_de_datos.funciones_json import devolverjson, guardarjson
    
def actualizar_notas_alumno(): #Matriz notas proveniente del registro
    print()
    matriz_legajos_notas = devolverjson()
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
            if legajo_actualizar not in matriz_legajos_notas: #Valida que el legajo exista en la matriz de notas
                print("No se ha podido encontrar ese legajo, ingrese otro.") #No se pudo encontrar el legajo
            else:
                flag_2 = False #Si se pudo encontrar.
        print()
        
        matriz_legajos_notas_act = actualizar_notas(matriz_legajos_notas, legajo_actualizar) #Encontro el legajo, y va a actualizar las materias
        guardarjson(matriz_legajos_notas_act)
        
        lin = (input(menu_agregar_notas)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
        while seguir_texto(lin) == False: #Valida que variable lin sea = a 1 o 2
            lin = (input(menu_agregar_notas)) #Menu2, si desea continuar actualizando alumnos, pero modularizado.
            
        if int (lin) == 2: #No quiere seguir actualizando alumnos.
            flag = False
            #En caso de ingresar 1, sigue actualizando alumnos.
    return True

def eliminar_alumno():
    print()
    matriz_legajos_notas = devolverjson()
    legajos = matriz_legajos_notas.keys()
    legajos_formateados = ", ".join(str(legajo) for legajo in legajos) # Se junta las claves en una cadena separada por comas
    print(f"Legajos existentes: {legajos_formateados}")
    flag = True
    menu_legajo_eliminar = "Ingrese el legajo que quiere eliminar: " #Ingresar el legajo
    menu_continuar = "\n1 Desea continuar eliminando alumnos. \n2 No desea continuar eliminando alumnos \nPor favor, elegir una opción: "
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            legajo_eliminar = input(menu_legajo_eliminar) #Mismo menu que arriba
            while validar_num(legajo_eliminar) == False:
                legajo_eliminar = input(menu_legajo_eliminar)
            try: #Manejo de excepciones por si la clave no existe en el diccionario
                matriz_legajos_notas.pop(legajo_eliminar)
            except KeyError: #En caso de que el legajo no exista en la matriz de alumnos
                print(f"Error: El legajo {legajo_eliminar} no existe en la base de datoss.")
            else:
                guardarjson(matriz_legajos_notas)
                print("Base de datos de alumnos actualizada")
                flag_2 = False
        print()
        lin = (input(menu_continuar)) #Mismo menú, pero modularizado.
        while seguir_texto(lin) == False: #Pregunta si quiere seguir eliminando.
            lin = (input(menu_continuar))
        print()
        if int (lin) == 2 or len(matriz_legajos_notas) == 0: # Si no quiere seguir o el diccionario se quedó sin legajos, sale de este apartado.
            flag = False
                            #En caso de ingresar 1, sigue eliminando.
    return True

def mostrar_calificacion_grupal ():
    print()        
    # Imprimir la lista con formato de f-strings
    matriz_legajos_notas = devolverjson()
    for legajo, info in matriz_legajos_notas.items(): #Se obtienen dos elementos por separado, la llave "legajo" y una lista de tuplas con dos elementos: "cursa" y "notas"
        print("-"*26)
        print(f"Legajo: {legajo}")
        for cursa, nota in zip(info["cursa"], info["notas"]): #Zip JUNTA la materia cursada con su RESPECTIVA nota (junta las dos sublistas)
            nota = "-" if nota == -1 else nota
            print(f"Cursa {cursa}, Nota: {nota}")
    return True
        
def mostrar_calificacion_individual ():
    print()
    flag = False
    matriz_legajos_notas = devolverjson()
    legajos = matriz_legajos_notas.keys()
    legajos_formateados = ", ".join(str(legajo) for legajo in legajos) # Se junta las claves en una cadena separada por comas
    print(f"Legajos inscriptos: {legajos_formateados}")
    menu_legajo = "Ingresar el legajo del alumno del cual quiere ver la calificación: " #Legajo individual.
    legajo= input(menu_legajo) #Menú de arriba, modularizado.
    while validar_num(legajo) == False:
        legajo = input(menu_legajo)
    if legajo in matriz_legajos_notas:
        flag = True
    while flag == False:
        print("No se pudo encontrar el legajo ingresado, por favor, volver a intentarlo.")
        legajo= input(menu_legajo)
        while validar_num(legajo) == False:
            legajo = input(menu_legajo)
        if legajo in matriz_legajos_notas:
            flag = True #No existe el legajo antes ingresado, pide otro y vuelve a validar.
    print()
    mostrar_notas(matriz_legajos_notas,legajo)
    return True