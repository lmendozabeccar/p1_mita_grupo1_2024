ingreso_profes = [ #Lista de profesores ya ingresados.
    ["nardonejuan@sistem.edu.ar", "nardonejuan10"],
    ["ramiroleiva@sistem.edu.ar", "ramiroleiva10"],
    ["daquino@sistem.edu.ar",   "daquino10"]
]

print("Lista de profesores ya registrados en el sistema.")
profeuser = "Usuario-Profesor"
contraprofe = "Contraseña"
profesores = [[email[:16], contra[:10]] for email, contra in ingreso_profes]  #Recortar.
print(f"|{profeuser:^16}| |{contraprofe:^10}|")   # Mostrar encabezados, con reestricciones.
print("-" * 30)
for email, contra in profesores:
    print(f"|{email:^16}| |{contra:^10}|") # Mostrar información, con reestricciones.
