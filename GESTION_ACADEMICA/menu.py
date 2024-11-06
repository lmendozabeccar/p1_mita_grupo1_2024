from loading.login import logeandose
from REGISTRO.Register import registro
from MATRICES.Menu_Diseño import mostrar_usuarios
print("\nSistema de Evaluación Académica\n")

mostrar_usuarios()
#Alumnos ya registrados en el sistema.

#Menú de inicio.
def menu_de_inicio():
    """
    pre: la función no recibe ningún dato, es el inicio del programa.
    pos: de acuerdo a las necesidades del usuario, puede redireccionarse a la función de login, a la de registro
    o a la de salir de la aplicación.
    """
    
    flag = True
    titulo = "\n¡Bienvenidos a nuestra Gestion Academica!"
    print(titulo.title().center(80))

    while flag == True:
        menu = "\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: "
        while True:
            try:
                inicio = int(input(menu)) #Menú de inicio.
            except ValueError:
                print("\nError. Debe ingresar un número")
            else:
                if inicio >= 1 and inicio <= 3:
                    break
                else:
                    print("\nDebe ingresar un número dentro de las opciones")

        if int (inicio)==1: #Se entra al inicio de sesión.
            valor = logeandose()
            if valor == True:
                return True

        elif int (inicio) == 2: #Se entra al registro.
            print("\n¡Registrate!")
            registro() #Se asignan las dos nuevas matrices formadas
        else:
            print("\nSaliendo..") #Opción 3 del menú principal, se sale de programa.
            flag = False    
    return True   
if __name__ == "__main__":     
    menu_de_inicio() 

print(f"\nFin de proceso")
    