def mostrar_notas (matriz_legajos_notas, legajo):
    #Si la suma de la lista (en la columna 2 y en su respectiva fila) son 
    #todos -1, quiere decir que no tiene ninguna nota cargada
    legajo = int(legajo)
    if legajo not in matriz_legajos_notas:
        print("Para ver sus calificaciones, primero debe anotarse a una")
        return 0
    else:
        print(matriz_legajos_notas)
        sublista_cursa = matriz_legajos_notas[legajo]["cursa"]
        sublista_notas = matriz_legajos_notas[legajo]["notas"]
        suma,cont = 0,0
        # Convertir el -1 en un guion para cada valor de la fila
        notas_formateadas = ["-" if valor == -1 else valor for valor in sublista_notas]
        for i in range(len(notas_formateadas)): ########################
            if notas_formateadas[i] != "-":
                suma += notas_formateadas[i]
                cont += 1
        if suma == 0 or cont == 0:
            print()
            print("No hay notas cargadas en este legajo.")
        else:
            # Imprimir la lista con formato de f-strings
            print(f"Legajo: {legajo}")
            for cursa, nota in zip(sublista_cursa, sublista_notas): #Junta las dos sublistas de las materias cursadas con su respectiva nota en una nueva matriz
                nota = "-" if nota == -1 else nota
                print(f"Cursa {cursa}, Nota: {nota}")
            print(f"Promedio: {suma/cont:.2f}") #Maximo dos decimales
