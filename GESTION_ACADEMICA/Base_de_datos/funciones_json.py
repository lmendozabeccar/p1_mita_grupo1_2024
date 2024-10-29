import json

def devolverjson():
    archivo = r"C:\Users\santi\OneDrive\Documents\GitHub\p1_mita_grupo1_2024\GESTION_ACADEMICA\Base_de_datos\materias.json"
    with open(archivo, "r", encoding="UTF-8") as archivobd:
            return json.load(archivobd)
def guardarjson(objeto):
    with open(r"C:\Users\santi\OneDrive\Documents\GitHub\p1_mita_grupo1_2024\GESTION_ACADEMICA\Base_de_datos\materias.json", "w", encoding="UTF-8") as guardjson:
        return json.dump(objeto, guardjson)