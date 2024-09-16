from VALIDACIONES.Validaciones import validar_num, validacion_4dig
from CRUDS.crudEstudiantes import ver_calificacion_nuevo
from MATRICES.matriz_calificaciones import matriz_notas
from MATRICES.Diccionario_Materias import agregar_materias

def estudiantes(pos):    
    flag_estudiantes = True
    menu="\nQué desea realizar ahora? \n1 Inscribirse en las materias correspondientes.\n2 Ver sus calificaciones y su promedio\n3 Volver al menú principal. \n4 Salir de la aplicación.  \nIngrese el numero para la operación que desee: "
    while flag_estudiantes == True:      
        respuesta_est = input(menu) #Menú modularizado.
        while validar_num(respuesta_est) == False: #Validacion numero
            respuesta_est = input(menu)
        while validacion_4dig (respuesta_est)== False: #Validacion numero entre 1 y 4 
            respuesta_est = input(menu)
            while validar_num(respuesta_est) == False:
                respuesta_est = input(menu)
        
        respuesta_est = int(respuesta_est) 
        if respuesta_est == 1:
            print()
            agregar_materias (pos) #Agrega las materias que quiere, y le pone una nota aleatoria.
                
        if respuesta_est == 2:
            print()
            ver_calificacion_nuevo (pos, matriz_notas) #Ve sus respectivas notas, 
        
        elif respuesta_est == 3:
            print("Volviendo al menú principal.") #Vuelve al menú principal.
            return False
                    
        elif respuesta_est == 4:
            print("Saliendo de la aplicación") #Sale de la aplicación.
            return True