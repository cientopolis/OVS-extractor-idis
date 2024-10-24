fincas = ["duggan" , "Duggan"]
#importamos todo
import spacy    #para el nlp()

from spacy.matcher import Matcher #importo spacy matcher para hacer los patrones

from spacy.matcher import PhraseMatcher # importo spacy phrasematcher para futuras pruebas

nlp = spacy.load("es_core_news_lg")#importamos la info entrenada en español con muchos datos

description = "El terreno ideal para tu casa en Parque Exaltación! - Gran Lote de 1050 m2 - Opción de sumar otro lindero de 1.550 m2 - Inmejorable vista hacia el campo infinito. - Excelente ubicación. A solo tres cuadras del ingreso del barrio y de la bajada de la Autopista. - Escriturable - Apto crédito Parque Exaltación es un barrio semicerradonmuy consolidado de más de 1.000 lotes forestados hace más de 30 años, cobrando un gran impulso en la última década. El Barrio Parque cuenta con una añeja e importante arboleda compuesta por variedades de Coníferas, Sauces , Eucaliptos entre otros. El acceso al barrio se encuentra exactamente a metros de la bajada del Km 74 de la nueva Autopista 8 a solo 10 minutos de Pilar Centro. Centros comerciales muy cercanos tanto en elRemanso, como en Parada de Robles. En BlueKorner Inmobiliaria Boutique contamos con los mejores lotes del Barrio Parque Exaltación / Remanso"

doc = nlp(description)# el doc tiene cada palabra/token
 
matcher = Matcher(nlp.vocab)
matcher.add("patron_analizado", 
        [
            [{"LOWER" : "son"},{"LIKE_NUM" : True},{"LOWER" : "lotes"}], # lotes de (num)
        ])

print("El beio match es: ")
el_resultadongo = ""
matches_dep = matcher(doc)

for match_id, start, end in matches_dep:
    span = doc[start:end]
    el_resultadongo += " " + span.text

print(el_resultadongo.strip())

  