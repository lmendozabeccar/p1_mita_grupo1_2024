from VALIDACIONES.Validaciones import validacion_dig, validacionmail, validar_contraseña, validar_mayus_nombre, validacion_cuenta_existente

def registro():
    """
    pre: el usuario en el menú de inicio, ingreso la opción 2 y fue redirigido a este menú, el menú de registro.
    pos: retorna True en caso de que el registro sea correcto y válido, en caso contrario, retorna False. 
    """
    
    
    menu_registro = "\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "
    menu_mail = "\nIngresar su mail de usuario nuevo: "
    menu_nombre = "Ingresar su nombre y apellido, ambas comenzando con mayúsculas: "
    menu_contraseña = "Ingrese su contraseña: "
    menu_error = "\n1 Volver a intentar el registro. \n2 Volver al inicio \nElija un número: "
    try:
        with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", mode="a", encoding="utf-8") as archivo:
            flag = True
            while flag:
                inicio_registro=(input(menu_registro)) #Modularizacion menú.
                while validacion_dig (inicio_registro, 3) == False: #Valida que el numero sea entre 1 y 3
                    inicio_registro=(input(menu_registro))  
                        
                if int(inicio_registro) == 3: #Vuelve al menú de inicio.
                    return -1
                else:
                
                    #Validación Mail.
                    user=str(input(menu_mail)) #Modularización de menú
                    while validacionmail(user) == False: #Validacion que el mail tenga las pautas necesarias.
                        user=str(input(menu_mail))   
                    
                    legajo, respuesta = validacion_cuenta_existente(user, False)            
                    if respuesta == True: #Valida si la cuenta ya existe. Se le pasa como contraseña False para diferenciarlo del login y poder usar la misma funcion
                        if int (inicio_registro)==1: #Si se registra como alumno
                            nom=str(input(menu_nombre))
                            while validar_mayus_nombre(nom) == False: #Valida que el nombre y el apellido comience con mayuscula.
                                nom=str(input(menu_nombre))           
                            pas=str(input(menu_contraseña))        
                            while validar_contraseña (pas) == False: #Valida que la contraseña tenga, al menos, una mayuscula, una minuscula y un numero, sin espacios en blanco.
                                pas=str(input(menu_contraseña))       

                            legajo = int(legajo)
                            legajo+=1 #Legajo = ultimo legajo + 1
                            archivo.write(f"{legajo};{user};{pas};{nom}\n") #Append en el archivo de texto.
                            print("\nRegistro exitoso como alumno, ahora inicie sesión")
                            flag = False                 
                                
                        if int (inicio_registro)==2: #Si se registra como profesor
                            nom=str(input(menu_nombre))
                            while validar_mayus_nombre(nom) == False: #Valida que el nombre y el apellido comience con mayuscula.
                                nom=str(input(menu_nombre)) 
                                
                            pas=str(input(menu_contraseña))
                            while validar_contraseña (pas) == False: #Valida que la contraseña tenga, al menos, una mayuscula, una minuscula y un numero, sin espacios en blanco.
                                pas=str(input(menu_contraseña))         
                                                
                            archivo.write(f"0000;{user};{pas};{nom}\n")
                            print("\nRegistro exitoso como profesor, ahora inicie sesión")
                            flag = False                
                                    
                    else: #En caso de usuario ya existente.
                        inicio_usuario_exist=(input(menu_error))
                        while validacion_dig (inicio_usuario_exist, 2) == False: #Validacion que sea un numero entre 1 y 2.
                            inicio_usuario_exist=(input(menu_error))

                        if int(inicio_usuario_exist) == 2: #Vuelve al menú de inicio, en caso de elegir la opción 2.
                            return False       
    except:
        print("\nHubo un error en el registro, inténtelo de vuelta en unos minutos...")
        return False
    return True