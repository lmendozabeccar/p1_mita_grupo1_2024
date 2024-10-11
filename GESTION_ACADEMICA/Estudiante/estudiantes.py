from VALIDACIONES.Validaciones import validacion_dig
from MATRICES.matriz_calificaciones import mostrar_notas
from MATRICES.diccionario_materias import agregar_materias

def estudiantes(matriz_legajos_notas, legajo): 
    flag_estudiantes = True
    #Agregar función para eliminar la inscripción de una materia, a la vez de indicar si recursa una materia en caso de que se saque un 2
    menu_estudiantes="\nQué desea realizar ahora? \n1 Inscribirse en las materias correspondientes.\n2 Ver sus calificaciones y su promedio\n3 Volver al menú principal. \n4 Salir de la aplicación.  \nIngrese el numero para la operación que desee: "
    while flag_estudiantes == True:    
        respuesta_est = input(menu_estudiantes) #Menú modularizado.
        while validacion_dig (respuesta_est, 4) == False: #Validacion numero entre 1 y 4 
            respuesta_est = input(menu_estudiantes)
        
        respuesta_est = int(respuesta_est) 
        if respuesta_est == 1:
            matriz_legajos_notas_act = agregar_materias (matriz_legajos_notas, legajo) #Agrega las materias que quiere, y le pone una nota aleatoria.
            matriz_legajos_notas = matriz_legajos_notas_act
                
        if respuesta_est == 2:
            if matriz_legajos_notas == {}:
                print("\nNo está cargada ninguna nota")   
            else:
                mostrar_notas(matriz_legajos_notas, legajo)
        
        elif respuesta_est == 3:
            print("Volviendo al menú principal.") #Vuelve al menú principal.
            return (False, matriz_legajos_notas)
                    
        elif respuesta_est == 4:
            print("Saliendo de la aplicación") #Sale de la aplicación.
            return (True, matriz_legajos_notas)