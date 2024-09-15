from Estudiantes.estudiantes import estudiantes, ingreso_materias
from Profesores.profesor import profesores
from VALIDACIONES.Validaciones import validacion_2dig, validacion_3dig, validacionmail, validar_contraseña, validar_mayus_nombre, validar_num, cuenta_existente_login, cuenta_existente_register
from MATRICES.matriz_alumnos import ingreso_alumnos
from MATRICES.matriz_profesor import ingreso_profes, user
def logeandose():   
    usuario,contra = user() #Pide usuario y contraseña
    flag=False
    cont=0 #Intentos
    while flag==False and cont<5:
        while validacionmail(usuario) == False and cont<5: #Se valida el mail
            cont += 1 #Máximo de 5 intentos.
            usuario,contra = user()
        num, apart = cuenta_existente_login(ingreso_alumnos,ingreso_profes,usuario,contra) #Se fija si existe una cuenta (estudiante o profesor), con ese nombre de usuario.
        if num == 1: #Existe un estudiante con ese nombre de usuario.
            flag=True
            ingreso_materias (apart)
            estudiantes(apart)
        elif num == 2: #Existe un profesor con ese nombre de usuario.
            flag = True
            profesores()
        else:  #En caso de no encontrar el usuario, vuelve a preguntar con un maximo de 5 intentos.
            cont += 1
            if cont<5:
                print()
                print("No se pudo acceder a una cuenta ya existente, por favor volver a intentarlo.")
                print()
                inicio_login=(input("\n1 Iniciar sesión.\n2 Volver atrás.\nElija un número: "))                
                #Validación de letra.
                while validar_num(inicio_login) == False:
                    inicio_login=(input("\n1 Iniciar sesión.\n2 Volver atrás.\nElija un número: "))
                #Validación de número.
                while validacion_2dig(inicio_login) == False:
                    print()
                    inicio_login=(input("\n1 Iniciar sesión.\n2 Volver atrás.\nElija un número: "))
                    while validar_num (inicio_login) == False:
                        inicio_login=(input("\n1 Iniciar sesión.\n2 Volver atrás.\nElija un número: "))                
                if int (inicio_login) == 1: #Vuelve a intentar el inicio de sesión.
                    usuario,contra = user()
                elif int (inicio_login) == 2: #Vuelve atrás, al menú principal.
                   return
            else:
                print("Numerosos intentos fallidos, reintentar nuevamente en unos minutos.") #En caso de llegar al maximo de intentos (cinco).

