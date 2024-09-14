from random import randint

# Función lambda para generar calificaciones aleatorias
aleatorio = lambda: randint(1, 10)

# Diccionario de materias
materias_dic = {
    "1": "algebra",
    "2": "sistemas",
    "3": "desarrollo",
    "4": "ingles",
    "5": "programacion"
}
"""
# Diccionario de estudiantes
estudiantes = {
    1: {
        'nombre': "Lucas",
        'apellido': "info",
        "lugar": "buenos aires",
        "materias": []
    },
    2: {
        'nombre': "Elian",
        'apellido': "pep",
        "lugar": "buenos aires",
        "materias": []
    }
}

"""
ingreso_alumnos = [   #Lista de alumnos ya ingresados.
    ["1000","nicovera@sistem.edu.ar","nicovera01","Vera Alejandro", []],
    ["1001","tomiweins@sistem.edu.ar","tomiweins01","Weinstelbaum Tomás", []],
    ["1002","santimatra@sistem.edu.ar","santimatra01","Matra Santino", []],
    ["1003","lucasmendo@sistem.edu.ar","lucasmendo01","Mendoza Lucas", []],
    ["1004","silvifalcon@sistem.edu.ar","silvifalcon01","Falcón Silvina", []],
    ["1005","alevera@sistem.edu.ar","alevera01","Vera Alejandro", []],
    ["1006","malecristaldi@sistem.edu.ar","malecristaldi01","Cristaldi Malena", []],
    ["1007","lucaspagli@sistem.edu.ar","lucaspagli01","Paglilla Lucas", []],
    ["1008","fabrisuccar@sistem.edu.ar","fabrisuccar01","Succar Fabricio", []],
    ["1009","lautipadin@sistem.edu.ar","lautipadin01","Padin Lautaro", []]
                                ]

# Inicialización de la lista de materias de estudiantes


for estudiantes_materias in ingreso_alumnos:
    print(estudiantes_materias)


flag = 0
while flag == 0:
    materia = input("Ingrese qué materia desea cursar: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion\n")
    # Obtener el nombre de la materia desde el mapeo
    materia_nombre = materias_dic.get(materia)
    
    if materia_nombre != None:
        # Agregar la calificación de la materia seleccionada al estudiante 1
        calificacion = aleatorio()
        estudiantes_materias[0].append(calificacion)

        ingreso_alumnos[0][4].append(materia_nombre)

        print(f"Materia {materia_nombre} con calificación {calificacion} agregada.")
    else:
        print("Opción no válida. Por favor ingrese un número entre 1 y 5.")
    
    # Preguntar si el usuario desea agregar otra materia
    continuar = input("¿Desea agregar otra materia? (s/n): ")
    if continuar.lower() != 's':
        flag = 1

print("Materias del estudiante con calificaciones:", estudiantes_materias)
print(ingreso_alumnos[0])

#Se recortan los nombres de los productos a un máximo de 8 caracteres.
estudiantes_recortados = [[legajo[:6], mail[:10], contraseña[:10], nombre[:15]] for legajo, mail, contraseña,nombre in ingreso_alumnos]

#Asignación para poder mostrar las listas con encabezados.
username = "Username"
passw = "Password"
nombre = "Nombre"
legajo = "Legajo"
# Lista ordenada por nombre (alfabeticamente) y luego por legajo (ascendente).
estudiantes_ordenados = sorted(estudiantes_recortados, key=lambda x: (x[3], int(x[0])))

# Imprimir la lista con formato de f-strings
print("Lista de alumnos ya registrados en el sistema.")
print(f"|{legajo:^10}||{username:^10}||{passw:^10}||{nombre:^15}|") #Mostrar encabezados, con reestricciones.
print("*" * 53)
for legajo, mail, contraseña, nombre in estudiantes_ordenados:
    print(f"|{legajo:^10}||{mail:^10}||{contraseña:^10}||{nombre:^15}|") #Mostrar información, con reestricciones.
print()