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
            print("Email no encontrado.")
    except:
        print("Hubo un error al eliminar tu cuenta, inténtelo de vuelta en unos minutos...")
        return False
    else:
        print("Cuenta eliminada con éxito.")
        return True