import re 
import spacy

from src.rbm.patterns.direccion import CALLE_SINONIMOS 

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

def medidas_terrenos(medidas: list[str]):
    medidas_largas= []
    for medida in medidas:
        if all([float(numero)>7 for numero in get_numeros(medida)]):
            medidas_largas.append(medida)
    return medidas_largas


def remover_previo_a_palabra(direccion):
    patrones = "|".join(CALLE_SINONIMOS)
    patron = r".*?(" + patrones + r")"
    resultado = re.search(patron, direccion, flags=re.IGNORECASE)
    
    if resultado:
        return direccion[resultado.start():].strip()
    else:
        return direccion.strip()

def clean_direccion(cadena: str):
    cadena= re.sub(r"^\. ", "", cadena)
    if cadena == "":
        return ""
    if (NLP(cadena))[0].pos_ == "ADP":
        cadena= cadena.split()[1:]
        cadena= " ".join(cadena)
    
    if  (NLP(cadena))[-1].pos_ == "ADP":
        cadena= cadena.split()[:-1]
        cadena= " ".join(cadena)
    return remover_previo_a_palabra(cadena.strip())


def reduce_superstrings(dimensions):
    # Normalizamos las dimensiones eliminando 'mts' y otros caracteres no necesarios
    normalized_dimensions = [re.sub(r'\s*mts?\s*', '', dim) for dim in dimensions]
    
    reduced_dimensions = []
    for dim in normalized_dimensions:
        # Verificar si la dimensión actual es un superstring de alguna ya en la lista
        if not any(dim in existing for existing in reduced_dimensions):
            # Filtrar las dimensiones que son subcadenas de la dimensión actual
            reduced_dimensions = [existing for existing in reduced_dimensions if existing not in dim]
            # Agregar la dimensión actual a la lista de resultados
            reduced_dimensions.append(dim)
    return reduced_dimensions