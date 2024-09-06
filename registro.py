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
#Se recortan los nombres de los productos a un máximo de 8 caracteres.
productos_recortados = [[mail[:10], contraseña[:10]] for mail, contraseña in ingreso_sistemas]
username = "Username"
passw = "Password"
# Imprimir la lista con formato de f-strings
print(f"|{username:^10}| |{passw:^10}|")
print("*" * 26)

for mail, contraseña in productos_recortados:
    print(f"|{mail:^10}| |{contraseña:^10}|")

print()
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
print("¡Registrate!")
registro(ingreso_sistemas)    
productos_recortados = [[mail[:10], contraseña[:10]] for mail, contraseña in ingreso_sistemas]
username = "Username"
passw = "Password"
# Imprimir la lista con formato de f-strings
print(f"|{username:^10}| |{passw:^10}|")
print("*" * 26)

for mail, contraseña in productos_recortados:
    print(f"|{mail:^10}| |{contraseña:^10}|")

print()
######################################## Hay que borrar este archivo?