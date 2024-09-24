import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load("es_core_news_lg")

description = "VENTA DE LOTE EN L COMPUESTO POR TRES PH DE 3 AMB Y FONDO LIBRE. .Publicado por Noely Rodriguez Majeric a traves de Inmomap"

doc = nlp(description)

matcher = PhraseMatcher(nlp.vocab,attr= "LOWER")

# Lista de frases a matchear
frases = ["departamento en ph.-en","APTO SUBDIVISIÓN EN PH","Posibilidad de dividir en PH","LOTE DIVISIBLE PH","LOTE EN L COMPUESTO POR TRES PH"]

# Convertir cada frase a un objeto Doc usando nlp
patterns = [nlp(frase) for frase in frases]

matcher.add("pattern_name", patterns)

el_resultadongo = ""
matches_dep = matcher(doc)

for match_id, start, end in matches_dep:
    span = doc[start:end]
    el_resultadongo += f"{span.text} "

# Mostrar el resultado
print("El beio match es: ", el_resultadongo.strip())
