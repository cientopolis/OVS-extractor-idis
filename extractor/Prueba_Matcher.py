fincas = ["duggan" , "Duggan"]
#importamos todo
import spacy    #para el nlp()

from spacy.matcher import Matcher #importo spacy matcher para hacer los patrones

from spacy.matcher import PhraseMatcher # importo spacy phrasematcher para futuras pruebas

nlp = spacy.load("es_core_news_lg")#importamos la info entrenada en español con muchos datos

description = "Av Gral. Guemes esquina Gral. Arredondo frente al Shopping Alto Avellaneda con 29 mts de frente sobre la Avenida Guemes x 29 mts sobre Arredondo. Son 4 lotes. Ubicado a 3 cuadras del CBC UBA (Sede Avellaneda). Ideal emprendimiento multifamiliar con zocalo comercial y cocheras. Parcela 01: 244.1 m2. Parcela 02: 226.0 m2. Parcela 24: 320.0 m2. Parcela 25: 248.6 m2. EDIFICABILIDAD: Fos máx.: 60% FOT residencial: 2.5 FOT comercial: 3"

doc = nlp(description)# el doc tiene cada palabra/token
 
matcher = Matcher(nlp.vocab)
matcher.add("patron_analizado", 
        [
            [{"LOWER" : "son"},{"LIKE_NUM" : True},{"LOWER" : "lotes"}]         
        ])

print("El beio match es: ")
el_resultadongo = ""
matches_dep = matcher(doc)

for match_id, start, end in matches_dep:
    span = doc[start:end]
    el_resultadongo += " " + span.text

print(el_resultadongo.strip())

  