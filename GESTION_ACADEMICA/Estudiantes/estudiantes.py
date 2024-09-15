from MATRICES.matriz_calificaciones import llenar_matriz, encabezado_calificaciones
from VALIDACIONES.Validaciones import validar_num, validacion_3dig, validacion_2dig, validacion_5dig
from CRUDS.crudEstudiantes import ver_calificacion, ver_materias
from MATRICES.matriz_alumnos import ingreso_alumnos
def estudiantes(posicion):
    alumnos_calificaciones = llenar_matriz(encabezado_calificaciones)
    legajo = alumnos_calificaciones[posicion+1][0]
    flag_estudiantes = True
    while flag_estudiantes == True:      
        respuesta_est = input("\nQué desea realizar ahora? \n1 Ver mis calificaciones y mi promedio\n2 Ver mi promedio por materia\n3 Salir de la aplicación. \nIngrese el numero para la operación que desee: ")
        #Se desea que sea una cadena para luego poder verificar si es un número
        while validar_num(respuesta_est) == False: #Validacion numero
            respuesta_est = input("\nQué desea realizar ahora? \n1 Ver mis calificaciones y mi promedio\n2 Ver mi promedio por materia\n3 Salir de la aplicación. \nIngrese el numero para la operación que desee: ")
        while validacion_3dig (respuesta_est)== False: #Validacion numero entre 1 y 3
            respuesta_est = input("\nQué desea realizar ahora? \n1 Ver mis calificaciones y mi promedio\n2 Ver mi promedio por materia\n3 Salir de la aplicación. \nIngrese el numero para la operación que desee: ")
            while validar_num(respuesta_est) == False:
                respuesta_est = input("\nQué desea realizar ahora? \n1 Ver mis calificaciones y mi promedio\n2 Ver mi promedio por materia\n3 Salir de la aplicación. \nIngrese el numero para la operación que desee: ")
                
        respuesta_est = int(respuesta_est) 
        if respuesta_est == 1:
            print()
            ver_calificacion(legajo, alumnos_calificaciones)
            inic = (input("\nQué desea realizar ahora? \n1 Ver promedio por materia. \n2 Volver al apartado de alumnos. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))
            while validar_num(inic) == False:
                inic = (input("\nQué desea realizar ahora? \n1 Ver promedio por materia. \n2 Volver al apartado de alumnos. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))           

            while validacion_3dig (inic)== False:
                inic = (input("\nQué desea realizar ahora? \n1 Ver promedio por materia. \n2 Volver al apartado de alumnos. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))
                while validar_num(inic) == False:
                    inic = (input("\nQué desea realizar ahora? \n1 Ver promedio por materia. \n2 Volver al apartado de alumnos. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))

            if int (inic) ==  1:
                ver_materias (alumnos_calificaciones)
                inic = input("\nUna vez visto su promedio por materia y su promedio general, qué desea realizar? \n1 Volver al apartado de alumnos. \n2 Salir de la aplicación. \nPor favor, elegir la opción que desee: ")
                while validar_num(inic) == False:
                    inic = input("\nUna vez visto su promedio por materia y su promedio general, qué desea realizar? \n1 Volver al apartado de alumnos. \n2 Salir de la aplicación. \nPor favor, elegir la opción que desee: ")

                while validacion_2dig (inic)== False:
                    inic = input("\nUna vez visto su promedio por materia y su promedio general, qué desea realizar? \n1 Volver al apartado de alumnos. \n2 Salir de la aplicación. \nPor favor, elegir la opción que desee: ")
                    while validar_num(inic) == False:
                        inic = input("\nUna vez visto su promedio por materia y su promedio general, qué desea realizar? \n1 Volver al apartado de alumnos. \n2 Salir de la aplicación. \nPor favor, elegir la opción que desee: ")
                
                if int (inic) == 1: 
                    print()
                    print("Volviendo al apartado de alumnos.")
                
                elif int (inic) == 2:
                    print()
                    print("Saliendo de la aplicación.")
                    flag_estudiantes = False

                
            elif int (inic) == 2:
                print()
                print("Volviendo al apartado de alumnos.")

            elif int (inic) == 3:
                flag_estudiantes = False
                print("Saliendo de la aplicación.")
   
        elif respuesta_est == 2:
            print()
            ver_materias(alumnos_calificaciones)
            inic = (input("\nQué desea realizar ahora? \n1 Ver sus calificaciones y su promedio general. \n2 Volver al apartado de alumnos. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))
            while validar_num(inic) == False:
                inic = (input("\nQué desea realizar ahora? \n1 Ver sus calificaciones y su promedio general. \n2 Volver al apartado de alumnos. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))

            while validacion_3dig (inic)== False:
                inic = (input("\nQué desea realizar ahora? \n1 Ver sus calificaciones y su promedio general. \n2 Volver al apartado de alumnos. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))
                while validar_num(inic) == False:
                    inic = (input("\nQué desea realizar ahora? \n1 Ver sus calificaciones y su promedio general. \n2 Volver al apartado de alumnos. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))

            if int (inic) ==  1:
                ver_calificacion(legajo, alumnos_calificaciones)     
                inic = input("\nUna vez visto su promedio por materia y su promedio general, qué desea realizar? \n1 Volver al apartado de alumnos. \n2 Salir de la aplicación. \nPor favor, elegir la opción que desee: ")
                while validar_num(inic) == False:
                    inic = input("\nUna vez visto su promedio por materia y su promedio general, qué desea realizar? \n1 Volver al apartado de alumnos. \n2 Salir de la aplicación. \nPor favor, elegir la opción que desee: ")

                while validacion_2dig (inic)== False:
                    inic = input("\nUna vez visto su promedio por materia y su promedio general, qué desea realizar? \n1 Volver al apartado de alumnos. \n2 Salir de la aplicación. \nPor favor, elegir la opción que desee: ")
                    while validar_num(inic) == False:
                        inic = input("\nUna vez visto su promedio por materia y su promedio general, qué desea realizar? \n1 Volver al apartado de alumnos. \n2 Salir de la aplicación. \nPor favor, elegir la opción que desee: ")
                
                if int (inic) == 1: 
                    print()
                    print("Volviendo al apartado de alumnos.")
                
                elif int (inic) == 2:
                    print()
                    print("Saliendo de la aplicación.")
                    flag_estudiantes = False
                    
            elif int (inic) == 2:
                print()
                print("Volviendo al apartado de alumnos.")

            elif int (inic) == 3:
                flag_estudiantes = False
                print("Saliendo de la aplicación.")

            
        elif respuesta_est == 3:
            flag_estudiantes = False
            print("Saliendo de la aplicación")
            
def ingreso_materias (i):
    from random import randint
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

    # Inicialización de la lista de materias de estudiantes
    estudiantes_materias = [[ingreso_alumnos[i]]  # Lista inicial con información del estudiante 1    
                            ]

    flag = 0
    contmaterias = 0
    while flag == 0:
        print()
        materia = input("Ingrese qué materia desea cursar: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: ")
        while validar_num(materia) == False:
            materia = input("Ingrese qué materia desea cursar: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: ")
        while validacion_5dig (materia)== False:
            materia = input("Ingrese qué materia desea cursar: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: ")
            while validar_num(materia) == False:
                materia = input("Ingrese qué materia desea cursar: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: ")
        # Obtener el nombre de la materia desde el mapeo
        materia_nombre = materias_dic.get(materia)

        if materia_nombre != None:
            # Agregar la calificación de la materia seleccionada al estudiante 1
            calificacion = aleatorio()
            estudiantes_materias[0].append(calificacion)

            ingreso_alumnos[i][4].append(materia_nombre)
            ingreso_alumnos[i][5].append(calificacion)
            print()
            print(f"La materia {materia_nombre} fue agregada con una calificación de: {calificacion}.")
            print()
            contmaterias += 1
        else:
            print("Opción no válida. Por favor ingrese un número entre 1 y 5.")
        
        # Preguntar si el usuario desea agregar otra materia
        continuar = input("¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: ")
        while validar_num(continuar) == False:
            continuar = input("¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: ")
        while validacion_2dig (continuar)== False:
            continuar = input("¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: ")
            while validar_num(continuar) == False:
                continuar = input("¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: ")
        if int(continuar) == 2:
            flag = 1 
    print("Estás inscripto a",contmaterias,"materias, las cuales son",ingreso_alumnos[i][4],"con unas calificaciones de",ingreso_alumnos[i][5],"respectivamente.")

