import spacy
from spacy.matcher import PhraseMatcher

similares_medidas_lotes = ["Medidas de los lotes","medidas de los lotes","Medidas de los terrenos","medidas de los lotes"]
similares_disp_ala_venta = ["Disponemos a la venta amplios lotes","disponemos a la venta amplios lotes","disponemos a la venta amplios Lotes","disponemos a la venta amplios terrenos","disponemos a la venta amplios inmbuebles"]


nlp = spacy.load("es_core_news_lg")

description = "El terreno ideal para tu casa en Parque Exaltación! - Gran Lote de 1050 m2 - Opción de sumar otro lindero de 1.550 m2 - Inmejorable vista hacia el campo infinito. - Excelente ubicación. A solo tres cuadras del ingreso del barrio y de la bajada de la Autopista. - Escriturable - Apto crédito Parque Exaltación es un barrio semicerradonmuy consolidado de más de 1.000 lotes forestados hace más de 30 años, cobrando un gran impulso en la última década. El Barrio Parque cuenta con una añeja e importante arboleda compuesta por variedades de Coníferas, Sauces , Eucaliptos entre otros. El acceso al barrio se encuentra exactamente a metros de la bajada del Km 74 de la nueva Autopista 8 a solo 10 minutos de Pilar Centro. Centros comerciales muy cercanos tanto en elRemanso, como en Parada de Robles. En BlueKorner Inmobiliaria Boutique contamos con los mejores lotes del Barrio Parque Exaltación / Remanso"


doc = nlp(description)

matcher = PhraseMatcher(nlp.vocab,attr= "LOWER")

# Lista de frases a matchear
frases = ["Disponemos a la venta amplios lotes","disponemos a la venta amplios lotes","disponemos a la venta amplios terrenos","disponemos a la venta amplios inmbuebles",
        "Medidas de los lotes","Medidas de los terrenos","medidas de los lotes","Lotes en PH","El inmueble consta de tres lotes","terreno consta de tres lotes",
        "La propiedad consta de tres lotes","El inmueble consta de cuatro lotes","El inmueble consta de dos lotes","El inmueble consta de cinco lotes",
        "dos lotes","tres lotes","cuatro lotes","cinco lotes","Opción de sumar otro lote lindero","Opción de sumar otro lindero"
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
