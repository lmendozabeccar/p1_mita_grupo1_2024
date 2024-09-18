from random import randint
from MATRICES.matriz_calificaciones import matriz_notas
from VALIDACIONES.Validaciones import validacion_5dig, validacion_2dig, validar_nota

# Diccionario de materias
materias_dic = {
    "1": "Álgebra",
    "2": "Sistemas",
    "3": "Desarrollo",
    "4": "Inglés",
    "5": "Programación"
}

def agregar_materias(matriz_notas_usar, posicion):
    sublista = matriz_notas_usar[posicion][1]
    print()
    flag = 0
    menu_materia = "Ingrese qué materia cursa: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: "
    menu_agregar_materia = "¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: "
    while flag == 0:
        if -1 not in sublista:
            print()
            print("\nEl alumno ya está inscripto en las 5 materias.")
            return matriz_notas_usar, posicion
        print()
        materia = input(menu_materia)
        while validacion_5dig (materia)== False: #Valida que sea un numero del 1 al 5
            materia = input(menu_materia)
        if sublista[int(materia)-1] != -1:
                print ()
                print("La materia ya fue seleccionada anteriormente, ingrese otra")
        else: 
            # Obtener el nombre de la materia desde el mapeo
            materia_nombre = materias_dic.get(materia) #Busca el valor asociado a la clave materia, en el diccionario (y devuelve el respectivo valor)
            if materia_nombre != None:
                # Agregar la calificación de la materia seleccionada al estudiante 1
                matriz_notas_usar[posicion][1][int(materia)-1] = -2 #Agrega a la matriz de notas la calificacion, en su respectivo orden
                #(1 algebra, 2 sistemas, 3 desarrollo, etc)
                print(f"\nLa materia {materia_nombre} fue agregada.") #Aviso al usuario.
                print()
                # Preguntar si el usuario desea agregar otra materia
                continuar = input(menu_agregar_materia) #Modularizacion de menú anterior.
                while validacion_2dig (continuar)== False: #Valida que ingrese 1 o 2.
                    continuar = input(menu_agregar_materia) #Modularizacion de menú anterior.
                if int(continuar) == 2:
                    flag = 1 
                    #Ingresa 2, sale del apartado y vuelve atras.
    return matriz_notas_usar, posicion

def actualizar_notas (matriz_notas_usar, posicion):
    flag = 0
    sublista = matriz_notas_usar[posicion][1]
    print()
    menu_nota = "Ingrese la materia la cual quiere agregar las notas: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: "
    menu_agregar_nota = "¿Desea agregar la nota de otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: "
    menu_calificacion = "Ingresar nota de la respectiva materia: "
    while flag == 0:
        if -2 not in sublista:
            print()
            print("\nEl alumno no está inscripto en ninguna materia.")
            return matriz_notas_usar, posicion
        materia = input(menu_nota)
        while validacion_5dig (materia)== False: #Valida que sea un numero del 1 al 5
            materia = input(menu_nota)
            
        materia_nombre = materias_dic.get(materia) #Busca el valor asociado a la clave materia, en el diccionario (y devuelve el respectivo valor)
        if materia_nombre != None:
            if sublista[int(materia)-1] == -1:
                print()
                print("El alumno no está inscripto en esa materia.")
            else:
                # Agregar la calificación de la materia seleccionada al estudiante 1
                calificacion = input(menu_calificacion)
                while validar_nota(calificacion) == False:
                    calificacion = input(menu_calificacion)
                    
                sublista[int(materia)-1] =  int (calificacion)#Agrega a la matriz de notas la calificacion, en su respectivo orden
                #(1 algebra, 2 sistemas, 3 desarrollo, etc)
                print(f"\nLa materia {materia_nombre} fue agregada con una calificación de {calificacion}.") #Aviso al usuario.
                print()
                # Preguntar si el usuario desea agregar otra materia
                continuar = input(menu_agregar_nota) #Modularizacion de menú anterior.
                while validacion_2dig (continuar)== False: #Valida que ingrese 1 o 2.
                    continuar = input(menu_agregar_nota) #Modularizacion de menú anterior.
                if int(continuar) == 2:
                    flag = 1                  #Ingresa 2, sale del apartado y vuelve atras.
    return matriz_notas_usar, posicion
