import json

def loadjson():
    """
    pre: no recibe ningun dato.
    pos: contenido del archivo json en forma de diccionario.
    """
    archivo = r"GESTION_ACADEMICA\Base_de_datos\materias.json"
    with open(archivo, "r", encoding="UTF-8") as archivobd:
            return json.load(archivobd)

def guardarjson(objeto):
    """
    pre: recibe la matriz de notas del alumno.
    pos: retorna y escribe en el json lo recibido.
    """
    try:
        with open(r"GESTION_ACADEMICA\Base_de_datos\materias.json", "w", encoding="UTF-8") as guardjson:
            return json.dump(objeto, guardjson, ensure_ascii=False) #Se escapan o no no los caracteres ASCII, para que se vean o no los acentos.
    except (FileNotFoundError, TypeError, PermissionError):
        print("\nNo se encontró el archivo de base de datos.")
    except Exception as e:
        print(f"\nError inesperado: {e}")

def devolverjson():
    """
    pre: no recibe nada.
    pos: retorna contenido del json como diccionario. En caso de que error, retorna un diccionario vacio.
    """
    try:
        matriz_legajos_notas = loadjson()  # Valida el diccionario notas para ver si existe o no
    except (FileNotFoundError, json.JSONDecodeError, TypeError):
        return {}
    else: 
         return matriz_legajos_notas
    
              