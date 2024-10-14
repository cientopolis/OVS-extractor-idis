import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load("es_core_news_lg")

description = "LOTE DOBLE FRENTE en Ramos Mejía. Excelente Terreno de 17 mts. de Frente x 40 mts. de Fondo. Posibilidad de venta por fracción de 8,66 x 40 mts. La propiedad se encuentra ubicada sobre la calle 11 de Septiembre al 300, en el barrio de Ramos Mejía. A metros de la Av. San Martín. Ideal para emprendimiento de Departamentos o Duplex/PH. Posibilidad de tomar menor valor en parte de pago. "

doc = nlp(description)

matcher = PhraseMatcher(nlp.vocab,attr= "LOWER")

# Lista de frases a matchear
frases = ["LOTE DOBLE FRENTE","terreno doble frente","LOTE TRIPLE FRENTE","lote con salida a 2 calles."]

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
