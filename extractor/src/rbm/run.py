import pandas as pd
import spacy

from .matcher import Matcher

NLP = spacy.load("es_core_news_lg")


def rbm(input: pd.DataFrame) -> pd.DataFrame:
    MATCHER = Matcher()
    data = []
    for _, row in input.iterrows():
        respuestas = MATCHER.get_pairs(row["descripcion"])
        respuestas["descripcion"]=row["descripcion"]
        data.append(respuestas)
    return pd.DataFrame(data, index=None)
