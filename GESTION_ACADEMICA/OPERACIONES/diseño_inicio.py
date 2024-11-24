def mostrar_usuarios ():
    """
    pre: no recibe ningun dato la función.
    pos: se encarga de mostrar los datos de los usuarios cuando inicia el programa, ya sean profesores o alumnos.
    """
    archivo_path = r'GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt'

    # Lista para almacenar cada usuario como una sublista
    usuarios = []

    # Abre el archivo y lee línea por línea
    try:
        with open(archivo_path, 'r', encoding="UTF-8") as archivo:
            while True:
                linea = archivo.readline()  # Lee una línea del archivo
                if not linea:  # Si la línea está vacía, se alcanzó el final del archivo. La linea vacía se considera falso, por eso el "not"
                    break

                elementos = linea.strip().split(';')
                
                legajo, email, contraseña, nombre = elementos
                usuarios.append([legajo, email, contraseña, nombre])
    except (IndexError, ValueError, FileNotFoundError, PermissionError):
        print("\nNo se ha podido cargar el archivo.")
    else:
    # Ordena por nombre, y luego x legajo.
        usuarios_ordenados = sorted(usuarios, key=lambda x: (x[3], x[0])) #Sorted recibe una matriz, y lo ordena segun el lambda, que en este caso, ordena por nombre y luego por legajo.
        
        print("\nLista de usuarios, con su respectivo legajo, mail, contraseña y nombre.")
        # Imprime los encabezados
        print(f"|{'Legajo':^6}||{'Mail':^30}||{'Constraseña':^15}||{'Nombre':^20}|")

        # Línea separadora
        print("-" * 78)

        # Imprime los usuarios ordenados
        for usuario in usuarios_ordenados:
            legajo, email, contraseña, nombre = usuario
            print(f"|{legajo:^6}||{email:^30}||{contraseña:^15}||{nombre:^20}|")