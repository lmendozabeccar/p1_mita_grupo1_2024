from loading.login import logeandose
from MATRICES.matriz_alumnos import ingreso_alumnos
from MATRICES.matriz_profesor import ingreso_profes
from REGISTRO.Register import registro
print()
#Alumnos ya registrados en el sistema.
#Menú de inicio.
def menu_de_inicio():
    flag = True
    titulo = "¡Bienvenidos a nuestra Gestion Academica!"
    print(titulo.title().center(80))

    matriz_legajos_notas = {} #Se inicializa el diccionario de notas vacía
    
    while flag == True:
        menu = "\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: "
        while True:
            try:
                inicio = int(input(menu)) #Menú de inicio.
            except ValueError:
                print("Error. Debe ingresar un número")
            else:
                if inicio >= 1 and inicio <= 3:
                    break
                else:
                    print("Debe ingresar un número dentro de las opciones")

        if int (inicio)==1: #Se entra al inicio de sesión.
            matriz_legajos_notas_act = logeandose (matriz_legajos_notas)
            if matriz_legajos_notas_act == True:
                return True
            elif matriz_legajos_notas_act != True and matriz_legajos_notas_act != False:
                matriz_legajos_notas = matriz_legajos_notas_act #Se le asignan las nuevas matrices actualizadas

        elif int (inicio) == 2: #Se entra al registro.
            print("¡Registrate!")
            registro() #Se asignan las dos nuevas matrices formadas
        else:
            print("Saliendo..") #Opción 3 del menú principal, se sale de programa.
            flag = False    
    return True   
               
if __name__ == "__main__":     
    menu_de_inicio() 

print(f"\nFin de proceso")