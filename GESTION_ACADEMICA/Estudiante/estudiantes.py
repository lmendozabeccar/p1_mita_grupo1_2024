import json
from VALIDACIONES.Validaciones import validacion_dig
from MATRICES.matriz_calificaciones import mostrar_notas
from MATRICES.Diccionario_Materias import agregar_materias
from Base_de_datos.funciones_json import devolverjson
from CRUDS.eliminar_modificar import eliminar_mail, modificaruser

def estudiantes(legajo, email):
    """
    pre: recibe como datos de entrada el legajo y el mail del usuario.
    pos: multiples funciones, inscribirse, ver calificaciones, eliminar cuenta, modificarla, volver al menu principal, salir de la aplicacion.
    """
    flag_estudiantes = True
    #Agregar función para eliminar la inscripción de una materia, a la vez de indicar si recursa una materia en caso de que se saque un 2
    menu_estudiantes="\nQué desea realizar ahora? \n1 Inscribirse en las materias correspondientes.\n2 Ver sus calificaciones y su promedio.\n3 Eliminar tu cuenta.\n4 Modificar su cuenta.\n5 Volver al menú principal.\n6.Salir de la aplicación. \nIngrese el numero para la operación que desee: "
    while flag_estudiantes == True:    
        respuesta_est = input(menu_estudiantes) #Menú modularizado.
        while validacion_dig (respuesta_est, 6) == False: #Validacion numero entre 1 y 6
            respuesta_est = input(menu_estudiantes)
        
        respuesta_est = int(respuesta_est) #Se pasa el string a entero
        if respuesta_est == 1:
            agregar_materias (legajo) #Agrega las materias que quiere, y le pone una nota aleatoria.
                
        elif respuesta_est == 2:
            matriz_legajos_notas = devolverjson()
            if len(matriz_legajos_notas)== 0:
                print("\nNo hay ninguna nota cargada")
            else:
                mostrar_notas(matriz_legajos_notas,legajo,"alumno")
        
        elif respuesta_est == 3:
            seguro = input("\nEstá seguro que desea eliminar su cuenta?\n1. Si\n2. No\nPor favor, elegir una opción: ")
            if seguro == "1":
                eliminar_mail(email)
                return False                    
            else:
                print("\nVolviendo al menú principal...")     
        elif respuesta_est == 4:
            modificaruser(email)
        
        elif respuesta_est == 5:
            print("\nVolviendo al menú principal...") #Vuelve al menú principal.
            return False

        elif respuesta_est == 6:
            print("\nSaliendo de la aplicación...") #Sale de la aplicación.
            return True
