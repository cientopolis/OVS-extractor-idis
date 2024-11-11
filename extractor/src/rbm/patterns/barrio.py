import pandas as pd
# cargar el archivo con los nombres de barrios
barrios_df = pd.read_csv("/home/apagano/OVS-extractor-idis/input/nombre_barrios.csv")
#convierto a lista el df
nombre_barrios = barrios_df['NOMBRE_BARRIO'].tolist()

def barrio(description):    
    description = str(description).lower()  
    for barrio in nombre_barrios:
        if barrio.lower() in description:
            return barrio  
    return ""  

