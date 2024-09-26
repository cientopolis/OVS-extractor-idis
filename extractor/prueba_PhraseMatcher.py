import spacy
from spacy.matcher import PhraseMatcher


nlp = spacy.load("es_core_news_lg")

description = "137 Y 90 LOTE EN VENTA, BARRIO PRIVADO FINCAS DE DUGGAN, 800 m2, Ubicado en la etapa 2, esta se ecuentra completamente desarrollada y el lote es el único que queda en este sector. Plano PH aprobado.  SERVICIOS E INFRAESTRUCTURA:  • Seguridad privada en accesos, y rondines por el barrio las 24 hs. de los 365 días del año, a lo que se le adiciona un puesto de control de la policía bonaerense en la esquina del barrio.  • Sala de control para monitoreo de imágenes.  • Sistema de control de acceso y egreso con llave magnética personalizada.  • Cerco olímpico perimetral.  • Alumbrado de calles.  • Servicios por tendido subterráneo:  >  Red de energía eléctrica.  >  Red de fibra óptica para Internet de alta velocidad, telefonía y televisión.  >  Red de agua corriente.  >  Red de gas natural.  "

doc = nlp(description)

matcher = PhraseMatcher(nlp.vocab,attr= "LOWER")

# Lista de frases a matchear
frases = ["próximo a la esquina","un puesto de control de la policía bonaerense en la esquina del barrio","puesto de control de la policía en la esquina"]

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
