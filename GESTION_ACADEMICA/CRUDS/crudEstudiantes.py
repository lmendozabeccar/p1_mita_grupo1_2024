from MATRICES.Diccionario_Materias import materias_dic
from MATRICES.matriz_calificaciones import mostrar_notas
def ver_calificacion_nuevo  (leg, lista):
    valor = sum(lista[leg][1]) #Si la suma de la lista (en la columna 2 y en su respectiva fila) son 
    #todos -1, quiere decir que no está inscripto a ninguna materia

    if valor == -5:
        print("No está inscripto a ninguna materia, por favor inscribirse en el menú anterior.")
    for i in range (len(lista[leg][1])):
        if lista[leg][1][i] >= 0:
            mostrar_notas (lista,leg)
    else:
        print("Está inscripto a alguna/s materias, pero sus notas no han sido cargadas.")
