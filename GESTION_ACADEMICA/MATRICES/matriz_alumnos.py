ingreso_alumnos = [   #Lista de alumnos ya ingresados.
    ["1000","nicovera@sistem.edu.ar","nicovera01","Vera Alejandro", [],[]],
    ["1001","tomiweins@sistem.edu.ar","tomiweins01","Weinstelbaum Tomás", [],[]],
    ["1002","santimatra@sistem.edu.ar","santimatra01","Matra Santino", [],[]],
    ["1003","lucasmendo@sistem.edu.ar","lucasmendo01","Mendoza Lucas", [],[]],
    ["1004","silvifalcon@sistem.edu.ar","silvifalcon01","Falcón Silvina", [],[]],
    ["1005","alevera@sistem.edu.ar","alevera01","Vera Alejandro", [],[]],
    ["1006","malecristaldi@sistem.edu.ar","malecristaldi01","Cristaldi Malena", [],[]],
    ["1007","lucaspagli@sistem.edu.ar","lucaspagli01","Paglilla Lucas", [],[]],
    ["1008","fabrisuccar@sistem.edu.ar","fabrisuccar01","Succar Fabricio", [],[]],
    ["1009","lautipadin@sistem.edu.ar","lautipadin01","Padin Lautaro", [],[]]
                                ]
"""
#Se recortan los nombres de los productos a un máximo de 8 caracteres.
estudiantes_recortados = [[legajo[:6], mail[:10], contraseña[:10], nombre[:15], materias [:16]] for legajo, mail, contraseña,nombre, materias in ingreso_alumnos]

#Asignación para poder mostrar las listas con encabezados.
username = "Username"
passw = "Password"
nombre = "Nombre"
legajo = "Legajo"
materias = "Materias"
# Lista ordenada por nombre (alfabeticamente) y luego por legajo (ascendente).
estudiantes_ordenados = sorted(estudiantes_recortados, key=lambda x: (x[3], int(x[0])))

# Imprimir la lista con formato de f-strings
print("Lista de alumnos ya registrados en el sistema.")
print(f"|{legajo:^10}||{username:^10}||{passw:^10}||{nombre:^15}||{materias:^10}|") #Mostrar encabezados, con reestricciones.
print("*" * 53)
for legajo, mail, contraseña, nombre, materias in estudiantes_ordenados:
    print(f"|{legajo:^10}||{mail:^10}||{contraseña:^10}||{nombre:^15}||{str(materias):^10}|") #Mostrar información, con reestricciones.
print()"""