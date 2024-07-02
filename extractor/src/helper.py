import re 
import spacy 

NLP = spacy.load("es_core_news_lg")

def descubrir_nuevos(predichos: dict):
    if predichos["irregular"] == "" and (
        len(set(get_numeros(predichos["medidas"]))) > 2
        or "martillo" in predichos["medidas"]
    ):
        predichos["irregular"] = True

    if predichos["esquina"] and predichos["frentes"] == "":
        predichos["frentes"] = 2.0

    return predichos

def get_numeros(cadena: str):
        return re.findall(r"\b\d+(?:[.,]\d+)?\b", cadena)

def clean_direccion(cadena: str):
    cadena= re.sub(r"^\. ", "", cadena)
    
    if  (NLP(cadena))[0].pos_ == "ADP":
        cadena= cadena.split()[1:]
        cadena= " ".join(cadena)
    
    if  (NLP(cadena))[-1].pos_ == "ADP":
        cadena= cadena.split()[:-1]
        cadena= " ".join(cadena)

    return cadena.strip()