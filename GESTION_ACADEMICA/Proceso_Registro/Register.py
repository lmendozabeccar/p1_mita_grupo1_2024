from VALIDACIONES.Validaciones import validacion_2dig, validacion_3dig, validacionmail, validar_contraseña, validar_mayus_nombre, validar_num, cuenta_existente_login, cuenta_existente_register
from MATRICES.matriz_alumnos import ingreso_alumnos
from MATRICES.matriz_profesor import ingreso_profes
def registro(listaalumnos, listaprofesor):
    flag = False
    while flag == False:
        print()
        inicio_registro=(input("\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "))
        #Validación de letra.
        while validar_num(inicio_registro) == False:
            inicio_registro=(input("\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "))
        #Validación de número.
        while validacion_3dig (inicio_registro) == False:
            print()
            inicio_registro=(input("\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "))
            while validar_num (inicio_registro) == False:
                inicio_registro=(input("\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "))        
        if int(inicio_registro) ==3: #Vuelve al menú de inicio.
                return
        #Validación Mail.
        user=str(input("Ingresar su mail de usuario nuevo: "))
        while validacionmail(user) == False:
            user=str(input("Ingresar su mail de usuario nuevo: "))                
        if cuenta_existente_register (ingreso_alumnos,ingreso_profes,user) != False: #Se fija si hay una cuenta existente, en caso que sea True, entra . 
            if int (inicio_registro)==1: #Si se registra como alumno
                nom=str(input("Ingresar su nombre y apellido, ambas comenzando con mayúsculas: "))
                while validar_mayus_nombre(nom) == False: #Valida que el nombre y el apellido comience con mayuscula.
                    print()
                    nom=str(input("Ingresar su nombre y apellido, ambas comenzando con mayúsculas: ")) 
                pas=str(input("Ingrese su contraseña: "))        
                while validar_contraseña (pas) == False: #Valida que la contraseña tenga, al menos, una mayuscula, una minuscula y un numero, sin espacios en blanco.
                    print()
                    pas=str(input("Ingrese su contraseña: "))                            
                listaalumnos.append([user, pas, nom]) #En caso de superar todas las validaciones, agrega a la lista de alumnos al nuevo alumno.
                flag = True                        
            if int (inicio_registro)==2: #Si se registra como profesor
                pas=str(input("Ingrese su contraseña: "))
                while validar_contraseña (pas) == False: #Valida que la contraseña tenga, al menos, una mayuscula, una minuscula y un numero, sin espacios en blanco.
                    print()
                    pas=str(input("Ingrese su contraseña: "))                            
                listaprofesor.append([user, pas]) #En caso de superar todas las validaciones, agrega a la lista de profesores al nuevo profesor.
                flag = True                    
        else: #En caso de usuario ya existente.
            print()
            inicio_usuario_exist=(input("\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "))
            #Validación de letra.
            while validar_num(inicio_usuario_exist) == False:
                inicio_usuario_exist=(input("\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "))
            #Validación de número.
            while validacion_2dig (inicio_usuario_exist) == False:
                print()
                inicio_usuario_exist=(input("\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "))
                while validar_num (inicio_usuario_exist) == False:
                    inicio_usuario_exist=(input("\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "))
            if int(inicio_usuario_exist) == 2: #Vuelve al menú de inicio, en caso de elegir la opción 2.
                return           
    return listaalumnos,listaprofesor