from VALIDACIONES.Validaciones import validacion_2dig, validacion_3dig, validacionmail, validar_contraseña,validar_num, validar_mayus_nombre, cuenta_existente_register
from MATRICES.matriz_alumnos import ingreso_alumnos
from MATRICES.matriz_profesor import ingreso_profes
from MATRICES.matriz_calificaciones import matriz_notas
def registro(listaalumnos, listaprofesor):
    flag = False
    menu_registro = "\n1 Registro como alumno.\n2 Registro como profesor.\n3 Volver atrás.\nElija un número: "
    menu_mail = "Ingresar su mail de usuario nuevo: "
    menu_nombre = "Ingresar su nombre y apellido, ambas comenzando con mayúsculas: "
    menu_contraseña = "Ingrese su contraseña: "
    menu_error = "\n1 Volver a intentar el inicio de sesión. \n2 Volver al inicio \nElija un número: "
    while flag == False:
        inicio_registro=(input(menu_registro)) #Modularizacion menú.
        while validacion_3dig (inicio_registro) == False: #Valida que el numero sea entre 1 y 3
            inicio_registro=(input(menu_registro))
            while validar_num (inicio_registro) == False: #Valida que sea un numero
                inicio_registro=(input(menu_registro))       
                 
        if int(inicio_registro) ==3: #Vuelve al menú de inicio.
            return [], [], [] 
        print()
        #Validación Mail.
        user=str(input(menu_mail)) #Modularización de menú
        while validacionmail(user) == False: #Validacion que el mail tenga las pautas necesarias.
            user=str(input(menu_mail))   
                         
        if cuenta_existente_register (ingreso_alumnos,ingreso_profes,user) != False: #Se fija si hay una cuenta existente, en caso que sea True, entra . 
            if int (inicio_registro)==1: #Si se registra como alumno
                nom=str(input(menu_nombre))
                while validar_mayus_nombre(nom) == False: #Valida que el nombre y el apellido comience con mayuscula.
                    nom=str(input(menu_nombre)) 
                    
                pas=str(input(menu_contraseña))        
                while validar_contraseña (pas) == False: #Valida que la contraseña tenga, al menos, una mayuscula, una minuscula y un numero, sin espacios en blanco.
                    pas=str(input(menu_contraseña))       

                legajo = (matriz_notas[-1][0] + 1) #Legajo= ultimo legajo +1
                listaalumnos.append([str(legajo), user, pas, nom]) #Append en la lista de alumnos.                          

                notas = [-1,-1,-1,-1,-1]
                matriz_notas.append((legajo, notas)) #Append de legajo, (linea 40) y las notas cargadas como -1
                
                flag = True                 
                       
            if int (inicio_registro)==2: #Si se registra como profesor
                nom=str(input(menu_nombre))
                while validar_mayus_nombre(nom) == False: #Valida que el nombre y el apellido comience con mayuscula.
                    nom=str(input(menu_nombre)) 

                pas=str(input(menu_contraseña))
                while validar_contraseña (pas) == False: #Valida que la contraseña tenga, al menos, una mayuscula, una minuscula y un numero, sin espacios en blanco.
                    pas=str(input(menu_contraseña))                            
                listaprofesor.append([user, pas, nom]) #En caso de superar todas las validaciones, agrega a la lista de profesores al nuevo profesor.
                flag = True                
                    
        else: #En caso de usuario ya existente.
            inicio_usuario_exist=(input(menu_error))
            while validacion_2dig (inicio_usuario_exist) == False: #Validacion que sea un numero entre 1 y 2.
                inicio_usuario_exist=(input(menu_error))

            if int(inicio_usuario_exist) == 2: #Vuelve al menú de inicio, en caso de elegir la opción 2.
                return [], [], []       
    return matriz_notas, listaalumnos, listaprofesor