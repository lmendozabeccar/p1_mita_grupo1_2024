try:
    archivo = open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt","r")
except:
    print("No se pudo abrir el archivo.")
else:
    lineas=archivo.readlines()
    for linea in lineas:
        lindividual = linea.strip().split(';')
        """"""
        recorte_usuarios = [[legajo, mail[:10], contraseña[:10], nombre[:15]] for legajo, mail, contraseña, nombre in lindividual]
        orden_usuarios = sorted(recorte_usuarios, key=lambda x: (x[3], -int(x[0])))

    # Asignación para poder mostrar las listas con encabezados.
    username = "Username"
    passw = "Password"
    nombre = "Nombre"
    legajo = "Legajo"


    # Imprimir la lista con formato de f-strings
    print()
    print("Lista de usuarios ya registrados en el sistema, ordenados en forma alfábetica por su nombre.")
    print("En caso de coincidir nombre de algún alumno, se muestra ordenado por legajo descendente.")
    print(f"|{legajo:^10}||{username:^10}||{passw:^10}||{nombre:^15}|")  # Mostrar encabezados, con restricciones.
    print("*" * 53)
    for legajo, mail, contraseña, nombre in orden_usuarios:
        print(f"|{legajo:^10}||{mail:^10}||{contraseña:^10}||{nombre:^15}|")  # Mostrar información, con restricciones.