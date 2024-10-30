import json
from VALIDACIONES.Validaciones import validacion_dig
from MATRICES.matriz_calificaciones import mostrar_notas
from MATRICES.Diccionario_Materias import agregar_materias
from Base_de_datos.funciones_json import devolverjson, guardarjson
from CRUDS.eliminar_usuario import eliminar_mail

def estudiantes(legajo, email): 
    flag_estudiantes = True
    #Agregar función para eliminar la inscripción de una materia, a la vez de indicar si recursa una materia en caso de que se saque un 2
    menu_estudiantes="\nQué desea realizar ahora? \n1 Inscribirse en las materias correspondientes.\n2 Ver sus calificaciones y su promedio\n3 Volver al menú principal.\n4 Salir de la aplicación.\n5 Eliminar tu cuenta. \nIngrese el numero para la operación que desee: "
    while flag_estudiantes == True:    
        respuesta_est = input(menu_estudiantes) #Menú modularizado.
        while validacion_dig (respuesta_est, 5) == False: #Validacion numero entre 1 y 4 
            respuesta_est = input(menu_estudiantes)
        
        respuesta_est = int(respuesta_est) 
        if respuesta_est == 1:
            agregar_materias (legajo) #Agrega las materias que quiere, y le pone una nota aleatoria.
                
        elif respuesta_est == 2:
            matriz_legajos_notas = devolverjson()
            if len(matriz_legajos_notas)== 0:
                print("\nNo hay ninguna nota cargada")
            else:
                mostrar_notas(matriz_legajos_notas,legajo)
        
        elif respuesta_est == 3:
            print("Volviendo al menú principal.") #Vuelve al menú principal.
            return False
                    
        elif respuesta_est == 4:
            print("Saliendo de la aplicación") #Sale de la aplicación.
            return True
        
        elif respuesta_est == 5:
            seguro = int(input("Está seguro que desea eliminar su cuenta?\n1. Si\n2. No\n"))
            if seguro == 1:
                eliminar_mail(email)

            return False