from random import randint
from MATRICES.matriz_calificaciones import matriz_notas
from VALIDACIONES.Validaciones import validar_num, validacion_5dig, validacion_2dig
# Función lambda para generar calificaciones aleatorias
aleatorio = lambda: randint(1, 10)


# Diccionario de materias
materias_dic = {
    "1": "Álgebra",
    "2": "Sistemas",
    "3": "Desarrollo",
    "4": "Inglés",
    "5": "Programación"
}

def agregar_materias(posicion):
    seleccionada_estudiantes = []
    flag = 0
    flag_seleccion = False
    while flag == 0:
        print()
        menu = "Ingrese qué materia cursa: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: "
        materia = input(menu)
        while validar_num(materia) == False: #Valida que lo que se ingreso sea un numero.
            materia = input(menu)
        while validacion_5dig (materia)== False: #Valida que sea un numero del 1 al 5
            materia = input(menu)
            while validar_num(materia) == False: #Valida nuevamente que sea un numero.
                materia = input(menu)
        if materia in seleccionada_estudiantes:
                print("La materia ya fue seleccionada anteriormente, Ingrese otra")
                flag_seleccion = False
        else: 
            # Obtener el nombre de la materia desde el mapeo
            materia_nombre = materias_dic.get(materia) #Busca el valor asociado a la clave materia, en el diccionario
            if materia_nombre != None:
                # Agregar la calificación de la materia seleccionada al estudiante 1
                calificacion = aleatorio() #Arriba en la funcion lambda le da un numero aleatorio.
                matriz_notas[posicion][1][int(materia)-1] = calificacion #Agrega a la matriz de notas la calificacion, en su respectivo orden
                seleccionada_estudiantes.append(materia)
                #(1 algebra, 2 sistemas, 3 desarrollo, etc)
                print()
                print(f"La materia {materia_nombre} fue agregada con una calificación de: {calificacion}.") #Aviso al usuario.
                flag_seleccion = True
                print()
            
            # Preguntar si el usuario desea agregar otra materia
            menu2 = "¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: "
            continuar = input(menu2) #Modularizacion de menú anterior.
            while validar_num(continuar) == False: #Valida que sea un numero.
                continuar = input(menu2) #Modularizacion de menú anterior.
            while validacion_2dig (continuar)== False: #Valida que ingrese 1 o 2.
                continuar = input(menu2) #Modularizacion de menú anterior.
                while validar_num(continuar) == False: #Valida que sea un numero.
                    continuar = input(menu2) #Modularizacion de menú anterior.
            if int(continuar) == 2:
                flag = 1 
                #Ingresa 2, sale del apartado y vuelve atras.

    return matriz_notas, posicion

def agregar_materias_profesor (posicion):
    flag = 0
    seleccionada_profesores = []
    flag_seleccionada2 = False
    while flag == 0:
        print()
        menu = "Ingrese qué materia desea agregar: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: "
        materia = input(menu) #Modularizacion de menu
        while validar_num(materia) == False: #Valida que sea un numero
            materia = input(menu)
        while validacion_5dig (materia)== False: #Valida que sea entre 1 y 5
            materia = input(menu)
            while validar_num(materia) == False: #Valida que sea un numero.
                materia = input(menu)
        if materia in seleccionada_profesores:
            print("La materia ya fue seleccionada anteriormente, Ingrese otra")
            flag_seleccionada2 = False
        else:
            # Obtener el nombre de la materia desde el mapeo
            materia_nombre = materias_dic.get(materia)
            if materia_nombre != None:
                # Agregar la calificación de la materia seleccionada al estudiante 1
                calificacion = aleatorio()

                matriz_notas[posicion][1][int(materia)-1] = calificacion #Agrega en la matriz la nota.
                seleccionada_profesores.append(materia)
                flag_seleccionada2 = True
                print()
                print(f"La materia {materia_nombre} fue agregada con una calificación de: {calificacion}.") #Aviso al usuario.
                
                print()
            # Preguntar si el usuario desea agregar otra materia
            menu2 = "¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: "
            continuar = input(menu2) #Modularizacion de menu
            while validar_num(continuar) == False: #Valida que sea un numero.
                continuar = input(menu2) 
            while validacion_2dig (continuar)== False: # Valida que sea 1 o 2.
                continuar = input(menu2)
                while validar_num(continuar) == False: #Valida que sea un numero.
                    continuar = input(menu2)
            if int(continuar) == 2:
                flag = 1 
                #Vuelve atrás.

    return matriz_notas, posicion    