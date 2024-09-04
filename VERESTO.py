from main import profesores, estudiantes, encabezado_calificaciones
print()
#Alumnos ya registrados en el sistema.
ingreso_sistemas = [
    ["nicovera@sistem.edu.ar","nicovera01"],
    ["tomiweins@sistem.edu.ar","tomiweins01"],
    ["santimatra@sistem.edu.ar","santimatra01"],
    ["lucasmendo@sistem.edu.ar","lucasmendo01"],
    ["silvifalcon@sistem.edu.ar","silvifalcon01"],
    ["alevera@sistem.edu.ar","alevera01"],
    ["malecristaldi@sistem.edu.ar","malecristaldi01"],
    ["lucaspagli@sistem.edu.ar","lucaspagli01"],
    ["fabrisuccar@sistem.edu.ar","fabrisuccar01"],
    ["lautipadin@sistem.edu.ar","lautipadin01"]
                                ]
ingreso_profes = [
    ["pepi@sistem.edu.ar", "pepito10"],
    ["profe@sistem.edu.ar", "profeuade"],
    ["uade@sistem.edu.ar",   "uade24"]
]


#Se recortan los nombres de los productos a un máximo de 8 caracteres.
productos_recortados = [[mail[:10], contraseña[:10]] for mail, contraseña in ingreso_sistemas]#####Ver los recortes con expresiones regulares
for mail, contraseña in ingreso_sistemas:
    print([mail[:10], contraseña[:10]])
username = "Username"
passw = "Password"
# Imprimir la lista con formato de f-strings
print(f"|{username:^10}| |{passw:^10}|")
print("*" * 26)

for mail, contraseña in productos_recortados:
    print(f"|{mail:^10}| |{contraseña:^10}|")
print()

profeuser = "User-Prof"
contraprofe = "Contraseña"
profesores = [[email[:10], contra[:10]] for email, contra in ingreso_profes]
print(f"|{profeuser:^10}| |{contraprofe:^10}|")
print("-" * 26)
for email, contra in profesores:
    print(f"|{email:^10}| |{contra:^10}|")

# Proceso Register

def inicio():
    flag = True
    print(f"\n¡Bienvenidos a nuestra Gestion Academica!")
    while flag!=False:
        inicio=int(input("Quieres Iniciar sesion?\n1 Si\n2 No\nElija un número: "))
        if inicio==1:
            login()
            flag = False
        elif inicio == 2:
            registero=int(input("Quieres registrarte?\n1 Si\n2 No\nElija un número: "))
            if registero==1:
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
            elif registero==2:
                print("Saliendo..")
                flag = False

# Proceso de Log-in
def login():
    #Verificar si la cuenta existe o no en el sistema
    user=str(input("Por favor, ingresar su mail de usuario de alumno, sin @sistem: "))  #######En la entrega final que sea con @sistem, los profesores no. Hacer segunda matriz para profesores
    #Concatenación de cadenas
    ma = "@sistem.edu.ar"
    username = user + ma
    password=str (input("Ingresar contraseña de usuario: "))
    flag=False
    cont=0
    while flag==False and cont<5:
        i=0
        while i<len(ingreso_sistemas) and flag!=True:
            if username==ingreso_sistemas[i][0] and password==ingreso_sistemas[i][1]:
                print("Ingreso correcto a la aplicación.")
                flag=True
                estudiantes(i,encabezado_calificaciones, encabezado_asistencias)
            i+=1

        if flag!=True:
            j = 0
            while j<len(ingreso_profes):
                if username==ingreso_profes[j][0] and password==ingreso_profes[j][1]:
                    print("Ingreso correcto al apartado ADMIN")
                    flag = True
                    profesores(encabezado_calificaciones, encabezado_asistencias)
                j+=1
                
        if flag==False: #En caso de no encontrar el usuario, vuelve a preguntar con un maximo de 5 intentos.
            cont += 1
            if cont<5:
                print("No se pudo acceder a una cuenta ya existente, por favor volver a intentarlo.")
                print()
                user=str (input("Por favor, ingresar su mail de usuario de alumno, sin @sistem: ")) 
                ma = "@sistem.edu.ar"
                username = user + ma
                password=str (input("Ingresar contraseña de usuario: "))
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

if __name__ == "__main__":
    inicio()
print(f"\nFin de proceso")
