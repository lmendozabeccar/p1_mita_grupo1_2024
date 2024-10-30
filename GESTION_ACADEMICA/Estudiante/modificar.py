from VALIDACIONES.Validaciones import validacionmail, validar_mayus_nombre, validar_contraseña
def modificaruser():
    while True:
        try:
            with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", "r", encoding="UTF-8" ) as archivo:
                linea = archivo.readlines()
                
        except (FileNotFoundError, TypeError):
            print("No se pudo abrir el archivo")
            return
            
        else:
            legajo = input("Ingrese su legajo: ").strip()
            legajo_encontrado = False  
            for i in range(len(linea)):
                parte = linea[i].strip().split(";")
                if parte[0] == legajo:
                    modificar = int(input("¿Que desea modificar?\n1.Email\n2.Contraseña\n3.Nombre y Apellido\n4Todo\nModificar: "))
                    if modificar == 1 or modificar == 4:
                        email = input("Ingrese su email nuevo: ")
                        if validacionmail(email) == False:
                            email = input("Ingrese su email nuevo: ")
                        parte[1] = email
                    elif modificar == 2 or modificar ==4:
                        contraseña=input("Ingrese su contraseña nueva: ")
                        if validar_contraseña(contraseña) == False:
                            contraseña=input("Ingrese su contraseña nueva: ")
                        parte[2] = contraseña
                    elif modificar == 3 or modificar == 4:
                        nom = input("Ingrese su nuevo apellido y su nuevo nombre: ")
                        if validar_mayus_nombre(nom) == False:
                            nom = input("Ingrese su nuevo apellido y su nuevo nombre: ")
                        parte[3] = nom
                    partecompleta = parte[0] + ";" + parte[1] + ";" + parte[2] + ";" + parte[3]
                    linea[i] = partecompleta + '\n'
                    legajo_encontrado = True
                    break
            if legajo_encontrado:
                with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", "w", encoding="UTF-8") as archi:
                    archi.writelines(linea)
                    print("Modificacion Aceptada")
            else:
                print("Legajo no encontrado")
            otravez = input("¿Quiere modificar algo más?\n1. Sí\n2. No\n").strip()
            if otravez != "1":
                break   
    