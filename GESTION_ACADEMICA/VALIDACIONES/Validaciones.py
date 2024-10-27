import re
#Verificar mayúsculas correspondientes a la hora de ingresar nombre (registro). 
def validar_mayus_nombre (nombre):
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

#E.R --> + Va a devolver al secuencia de caracteres.

#Validacion letras.
def validar_num (car):    
    if car.isnumeric()==False: #Si la cadena tiene numeros, devuelve True
        print("\nPor favor, ingresar un número.\n")
    return car.isnumeric()

#Validacion de que los numeros esten bien. Valida que la respuesta sea "1" o "2",etc respectivamente
def validacion_dig (texto, numero_opciones):                  
    patron = f"^[1-{numero_opciones}]$" #Tiene que empezar y terminar con 1 digito
    while re.match(patron,texto) == None:
        print("\nPor favor, ingresar un numero válido.\n")
        return False 
    
#Validación del Mail.
def validacionmail (mail):
    patron = r"[a-zA-Z0-9]{3,}@sistem+\.edu+\.ar" # R String --> Para que tome las secuencias de escape bien (Daba un warning)
    busq = re.findall (patron, mail)
    if len(busq) == 0:
        print('\nIngresar @sistem.edu.ar junto con el nombre de usuario, con un mínimo de tres caracteres antes del "@"\n')
        return False
    else:
        return True
#Verificar si la cuenta existe o no en el sistema
def validacion_cuenta_existente (user,contraseña):
    with open(r"C:\Users\santi\OneDrive\Documents\GitHub\p1_mita_grupo1_2024\GESTION_ACADEMICA\Base_de_datos\alumnos_profesores.txt", mode="r", encoding="utf-8") as archivo:
        flag = True
        encontrado = True
        tipo_usuario = 0
        while flag:
            linea = archivo.readline()
            if linea == "": # EL ARCHIVO DE TEXTO DEBE TENER MAXIMO UNA LINEA VACÍA AL FINAL
                flag = False
                encontrado = False
            else:
                linea = linea.strip()
                lista = linea.split(";")
                if contraseña == False: #Para el registro
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
                            flag = False
                        else:
                            print("Ingreso correcto al apartado alumnos.")
                            tipo_usuario = 1
                            legajo = lista[0]
                            flag = False
        if encontrado == False and contraseña != False: #Si el usuario no se encontró en el login
            print("Usuario no encontrado.")
        elif encontrado == False and contraseña == False: #Si el usuario no se encontró en el registro
            return legajo, True
        else: #Si se encontró en el login
            return tipo_usuario, legajo
'''i=0
a=0
while i<len(list_alumnos):
    if user==list_alumnos[i][1] and contraseña==list_alumnos[i][2]: 
        print("\nIngreso correcto al apartado alumnos.\n")
        return 1, list_alumnos[i][0] 
    i+=1
j = 0
while j<len(list_profesores):
    if user==list_profesores[j][0] and contraseña==list_profesores[j][1]:
        print("\nIngreso correcto al apartado profesores.\n")
        return 2, list_profesores[j][0]
    j += 1
return 3,a'''

#Verificar si existe un USUARIO registrado anteriormente.
def cuenta_existente_register (listaalumnos,listaprofes,usuario):
    i,j=0,0    
    while i<len(listaalumnos):
        if usuario==listaalumnos[i][1]: 
            print("\nUsuario ya existente.\n")
            return False
        i += 1
    while j<len(listaprofes):
        if  usuario==listaprofes[j][0]:
            print("\nUsuario ya existente.\n")
            return False
        j += 1    

#Si se sigue o no con las opciones.    
def seguir_texto (text): ### REMPLAZAR por funcion validacion_dig() ######################################
    patron = "^[1-2]$"
    while re.match(patron,text) == None:
        print("\nPor favor, ingresar un numero válido.\n")
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

#Validación de nota, entre 0 y 10 y con 
def validar_nota (car):
    patron = r"^(10(\.0)?|[0-9](\.\d)?)$" # ()? Quiere decir que es opcional que haya un punto y un 0, | es operador OR
    nota_valida= re.match(patron,car)
    if nota_valida == None:
        print("\nNota incorrecta, por favor ingresar una nota válida.\n")
        return False    