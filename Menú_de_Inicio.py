from main import profesores, estudiantes
from Validaciones import validacion_2dig, validacion_3dig, validacionmail, validar_contraseña, validar_mayus_nombre, validar_num, cuenta_existente_login, cuenta_existente_register
import re
#Alumnos ya registrados en el sistema.
ingreso_alumnos = [
    ["1000","nicovera@sistem.edu.ar","nicovera01","Nicolas Vera"],
    ["1001","tomiweins@sistem.edu.ar","tomiweins01","Tomas Weinstelbaum"],
    ["1002","santimatra@sistem.edu.ar","santimatra01","Santino Matra"],
    ["1003","lucasmendo@sistem.edu.ar","lucasmendo01","Lucas Mendoza"],
    ["1004","silvifalcon@sistem.edu.ar","silvifalcon01","Silvina Falcon"],
    ["1005","alevera@sistem.edu.ar","alevera01","Alejandro Vera"],
    ["1006","malecristaldi@sistem.edu.ar","malecristaldi01","Malena Cristaldi"],
    ["1007","lucaspagli@sistem.edu.ar","lucaspagli01","Lucas Paglilla "],
    ["1008","fabrisuccar@sistem.edu.ar","fabrisuccar01","Fabricio Succar"],
    ["1009","lautipadin@sistem.edu.ar","lautipadin01","Lautaro Padin"]
                                ]
ingreso_profes = [
    ["pepi@sistem.edu.ar", "pepito10"],
    ["profe@sistem.edu.ar", "profeuade"],
    ["uade@sistem.edu.ar",   "uade24"]
]
#Se recortan los nombres de los productos a un máximo de 8 caracteres.
productos_recortados = [[legajo[:6], mail[:10], contraseña[:10], nombre[:15]] for legajo, mail, contraseña,nombre in ingreso_alumnos]

username = "Username"
passw = "Password"
nombre = "Nombre"
legajo = "Legajo"
# Imprimir la lista con formato de f-strings
print(f"|{legajo:^6}||{username:^10}| |{passw:^10}| |{nombre:^15}|")
print("*" * 44)

for legajo, mail, contraseña, nombre in productos_recortados:
    print(f"|{legajo:^10}| |{mail:^10}| |{contraseña:^10}| |{nombre:^15}|")
print()

profeuser = "User-Prof"
contraprofe = "Contraseña"
profesores = [[email[:10], contra[:10]] for email, contra in ingreso_profes]
print(f"|{profeuser:^10}| |{contraprofe:^10}|")
print("-" * 26)
for email, contra in profesores:
    print(f"|{email:^10}| |{contra:^10}|") ###APLICAR EXPRESIONES REGULARES 

#Pedir usuario y contraseña
def user ():
    username=str(input("Ingresar su mail de usuario: "))
    password=str (input("Ingresar contraseña: "))
    return username,password
