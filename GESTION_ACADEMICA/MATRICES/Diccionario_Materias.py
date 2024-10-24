from VALIDACIONES.Validaciones import validacion_dig, validar_nota

# Diccionario de materias
materias_dic = {
    "1": "Álgebra",
    "2": "Sistemas",
    "3": "Desarrollo",
    "4": "Inglés",
    "5": "Programación"
}

def agregar_materias(matriz_legajos_notas, legajo):
    if legajo in matriz_legajos_notas:
        notas_sublista = matriz_legajos_notas[legajo]["notas"]
        existe = 1
    else:
        notas_sublista = []
        cursa_sublista = []
        existe = 0
    print()
    flag = 0
    menu_materia = "Ingrese qué materia cursa: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion \nPor favor, elegir un número de acuerdo a su materia: "
    menu_agregar_materia = "¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: "
    
    while flag == 0:
        if existe == 1:
            cursa_sublista = matriz_legajos_notas[legajo]["cursa"]
            notas_sublista = matriz_legajos_notas[legajo]["notas"]
            if sum(notas_sublista) == -5:
                print()
                print("\nEl alumno ya está inscripto en las 5 materias.")
                return matriz_legajos_notas
            print()
        
        materia = input(menu_materia)
        while validacion_dig (materia, 5)== False: #Valida que sea un numero del 1 al 5
            materia = input(menu_materia)
            
        materia_nombre = materias_dic.get(materia) #Busca el valor asociado a la clave materia, en el diccionario (y devuelve el respectivo valor)
        if materia_nombre in cursa_sublista:
            print("\nUsted ya esta cursando esa materia")
        else:
            if existe == 0:
                matriz_legajos_notas[legajo] = {
                    "cursa": [materia_nombre],
                    "notas": [-1]
                }
                existe = 1
                print(f"\nLa materia {materia_nombre} fue agregada.")
            else:
                matriz_legajos_notas[legajo]["cursa"].append(materia_nombre) #Si hago esta linea de una y el legajo no esta registrado en la matriz de notas, entonces el programa se rompe, por eso se inventó la flag "existe"
                matriz_legajos_notas[legajo]["notas"].append(-1)
                print(f"\nLa materia {materia_nombre} fue agregada.") #Aviso al usuario.
                print()
                
            # Preguntar si el usuario desea agregar otra materia
            continuar = input(menu_agregar_materia) #Modularizacion de menú anterior.
            while validacion_dig(continuar, 2)== False: #Valida que ingrese 1 o 2.
                continuar = input(menu_agregar_materia) #Modularizacion de menú anterior.
            if int(continuar) == 2:
                flag = 1 
                #Ingresa 2, sale del apartado y vuelve atras.
    return matriz_legajos_notas

def actualizar_notas (matriz_legajos_notas, legajo):
    flag = 0
    legajo = int(legajo)
    cursa_sublista = matriz_legajos_notas[legajo]["cursa"]
    print()
    dic_materias_inscriptas = {}
    contador = 1
    materias_formateadas = ""
    for materia in cursa_sublista: #Preparo qué materias mostrar segun a qué materias está inscripto el alumno
        materias_formateadas += f"{contador}. {materia}\n"
        dic_materias_inscriptas[contador] = materia #Creo un nuevo diccionario según que cursa el alumno
        contador += 1 
        
    menu_nota = materias_formateadas + "Por favor, elegir un número de acuerdo a su materia: "
    menu_agregar_nota = "¿Desea agregar la nota de otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: "
    menu_calificacion = "Ingresar nota de la respectiva materia: "
    while flag == 0:
        materia = input(menu_nota)
        while validacion_dig(materia, 5)== False: #Valida que sea un numero del 1 al 5
            materia = input(menu_nota)

        materia_nombre = dic_materias_inscriptas.get(int(materia)) #Busca el valor asociado a la clave materia, en el diccionario (y devuelve el respectivo valor)
        if materia_nombre in cursa_sublista:
                calificacion = input(menu_calificacion)
                while validar_nota(calificacion) == False:
                    calificacion = input(menu_calificacion)
                
                posicion = cursa_sublista.index(materia_nombre) # .index() me devuelve en qué posicion está el elemento en la lista
                matriz_legajos_notas[legajo]["notas"][posicion] = int(calificacion)
                print(f"\nLa materia {materia_nombre} fue agregada con una calificación de {calificacion}.") #Aviso al usuario.
                print()
                # Preguntar si el usuario desea agregar otra materia
                continuar = input(menu_agregar_nota) #Modularizacion de menú anterior.
                while validacion_dig(continuar, 2)== False: #Valida que ingrese 1 o 2.
                    continuar = input(menu_agregar_nota) #Modularizacion de menú anterior.
                if int(continuar) == 2:
                    flag = 1                  #Ingresa 2, sale del apartado y vuelve atras.
        else:
            print("El alumno no cursa esa materia")
    return matriz_legajos_notas
