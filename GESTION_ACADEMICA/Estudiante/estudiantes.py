from MATRICES.matriz_calificaciones import llenar_matriz, encabezado_calificaciones
from VALIDACIONES.Validaciones import validar_num, validacion_3dig, validacion_2dig
from CRUDS.crudEstudiantes import ver_calificacion, ver_materias
def estudiantes(posicion):
    alumnos_calificaciones = llenar_matriz(encabezado_calificaciones)
    legajo = alumnos_calificaciones[posicion+1][0]
    flag_estudiantes = True
    while flag_estudiantes == True:      
        respuesta_est = input("\nQué desea realizar ahora? \n1 Ver mis calificaciones y mi promedio\n2 Ver mi promedio por materia\n3 Salir de la aplicación. \nIngrese el numero para la operación que desee: ")
        #Se desea que sea una cadena para luego poder verificar si es un número
        while validar_num(respuesta_est) == False:
            respuesta_est = input("\nQué desea realizar ahora? \n1 Ver mis calificaciones y mi promedio\n2 Ver mi promedio por materia\n3 Salir de la aplicación. \nIngrese el numero para la operación que desee: ")
        while validacion_3dig (respuesta_est)== False:
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