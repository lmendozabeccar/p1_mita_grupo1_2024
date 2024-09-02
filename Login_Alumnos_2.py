print()
print("Bienvenido al sector de Ingreso de la aplicación.")

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
productos_recortados = [[mail[:10], contraseña[:10]] for mail, contraseña in ingreso_sistemas]#####Ver los recortes
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

# Proceso de Log-in


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
        i+=1

    if flag!=True:
        j = 0
        while j<len(ingreso_profes):
            if username==ingreso_profes[j][0] and password==ingreso_profes[j][1]:
                print("Ingreso correcto al apartado ADMIN")
                flag = True
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
    print(f"\nFin de proceso") ###########Usar expresiones regulares