#Menú de inicio.
def menu_de_inicio():
    flag = True
    print(f"\n¡Bienvenidos a nuestra Gestion Academica!")
    while flag!=False:
        inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")
        #Validación para que no sea una letra.
        while validar_num(inicio) == False:
            inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")
        #Validacion del número.
        while validacion_3dig (inicio)== False:
            print()
            inicio=input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")
            while validar_num(inicio) == False:
                inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")                                
        if int (inicio)==1:
            login()
            flag = False
        elif int (inicio) == 2:
            print("¡Registrate!")
            registro(ingreso_alumnos,ingreso_profes)
            flag = False
            inicio_2=input("Qué desea realizar ahora?\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            #Validación de letra.
            while validar_num(inicio_2) == False:
                inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            #Validación de número.            
            while validacion_2dig (inicio_2) == False: 
                print()
                inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
                while validar_num (inicio_2) == False:
                    inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            if  int (inicio_2) == 1:
                login()
                flag = False
            elif  int (inicio_2)==2:
                print("Saliendo..")
                flag = False
        else:
            print("Saliendo..")
            flag = False
def login():   # Proceso de Log-in
    usuario,contra = user()
    flag=False
    cont=0 #Intentos
    while flag==False and cont<5:
        while validacionmail(usuario) == False and cont<5: #Se valida el mail
            cont += 1
            usuario,contra = user()
        num, apart = cuenta_existente_login(ingreso_alumnos,ingreso_profes,usuario,contra)
        if num == 1:
            flag=True
            estudiantes(apart)
        elif num == 2:
            flag = True
            profesores()
        else:  #En caso de no encontrar el usuario, vuelve a preguntar con un maximo de 5 intentos.
            cont += 1
            if cont<5:
                print()
                print("No se pudo acceder a una cuenta ya existente, por favor volver a intentarlo.")
                print()
                inicio_login=(input("\n1 Iniciar sesión.\n2 Volver atrás.\nElija un número: "))                
                #Validación de letra.
                while validar_num(inicio_login) == False:
                    inicio_login=(input("\n1 Iniciar sesión.\n2 Volver atrás.\nElija un número: "))
                #Validación de número.
                while validacion_2dig(inicio_login) == False:
                    print()
                    inicio_login=(input("\n1 Iniciar sesión.\n2 Volver atrás.\nElija un número: "))
                    while validar_num (inicio_login) == False:
                        inicio_login=(input("\n1 Iniciar sesión.\n2 Volver atrás.\nElija un número: "))                
                if int (inicio_login) == 1:
                    usuario,contra = user()
                elif int (inicio_login) == 2:
                    menu_de_inicio()
            else:
                print("Numerosos intentos fallidos, reintentar nuevamente en unos minutos.")
def registro(listaalumnos, listaprofesor):
    flag = False
    while flag == False:
        print()
        inicio_registro=(input("\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "))
        #Validación de letra.
        while validar_num(inicio_registro) == False:
            inicio_registro=(input("\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "))
        #Validación de número.
        while validacion_3dig (inicio_registro) == False:
            print()
            inicio_registro=(input("\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "))
            while validar_num (inicio_registro) == False:
                inicio_registro=(input("\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "))        
        if int(inicio_registro) ==3:
                menu_de_inicio()
        #Validación Mail.
        user=str(input("Ingresar su mail de usuario nuevo: "))
        while validacionmail(user) == False:
            user=str(input("Ingresar su mail de usuario nuevo: "))                
        if cuenta_existente_register (ingreso_alumnos,ingreso_profes,user) != False:
            if int (inicio_registro)==1: #Si se registra como alumno
                nom=str(input("Ingresar su nombre y apellido, ambas comenzando con mayúsculas: "))
                while validar_mayus_nombre(nom) == False: 
                    print()
                    nom=str(input("Ingresar su nombre y apellido, ambas comenzando con mayúsculas: "))
                pas=str(input("Ingrese su contraseña: "))        
                while validar_contraseña (pas) == False:
                    print()
                    pas=str(input("Ingrese su contraseña: "))                            
                listaalumnos.append([user, pas, nom])
                flag = True                        
            if int (inicio_registro)==2: #Si se registra como profesor
                pas=str(input("Ingrese su contraseña: "))
                while validar_contraseña (pas) == False:
                    print()
                    pas=str(input("Ingrese su contraseña: "))                            
                listaprofesor.append([user, pas])
                flag = True                    
        else: #En caso de usuario ya existente.
            print()
            inicio_usuario_exist=(input("\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "))
            #Validación de letra.
            while validar_num(inicio_usuario_exist) == False:
                inicio_usuario_exist=(input("\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "))
            #Validación de número.
            while validacion_2dig (inicio_usuario_exist) == False:
                print()
                inicio_usuario_exist=(input("\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "))
                while validar_num (inicio_usuario_exist) == False:
                    inicio_usuario_exist=(input("\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "))
            if int(inicio_usuario_exist) == 2:
                menu_de_inicio ()                
    return listaalumnos,listaprofesor            
menu_de_inicio()
print(f"\nFin de proceso")