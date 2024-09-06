from main import profesores, estudiantes
print()
print()
print("Bienvenido a la aplicación.")
import re
#Alumnos ya registrados en el sistema.
ingreso_sistemas = [
    ["nicovera@sistem.edu.ar","nicovera01","Nicolas Vera"],
    ["tomiweins@sistem.edu.ar","tomiweins01","Tomas Weinstelbaum"],
    ["santimatra@sistem.edu.ar","santimatra01","Santino Matra"],
    ["lucasmendo@sistem.edu.ar","lucasmendo01","Lucas Mendoza"],
    ["silvifalcon@sistem.edu.ar","silvifalcon01","Silvina Falcon"],
    ["alevera@sistem.edu.ar","alevera01","Alejandro Vera"],
    ["malecristaldi@sistem.edu.ar","malecristaldi01","Malena Cristaldi"],
    ["lucaspagli@sistem.edu.ar","lucaspagli01","Lucas Paglilla "],
    ["fabrisuccar@sistem.edu.ar","fabrisuccar01","Fabricio Succar"],
    ["lautipadin@sistem.edu.ar","lautipadin01","Lautaro Padin"]
                                ]
ingreso_profes = [
    ["pepi@sistem.edu.ar", "pepito10"],
    ["profe@sistem.edu.ar", "profeuade"],
    ["uade@sistem.edu.ar",   "uade24"]
]


#Se recortan los nombres de los productos a un máximo de 8 caracteres.
productos_recortados = [[mail[:10], contraseña[:10], nombre[:15]] for mail, contraseña,nombre in ingreso_sistemas]#####Ver los recortes con expresiones regulares

username = "Username"
passw = "Password"
nombre = "Nombre"
# Imprimir la lista con formato de f-strings
print(f"|{username:^10}| |{passw:^10}| |{nombre:^15}|")
print("*" * 44)

for mail, contraseña, nombre in productos_recortados:
    print(f"|{mail:^10}| |{contraseña:^10}| |{nombre:^15}|")
print()

profeuser = "User-Prof"
contraprofe = "Contraseña"
profesores = [[email[:10], contra[:10]] for email, contra in ingreso_profes]
print(f"|{profeuser:^10}| |{contraprofe:^10}|")
print("-" * 26)
for email, contra in profesores:
    print(f"|{email:^10}| |{contra:^10}|") ###APLICAR EXPRESIONES REGULARES 
###HACER TODO CON FUNCIONES
# Proceso Register

def menu_de_inicio():
    flag = True
    print(f"\n¡Bienvenidos a nuestra Gestion Academica!")
    while flag!=False:
        inicio=int(input("Quieres Iniciar sesion?\n1 Si\n2 No, deseo registrarme\n3 Salir \nElija un número: "))
        while inicio<1 or inicio>3:
            print()
            print("Ingresar un número correcto para poder continuar.")
            inicio=int(input("Quieres Iniciar sesion?\n1 Si\n2 No, deseo registrarme\n3 Salir \nElija un número: "))
        if inicio==1:
            login()
            flag = False
        elif inicio == 2:
            print("¡Registrate!")
            registro(ingreso_sistemas,ingreso_profes)
            flag = False
            inicio_2=int(input("Quieres Iniciar sesion ahora?\n1 Si\n2 No\nElija un número: "))
            if inicio_2 == 1:
                login()
                flag = False
            elif inicio_2==2:
                print("Saliendo..")
                flag = False
        elif inicio==3:
                print("Saliendo..")
                flag = False

#Validación del Mail.
def validacionmail (mail):
    patron = "[a-zA-Z0-9]+@[sistem]+\.[edu]+\.[ar]"
    busqarr = re.findall (patron, mail)
    return busqarr
  
