import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load("es_core_news_lg")

description = "Vendo lote de 12x49 en barrio cerrado Aires de Arana. El mismo es el tercer lote desde ingreso del predio. Nivelado. Posee bomba de agua. Bases de 90m2 para vivienda familiar. El predio tiene portón automatizado con apertura tanto por control remoto como por app desde el celular. Cámaras de seguridad. Calle interna iluminada. Se encuentra en una zona muy tranquila, próximo a la Av 137 a tan solo 20min del centro de la ciudad de La Plata. Posee escritura indivisa(próximo a escritura definitiva). Escucho Oferta Razonable"

doc = nlp(description)

matcher = PhraseMatcher(nlp.vocab,attr= "LOWER")

# Lista de frases a matchear
frases = ["Posee escritura indivisa(próximo","posee escritura indivsa","posee escritura por la parte indiva",]

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
