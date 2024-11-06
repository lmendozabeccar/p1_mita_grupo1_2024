from VALIDACIONES.Validaciones import validacionmail, validar_mayus_nombre, validar_contraseña
def modificaruser():
    """
    pre: no recibe ningun dato, viene desde el apartado de estudiantes a la hora de solicitar modificar su usuario.
    pos: una vez modificados todos los datos (y validados), escribe en el archivo de texto los nuevos cambios.
    """
    while True:
        try:
            with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", "r", encoding="UTF-8" ) as archivo:
                linea = archivo.readlines()       
        except (FileNotFoundError, TypeError):
            print("\nNo se pudo abrir el archivo")
            return
            
        else:
            legajo = input("\nIngrese su legajo: ").strip()
            legajo_encontrado = False  
            for i in range(len(linea)):
                parte = linea[i].strip().split(";")
                if parte[0] == legajo:
                    modificar = int(input("\n¿Que desea modificar?\n1.Email\n2.Contraseña\n3.Nombre y Apellido\n4Todo\nModificar: "))
                    if modificar == 1 or modificar == 4:
                        email = input("\nIngrese su email nuevo: ")
                        if validacionmail(email) == False:
                            email = input("\nIngrese su email nuevo: ")
                        parte[1] = email

                    elif modificar == 2 or modificar ==4:
                        contraseña=input("\nIngrese su contraseña nueva: ")
                        if validar_contraseña(contraseña) == False:
                            contraseña=input("\nIngrese su contraseña nueva: ")
                        parte[2] = contraseña

                    elif modificar == 3 or modificar == 4:
                        nom = input("\nIngrese su nuevo apellido y su nuevo nombre: ")
                        if validar_mayus_nombre(nom) == False:
                            nom = input("\nIngrese su nuevo apellido y su nuevo nombre: ")
                        parte[3] = nom

                    partecompleta = f"{parte[0]};{parte[1]};{parte[2]};{parte[3]}"
                    linea[i] = partecompleta + '\n'
                    legajo_encontrado = True
                    break
            if legajo_encontrado:
                with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", "w", encoding="UTF-8") as archi:
                    archi.writelines(linea)
                    print("\nModificacion Aceptada")
            else:
                print("\nLegajo no encontrado")
            otravez = input("\n¿Quiere modificar algo más?\n1. Sí\n2. No\n").strip()
            if otravez != "1":
                break   
    