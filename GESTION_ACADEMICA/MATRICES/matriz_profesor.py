ingreso_profes = [ #Lista de profesores ya ingresados.
    ["nardonejuan@sistem.edu.ar", "nardonejuan10","Nardone Juan"],
    ["ramiroleiva@sistem.edu.ar", "ramiroleiva10","Leiva Ramiro"],
    ["daquino@sistem.edu.ar",   "daquino10", "Daquino Nicolás"]
]
print()
print("Lista de profesores ya registrados en el sistema.")
profeuser = "Usuario-Profesor"
contraprofe = "Contraseña"
nombre = "Nombre"

profesores_recortados = [[email[:16], contra[:10], nombre [:15]] for email, contra, nombre in ingreso_profes]  #Recortar.

#Ordenamiento en forma alfabética.
profesores_ordenados = sorted(profesores_recortados, key=lambda x: (x[2]))


print(f"|{profeuser:^16}||{contraprofe:^10}||{nombre:^15}|")   # Mostrar encabezados, con reestricciones.
print("-" * 48)
for email, contra, nombre in profesores_ordenados:
    print(f"|{email:^16}||{contra:^10}||{nombre:^15}|") # Mostrar información, con reestricciones.
