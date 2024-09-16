from loading.login import logeandose
from VALIDACIONES.Validaciones import validacion_3dig, validar_num
from MATRICES.matriz_alumnos import ingreso_alumnos
from MATRICES.matriz_profesor import ingreso_profes
from REGISTRO.Register import registro
print()
#Alumnos ya registrados en el sistema.
#Menú de inicio.
def menu_de_inicio():
    flag = True
    print(f"\n¡Bienvenidos a nuestra Gestion Academica!")
    while flag!=False:
        menu = "\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: "
        inicio= input(menu) #Menú de inicio.
        while validar_num(inicio) == False: #Validacion para que sea un numero
            inicio= input(menu)
        while validacion_3dig (inicio)== False: #Validacion que sea un numero entre 1 y 3
            print()
            inicio=input(menu)
            while validar_num(inicio) == False: #Validacion para que sea un numero.
                inicio= input(menu)     
                                           
        if int (inicio)==1: #Se entra al inicio de sesión.
            if logeandose () == True:
                flag = False
                
        elif int (inicio) == 2: #Se entra al registro.
            print("¡Registrate!")
            registro(ingreso_alumnos,ingreso_profes)
        else:
            print("Saliendo..") #Opción 3 del menú principal, se sale de programa.
            flag = False       
if __name__ == "__main__":     
    menu_de_inicio() 

print(f"\nFin de proceso")