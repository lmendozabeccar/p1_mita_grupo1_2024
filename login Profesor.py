import random
def crear(n,m):
    return [[0]*m for fill in range(n)]




def llenar(m):
    filas=len(m)
    columnas=len(m[0])
    for fil in range(filas):
        for col in range(filas):
            num_aleatorio=random.randint(1,10)
            m[fil][col]=num_aleatorio

def imprimir(matriz,contraseña,gmail):
    filas=len(matriz)
    columnas=len(matriz[0])
    print(f"{'':<15}", end="")  # Espacio para alinear encabezado de filas
    for nombre_col in contraseña:
        print(f"|{nombre_col:^10}", end="")  # Alinear nombres de columnas centrados
    print("|")  # Cerrar la línea de encabezados de columna
    print("-" * (12 + (11 * len(contraseña))))  # Línea divisoria

    
    for fil in range(filas):
        print(f"{gmail[fil]:<12}", end="")  
        for col in range(columnas):
            print(f"|{matriz[fil][col]:^10}", end="")  
        print("|")  
  
    
matriz=crear(4,4)
llenar(matriz)
contraseña=["Juan", "Manolo", "Roberto", "Octuso"]
gmail=["juan@gmail.com", "manolo@gmail.com", "roberto@gmail.com", "octuso@gmail.com"]






imprimir(matriz,contraseña,gmail)