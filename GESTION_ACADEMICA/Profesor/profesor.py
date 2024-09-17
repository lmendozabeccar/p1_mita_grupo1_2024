from CRUDS.crudProfesores import  mostrar_calificacion_grupal, mostrar_calificacion_individual, eliminar_alumno, actualizar_notas_alumno
from VALIDACIONES.Validaciones import validacion_6dig
from MATRICES.matriz_calificaciones import matriz_notas

def profesores(matriz_notas_register):
    if matriz_notas_register == []:
        matriz_notas_usar = matriz_notas
    else:
        matriz_notas_usar = matriz_notas_register
    flag_profes = True
    menu="Qué desea realizar? \n1 Mostrar calificación individual. \n2 Mostrar calificación de todos los alumnos inscriptos.\n3 Agregar notas. \n4 Eliminar alumno. \n5 Volver al menú principal. \n6 Salir de la aplicación.\nIngrese el numero para la operación que desee: "
    while flag_profes == True:
        print()
        respuesta_prof = input(menu) #Modularizacion de menu.
        while validacion_6dig (respuesta_prof)== False: #Valida que el numero sea entre 1 y 6
            respuesta_prof = input(menu)
            
        respuesta_prof = int(respuesta_prof)
        if respuesta_prof == 1:
            mostrar_calificacion_individual (matriz_notas_usar) #Muestra calificación por alumno, preguntando su legajo.

        elif respuesta_prof == 2:
            mostrar_calificacion_grupal (matriz_notas_usar) #Muestra calificacion de todos los alumnos.
            print()

        elif respuesta_prof == 3:
            matriz_notas_actualizadas = actualizar_notas_alumno (matriz_notas_usar) #Puede cambiar las notas de un alumno YA EXISTENTE.
            print()
            
        elif respuesta_prof == 4:
            matriz_notas_actualizadas = eliminar_alumno (matriz_notas_usar) #Elimina alumnos 
            print()

        elif respuesta_prof == 5:
            print("Volviendo al menú principal.") #Vuelve al menú
            return matriz_notas_actualizadas

        elif respuesta_prof == 6:
            print("Saliendo..") #Sale de la aplicación.
            return True
            