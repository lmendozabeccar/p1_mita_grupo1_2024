from Estudiante.estudiantes import estudiantes
from Profesor.profesor import profesores
from VALIDACIONES.Validaciones import validacion_dig, validacionmail, validacion_cuenta_existente
#from MATRICES.matriz_alumnos import ingreso_alumnos
#from MATRICES.matriz_profesor import ingreso_profes

#Pedir usuario y contraseña
def user():
    """
    pre: no recibe ningún dato.
    pos: devuelve un mail y una contraseña, ambos ingresados por el usuario.
    """
    username=str(input("\nIngresar su mail de usuario: "))
    password=str(input("Ingresar contraseña: "))
    return username,password

def logeandose():
    """
    pre: el usuario en el menú de inicio, ingreso la opción 1 y fue redirigido a este menú, el menú de login. 
    pos: tiene varios caminos, en caso de coincidir el nombre de usuario se logea (ya sea apartado de profesores
    o de alumnos). En caso de no coincidir sigue preguntando con un máximo de 5 intentos.
    En caso de pretender volver al menú principal o superar el máximo de intentos, se vuelve al menú de inicio.
    """
    usuario,contra = user() #Pide usuario y contraseña
    flag=False
    cont=0 #Intentos
    while flag==False and cont<5:
        while validacionmail(usuario) == False and cont<5: #Se valida el mail
            usuario,contra = user()
        
        num, legajo, email = validacion_cuenta_existente(usuario,contra) #Se fija si existe una cuenta (estudiante o profesor), con ese nombre de usuario.
        if num == 1: #Existe un estudiante con ese nombre de usuario.
            flag=True
            valor = estudiantes(legajo, email)
            if valor == True:
                return True
            else:
                return False
                
        elif num == 2: #Existe un profesor con ese nombre de usuario.
            flag = True
            valor = profesores(email) #Le asigno a una matriz las notas actualizadas provenientes del crud de profesores
            if valor == True:
                return True
            else:
                return False
        else:  #En caso de no encontrar el usuario, vuelve a preguntar con un maximo de 5 intentos.
            cont += 1
            if cont<5:
                print("\nNo se pudo acceder a una cuenta ya existente, por favor volver a intentarlo.")
                menu_error = "\n1 Volver a intentarlo.\n2 Volver al menú principal.\nElija un número: "
                inicio_login=(input(menu_error)) #Menu de arriba, modularizado       
                #Validación de letra.
                while validacion_dig(inicio_login, 2) == False: #Valida que el número sea 1 o 2
                    inicio_login=(input(menu_error)) #Menu de arriba, modularizado                                           

                if int (inicio_login) == 1: #Vuelve a intentar el inicio de sesión.
                    usuario,contra = user()
                elif int (inicio_login) == 2: #Vuelve atrás, al menú principal.
                   flag = True
                   return False
            else:
                print("\nNumerosos intentos fallidos, reintentar nuevamente en unos minutos.") 
                return True
                #En caso de llegar al maximo de intentos (cinco), sale y vuelve al menú