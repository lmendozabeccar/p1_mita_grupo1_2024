import json
from VALIDACIONES.Validaciones import validacion_dig, validar_nota
from Base_de_datos.funciones_json import devolverjson, guardarjson
# Diccionario de materias
materias_dic = {
    "1": "Álgebra",
    "2": "Sistemas",
    "3": "Desarrollo",
    "4": "Inglés",
    "5": "Programación",
    "6": "Estadística",
    "7": "Física",
    "8": "Cálculo",
    "9": "Redes",
    "10": "Marketing"
    }

def agregar_materias(legajo):
    """
    pre: recibe el legajo del alumno el cual quiere inscribirse a las materias.
    pos: agrega la materias y su nota (-1) a la matriz de notas, en el respectivo legajo del alumno.
    """
    try:
        matriz_legajos_notas = devolverjson()  # Valida el diccionario notas para ver si existe o no
    except (FileNotFoundError, json.JSONDecodeError, TypeError): #Errores que se presentan si el JSON está vacío
        matriz_legajos_notas = {}
        
    if legajo in matriz_legajos_notas:
        notas_sublista = matriz_legajos_notas[legajo]["notas"]
        existe = True
        print(f"Usted está cursando estas materias:\n{", ".join(matriz_legajos_notas[legajo]["cursa"])}")
    else:
        notas_sublista = []
        cursa_sublista = []
        existe = False
        print("No está cursando ninguna materia todavía.")
    flag = True
    menu_materia = "\nIngrese qué materia desea cursar: \n1.Algebra\n2.Sistemas\n3.Desarrollo Web\n4.Ingles\n5.Programacion\n6.Estadística\n7.Física\n8.Cálculo\n9.Redes\n10.Marketing\nPor favor, elegir un número de acuerdo a su materia: "
    menu_agregar_materia = "\n¿Desea agregar otra materia? \n1 Sí. \n2 No. \nPor favor elegir una opción: "
    if len(notas_sublista) == 10:
        print("\nUsted ya está inscripto en las 10 materias.")
        return True
    else:
        while flag == True:
            if existe == True:
                cursa_sublista = matriz_legajos_notas[legajo]["cursa"]
                notas_sublista = matriz_legajos_notas[legajo]["notas"]
                if len(notas_sublista) == 10:
                    print("\nEl alumno ya está inscripto en las 10 materias.")
                    break # No queda de otra que aplicar break, porque si no, el programa se rompe
            
            materia = input(menu_materia)
            while validacion_dig (materia, 10)==False: #Valida que sea un numero del 1 al 10
                materia = input(menu_materia)
                
            materia_nombre = materias_dic.get(materia) #Busca el valor asociado a la clave materia, en el diccionario (y devuelve el respectivo valor)
            if materia_nombre in cursa_sublista:
                print("\nUsted ya esta cursando esa materia")
            else:
                if existe == False: #Si el alumno no existe, se crea una nueva llave en el diccionario
                    matriz_legajos_notas[legajo] = {
                        "cursa": [materia_nombre],
                        "notas": [-1]
                    }
                    existe = True
                    print(f"\nLa materia {materia_nombre} fue agregada.")
                else:
                    matriz_legajos_notas[legajo]["cursa"].append(materia_nombre) #Si hago esta linea de una y el legajo no esta registrado en la matriz de notas, entonces el programa se rompe, por eso se inventó la flag "existe"
                    matriz_legajos_notas[legajo]["notas"].append(-1)
                    print(f"\nLa materia {materia_nombre} fue agregada.") #Aviso al usuario.
            
                # Preguntar si el usuario desea agregar otra materia
                continuar = input(menu_agregar_materia) #Modularizacion de menú anterior.
                while validacion_dig(continuar, 2)== False: #Valida que ingrese 1 o 2.
                    continuar = input(menu_agregar_materia) #Modularizacion de menú anterior.
                if int(continuar) == 2:
                    flag = False
                    #Ingresa 2, sale del apartado y vuelve atras.
        guardarjson(matriz_legajos_notas)
        print("\nVolviendo al menú principal...")          
        return True
