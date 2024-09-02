from random import randint
encabezado_calificaciones = [
    ["Legajos", "Algebra", "Programación", "Análisis", "Sistemas", "Desarrollo web"]
]
#La primera variable de cada lista es el legajo

encabezado_asistencias = [
    ["Legajo", "Clase1", "Clase2", "Clase3", "Clase4", "Clase5", "Clase6", "Clase7", "Clase8"],
]
# Presente = 1, Ausente = 0
def aleatorio():
    return randint(1, 10)

def llenar_matriz(lista):
    for i in range(31):
        lista.append([1000+i, aleatorio(), aleatorio(), aleatorio(), aleatorio(), aleatorio()])
    return lista

def agregar_alumno(lista):
    flag_legajo = True
    flag_while_1 = True
    while flag_while_1 == True: #Esto es solo para verificar si el legajo existe
        legajo = int(input("Ingrese el legajo del alumno: "))
        for fila in lista:
            if legajo in fila:
                flag_legajo = False
        if flag_legajo == False:
            print("Ese legajo ya existe, ingrese otro de vuelta.")
        else:
            legajo_nuevo=int(input("Ingrese el nuevo legajo: "))
            algebra =int(input("Ingrese la nueva nota de algebra: "))
            programacion =int(input("Ingrese la nueva nota de Programacion: "))
            analisis =int(input("Ingrese la nueva nota de analisis: "))
            sistemas =int(input("Ingrese la nueva nota de sistemas: "))
            desarrolloweb =int(input("Ingrese la nueva nota de desarrolloweb: "))
            lista.append([legajo_nuevo,algebra,programacion,analisis,sistemas,desarrolloweb])
            respuesta = int(input("Quiere actualizar otro legajo?\n1 Si\n2 No\nElija un número: "))
            if respuesta == 2:
                flag_while_1 = False
    return lista

def mostrar_calificacion(lista):
    for legajo, algebra, programacion, analisis, sistemas, desarrollo in lista:
        print(f"|{legajo:^8}|{algebra:^12}|{programacion:^12}|{analisis:^8}|{sistemas:^8}|{desarrollo:^14}|")

    return main(encabezado_calificaciones, encabezado_asistencias)
    
def actualizar_alumno(lista):
    flag = True
    while flag == True:
        flag_for = False
        posicion = 0
        legajo_actualizar = int(input("Ingrese el legajo que quiere actualizar: "))
        for i in range(len(lista)):
            if lista[i][0] == legajo_actualizar:
                posicion = i
                flag_for = True
        if flag_for == True:
            print("-"*26)
            print(lista[posicion])
            print("-"*26)
            algebra =int(input("Ingrese la nueva nota de algebra: "))
            programacion =int(input("Ingrese la nueva nota de Programacion: "))
            analisis =int(input("Ingrese la nueva nota de analisis: "))
            sistemas =int(input("Ingrese la nueva nota de sistemas: "))
            desarrolloweb =int(input("Ingrese la nueva nota de desarrolloweb: "))
            lista[posicion] = [legajo_actualizar, algebra, programacion, analisis, sistemas, desarrolloweb]
            print("Legajo actualizado")
            print("-"*26)
        respuesta = int(input("Quiere actualizar otro legajo?\n1 Si\n2 No\nElija un número: "))
        if respuesta == 2:
            flag = False
    return lista
def eliminar_alumno(lista):
    flag = True
    while flag == True:
        legajo_eliminar = int(input("Ingrese el legajo que quiere eliminar: "))
        for i in range(len(lista)-1):
            if lista[i][0] == legajo_eliminar:
                lista.pop(i)
                print("Legajo correctamente eliminado")
                print("-"*26)
        respuesta = int(input("Quiere actualizar otro legajo?\n1 Si\n2 No\nElija un número: "))
        if respuesta == 2:
            flag = False
    return lista
def main(encabezado_calificaciones, encabezado_asistencias):
    alumnos_calificaciones = llenar_matriz(encabezado_calificaciones)
    flag = True
    while flag== True:
        print("-"*26)
        respuesta = int(input("1 Agregar alumno\n2 Mostrar calificaciones\n3 Modificar alumno\n4 Eliminar alumno\n5 Finalizar\nIngrese el numero para la operación que desee: "))
        if respuesta == 1:
            alumnos_calificaciones = agregar_alumno(alumnos_calificaciones)
        elif respuesta == 2:
            print(mostrar_calificacion(alumnos_calificaciones))
        elif respuesta == 3:
            alumnos_calificaciones = actualizar_alumno(alumnos_calificaciones)
        elif respuesta == 4:
            alumnos_calificaciones = eliminar_alumno(alumnos_calificaciones)
        elif respuesta==5:
            flag = False
main(encabezado_calificaciones, encabezado_asistencias)
#Utilizar diccionarios para gestionar la información del alumno, tal como el nombre, apellido, carrera, email y otros datos
