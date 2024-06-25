import pandas as pd
import spacy

from .select_best_candidate import select_best_candidate

from .matcher import Matcher
from normalize import normalize


def rbm(input: pd.DataFrame) -> pd.DataFrame:
    MATCHER = Matcher()
    input= input.fillna("")
    data = []
    for _, row in input.iterrows():
        description= normalize(row["description"])
        candidate_pairs = MATCHER.get_pairs(description)

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
            "es_multioferta": None
        }
        select_best_candidate(candidate_pairs, estructura)
        estructura["description"] = description
        data.append(estructura)
    return pd.DataFrame(data, index=None)
