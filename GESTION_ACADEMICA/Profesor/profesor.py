from CRUDS.crudProfesores import  *
from VALIDACIONES.Validaciones import validacion_dig
from Base_de_datos.funciones_json import devolverjson
from CRUDS.eliminar_usuario import eliminar_mail

def profesores(email):
    flag_profes = True
    menu_profesor="Qué desea realizar? \n1 Mostrar calificación individual. \n2 Mostrar calificación de todos los alumnos inscriptos.\n3 Agregar/Actualizar notas. \n4 Eliminar alumno. \n5 Volver al menú principal. \n6 Salir de la aplicación.\n7 Eliminar tu cuenta.\nIngrese el numero para la operación que desee: "
    while flag_profes == True:
        print()
        respuesta_prof = input(menu_profesor) #Modularizacion de menu.
        while validacion_dig (respuesta_prof, 7)== False: #Valida que el numero sea entre 1 y 6
            respuesta_prof = input(menu_profesor)
        respuesta_prof = int(respuesta_prof)


        if respuesta_prof == 1:
            if len(devolverjson()) == 0:
                print("\nNo hay ninguna nota cargada")
            else:
                mostrar_calificacion_individual() #Muestra calificación por alumno, preguntando su legajo.

        elif respuesta_prof == 2:
            if len(devolverjson()) == 0:
                print("\nNo hay ninguna nota cargada")
            else:
                mostrar_calificacion_grupal() #Muestra calificacion de todos los alumnos.
 
        elif respuesta_prof == 3:
            if len(devolverjson()) == 0:
                print("\nNo hay ninguna nota cargada")
            else:
                actualizar_notas_alumno() #Puede cambiar las notas de un alumno YA EXISTENTE. Devuelve la matriz actualizada.
            
        elif respuesta_prof == 4:
            if len(devolverjson()) == 0:
                print("\nNo hay ninguna nota cargada")
            else:
                eliminar_alumno()#Elimina alumnos y devuelve la matriz actualizada. 
 
        elif respuesta_prof == 5:
            print("Volviendo al menú principal.") #Vuelve al menú
            return False

        elif respuesta_prof == 6:
            print("Saliendo..")#Sale de la aplicación.
            return True

        elif respuesta_prof == 7:
            seguro = int(input("Está seguro que desea eliminar su cuenta?\n1. Si\n2. No\n"))
            if seguro == 1:
                eliminar_mail(email)
            return False