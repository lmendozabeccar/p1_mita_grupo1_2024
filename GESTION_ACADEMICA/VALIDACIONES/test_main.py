def aprobado_desaprobado (notafinal):
    if notafinal == -1:
        return True
    notaminima = 4
    return notafinal >= notaminima   #si notafinal es menor a 4, devuelve False, si es mayor o igual a 4, devuelve True 