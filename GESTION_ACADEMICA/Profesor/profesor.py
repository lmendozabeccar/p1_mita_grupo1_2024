from CRUDS.crudProfesores import  *
from VALIDACIONES.Validaciones import validacion_6dig

def profesores(matriz_alumnos, matriz_legajos_notas):
    flag_profes = True
    matriz_notas_actualizadas = []
    matriz_alumnos_actualizados = []
    menu_profesor="Qué desea realizar? \n1 Mostrar calificación individual. \n2 Mostrar calificación de todos los alumnos inscriptos.\n3 Agregar/Actualizar notas. \n4 Eliminar alumno. \n5 Volver al menú principal. \n6 Salir de la aplicación.\nIngrese el numero para la operación que desee: "
    while flag_profes == True:
        print()
        respuesta_prof = input(menu_profesor) #Modularizacion de menu.
        while validacion_6dig (respuesta_prof)== False: #Valida que el numero sea entre 1 y 6
            respuesta_prof = input(menu_profesor)
        respuesta_prof = int(respuesta_prof)
        
        if matriz_notas_actualizadas != []: #Si la matriz_notas_actualizadas fue actualizada, entonces se le asigna a la matriz_legajos_notas
            matriz_legajos_notas = matriz_notas_actualizadas

        if matriz_alumnos_actualizados != []: #Si la matriz_alumnos_actualizados fue actualizada, entonces se le asigna a la matriz_alumnos
            matriz_alumnos = matriz_alumnos_actualizados
            
        if respuesta_prof == 1:
            if matriz_legajos_notas == {}:
                print("\nNo hay ninguna nota cargada")
            else:
                mostrar_calificacion_individual(matriz_legajos_notas) #Muestra calificación por alumno, preguntando su legajo.

        elif respuesta_prof == 2:
            if matriz_legajos_notas == {}:
                print("\nNo hay ninguna nota cargada")
            else:
                mostrar_calificacion_grupal (matriz_legajos_notas) #Muestra calificacion de todos los alumnos.
 
        elif respuesta_prof == 3:
            if matriz_legajos_notas == {}:
                print("\nNo hay ninguna nota cargada")
            else:
                matriz_notas_actualizadas = actualizar_notas_alumno (matriz_legajos_notas) #Puede cambiar las notas de un alumno YA EXISTENTE. Devuelve la matriz actualizada.
            
        elif respuesta_prof == 4:
            matriz_alumnos_actualizados, matriz_notas_actualizadas = eliminar_alumno (matriz_alumnos, matriz_legajos_notas) #Elimina alumnos y devuelve la matriz actualizada. 
 
        elif respuesta_prof == 5:
            print("Volviendo al menú principal.") #Vuelve al menú
            return matriz_alumnos, matriz_legajos_notas

        elif respuesta_prof == 6:
            print("Saliendo..") #Sale de la aplicación.
            return (True, True)
            