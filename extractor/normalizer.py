import pandas as pd
from normalize import normalize

input_file =  '/home/apagano/OVS-extractor-idis/input/ground_truth_100_sin_inferencias.csv'
output_file = '/home/apagano/OVS-extractor-idis/input/ground_truth_100_sin_inferencias_normalizado.csv'

df = pd.read_csv(input_file, delimiter='|', dtype=str,keep_default_na=False) #Leo el archivo CSV como un dataFrame

for column in df.columns:
    df[column] = df[column].astype(str).apply(normalize)

df.to_csv(output_file,sep='|',index=False,na_rep='')



