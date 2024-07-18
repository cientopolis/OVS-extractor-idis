import re
import pandas as pd
import spacy

from src.helper import reduce_superstrings

from .select_best_candidate import select_best_candidate

from .matcher import Matcher
from normalize import normalize

def get_numeros(cadena: str):
        return re.findall(r"\b\d+(?:[.,]\d+)?\b", cadena)


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
    for _, row in input.iterrows():
        description= normalize(row["description"])
        candidate_pairs = MATCHER.get_pairs(description)

        #detectar multioferta debe ser el primero porque de esto depende la selección del mejor candidato

        # condiciones para multioferta:
        # le dió true el matcher, y además:
            # 1) le dió que hay más de 1 lote
            # 2) le dió que hay más de una medida
        # if (candidate_pairs["es_multioferta"] and (candidate_pairs["urb_cerrada"] or candidate_pairs["urb_semicerrada"])):
        #     candidate_pairs["es_multioferta"]= ""
        if (candidate_pairs["es_multioferta"]):
            if (len(medidas(candidate_pairs["medidas"]))>1):
                candidate_pairs["es_multioferta"]=True
            else:
                candidate_pairs["es_multioferta"]=""
            if (len(reduce_superstrings(set([x.lower() for x in candidate_pairs["dir_lote"]])))>1):
                candidate_pairs["es_multioferta"]=True
            else:
                candidate_pairs["es_multioferta"]=""

        # elif ((len(reduce_superstrings(set(candidate_pairs["dir_lote"])))==1)):
        #     candidate_pairs["es_multioferta"]= ""

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
