from crud_promedios import encabezado_calificaciones, aleatorio, seguir, posicion, mostrar_calificacion, promedio_materia, llenar_matriz, ingreso_notas, agregar_alumno, actualizar_alumno, eliminar_alumno, ver_calificacion, ver_materias
def profesores():
    alumnos_calificaciones = llenar_matriz(encabezado_calificaciones)
    flag_profes = True
    while flag_profes == True:
        print("-"*26)
        respuesta_prof = int(input("1 Agregar alumno\n2 Mostrar calificaciones\n3 Modificar alumno\n4 Eliminar alumno\n5 Finalizar\nIngrese el numero para la operación que desee: "))
        if respuesta_prof == 1:
            alumnos_calificaciones = agregar_alumno(alumnos_calificaciones)
        elif respuesta_prof == 2:
            print(mostrar_calificacion(alumnos_calificaciones))
        elif respuesta_prof == 3:
            alumnos_calificaciones = actualizar_alumno(alumnos_calificaciones)
        elif respuesta_prof == 4:
            alumnos_calificaciones = eliminar_alumno(alumnos_calificaciones)
        elif respuesta_prof == 5:
            flag_profes = False
            print("Saliendo..")

def estudiantes(posicion):
    alumnos_calificaciones = llenar_matriz(encabezado_calificaciones)
    legajo = alumnos_calificaciones[posicion+1][0]
    flag_estudiantes = True
    while flag_estudiantes == True:
        respuesta_est = int(input("1 Ver tus calificaciones y el promedio\n2 Ver promedio por materia\n3 Finalizar\nIngrese el numero para la operación que desee: "))
        if respuesta_est == 1:
            ver_calificacion(legajo, alumnos_calificaciones)
        elif respuesta_est == 2:
            ver_materias(alumnos_calificaciones)
        elif respuesta_est == 3:
            flag_estudiantes = False
            print("Saliendo..")
#estudiantes()
#Utilizar diccionarios para gestionar la información del alumno, tal como el nombre, apellido, carrera, email y otros datos
####Funcion exclusiva para verificar variable un una lista
