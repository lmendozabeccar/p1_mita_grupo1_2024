from Proceso_Login.login import logeandose
from VALIDACIONES.Validaciones import validacion_2dig, validacion_3dig, validacionmail, validar_contraseña, validar_mayus_nombre, validar_num, cuenta_existente_login, cuenta_existente_register
from MATRICES.matriz_alumnos import ingreso_alumnos
from MATRICES.matriz_profesor import ingreso_profes
from Proceso_Registro.Register import registro
print()
#Alumnos ya registrados en el sistema.
#Menú de inicio.
def menu_de_inicio():
    flag = True
    print(f"\n¡Bienvenidos a nuestra Gestion Academica!")
    while flag!=False:
        inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ") #Menú de inicio.
        #Validación para que no sea una letra.
        while validar_num(inicio) == False:
            inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")
        #Validacion del número.
        while validacion_3dig (inicio)== False:
            print()
            inicio=input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")
            while validar_num(inicio) == False:
                inicio= input("\n1 Iniciar sesión.\n2 Registrarse\n3 Salir \nElija un número: ")                                
        if int (inicio)==1: #Se entra al inicio de sesión.
            logeandose()
            flag = False
        elif int (inicio) == 2: #Se entra al registro.
            print("¡Registrate!")
            registro(ingreso_alumnos,ingreso_profes)
            flag = False
            inicio_2=input("Qué desea realizar ahora?\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            #Validación de letra.
            while validar_num(inicio_2) == False:
                inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            #Validación de número.            
            while validacion_2dig (inicio_2) == False: 
                print()
                inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
                while validar_num (inicio_2) == False:
                    inicio_2=input("\n1 Iniciar sesión.\n2 No iniciar sesión.\nElija un número: ")
            if  int (inicio_2) == 1: #Se entra al inicio de sesión.
                logeandose()
                flag = False
            elif  int (inicio_2)==2: #Se sale del programa.
                print("Saliendo..")
                flag = False
        else:
            print("Saliendo..") #Opción 3 del menú principal, se sale de programa.
            flag = False       
if __name__ == "__main__":     
    menu_de_inicio() #PQ?

print(f"\nFin de proceso")