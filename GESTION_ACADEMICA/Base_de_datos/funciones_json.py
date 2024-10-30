import json

def loadjson():
    archivo = r"GESTION_ACADEMICA\Base_de_datos\materias.json"
    with open(archivo, "r", encoding="UTF-8") as archivobd:
            return json.load(archivobd)
def guardarjson(objeto):
    with open(r"GESTION_ACADEMICA\Base_de_datos\materias.json", "w", encoding="UTF-8") as guardjson:
        return json.dump(objeto, guardjson, ensure_ascii=False) #Se escapan o no no los caracteres ASCII, 
def devolverjson():
    try:
        matriz_legajos_notas = loadjson()  # Valida el diccionario notas para ver si existe o no
    except (FileNotFoundError, json.JSONDecodeError, TypeError):
        return {}
    else: 
         return matriz_legajos_notas
    
              