# Proceso de Log-in
def login():
    #Verificar si la cuenta existe o no en el sistema
    username=str(input("Ingresar su mail de usuario de alumno: "))
    password=str (input("Ingresar contraseña de usuario: "))
    flag=False
    cont=0 #Intentos

    while flag==False and cont<5:
        while validacionmail(username) == [] and cont<5: #Se valida el mail
            print("Información incorrecta. Ingresar @sistem.edu.ar después de su nombre de usuario.")
            cont += 1
            username=str(input("Ingresar su mail de usuario: "))
            password=str (input("Ingresar contraseña de usuario: "))           
        i=0
        while i<len(ingreso_sistemas) and flag!=True:
            if username==ingreso_sistemas[i][0] and password==ingreso_sistemas[i][1]: #Verifica si el mail existe en la base de datos de alumnos
                print("Ingreso correcto al apartado alumnos.")
                flag=True
                estudiantes(i)
            i+=1

        if flag!=True:##########################################
            j = 0
            while j<len(ingreso_profes):
                if username==ingreso_profes[j][0] and password==ingreso_profes[j][1]:
                    print("Ingreso correcto al apartado profesores.")
                    flag = True
                    profesores()
                j+=1
                
        if flag==False: #En caso de no encontrar el usuario, vuelve a preguntar con un maximo de 5 intentos.
            cont += 1
            if cont<5:
                print("No se pudo acceder a una cuenta ya existente, por favor volver a intentarlo.")
                print()
                ini=int(input("Quieres Iniciar sesion?\n1 Si\n2 No, deseo volver atrás.\nElija un número: "))
                if ini == 1:
                    username=str (input("Por favor, ingresar su mail de usuario de alumno: ")) 
                    password=str (input("Ingresar contraseña de usuario: "))
                elif ini== 2:
                    menu_de_inicio()
            else:
                print("Numerosos intentos fallidos, reintentar nuevamente en unos minutos.")

def registro(listaalumnos, listaprofesor):
    flag = False
    while flag == False:
        flag_registro =True        
        print()
        inicio=int(input("Elija su opción correspondiente.\n1 Se quiere registrar como alumno.\n2 Se quiere registrar como profesor.\n3 Salir\nElija un número: "))
        while inicio<1 or inicio>3: #En caso de que no se ingrese un número válido
            print("Ingresar un número correcto para poder continuar con el registro.") 
        user=str(input("Ingresar su nombre de usuario nuevo: "))
        while validacionmail(user) == []:
            print("Información incorrecta. Ingresar @sistem.edu.ar después de su nombre de usuario.")
            user=str(input("Ingresar su mail de usuario nuevo: "))
        if inicio==1: #Si se registra como alumno
            i=0
            while i<len(listaalumnos) and flag_registro==True:
                if user == listaalumnos[i][0]: #Verifica si el usuario ya existe en la base de datos de alumnos
                    flag_registro = False
                i += 1
            if flag_registro == False:
                print("Ese usuario ya existe, intentelo de nuevo.")
            else:
                nom=str(input("Ingresar su nombre y apellido, ambas comenzando con mayúsculas: "))####### No hay un usuario (user)?
                pas=str(input("Ingrese su contraseña: "))
                
                #FALTA VALIDACIÓN DE ESTO.
                while re.findall ("^[A-Z]", nom) == None:
                    print("Iniciar su nombre y apellido con letras mayúsculas.")
                
                
                listaalumnos.append([user, pas, nom])
                flag = True        
                
        if inicio==2: #Si se registra como profesor
            i=0 #Intentos
            while i<len(listaprofesor) and flag_registro==True:                
                if user == listaprofesor[i][0]: #Verifica si el usuario ya existe en la base de datos de profesores
                    flag_registro = False
                i += 1
            if flag_registro == False:
                print("Ese usuario ya existe, inténtelo de nuevo.")
            else:
                pas=str(input("Ingrese su contraseña: "))
                listaprofesor.append([user, pas])
                flag = True
        
        if inicio==3:
            menu_de_inicio()
            
        if flag_registro == False:
            print()
            ini=int(input("Elegir la opción que desee: \n1 Quiere volver a iniciar sesión. \n2 Quiere regresar al inicio \nElija un número: "))
            while ini<1 or ini>2:
                print("Ingresar una opción válida.")
                ini=int(input("Elegir la opción que desee: \n1 Quiere volver a iniciar sesión. \n2 Quiere regresar al inicio \nElija un número: "))

            if ini == 2:
                menu_de_inicio ()                

    return listaalumnos,listaprofesor
            
"""
if __name__ == "__main__":
"""
menu_de_inicio()
print(f"\nFin de proceso")
