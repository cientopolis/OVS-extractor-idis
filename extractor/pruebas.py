from collections import OrderedDict
import pandas as pd
import spacy

from src.helper import reduce_superstrings
from src.rbm.select_best_candidate import select_best_candidate

from src.rbm.matcher import Matcher
from normalize import normalize
NLP = spacy.load("es_core_news_lg")
import re

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

def rbm():
    MATCHER = Matcher()

    input= [
        "Venta de lotes dentro del barrio semi-cerrado ''El Juncal'', en la localidad de Melchor Romero Disponibilidad: 2\r\nLote 21 medidas: 10 x 25 Lote 42 medidas: 10 x 25 Servicios: Agua corriente y Luz Valor: U$S7000 (x lote)\r\nPUEDE TOMAR VEHICULO COMO PARTE DE PAGO Aviso publicado por Pixel Inmobiliario (Servicio de\r\nPáginas Web para Inmobiliarias). #1437",
        ]

    data = []
    for description in input:
        for token in NLP(description):
            print(token.text, token.pos_, token.dep_)
        candidate_pairs = MATCHER.get_pairs(normalize(description))

        if (candidate_pairs["es_multioferta"] or "lotes" in description.lower()):
            # enumera más de una medida de lote, o mas de un numero de lote
            if description.lower().split().count("lotes")>1 or (len(reduce_superstrings(set([x.lower() for x in candidate_pairs["es_multioferta"]])))>2) or (len(medidas(candidate_pairs["medidas"]))>1) or (len(reduce_superstrings(set([x.lower() for x in candidate_pairs["dir_lote"]])))>1):
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
            "es_monetizable": None
        }

        select_best_candidate(candidate_pairs, estructura)
        estructura["description"] = description
        data.append(estructura)
    return pd.DataFrame(data, index=None)

rbm()