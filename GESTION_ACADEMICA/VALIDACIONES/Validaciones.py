import re
#Verificar mayúsculas correspondientes a la hora de ingresar nombre (registro). 
def validar_mayus_nombre (nombre):
    if re.findall ("[0-9]+",nombre) != []:
        print("Por favor, no ingresar números en su nombre y apellido.") 
        return False
    if re.findall ("^[A-Z][a-z]*\\s[A-Z][a-z]*$",nombre) == []:
        print("Ingresar mayúsculas al comienzo del nombre y del apellido.") #####FUNCIONES: En caso de que la cadena cumpla, la función devuelve "None"
        return False
    
#Verificar que la contraseña cumpla con requisitos. 
def validar_contraseña (contra):
    if len(contra)<8: #Minimo ocho caracteres
        print("Contraseña inválida, por favor ingresar al menos 8 caracteres.")
        return False
    if re.findall ("\\s",contra) != []: #Que no haya espacios en blanco
        print("Por favor, no ingresar espacios en blanco a la hora de ingresar su contraseña.")
        return False        
    if re.findall ("[A-Z]+[a-z]+[0-9]+",contra) == []: #Contraseña segura
        print("Su contraseña no pudo ser validada. Por favor ingresar al menos una mayúscula, una minúscula y un número.)")
        return False
    return True

#E.R --> + Va a devolver al secuencia de caracteres.

#Validacion letras.
def validar_num (car):    
    if car.isnumeric()==False: #Si la cadena tiene numeros, devuelve True
        print()
        print("Por favor, ingresar un número.")
    return car.isnumeric()

#Validacion de que los numeros esten bien. Valida que la respuesta sea "1" o "2",etc respectivamente
def validacion_2dig (texto):                  
    patron = "^[1-2]$" #Tiene que empezar y terminar con 1 digito
    while re.match(patron,texto) == None:
        print("Por favor, ingresar un numero válido.")
        return False

def validacion_3dig (texto):                 
    patron = "^[1-3]$"
    while re.match(patron,texto) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False

def validacion_4dig (texto):
    patron = "^[1-4]$"
    while re.match(patron,texto) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False
    
def  validacion_5dig (texto):
    patron = "^[1-5]$"
    while re.match(patron,texto) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False

def validacion_6dig (texto):
    patron = "^[1-6]$"
    while re.match(patron,texto) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False
    
#Validación del Mail.
def validacionmail (mail):
    patron = r"[a-zA-Z0-9]{3,}@sistem+\.edu+\.ar" # R String --> Para que tome las secuencias de escape bien (Daba un warning)
    busqarr = re.findall (patron, mail)
    if busqarr == []:
        print('Ingresar @sistem.edu.ar junto con el nombre de usuario, con un mínimo de tres caracteres antes del "@"')
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
        if usuario==listaalumnos[i][1]: 
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
    patron = "^[1-2]$"
    while re.match(patron,text) == None:
        print()
        print("Por favor, ingresar un numero válido.")
        return False

#Validacion legajo.
def validar_legajo (lista, pos):
    i=0
    posicion_alumno = -1
    while i<len(lista) and posicion_alumno == -1:
        if  int(pos) == lista[i][0]:
            posicion_alumno = i
            return posicion_alumno                
        i += 1
    return posicion_alumno
#R STRING --> PARA QUE PYTHON INTERPRETE LOS CARACTERES DE ESCAPE, COMO \s

def validar_nota (car):
    patron = "^(10(\.0)?|[0-9](\.\d)?)$"
    nota_valida= re.match(patron,car)
    if nota_valida == None:
        print("Nota incorrecta, por favor ingresar una nota válida.")
        return False
    