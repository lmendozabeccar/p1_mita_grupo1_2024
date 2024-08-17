alumnos_calificaciones = [
    ["    ", "Algebra", "Pensamiento crítico"],
    [1001, 4, 10],
    [1002, 7, 4],
    [1003, 6, 2]
]
#La primera variable de cada lista es el legajo

alumnos_asistencias = [
    ["    ", "2024-08-16"],
    [1001, 1],
    [1002, 1],
    [1003, 1]
]
# Presente = 1, Ausente = 0
def agregar_alumno():
    flag_legajo = 0
    flag_while_1 = 0
    while flag_while_1 == 0: #Esto es solo para verificar si el legajo ya existe
        legajo = int(input("Ingrese el legajo del alumno"))
        for i in range(len(alumnos_calificaciones)):
            for x in range(len(alumnos_calificaciones[i])):
                if alumnos_calificaciones[i][x] == legajo:
                    flag_legajo = 1
    if flag_legajo == 1:
        print("Ese legajo ya existe, ingrese otro de vuelta.")
    else:
        flag_while_1 = 1
    
def main():
    respuesta = input("1 Agregar alumno\n2 Mostrar alumnos\n3 Modificar alumno\n4 Eliminar alumno\nIngrese el numero para la operación que desee: ")
    if respuesta == 1:
        agregar_alumno()
    
main()
#Utilizar diccionarios para gestionar la información del alumno, tal como el nombre, apellido, carrera, email y otros datos