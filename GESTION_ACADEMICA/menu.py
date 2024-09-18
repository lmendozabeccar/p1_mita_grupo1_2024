from loading.login import logeandose
from VALIDACIONES.Validaciones import validacion_3dig
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

    matriz_notas, matriz_alumnos, matriz_profesores = [], [], []
    while flag == True:
        menu = "\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: "
        inicio= input(menu) #Menú de inicio.
        while validacion_3dig (inicio)== False: #Validacion que sea un numero entre 1 y 3
            print()
            inicio=input(menu)
                                           
        if int (inicio)==1: #Se entra al inicio de sesión.
            valor = logeandose (matriz_notas, matriz_alumnos, matriz_profesores)
            if valor == True: #Se mandan como parametro las nuevas matrices del register
                flag = False
                
        elif int (inicio) == 2: #Se entra al registro.
            print("¡Registrate!")
            matriz_notas, matriz_alumnos, matriz_profesores = registro(ingreso_alumnos,ingreso_profes) #Se asignan las dos nuevas matrices formadas
        else:
            print("Saliendo..") #Opción 3 del menú principal, se sale de programa.
            flag = False       
               
if __name__ == "__main__":     
    menu_de_inicio() 

print(f"\nFin de proceso")