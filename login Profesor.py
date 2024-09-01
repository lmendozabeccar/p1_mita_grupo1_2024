import random
def crear(n,m):
    return [[0]*m for fill in range(n)]

def llenar(m):
    filas = len(m)
    for fil in range(filas):
        m[fil][0] = random.randint(1, 9)

def imprimir(matriz, gmails):
    filas = len(matriz)
    print(f"{'':<20}", end="")  # Espacio para alinear encabezado de columnas
    print("| Contraseña |")
    print("-" * 14)  # Línea divisoria

    for fil in range(filas):
        print(f"{gmails[fil]:<20}", end="")
        print(f"|   {matriz[fil][0]:^10} |") 
  
    
matriz=crear(4,1)
llenar(matriz)

gmail=["juan31", "manolo67", "roberto296", "octuso3478"]
imprimir(matriz, gmail)

def verificar_usuario(matriz, gmail, usuario, contraseña):
    if usuario in gmail:
        indice = gmail.index(usuario)
        if contraseña == matriz[indice][0]:  # Compara la contraseña ingresada con el número en la fila
            print("Acceso permitido")
        else:
            print("Acceso denegado")
    else:
        print("Acceso denegado")

usuario=(input("Ingrese su usario:"))
contraseña=int(input("Ingrese su contraseña:"))
verificar_usuario(matriz, gmail, usuario, contraseña)