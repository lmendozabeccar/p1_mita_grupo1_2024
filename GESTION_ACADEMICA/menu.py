from loading.login import logeandose
from VALIDACIONES.Validaciones import validacion_dig
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

    matriz_a_register, matriz_p_register = [], [] #Se inicializan las matrices de est y prof vacías para que luego sean modificadas por el registro
    matriz_legajos_notas = {} #Se inicializa el diccionario de notas vacía
    while flag == True:
        menu = "\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: "
        inicio= input(menu) #Menú de inicio.
        while validacion_dig (inicio, 3)== False: #Validacion que sea un numero entre 1 y 3
            inicio=input(menu)
                                           
        if int (inicio)==1: #Se entra al inicio de sesión.
            matriz_alumnos_act, matriz_legajos_notas_act = logeandose (matriz_legajos_notas, matriz_a_register, matriz_p_register)
            if matriz_legajos_notas_act == True:
                flag = False
            elif matriz_legajos_notas_act == False:
                return 1
            else:
                matriz_legajos_notas = matriz_legajos_notas_act #Se le asignan las nuevas matrices actualizadas
                matriz_a_register = matriz_alumnos_act
                
        elif int (inicio) == 2: #Se entra al registro.
            print("¡Registrate!")
            matriz_a_register, matriz_p_register = registro(ingreso_alumnos,ingreso_profes) #Se asignan las dos nuevas matrices formadas
        else:
            print("Saliendo..") #Opción 3 del menú principal, se sale de programa.
            flag = False       
               
if __name__ == "__main__":     
    menu_de_inicio() 

print(f"\nFin de proceso")