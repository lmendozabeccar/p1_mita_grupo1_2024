import re
#Verificar mayúsculas correspondientes a la hora de ingresar nombre (registro). 
def validar_mayus_nombre (nombre):
    
    """
    pre: recibe un nombre y un apellido, ingresado por el usuario a la hora del registro.
    pos: devuelve False, en caso de que existan números o en caso de que el nombre/apellido no comiencen con 
    mayúscula. En caso de devolver False, se piden nuevamente los datos.
    """
    
    busq = re.findall ("[0-9]+",nombre) 
    if len(busq) != 0:
        print("\nPor favor, no ingresar números en su nombre y apellido.\n") 
        return False
    busq2 = re.findall ("^[A-Z][a-z]*\\s[A-Z][a-z]*$",nombre)
    if len(busq2) == 0:
        print("\nIngresar mayúsculas al comienzo del nombre y del apellido.\n")
        return False
    
#Verificar que la contraseña cumpla con requisitos. 
def validar_contraseña (contra):
    
    """
    pre: recibe la contraseña nueva, ingresada por el usuario a la hora del registro.
    pos: devuelve False, en caso de que no cumpla con los requisitos (8 caracteres, sin espacios en blanco, al 
    menos una mayúscula, una minúscula y un número). En caso de devolver False, se piden nuevamente los datos.
    """
    
    if len(contra)<8: #Minimo ocho caracteres
        print("\nContraseña inválida, por favor ingresar al menos 8 caracteres.\n")
        return False
    busq = re.findall ("\\s",contra)
    if len(busq) != 0: #Que no haya espacios en blanco
        print("\nPor favor, no ingresar espacios en blanco a la hora de ingresar su contraseña.\n")
        return False        
    busq2 = re.findall ("[A-Z]+[a-z]+[0-9]+",contra)
    if len(busq2) == 0: #Contraseña segura
        print("\nSu contraseña no pudo ser validada. Por favor ingresar al menos una mayúscula, una minúscula y un número.\n")
        return False
    return True

#Validacion letras.
def validar_num (car):    
    """
    pre: recibe un legajo.
    pos: retorna False, en caso de que existan letras en la cadena, retorna True, en caso de que no existan letras
    en el legajo.
    """
    
    if car.isnumeric()==False: #Si la cadena tiene numeros, devuelve True
        print("\nPor favor, ingresar un número.\n")
    return car.isnumeric()

def validacion_dig(texto, numero_opciones):
    
    """
    pre: recibe la respuesta del uusario a la hora que le pregunta cual de todas las opciones del menú quiere 
    utilizar como primer parámetro, y como segundo parámetro la cantidad de opciones que puede elegir.
    pos: la funcion retorna True, en caso de que el usuario haya ingresado un número válido, y retorna 
    False, en caso que no lo sea.
    """

    if numero_opciones <= 9:
        patron = f"^[1-{numero_opciones}]$"  # Tiene que empezar y terminar con 1 dígito
    else:
        patron = f"^([1-9]|1[0-{numero_opciones % 10}])$"  # Maneja opciones de 1 a 19
    while re.match(patron, texto) is None:
        print("\nPor favor, ingresar un número válido.\n")
        return False
    return True
    
#Validación del Mail.
def validacionmail (mail):
    
    """
    pre: recibe un mail ingresado por el usuario.
    pos: retorna False en caso de que no se cumplan con los requisitos pedidos (minimo de tres caracteres 
    antes del "@", además de su respectiva forma) y vuelve a solicitar el ingreso del mail. En caso de cumplir 
    con los requisitos, retorna True.
    """

    patron = r"[a-zA-Z0-9]{3,}@sistem+\.edu+\.ar" # R String --> Para que tome las secuencias de escape bien (Daba un warning)
    busq = re.findall (patron, mail)
    if len(busq) == 0:
        print('\nIngresar @sistem.edu.ar junto con el nombre de usuario, con un mínimo de tres caracteres antes del "@"\n')
        return False
    else:
        return True
#Verificar si la cuenta existe o no en el sistema
def validacion_cuenta_existente (user,contraseña):
    
    """
    pre: recibe un mail de usuario y una contraseña (en caso de estar registrandose la contraseña es "False")
    pos: retorna False, en caso de que el usuario se encuentre ya ingresado en el sistema 
    CONTINUAR ##########################################################################################
    """
    with open(r"GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", mode="r", encoding="utf-8") as archivo:
        flag = True
        encontrado = True
        tipo_usuario = 0
        while flag:
            linea = archivo.readline() #linea por linea del archivo de texto
            if linea == "": # EL ARCHIVO DE TEXTO DEBE TENER MAXIMO UNA LINEA VACÍA AL FINAL
                flag = False
                encontrado = False
            else:
                linea = linea.strip() #elimina los espacios en blanco al inicio y al final
                lista = linea.split(";") #divide la línea en una lista de elementos usando ; como delimitador.
                if contraseña == False: #Si se está registrando, es false, si es un login, es la contraseña ingresada x el usuario.
                    if lista[0] != "0000":
                        legajo = lista[0]
                    if lista[1] == user:
                        print("Usuario ya existente, ingrese otro.")
                        return 0, False
                else:
                    if lista[1] == user and lista[2] == contraseña: #Para el login
                        if lista[0] == "0000": #El profesor tiene legajo 0000
                            print("Ingreso correcto al apartado profesores.")
                            tipo_usuario = 2
                            legajo = -1
                            email = lista[1]
                            flag = False
                        else:
                            print("Ingreso correcto al apartado alumnos.")
                            tipo_usuario = 1
                            legajo = lista[0]
                            email = lista[1]
                            flag = False
        if encontrado == False and contraseña != False: #Si el usuario no se encontró en el login
            print("Usuario no encontrado.")
        elif encontrado == False and contraseña == False: #Si el usuario no se encontró en el registro
            return legajo, True
        else: #Si se encontró en el login
            return tipo_usuario, legajo, email

#Validación de nota, entre 0 y 10 y con 
def validar_nota (car):
    """
    pre: la función recibe la nota ingresada por el profesor, a la hora de calificar al alumno.
    pos: en caso de no coincidir con el patrón, devuelve False y le pide al profesor que ingrese una nota 
    válida. En caso de coincidir, no devuelve nada y el programa sigue con normalidad.
    """
    patron = r"^(10(\.0)?|[0-9](\.\d)?)$" # ()? Quiere decir que es opcional que haya un punto y un 0, | es operador OR
    nota_valida= re.match(patron,car)
    if nota_valida == None:
        print("\nNota incorrecta, por favor ingresar una nota válida.\n")
        return False    