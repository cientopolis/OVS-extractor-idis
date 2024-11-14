import pandas as pd
# cargar el archivo con los nombres de barrios
barrios_df = pd.read_csv("/home/apagano/OVS-extractor-idis/input/nombre_barrios.csv")
#convierto a lista el df
nombre_barrios = barrios_df['NOMBRE_BARRIO'].tolist()

def barrio_coincidencia_archivo(description):    
    description = str(description).lower()  
    for barrio in nombre_barrios:
        if barrio.lower() in description:
            return barrio  
    return ""  


INICIO_NOMBRE = ["PROPN","DET"]
NOMBRE_BARRIO = ["PROPN", "DET", "ADP", "NUM"]
DESCRIPCION = ["PRON", "VERB", "ADP", "NOUN", "DET", "ADJ"]
INICIO_DESCRIPCION = ["PRON", "VERB", "NOUN"]

BARRIO_SINONIMOS = ["barrio", "estancia", "country", "club", "finca", "sector", "urbanizacion"] #debemos mejorar el helper.py
        
def barrio():
    return  list([
                #barrio sin DESCRIPCION -> no aportan precisión
                [{"LOWER": {"IN":BARRIO_SINONIMOS}},{"POS": "PROPN"}],
                [{"LOWER": {"IN":BARRIO_SINONIMOS}},{"POS": {"IN":INICIO_NOMBRE}},{"POS": {"IN": NOMBRE_BARRIO}, "OP":"*"},{"POS": "PROPN"}],

                #barrio con DESCRIPCION
                #no aporta
                #[{"LOWER": {"IN":BARRIO_SINONIMOS}},{"POS":{"IN":INICIO_DESCRIPCION}},{"POS": {"IN":DESCRIPCION}, "OP":"*"},{"POS": "PROPN"}],
                [{"LOWER": {"IN":BARRIO_SINONIMOS}},{"POS":{"IN":INICIO_DESCRIPCION}},{"POS": {"IN":DESCRIPCION}, "OP":"*"},{"POS": {"IN":INICIO_NOMBRE}},{"POS": {"IN": NOMBRE_BARRIO}, "OP":"*"},{"POS": "PROPN"}],
                
                #no aporta
                #[
                #    {"LOWER": {"IN": ["estancia", "barrio", "country", "club"]}},
                #    {"POS": "PROPN", "OP": "+"},
                #],
            
            ])