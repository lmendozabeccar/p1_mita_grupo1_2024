promedio_materia = lambda indice, lista: (sum(fila[indice] for fila in lista[1:]) / len(lista)) 
#lista[1:] --> Se necesita que el bucle "for" saltee el encabezado para calcular bien el promedio
#La lista por comprensión devuelve un objeto (una lista). sum() va a sumar la lista, y luego es dividido por la cantidad de registros

def ver_calificacion(legajo, lista):
    posicion = [i for i in range(len(lista)) if lista[i][0] == legajo]#Me devuelve en qué posicion está el legajo en la matriz. La funcion devuelve una lista con el numero
    fila = lista[posicion[0]] #Saco la fila donde quiero ver las calificaciones, con posicion[0] ya que es una lista, y se desea leer el entero
    calificaciones = fila[1:] #Quiero que no esté el legajo a la hora de calcular el promedio
    promedio = sum(calificaciones) / 5
    print(f'|{"legajo":^8}|{"algebra":^12}|{"programacion":^12}|{"analisis":^8}|{"sistemas":^8}|{"desarrollo":^14}|')
    print(f"|{legajo:^8}|{lista[posicion[0]][0]:^12}|{lista[posicion[0]][1]:^12}|{lista[posicion[0]][2]:^8}|{lista[posicion[0]][3]:^8}|{lista[posicion[0]][4]:^14}|")
    print(f"Su promedio final fue de: = {promedio:.2f}") #Limitar el promedio hasta dos decimales
    return 1

def ver_materias(lista):
    algebra = promedio_materia(1, lista)
    programacion = promedio_materia(2, lista)
    analisis = promedio_materia(3, lista)
    sistemas = promedio_materia(4, lista)
    desarrollo = promedio_materia(5, lista)
    print(f'|{"Álgebra":^12}|{"Programación":^12}|{"Análisis":^8}|{"Sistemas":^8}|{"Desarrollo":^14}|')
    print(f'|{algebra:^12.2f}|{programacion:^12.2f}|{analisis:^8.2f}|{sistemas:^8.2f}|{desarrollo:^14.2f}|') #.2f limita el numero decimal a 2 dígitos
    return 1

########## Vincular tabla de registros