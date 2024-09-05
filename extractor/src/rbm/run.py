import re
import pandas as pd
import spacy

from src.helper import reduce_superstrings

from .select_best_candidate import select_best_candidate

from .matcher import Matcher
from normalize import normalize

def get_numeros(cadena: str):
        return re.findall(r"\b\d+(?:[.,]\d+)?\b", cadena)

def descartar_ultimo_token(lista):
    nueva_lista = []
    for elemento in lista:
        if (elemento.endswith(".") or elemento.endswith(",") or elemento.endswith("(")):
            nuevo_elemento= elemento[:-1]
        else:
            tokens =elemento.split()  # Dividir el elemento en tokens
            nuevo_elemento = ' '.join(tokens[:-1])  # Unir todos los tokens excepto el último
        nueva_lista.append(nuevo_elemento.strip())
    return nueva_lista

def medidas(predichos):

    if not predichos:
        return ""
    result= []
    for candidato in list(reduce_superstrings(set(predichos))):
        medidas = ""
        for numero in list(map(str, get_numeros(candidato))):
            medidas += numero + " x "
        
        if (medidas.count("x")>1):
            medidas= medidas.replace(",",".")
            result.append(medidas.rstrip(" x"))
    return result

def rbm(input: pd.DataFrame) -> pd.DataFrame:
    MATCHER = Matcher()
    input= input.fillna("")
    data = []

    #i=1  para debuggear
    for _, row in input.iterrows():
        description= normalize(row["description"])
        #print(f"fila {i}: {description} \n") para debugger
        #i +=1  para debuggear
        candidate_pairs = MATCHER.get_pairs(description)
        candidate_pairs["dir_nro"]= descartar_ultimo_token(candidate_pairs["dir_nro"])
        candidate_pairs["dir_interseccion"]= descartar_ultimo_token(candidate_pairs["dir_interseccion"])
        

        #detectar multioferta debe ser el primero porque de esto depende la selección del mejor candidato

        if (candidate_pairs["es_multioferta"] or "lotes" in description.lower()):
            # enumera más de una medida de lote, o mas de un numero de lote
            if description.lower().split().count("lotes")>2 or (len(reduce_superstrings(set([x.lower() for x in candidate_pairs["es_multioferta"]])))>2) or (len(medidas(candidate_pairs["medidas"]))>1) or (len(reduce_superstrings(set([x.lower() for x in candidate_pairs["dir_lote"]])))>1):
                candidate_pairs["es_multioferta"]=True
            else:
                candidate_pairs["es_multioferta"]=""

        estructura =  {
            "direccion": None,
            "fot": None,
            "irregular":None,
            "medidas": None,
            "esquina": None,
            "barrio": None,
            "frentes": None,
            "pileta": None,
            "urb_cerrada":  None,
            "posesion": None,
            "urb_semicerrada": None,
            "preventa": None,
            "indiviso": None,
            "a_demoler": None,
            "es_multioferta": None,
            "es_monetizable": None,
            "loteo_ph": None, 
        }
        select_best_candidate(candidate_pairs, estructura)
        estructura["description"] = description
        data.append(estructura)
    return pd.DataFrame(data, index=None)
