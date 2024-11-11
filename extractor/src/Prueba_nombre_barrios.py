import pandas as pd

# Cargo los archivos CSV
avisos_df = pd.read_csv("/home/apagano/OVS-extractor-idis/input/ground_truth_sin_inferencias.csv",delimiter="|")
barrios_df = pd.read_csv("/home/apagano/OVS-extractor-idis/input/nombre_barrios.csv")

# Convierto los nombres de barrios a una lista
nombres_barrios = barrios_df['NOMBRE_BARRIO'].tolist()

# Función para verificar si una descripción contiene algún nombre de barrio
def contiene_barrio(descripcion):
    # Convierto la descripción a minúsculas para una búsqueda sin distinción de mayúsculas
    descripcion = str(descripcion).lower()
    for barrio in nombres_barrios:
        if barrio.lower() in descripcion:
            return True
    return False

# Creo una nueva columna que indique si hay coincidencia con algún barrio
avisos_df['contiene_barrio'] = avisos_df['description'].apply(contiene_barrio)

# Muestro el resultado
print(avisos_df[['description', 'contiene_barrio']])
