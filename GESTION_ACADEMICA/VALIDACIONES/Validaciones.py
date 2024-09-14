import re
#Verificar mayúsculas correspondientes a la hora de ingresar nombre (registro). 
def validar_mayus_nombre (nombre):
    if re.findall ("[0-9]+",nombre) != []:
        print("Por favor, no ingresar números en su nombre y apellido.") 
        return False
    if re.findall ("^[A-Z][a-z]*\\s[A-Z][a-z]*$",nombre) == []:
        print("Ingresar mayúsculas al comienzo del nombre y del apellido.")
        return False
#Verificar que la contraseña cumpla con requisitos. 
def validar_contraseña (contra):
    if len(contra)<8:
        print("Contraseña inválida, por favor ingresar al menos 8 caracteres.")
        return False
    if re.findall ("\\s",contra) != []:
        print("Por favor, no ingresar espacios en blanco a la hora de ingresar su contraseña.")
        return False        
    if re.findall ("[A-Z]+[a-z]+[0-9]+",contra) == []:
        print("Su contraseña no pudo ser validada. Por favor ingresar al menos una mayúscula, una minúscula y un número.)")
        return False
    return True
#Validacion letras.
def validar_num (car):    
    if car.isnumeric()==False:
        print()
        print("Por favor, ingresar un número.")
    return car.isnumeric()
#Validacion de que los numeros esten bien.
def validacion_2dig (texto):                 
    patron = "[1-2]{1}"
    while re.match(patron,texto) == None:
        print("Por favor, ingresar un numero válido.")
        return False
def validacion_3dig (texto):                 
    patron = "[1-3]{1}"
    while re.match(patron,texto) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False
def  validacion_5dig (texto):
    patron = "[1-5]{1}"
    while re.match(patron,texto) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False
        
#Validación del Mail.
def validacionmail (mail):
    patron = "[a-zA-Z0-9]+@[sistem]+\.[edu]+\.[ar]"
    busqarr = re.findall (patron, mail)
    if busqarr == []:
        print("Ingresar @sistem.edu.ar junto con el nombre de usuario.")
        return False
#Verificar si la cuenta existe o no en el sistema
def cuenta_existente_login (list_alumnos,list_profesores,user,contraseña):
    i=0
    a=0
    while i<len(list_alumnos):
        if user==list_alumnos[i][1] and contraseña==list_alumnos[i][2]: 
            print("Ingreso correcto al apartado alumnos.")
            return 1,i
        i+=1
    j = 0
    while j<len(list_profesores):
        if user==list_profesores[j][0] and contraseña==list_profesores[j][1]:
            print("Ingreso correcto al apartado profesores.")
            return 2,j
        j += 1
    return 3,a
#Verificar si existe un USUARIO registrado anteriormente.
def cuenta_existente_register (listaalumnos,listaprofes,usuario):
    i,j=0,0    
    while i<len(listaalumnos):
        if usuario==listaalumnos[i][0]: 
            print("Usuario ya existente.")
            return False
        i += 1
    while j<len(listaprofes):
        if  usuario==listaprofes[j][0]:
            print("Usuario ya existente.")
            return False
        j += 1    
#Si se sigue o no con las opciones.    
def seguir_texto (text):
    patron = "[1-2]{1}"
    while re.match(patron,text) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False

#Que las notas sean, entre 1 y 10, y que puedan tener como maximo 1 decimal.
def validacion_notas(x, b, c, d, e):
    pattern = "^(10|[0-9](\.\d{1})?)$"
    for nota in [x, b, c, d, e]:
        if not re.match(pattern, str(nota)):
            return False  # Si alguna nota no es válida, retornamos False.
    