import json
def devolverjson():
    with open(r"C:\Users\santi\Downloads\p1_mita_grupo1_2024\p1_mita_grupo1_2024\GESTION_ACADEMICA\Base_de_datos\materias.json", "r", encoding="UTF-8") as archijson:
        return json.load(archijson) 
    
def guardarjson(objeto):
    with open(r"C:\Users\santi\Downloads\p1_mita_grupo1_2024\p1_mita_grupo1_2024\GESTION_ACADEMICA\Base_de_datos\materias.json", "w", encoding="UTF-8") as guardjson:
        return json.dump(objeto, guardjson)