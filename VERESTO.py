from main import profesores, encabezado_calificaciones
print()
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

# Proceso Register

def inicio():
    flag = True
    print(f"\n¡Bienvenidos a nuestra Gestion Academica!")
    while flag!=False:
        inicio=int(input("Quieres Iniciar sesion?\n1 Si\n2 No, deseo registrarme\n3 Salir \nElija un número: "))
        if inicio==1:
            login()
            flag = False
        elif inicio == 2:
            print("¡Registrate!")
            registro(ingreso_sistemas)
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
        
# Proceso de Log-in
def login():
    #Verificar si la cuenta existe o no en el sistema
    username=str(input("Por favor, ingresar su mail de usuario de alumno: "))  
    password=str (input("Ingresar contraseña de usuario: "))
    flag=False
    cont=0
    flagwhile1=True
    while flag==False and cont<5 and flagwhile1 ==True:
        i=0
        while i<len(ingreso_sistemas) and flag!=True:
            if username==ingreso_sistemas[i][0] and password==ingreso_sistemas[i][1]:
                print("Ingreso correcto al apartado alumnos.")
                flag=True
                estudiantes(i)
            i+=1

        if flag!=True:
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
                    flagwhile1 = False
                    inicio()
            else:
                print("Numerosos intentos fallidos, reintentar nuevamente en unos minutos.")

def registro(lista):
    flag = 0
    while flag == 0:
        flag_registro =True
        user=str(input("ingresar su usuario nuevo, sin @sistem: "))
        sis = "@sistem.edu.ar"
        us = user + sis
        for fil in lista:
            if us == fil[0]:
                print(us, fil[0])
                flag_registro = False
        if flag_registro == False:
            print("Ese usuario ya existe, intentelo de nuevo.")
        else:
            pas=str(input("Ingrese su contraseña: "))
            lista.append([us, pas])
            flag = 1
    return lista
"""
if __name__ == "__main__":
"""
inicio()
print(f"\nFin de proceso")
