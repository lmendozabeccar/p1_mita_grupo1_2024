from CRUDS.crudProfesores import  mostrar_calificacion_grupal, mostrar_calificacion_individual, eliminar_alumno, actualizar_notas_alumno
from VALIDACIONES.Validaciones import validar_num, validacion_6dig

def profesores():
    menu="Qué desea realizar? \n1 Mostrar calificación individual. \n2 Mostrar calificación de todos los alumnos inscriptos.\n3 Agregar notas. \n4 Eliminar alumno. \n5 Volver al menú principal. \n6 Salir de la aplicación.\nIngrese el numero para la operación que desee: "

    flag_profes = True
    while flag_profes == True:
        print()
        respuesta_prof = input(menu) #Modularizacion de menu.
        while validar_num(respuesta_prof) == False: #Valida que sea un numero.
            respuesta_prof = input(menu)
        while validacion_6dig (respuesta_prof)== False: #Valida que el numero sea entre 1 y 6
            respuesta_prof = input(menu)
            while validar_num(respuesta_prof) == False: #Valida que sea un numero.
                respuesta_prof = input(menu)
            
        respuesta_prof = int(respuesta_prof)
        if respuesta_prof == 1:
            mostrar_calificacion_individual () #Muestra calificación por alumno, preguntando su legajo.

        elif respuesta_prof == 2:
            mostrar_calificacion_grupal () #Muestra calificacion de todos los alumnos.
            print()

        elif respuesta_prof == 3:
            print()
            actualizar_notas_alumno () #Puede cambiar las notas de un alumno YA EXISTENTE.
        elif respuesta_prof == 4:
            eliminar_alumno () #Elimina alumnos 
            print()

        elif respuesta_prof == 5:
            print("Volviendo al menú principal.") #Vuelve al menú
            return False

        elif respuesta_prof == 6:
            print("Saliendo..") #Sale de la aplicación.
            return True
            