from MATRICES.matriz_calificaciones import llenar_matriz, encabezado_calificaciones
from CRUDS.crudProfesores import agregar_alumno, mostrar_calificacion, actualizar_alumno, eliminar_alumno
from VALIDACIONES.Validaciones import validar_num
def profesores():
    alumnos_calificaciones = llenar_matriz(encabezado_calificaciones)
    flag_profes = True
    while flag_profes == True:
        print("-"*26)
        respuesta_prof = input("1 Agregar alumno\n2 Mostrar calificaciones\n3 Modificar alumno\n4 Eliminar alumno\n5 Finalizar\nIngrese el numero para la operación que desee: ")
        while validar_num(respuesta_prof) == False:
            print("*"*26)
            respuesta_prof = input("1 Agregar alumno\n2 Mostrar calificaciones\n3 Modificar alumno\n4 Eliminar alumno\n5 Finalizar\nIngrese el numero para la operación que desee: ")
        respuesta_prof = int(respuesta_prof)
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