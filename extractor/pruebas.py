import pandas as pd
import spacy

from src.rbm.select_best_candidate import select_best_candidate

from src.rbm.matcher import Matcher
from normalize import normalize
NLP = spacy.load("es_core_news_lg")


def rbm():
    MATCHER = Matcher()
    input= [
      "ATENCIÓN CONSTRUCTORAS: Excelente lote de 8.66 de Frente x 35 de largo, ideal inversión para construcción de departamentos en torre, emprendimiento o vivienda, en zona centrica En inmejorable ubicación sobre la calle Sitio de Montevideo entre Salta y Oncativo. posee un FOS de 0.6 y un FOT de 3. CONSULTE OPCIONES. SE ESCUCHAN OFERTAS. SE TOMA PROPIEDAD TERMINADA POR MENOR VALOR.",
       "Ubicados sobre la Calle De Luca entre calle Alsina y Av. San Martín (arteria principal de acceso). A sólo 350 metros de la Ruta Provincial N° 6. Localidad de Los Cardales, Partido de Exaltación de la Cruz, Provincia de Buenos Aires. Características: Se trata de dos terrenos ubicados en el casco urbano de Los Cardales. Se encuentran dentro de la Zona Residencial Comercial de Densidad Media Baja (RCmb) acorde al Código de Planeamiento de Exaltación de la Cruz en la cuál se admite la edificación de departamentos y locales comerciales. Con indicadores de ocupación de: FOS: O.6 y FOT: 1." ]
    
    data = []
    for description in input:
        for token in NLP(description):
            print(token.text, token.pos_, token.dep_)
        candidate_pairs = MATCHER.get_pairs(normalize(description))

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