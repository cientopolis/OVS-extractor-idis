import pandas as pd

# cargo archivos CSV
avisos_df = pd.read_csv("/home/apagano/OVS-extractor-idis/input/ground_truth_sin_inferencias.csv",delimiter="|")
barrios_df = pd.read_csv("/home/apagano/OVS-extractor-idis/input/nombre_barrios.csv")

# nombres de barrios a una lista
nombres_barrios = barrios_df['NOMBRE_BARRIO'].tolist()

# verificar si una descripción contiene algún nombre de barrio del csv nombre_barrios.csv
def contiene_barrio(description):    
    description = str(description).lower()
    for barrio in nombres_barrios:
        if barrio.lower() in description:
            return barrio
    return ""

# para visualizacion de resultados
avisos_df['contiene_barrio'] = avisos_df['description'].apply(contiene_barrio)

# muestro el resultado
print(avisos_df[['description', 'contiene_barrio']])
