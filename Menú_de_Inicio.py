from main import profesores
from main import estudiantes
from Validaciones import validacion_2dig, validacion_3dig, validacionmail, validar_contraseña, validar_mayus_nombre, validar_num, cuenta_existente_login, cuenta_existente_register

print()
#Alumnos ya registrados en el sistema.
ingreso_alumnos = [   #Lista de alumnos ya ingresados.
    ["1000","nicovera@sistem.edu.ar","nicovera01","Vera Alejandro"],
    ["1001","tomiweins@sistem.edu.ar","tomiweins01","Weinstelbaum Tomás"],
    ["1002","santimatra@sistem.edu.ar","santimatra01","Matra Santino"],
    ["1003","lucasmendo@sistem.edu.ar","lucasmendo01","Mendoza Lucas"],
    ["1004","silvifalcon@sistem.edu.ar","silvifalcon01","Falcón Silvina"],
    ["1005","alevera@sistem.edu.ar","alevera01","Vera Alejandro"],
    ["1006","malecristaldi@sistem.edu.ar","malecristaldi01","Cristaldi Malena"],
    ["1007","lucaspagli@sistem.edu.ar","lucaspagli01","Paglilla Lucas"],
    ["1008","fabrisuccar@sistem.edu.ar","fabrisuccar01","Succar Fabricio"],
    ["1009","lautipadin@sistem.edu.ar","lautipadin01","Padin Lautaro"]
                                ]
ingreso_profes = [ #Lista de profesores ya ingresados.
    ["pepi@sistem.edu.ar", "pepito10"],
    ["profe@sistem.edu.ar", "profeuade"],
    ["uade@sistem.edu.ar",   "uade24"]
]
#Se recortan los nombres de los productos a un máximo de 8 caracteres.
estudiantes_recortados = [[legajo[:6], mail[:10], contraseña[:10], nombre[:15]] for legajo, mail, contraseña,nombre in ingreso_alumnos]

#Asignación para poder mostrar las listas con encabezados.
username = "Username"
passw = "Password"
nombre = "Nombre"
legajo = "Legajo"
# Lista ordenada por nombre (alfabeticamente) y luego por legajo (ascendente).
estudiantes_ordenados = sorted(estudiantes_recortados, key=lambda x: (x[3], int(x[0])))

# Imprimir la lista con formato de f-strings
print("Lista de alumnos ya registrados en el sistema.")
print(f"|{legajo:^10}||{username:^10}||{passw:^10}||{nombre:^15}|") #Mostrar encabezados, con reestricciones.
print("*" * 53)
for legajo, mail, contraseña, nombre in estudiantes_ordenados:
    print(f"|{legajo:^10}||{mail:^10}||{contraseña:^10}||{nombre:^15}|") #Mostrar información, con reestricciones.
print()

print("Lista de profesores ya registrados en el sistema.")
profeuser = "User-Prof"
contraprofe = "Contraseña"
profesores = [[email[:10], contra[:10]] for email, contra in ingreso_profes]  #Recortar.
print(f"|{profeuser:^10}| |{contraprofe:^10}|")   # Mostrar encabezados, con reestricciones.
print("-" * 26)
for email, contra in profesores:
    print(f"|{email:^10}| |{contra:^10}|") # Mostrar información, con reestricciones.

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
        inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ") #Menú de inicio.
        #Validación para que no sea una letra.
        while validar_num(inicio) == False:
            inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")
        #Validacion del número.
        while validacion_3dig (inicio)== False:
            print()
            inicio=input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")
            while validar_num(inicio) == False:
                inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")                                
        if int (inicio)==1: #Se entra al inicio de sesión.
            login()
            flag = False
        elif int (inicio) == 2: #Se entra al registro.
            print("¡Registrate!")
            registro(ingreso_alumnos,ingreso_profes)
            flag = False
            print()
            inicio_2=input("Finalizado su registro, qué desea realizar ahora?\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            #Validación de letra.
            while validar_num(inicio_2) == False:
                inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            #Validación de número.            
            while validacion_2dig (inicio_2) == False: 
                print()
                inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
                while validar_num (inicio_2) == False:
                    inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            if  int (inicio_2) == 1: #Se entra al inicio de sesión.
                login()
                flag = False
            elif  int (inicio_2)==2: #Se sale del programa.
                print("Saliendo..")
                flag = False
        else:
            print("Saliendo..") #Opción 3 del menú principal, se sale de programa.
            flag = False
def login():   
    usuario,contra = user() #Pide usuario y contraseña
    flag=False
    cont=0 #Intentos
    while flag==False and cont<5:
        while validacionmail(usuario) == False and cont<5: #Se valida el mail
            cont += 1 #Máximo de 5 intentos.
            usuario,contra = user()
        num, apart = cuenta_existente_login(ingreso_alumnos,ingreso_profes,usuario,contra) #Se fija si existe una cuenta (estudiante o profesor), con ese nombre de usuario.
        if num == 1: #Existe un estudiante con ese nombre de usuario.
            flag=True
            estudiantes(apart)
        elif num == 2: #Existe un profesor con ese nombre de usuario.
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
                if int (inicio_login) == 1: #Vuelve a intentar el inicio de sesión.
                    usuario,contra = user()
                elif int (inicio_login) == 2: #Vuelve atrás, al menú principal.
                    menu_de_inicio()
            else:
                print("Numerosos intentos fallidos, reintentar nuevamente en unos minutos.") #En caso de llegar al maximo de intentos (cinco).
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
        if int(inicio_registro) ==3: #Vuelve al menú de inicio.
                menu_de_inicio()
        #Validación Mail.
        user=str(input("Ingresar su mail de usuario nuevo: "))
        while validacionmail(user) == False:
            user=str(input("Ingresar su mail de usuario nuevo: "))                
        if cuenta_existente_register (ingreso_alumnos,ingreso_profes,user) != False: #Se fija si hay una cuenta existente, en caso que sea True, entra . 
            if int (inicio_registro)==1: #Si se registra como alumno
                nom=str(input("Ingresar su nombre y apellido, ambas comenzando con mayúsculas: "))
                while validar_mayus_nombre(nom) == False: #Valida que el nombre y el apellido comience con mayuscula.
                    print()
                    nom=str(input("Ingresar su nombre y apellido, ambas comenzando con mayúsculas: ")) 
                pas=str(input("Ingrese su contraseña: "))        
                while validar_contraseña (pas) == False: #Valida que la contraseña tenga, al menos, una mayuscula, una minuscula y un numero, sin espacios en blanco.
                    print()
                    pas=str(input("Ingrese su contraseña: "))                            
                listaalumnos.append([user, pas, nom]) #En caso de superar todas las validaciones, agrega a la lista de alumnos al nuevo alumno.
                flag = True                        
            if int (inicio_registro)==2: #Si se registra como profesor
                pas=str(input("Ingrese su contraseña: "))
                while validar_contraseña (pas) == False: #Valida que la contraseña tenga, al menos, una mayuscula, una minuscula y un numero, sin espacios en blanco.
                    print()
                    pas=str(input("Ingrese su contraseña: "))                            
                listaprofesor.append([user, pas]) #En caso de superar todas las validaciones, agrega a la lista de profesores al nuevo profesor.
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
            if int(inicio_usuario_exist) == 2: #Vuelve al menú de inicio, en caso de elegir la opción 2.
                menu_de_inicio ()                
    return listaalumnos,listaprofesor            
menu_de_inicio()
print(f"\nFin de proceso")