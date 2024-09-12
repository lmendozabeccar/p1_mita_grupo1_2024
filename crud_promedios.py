from random import randint

encabezado_calificaciones = [
    ["Legajos", "Algebra", "Programación", "Análisis", "Sistemas", "Desarrollo web"]
]
#La primera variable de cada lista es el legajo

aleatorio = lambda: randint(1, 10)

seguir = lambda: int(input("Quiere repetir el procedimiento?\n1 Si\n2 No\nElija un número: ")) == 1 
#Si el input es 1, la funcion devuelve True. Si es 2, devuelve False

posicion = lambda legajo, lista: [i for i in range(len(lista)) if lista[i][0] == legajo]
#Devuelve en qué fila esta el legajo dentro de la matriz

mostrar_calificacion = lambda lista: [print(f"|{legajo:^8}|{algebra:^12}|{programacion:^12}|{analisis:^8}|{sistemas:^8}|{desarrollo:^14}|") for legajo, algebra, programacion, analisis, sistemas, desarrollo in lista] 
#Uso de corchetes solo para el print

promedio_materia = lambda indice, lista: (sum(fila[indice] for fila in lista[1:]) / len(lista)) #lista[1:] --> Se necesita que el bucle "for" saltee el encabezado para calcular bien el promedio
#La lista por comprensión devuelve un objeto (una lista). sum() va a sumar la lista, y luego es dividido por la cantidad de registros

def llenar_matriz(lista):
    for i in range(9):
        lista.append([1000+i, aleatorio(), aleatorio(), aleatorio(), aleatorio(), aleatorio()])
    return lista

def ingreso_notas():
    flag = True
    algebra =int(input("Ingrese la nueva nota de algebra: "))
    programacion =int(input("Ingrese la nueva nota de Programacion: "))
    analisis =int(input("Ingrese la nueva nota de analisis: "))
    sistemas =int(input("Ingrese la nueva nota de sistemas: "))
    desarrolloweb =int(input("Ingrese la nueva nota de desarrolloweb: "))
    return algebra, programacion, analisis, sistemas, desarrolloweb

def agregar_alumno(lista):
    flag_while = True
    while flag_while == True: #Esto es solo para verificar si el legajo existe
        calif = ingreso_notas() #Esta funcion me va a devolver una tupla
        lista.append([lista[-1][0]+1,calif[0],calif[1],calif[2],calif[3],calif[4]]) #Append de cada posicion de la tupla
        if seguir() == False:
            flag_while = False
    return lista

def actualizar_alumno(lista):
    flag = True
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            legajo_actualizar = int(input("Ingrese el legajo que quiere actualizar: "))
            indice = posicion(legajo_actualizar, lista) #Saco en qué posicion esta el legajo en la lista
            if indice == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
            else:
                flag_2 = False
        print("-"*26)
        print(lista[indice[0]])#Lo imprimo para que el usuario vea lo que hay en la fila
        print("-"*26)
        calif = ingreso_notas()
        lista[indice[0]] = [legajo_actualizar,calif[0],calif[1],calif[2],calif[3],calif[4]]#"indice" es una lista, entonces me fijo en la posición 0 para sacar el índice como entero, y luego actualizar esa posicion
        print("Legajo actualizado")
        print("-"*26)
        if seguir() == False:
            flag = False
    return lista

def eliminar_alumno(lista):
    flag = True
    while flag == True:
        flag_2 = True
        while flag_2 == True:
            legajo_actualizar = int(input("Ingrese el legajo que quiere eliminar "))
            indice = posicion(legajo_actualizar, lista) #Saco en qué posicion esta el legajo en la lista
            if indice == []:
                print("No se ha podido encontrar ese legajo, ingrese otro.")
            else:
                flag_2 = False
        lista.pop(indice[0]) #"indice" es una lista, entonces me fijo en la posición 0 para sacar el índice como entero, y luego borrar esa posicion
        if seguir() == False:
            flag = False
    return lista

def ver_calificacion(legajo, lista):
    posicion = [i for i in range(len(lista)) if lista[i][0] == legajo]#Me devuelve la posición de la matriz(devolviendo posicion como una lista)
    fila = lista[posicion[0]] #Saco la fila donde quiero ver las calificaciones, con posicion[0] ya que es una lista, y se desea leer el entero
    fila.remove(legajo) #Elimino el legajo en la lista para poder sacar el promedio de la fila (las materias)
    promedio = sum(fila) / 5
    print(f'|{"legajo":^8}|{"algebra":^12}|{"programacion":^12}|{"analisis":^8}|{"sistemas":^8}|{"desarrollo":^14}|')
    print(f"|{legajo:^8}|{lista[posicion[0]][0]:^12}|{lista[posicion[0]][1]:^12}|{lista[posicion[0]][2]:^8}|{lista[posicion[0]][3]:^8}|{lista[posicion[0]][4]:^14}|")
    print(f"Promedio = {promedio:.2f}") #Limitar el promedio hasta dos decimales
    return 1

def ver_materias(lista):
    algebra = promedio_materia(1, lista)
    programacion = promedio_materia(2, lista)
    analisis = promedio_materia(3, lista)
    sistemas = promedio_materia(4, lista)
    desarrollo = promedio_materia(5, lista)
    print(f'|{"algebra":^12}|{"programacion":^12}|{"analisis":^8}|{"sistemas":^8}|{"desarrollo":^14}|')
    print(f'|{algebra:^12.2f}|{programacion:^12.2f}|{analisis:^8.2f}|{sistemas:^8.2f}|{desarrollo:^14.2f}|') #.2f limita el numero decimal a 2 dígitos
    return 1
