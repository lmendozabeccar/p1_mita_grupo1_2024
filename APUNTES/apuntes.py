
'''
Potencias
lista[-1]
for i in lista
#LISTAS POR COMPRENSIÓN:
num = [1, 2, 3, 4, 5]
lista = [expresión(el calculo) for num in numeros]
## CON FILTROS
lista = [expresión(el calculo) for num in numeros if num%2 == 0]
lista = [expresión(el calculo) if num%2 == 0 else num for num in numeros]

#METODOS
lista.append(valor) (Agrega sólo un elemento)
lista.extend([valor1, valor2, valor3]) (Agrega varios valores)
estaciones = ["verano", "otoño", "primavera"]
estaciones.insert(parametro, "invierno") (agrega elementos en cualquier lugar de la lista (parametro 1)) --- estaciones = [verano, otoño, inverno, primavera]
lista.remove(paramatro) (Elimina un elemento por su nombre)
lista.pop() (Elimina el ultimo elemento de la lista y lo devuelve)
lista.pop(parametro) (Elimina el elemento de esa posicion de la lista y lo devuelve)
lista.clear() (Elimina todo)
lista.index(parametro) (Te devuelve la posicion de ese valor en la lista)
lista.count(parametro) (Te devuelve la cantidad de veces que aparece ese parametro en la lista)
lista.sort() (ordena la lista)
lista.sort(reverse=True) (ordena la lista de forma al reves (descendente))
lista.reverse() ()

#FUNCIONES
len() (largo)
sum() (suma de toda la lista)
max() (valor mas alto de la lista)
min() (valor minimo de la lista)
#Slicing, se puede hacer LO MISMO con cadenas
lista[inicio:fin:paso] (Extrae una parte de la lista, primer indice incluido, segundo no. Paso opcional, se puedo omitir uno de los subindices. Se pude con indices negativos)
lista[::-1] (Muestra lista invertida)
lista[2:4] = [10 , 15] (Reemplaza valores. No se agregan)
lista[2:4] = [] (Elimina los valores dentro de ese intervalo)
for i in lista[inicio:fin] (itera la lista con solo esas posiciones)
#concatenar listas sumandolas entre si : lista1+lista2

#Copiar listas
listacopia = lista[:] (copia la lista)
listacopia = list(lista)
listacopia = lista.copy()

lista[funcion()] (Siempre que la funcion devuelva un entero)
list("cadena") (convierte una cadena a una lista (caraceter por caracter))

#Desempaquetado
lista = [1, 2, 3, 4]
num, num2, num3, num4 = lista (Cada numero es asignado por cada elemento de la lista. Tiene que coincidir con el largo de la lista)
frase = 'hola "Lucas", buenas' (Usar las comillas dentro de un string)

#Operaciones con cadenas 
Concatenacion(+) (Concatena dos cadenas)
Multiplicacion(*) 
Adicion(+=) (añade un caracter a lo ultimo)
in (Compara si un elemento pertenece a la cadena, booleano)
is (Compara las cadenas para saber si son exactamente iguales, booleno)
len() (largo de la cadena)
max() (valor mas alto alfanumerico o numerico)
min() (valor mas chico)

#Metodos con cadenas
cadena = "Hola mundo"
cadena.index("mundo") (devuelve en que posicion está el parametro) --> 6
cadena.count("o") (Devuelve la cantidad de veces que esta el parametro en la cadena)
cadena.replace(parametro1, parametro2) (Parametro 1: Valor a reemplazar. Parametro 2: Valor que reemplazo)
cadena.strip() (Elimina los espacios de la derecha y de la izquierda) .lstrip y .rstrip (solo izquierda, o solo derecha respectivamente)
cadena.center(parametro1, "parametro2") (La cadena es rellenada por el numero del parametro 1, con los caracteres del parametro 2)
cadena.ljust(parametro1, "parametro2") o .rjust ()
str() Pasar a string la cadena :)
cadena.zfill(parametro) (Se rellena con ceros la cadena, con la longitud del parametro)
cadena.isalnum (Si tiene caracteres alfanumericos, booleano)
cadena.isdigit (Si tiene nuemeros ,estricto solo numeros, booleano)
cadena.isdecimal (Si tiene caracteres numeros, booleano)
cadena.find(parametro1, inicio, fin) (parametro 1: Lo que quiero buscar. Con inicio y fin (de izquierda a derecha))
cadena.rfind(parametro1, inicio, fin) (lo mismo, pero de derecha a izquierda)
cadena.capitalize (Solo la primera pasa a ser mayuscula)
cadena.title (Reemplaza a mayuscula luego de un espacio)
cadena.lower (minuscula)
cadena.upper (mayuscula)
cadena.swapcase (invierte entre mayusculas y minusculas)
cadena.split(separador, cantidad) (hace una lista dividida por cada una de los separadores, como las "," por ej.)
cadena.splitlines(keeplinebreaks) (divide una cadena en una lista en los saltos de linea) (Recomendado no usar)
cadena.partition(separador) (Devuelve una tupla en lugar de una lista, con el separador)
separador.join() ej: " ".join(cadena) --> Pasa una lista de cadenas de texto a una cadena sola, todo unido por el separador

#Formato de cadenas
print("Legajo {}, Nombre: {}, Nota: {}".format(legajo, nombre, nota)) 
##F Strings (lo mejor)
cadena1 = 25
cadena2 = Diciembre
cadena3 = f"Navidad es el {cadena1} de {cadena2}"
print(cadena3) --> Navidad es el 25 de noviembre
print(f'{23*2+12}'
cad = f'|{num}ˆlargo|' (Lo centra, con el largo, o con > < se puede hacer un margen a la derecha o a la izquierda)

\n salto de linea
\" comillas dobles
\' comilla simple

------CLASE4-------
###Funciones
def funcion(valor="hola") --> En caso de que la función no reciba un parámetro
se puede no respetar el orden de los parametros de la funcion ----> funcion(edad=15, nombre="lucas")

##Lambda --> Guarda la definición de la función
funcion = lambda x, y: x + y
print(funcion(3, 4)) (Salida: 7)
#Map --> la x se reemplaza por cada elemento | operación | parametro
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
#Filter --> valor de cada elemento | condicion | parametro
pares = list(filter(lambda x: x % 2 == 0, numeros))
#Reduce
from functools import reduce
producto = reduce(lambda x, y: x * y, numeros)
print(producto) (Salida: 24)

###Modularizar con archivos
En el otro archivo, import nombre_de_archivo (solo el nombre)
Una vez importado se puede usar, por ejemplo: nombre_de_archivo.suma() 

#####DICCIONARIOS
for key in diccionario:
    print(f'{key}: {diccionario[key]}') --> recorrer un diccionario

'''