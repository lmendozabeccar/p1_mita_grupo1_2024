from CRUD.crud_profesores import  *
from VALIDACIONES.validaciones import validacion_dig
from BASE_DE_DATOS.funciones_json import devolverjson
from CRUD.eliminar_modificar_usuario import eliminar_mail, modificaruser

def profesores(email):
    """
    pre: recibe el mail del profesor el cual realizó el login.
    pos: retorna True, en caso de salir de la aplicación, por lo contrario, retorna False, en caso de eliminar 
    la cuenta o volver al menú principal.
    """
    
    flag_profes = True
    menu_profesor="\nQué desea realizar? \n1 Mostrar calificación individual. \n2 Mostrar calificación de todos los alumnos inscriptos.\n3 Agregar/Actualizar notas. \n4 Eliminar alumno. \n5 Modificar cuenta. \n6 Eliminar cuenta. \n7 Volver al menú principal.\n8 Salir de la aplicación.\nIngrese el numero para la operación que desee: "
    while flag_profes == True:
       
        respuesta_prof = input(menu_profesor) #Modularizacion de menu.
        while validacion_dig (respuesta_prof, 8)== False: #Valida que el numero sea entre 1 y 8
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
                menu_actualizar_notas() #Puede cambiar las notas de un alumno YA EXISTENTE. La modificación es guardada en el archivo JSON.
            
        elif respuesta_prof == 4:
            if len(devolverjson()) == 0:
                print("\nNo hay ninguna nota cargada")
            else:
                eliminar_alumno()#Elimina alumnos
 
        elif respuesta_prof == 5:
            modificaruser(email)
            
        elif respuesta_prof == 6:
            seguro = input("\nEstá seguro que desea eliminar su cuenta?\n1. Si\n2. No\nElegir una opción: ")
            while validacion_dig(seguro,2) == False:
                seguro = input("\nEstá seguro que desea eliminar su cuenta?\n1. Si\n2. No\nElegir una opción: ")

            if seguro == "1":
                eliminar_mail(email)
                print("\nVolviendo al menú principal...") 
                return False
            else:
                print("\nVolviendo al menú principal...") #Vuelve al menú
                

        elif respuesta_prof == 7:
            print("\nVolviendo al menú principal...") #Vuelve al menú
            return False

        elif respuesta_prof == 8:
            print("\nSaliendo de la aplicación...")#Sale de la aplicación.
            return True