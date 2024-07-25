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
 "Lote en venta ubicado en la calle 71 entre 22 y 23, Casco Urbano, La Plata.-  EXCELENTE LOTE 11X30 UR1 CON LOZA CONSTRUIDA  VENDO LOTE zonificado U/R1, medidas 11x30, ubicado en barrio residencial próximo a avenidas 19, 25 y 72. Posee loza de 1º piso construida, superficie construida 141 m2 (11x13), con posibilidad de expandir a 2º piso y/o expandir la superficie de forma horizontal. Servicios todos. Orientado al sur.  Superficie total de lote 330m2. Posee portón metálico de ingreso.  Ideal vivienda multifamiliar.-  Permuta por departamento 2 dormitorios (Zonas parque san Martin, plaza Malvinas, aledaños)  Servicios: Cloacas, Gas","Lotes en calle Rio Reconquista, entre calles Atuel y Matanza, en Marcos Paz, provincia de Buenos Aires. Estos terrenos se encuentran en una zona privilegiada, rodeados de naturaleza y tranquilidad, pero a su vez cercanos a importantes vías de acceso y servicios.  El lote número 20 cuenta con una superficie total de 3550 m2, con medidas de 35.5 m. x 100 m., Mientras que el lote número 21 también tiene una superficie total de 3550 m2 y medidas de 35.5 m. x 100 m. Este último lote cuenta además con una hermosa cabaña de madera, ideal para disfrutar de momentos de descanso y relax en contacto con la naturaleza. ",
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