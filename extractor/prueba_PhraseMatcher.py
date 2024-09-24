import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load("es_core_news_lg")

description = "Se vende lote en gran zona. Zona de countrys (Grand Bell, Los Ceibos, Country Club de Estudiantes). 10 mts de frente x 30 mts de fondo. 300 mt2 totales. Tiene paredón al frente, alambrado, parrilla en el fondo, sala de maquinas/galpón. Zona con todos los servicios"

doc = nlp(description)

matcher = PhraseMatcher(nlp.vocab,attr= "LOWER")

# Lista de frases a matchear
frases = ["zona de countrys", "grand bell", "servicio de gas"]

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
