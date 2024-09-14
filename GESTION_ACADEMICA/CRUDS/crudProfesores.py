from VALIDACIONES.Validaciones import seguir_texto, validacion_notas
posicion = lambda legajo, lista: [i for i in range(len(lista)) if lista[i][0] == legajo]
#Devuelve en qué fila esta el legajo dentro de la matriz
mostrar_calificacion = lambda lista: [print(f"|{legajo:^8}|{algebra:^12}|{programacion:^12}|{analisis:^8}|{sistemas:^8}|{desarrollo:^14}|") for legajo, algebra, programacion, analisis, sistemas, desarrollo in lista] 
#Uso de corchetes solo para el print
def ingreso_notas():
    print()
    print("Por favor, introducir las materias del nuevo alumno.")
    algebra =(input("Ingrese la nueva nota de Álgebra: "))        
    programacion =(input("Ingrese la nueva nota de Programación: "))
    analisis =(input("Ingrese la nueva nota de Análisis: "))
    sistemas =(input("Ingrese la nueva nota de Sistemas: "))
    desarrolloweb =(input("Ingrese la nueva nota de Desarrollo web: "))
    while validacion_notas (algebra,programacion,analisis,sistemas,desarrolloweb) == False:
        print("Por favor, ingresar notas entre 0 y 10 en cada materia, con solamente 1 número decimal posible.")
        print()
        algebra =(input("Ingrese la nueva nota de Álgebra: "))        
        programacion =(input("Ingrese la nueva nota de Programación: "))
        analisis =(input("Ingrese la nueva nota de Análisis: "))
        sistemas =(input("Ingrese la nueva nota de Sistemas: "))
        desarrolloweb =(input("Ingrese la nueva nota de Desarrollo web: "))
    return algebra, programacion, analisis, sistemas, desarrolloweb

def agregar_alumno(lista):
    flag_while = True
    while flag_while == True: #Esto es solo para verificar si el legajo existe
        calif = ingreso_notas() #Esta funcion me va a devolver una tupla
        lista.append([lista[-1][0]+1,calif[0],calif[1],calif[2],calif[3],calif[4]]) #Append de cada posicion de la tupla
        lin = (input("\n1 Desea continuar agregando alumnos. \n2 No desea continuar agregando alumnos \nPor favor, elegir una opción: "))
        while seguir_texto(lin) == False:
            lin = (input("\n1 Desea continuar agregando alumnos. \n2 No desea continuar agregando alumnos \nPor favor, elegir una opción: "))
        if int (lin) ==2:
            flag_while = False    
    return lista

def actualizar_alumno(lista):
    flag = True
    while flag == True:
        print()
        flag_2 = True
        while flag_2 == True:
            legajo_actualizar = int(input("Ingrese el legajo que quiere actualizar: "))
            indice = posicion(legajo_actualizar, lista) #Saco en qué posicion esta el legajo en la lista
            if indice == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
            else:
                flag_2 = False
        print("Este es el legajo que va a actualizar: ")
        print(lista[indice[0]])#Lo imprimo para que el usuario vea lo que hay en la fila
        calif = ingreso_notas()
        lista[indice[0]] = [legajo_actualizar,calif[0],calif[1],calif[2],calif[3],calif[4]]#"indice" es una lista, entonces me fijo en la posición 0 para sacar el índice como entero, y luego actualizar esa posicion
        print("Legajo actualizado")
        print()
        lin = (input("\n1 Desea continuar actualizando alumnos. \n2 No desea continuar actualizando alumnos \nPor favor, elegir una opción: "))
        while seguir_texto(lin) == False:
            lin = (input("\n1 Desea continuar actualizando alumnos. \n2 No desea continuar actualizando alumnos \nPor favor, elegir una opción: "))
        if int (lin) == 2:
            flag = False
    return lista

def eliminar_alumno(lista):
    print()
    flag = True
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            legajo_actualizar = int(input("Ingrese el legajo que quiere eliminar: "))
            indice = posicion(legajo_actualizar, lista) #Saco en qué posicion esta el legajo en la lista
            if indice == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
            else:
                flag_2 = False
        lista.pop(indice[0]) #"indice" es una lista, entonces me fijo en la posición 0 para sacar el índice como entero, y luego borrar esa posicion
        print()
        lin = (input("\n1 Desea continuar eliminando alumnos. \n2 No desea continuar eliminando alumnos \nPor favor, elegir una opción: "))
        while seguir_texto(lin) == False:
            lin = (input("\n1 Desea continuar eliminando alumnos. \n2 No desea continuar eliminando alumnos \nPor favor, elegir una opción: "))
        print()
        if int (lin) == 2:
            flag = False
            
    return lista