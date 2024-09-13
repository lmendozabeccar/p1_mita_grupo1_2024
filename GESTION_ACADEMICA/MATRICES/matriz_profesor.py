ingreso_profes = [ #Lista de profesores ya ingresados.
    ["pepi@sistem.edu.ar", "pepito10"],
    ["profe@sistem.edu.ar", "profeuade"],
    ["uade@sistem.edu.ar",   "uade24"]
]

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