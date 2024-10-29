import spacy
from spacy.matcher import PhraseMatcher

similares_medidas_lotes = ["Medidas de los lotes","medidas de los lotes","Medidas de los terrenos","medidas de los lotes"]
similares_disp_ala_venta = ["Disponemos a la venta amplios lotes","disponemos a la venta amplios lotes","disponemos a la venta amplios Lotes","disponemos a la venta amplios terrenos","disponemos a la venta amplios inmbuebles"]


nlp = spacy.load("es_core_news_lg")

description = "TERRENOS EN PRE-VENTA VENTA DE TERRENOS - EXCELENTE OPORTUNIDAD DE INVERSIÒN. Ubicados a tan solo 45 minutos de CABA y a 5 minutos de la nueva autopista Presidente Perón (Continuación del Camino del Buen Ayre) que conectara directamente Zona Norte con Ezeiza-La Plata. PRE VENTA DE LAS PRIMERAS 10 UNIDADADES DISPONIBLES DE 724 mts2 - DOCUMENTACION: Escritura al día. Posesión a 12 meses, escritura indivisa. DESCRIPCIONES GENERALES Barrio cerrado VIEDMA CHICO compuesto por 41 unidades funcionales que van desde los 724 a 850mts2 / Trabajo de agrimensura realizado, lotes amojonados / / Calles internas ( cul de sac ) / / Vigilancia / / Portón automático / / Cerco perimetral y alarma / / Circuito cerrado cámaras seguridad con acceso para cada propietario / / Iluminación LED / / Forestación / INFORMACION DE INTERES -Linea de transporte publico a 3 cuadras. -Ubicado a 300 metros de Avenida Constituyentes. -Ubicado a 10 minutos del centro comercial de Mariano Acosta., -Ubicado a 5 minutos del Lago San Francisco y Reserva Parque Los Robles. -Ubicado a 5 minutos de la subida de la nueva autopista con fácil acceso."

doc = nlp(description)

matcher = PhraseMatcher(nlp.vocab,attr= "LOWER")

# Lista de frases a matchear
frases = ["venta de unidades funcionales","Venta de terrenos","venta de lotes","VENTA EN BLOCK",
          "Disponemos a la venta amplios lotes","Medidas de los lotes","LOTES en","posibilidad de venderse por separado o en bloque",
          "El inmueble consta de tres lotes","se puede comprar lotes contiguos","DOS LOTES EN BLOQUE","para la venta Lotes"
        ]

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
