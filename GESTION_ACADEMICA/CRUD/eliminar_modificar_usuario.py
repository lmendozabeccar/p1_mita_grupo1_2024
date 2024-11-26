from VALIDACIONES.Validaciones import validacion_dig, validacionmail, validar_mayus_nombre, validar_contraseña

def eliminar_mail(email):
    """
    pre: recibe el mail de usuario que se quiere eliminar.
    pos: retorna True en caso de que se elimine la cuenta con éxito.
         retorna False en caso que no se pueda eliminar por algún motivo.
    """
    # Abrimos el archivo en modo lectura
    try:
        with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", 'r', encoding="UTF-8") as archivo_lectura:
            lineas = archivo_lectura.readlines()
        
        #Filtracion de lineas sin el correo
        lineas_actualizadas = [linea for linea in lineas if email not in linea] 

        # Reescritura del archivo sin el email que se desea eliminar
        with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", 'w', encoding="UTF-8") as archivo_escritura:
            for linea in lineas_actualizadas:
                archivo_escritura.write(linea)
        if len(lineas) == len(lineas_actualizadas):
            print("\nEmail no encontrado.")
    except  (FileNotFoundError, TypeError, PermissionError):
        print("\nHubo un error al eliminar tu cuenta, inténtelo de vuelta en unos minutos...")
        return False
    else:
        print("\nCuenta eliminada con éxito.")
        return True
    
def modificaruser(mai):
    """
    pre: recibe el mail perteneciente al usuario que quiera modificar sus datos.
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
            menu_mail = "\nIngrese su email nuevo: "
            menu_contraseña = "Ingrese su contraseña nueva: "
            menu_nombre = "Ingrese su nuevo apellido y su nuevo nombre: "
            legajo_encontrado = False  
            for i in range(len(linea)): #Recorre la lista de lineas
                parte = linea[i].strip().split(";") 
                if parte[1] == mai:
                    modificar = (input("\n¿Que desea modificar?\n1.Email\n2.Contraseña\n3.Nombre y Apellido\n4.Todo\nElegir una opción: "))
                    while validacion_dig (modificar,4) == False:
                        modificar = (input("\n¿Que desea modificar?\n1.Email\n2.Contraseña\n3.Nombre y Apellido\n4.Todo\nElegir una opción: "))

                    if modificar == "1":
                        email = input(menu_mail)
                        if validacionmail(email) == False:
                            email = input(menu_mail)
                        parte[1] = email

                    elif modificar == "2":
                        contraseña=input(menu_contraseña)
                        if validar_contraseña(contraseña) == False:
                            contraseña=input(menu_contraseña)
                        parte[2] = contraseña

                    elif modificar == "3":
                        nom = input(menu_nombre)
                        if validar_mayus_nombre(nom) == False:
                            nom = input(menu_nombre)
                        parte[3] = nom
                    else:
                        email = input(menu_mail)
                        if validacionmail(email) == False:
                            email = input(menu_mail)
                        parte[1] = email
                        
                        contraseña=input(menu_contraseña)
                        if validar_contraseña(contraseña) == False:
                            contraseña=input(menu_contraseña)
                        parte[2] = contraseña
                        
                        nom = input(menu_nombre)
                        if validar_mayus_nombre(nom) == False:
                            nom = input(menu_nombre)
                        parte[3] = nom
                        
                    partecompleta = f"{parte[0]};{parte[1]};{parte[2]};{parte[3]}"
                    linea[i] = partecompleta + '\n'
                    legajo_encontrado = True
                    break
            if legajo_encontrado:
                try:
                    with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", "w", encoding="UTF-8") as archi:
                        archi.writelines(linea)
                        print("\nModificacion Aceptada")
                except (FileNotFoundError, TypeError, PermissionError):
                    print("\nNo se pudo modificar el archivo ya que éste no se pudo abrir")
            else:
                print("\nLegajo no encontrado")
            otravez = input("¿Quiere modificar algo más?\n1. Sí\n2. No\nElegir una opción: ").strip()
            while validacion_dig(otravez,2) == False:
                otravez = input("¿Quiere modificar algo más?\n1. Sí\n2. No\nElegir una opción: ").strip()
                
            if otravez != "1":
                print("\nVolviendo al menú principal...")
                break   
    