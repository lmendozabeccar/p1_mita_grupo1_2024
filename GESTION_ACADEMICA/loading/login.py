from Estudiante.estudiantes import estudiantes
from Profesor.profesor import profesores
from VALIDACIONES.Validaciones import validacion_digitos, validacionmail, cuenta_existente_login
from MATRICES.matriz_alumnos import ingreso_alumnos
from MATRICES.matriz_profesor import ingreso_profes

#Pedir usuario y contraseña
def user ():
    username=str(input("Ingresar su mail de usuario: "))
    password=str(input("Ingresar contraseña: "))
    return username,password

def logeandose(matriz_legajos_notas, matriz_a_register, matriz_p_register):
    if matriz_a_register == []: #Estos condicionales verifican si la lista fue modificada por el registro. En tal caso, se usa la matriz nueva o la preestablecida
        matriz_alumnos_usar = ingreso_alumnos
    else:
        matriz_alumnos_usar = matriz_a_register 
        
    if matriz_p_register == []:
        matriz_profesores_usar = ingreso_profes
    else:
        matriz_profesores_usar = matriz_p_register 

    usuario,contra = user() #Pide usuario y contraseña
    flag=False
    cont=0 #Intentos
    while flag==False and cont<5:
        while validacionmail(usuario) == False and cont<5: #Se valida el mail
            cont += 1 #Máximo de 5 intentos.
            usuario,contra = user()
        
        num, legajo = cuenta_existente_login(matriz_alumnos_usar,matriz_profesores_usar,usuario,contra) #Se fija si existe una cuenta (estudiante o profesor), con ese nombre de usuario.
        if num == 1: #Existe un estudiante con ese nombre de usuario.
            flag=True
            valor, matriz_legajos_notas_act = estudiantes(matriz_legajos_notas, legajo)
            if valor == True:
                return (True, True) #Devuelve una tupla con dos True ya que esta funcion debe devolver siempre dos valores, sino se rompe el programa.
            else:
                return matriz_alumnos_usar, matriz_legajos_notas_act
                
        elif num == 2: #Existe un profesor con ese nombre de usuario.
            flag = True
            matriz_alumnos_act, matriz_legajos_notas_act = profesores(matriz_alumnos_usar, matriz_legajos_notas) #Le asigno a una matriz las notas actualizadas provenientes del crud de profesores
            if matriz_legajos_notas_act == True:
                return (True, True)
            else:
                return matriz_alumnos_act, matriz_legajos_notas_act
        else:  #En caso de no encontrar el usuario, vuelve a preguntar con un maximo de 5 intentos.
            cont += 1
            if cont<5:
                print("No se pudo acceder a una cuenta ya existente, por favor volver a intentarlo.")
                print()
                menu_error = "\n1 Volver a intentarlo.\n2 Volver al menú principal.\nElija un número: "
                inicio_login=(input(menu_error)) #Menu de arriba, modularizado       
                #Validación de letra.
                while validacion_digitos(inicio_login, 2) == False: #Valida que el número sea 1 o 2
                    inicio_login=(input(menu_error)) #Menu de arriba, modularizado                                           

                if int (inicio_login) == 1: #Vuelve a intentar el inicio de sesión.
                    usuario,contra = user()
                elif int (inicio_login) == 2: #Vuelve atrás, al menú principal.
                   flag = True
            else:
                print("Numerosos intentos fallidos, reintentar nuevamente en unos minutos.") 
                return False, False
                #En caso de llegar al maximo de intentos (cinco), sale y vuelve al menú