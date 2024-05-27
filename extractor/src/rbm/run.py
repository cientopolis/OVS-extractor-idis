import pandas as pd
import spacy

from .matcher import Matcher

NLP = spacy.load("es_core_news_lg")


def rbm(input: pd.DataFrame) -> pd.DataFrame:
    MATCHER = Matcher()
    data = []
    for _, row in input.iterrows():
        respuestas = MATCHER.get_pairs(row["descripcion"])
        data.append(
            {
                "descripcion": row["descripcion"],
                "direccion": respuestas["direccion"],
                "fot": respuestas["fot"],
                "irregular": respuestas["irregular"],
                "medidas": respuestas["medidas"],
                "esquina": respuestas["esquina"],
                "barrio": respuestas["barrio"],
                "frentes": respuestas["frentes"],
                "pileta": respuestas["pileta"],
                "urb_cerrada": respuestas["urb_cerrada"],
                "urb_semicerrada": respuestas["urb_semicerrada"], 
                "posesion": respuestas["posesion"],
                "preventa": respuestas["preventa"],
                "indiviso": respuestas["indiviso"],
                "a_demoler": respuestas["a_demoler"]
            }
        )
    return pd.DataFrame(data, index=None)
