from MATRICES.matriz_calificaciones import llenar_matriz, encabezado_calificaciones
from CRUDS.crudEstudiantes import ver_calificacion, ver_materias
def estudiantes(posicion):
    alumnos_calificaciones = llenar_matriz(encabezado_calificaciones)
    legajo = alumnos_calificaciones[posicion+1][0]
    flag_estudiantes = True
    while flag_estudiantes == True:
        print()
        respuesta_est = int(input("\n1 Ver tus calificaciones y el promedio\n2 Ver promedio por materia\n3 Finalizar\nIngrese el numero para la operación que desee: "))
        if respuesta_est == 1:
            ver_calificacion(legajo, alumnos_calificaciones)
            inic = int (input("\nQué desea realizar ahora? \n1 Ver promedio por materia. \n2 Volver al menú inicial. \n3 Salir de la aplicación. \nPor favor, elegir una opción: "))
            if inic ==  1:
                ver_materias (alumnos_calificaciones)
   
        elif respuesta_est == 2:
            ver_materias(alumnos_calificaciones)
        elif respuesta_est == 3:
            flag_estudiantes = False
            print("Saliendo..")