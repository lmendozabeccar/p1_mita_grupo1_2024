from MATRICES.matriz_calificaciones import llenar_matriz, encabezado_calificaciones
from VALIDACIONES.Validaciones import validar_num
from CRUDS.crudEstudiantes import ver_calificacion, ver_materias
def estudiantes(posicion):
    alumnos_calificaciones = llenar_matriz(encabezado_calificaciones)
    legajo = alumnos_calificaciones[posicion+1][0]
    flag_estudiantes = True
    while flag_estudiantes == True:
        print("*"*26)
        respuesta_est = input("1 Ver tus calificaciones y el promedio\n2 Ver promedio por materia\n3 Finalizar\nIngrese el numero para la operación que desee: ")
        #Se desea que sea una cadena para luego poder verificar si es un número
        while validar_num(respuesta_est) == False:
            print("*"*26)
            respuesta_est = input("1 Ver tus calificaciones y el promedio\n2 Ver promedio por materia\n3 Finalizar\nIngrese el numero para la operación que desee: ")
        respuesta_est = int(respuesta_est) 
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