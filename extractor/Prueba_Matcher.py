fincas = ["duggan" , "Duggan"]
#importamos todo
import spacy    #para el nlp()

from spacy.matcher import Matcher #importo spacy matcher para hacer los patrones

from spacy.matcher import PhraseMatcher # importo spacy phrasematcher para futuras pruebas

nlp = spacy.load("es_core_news_lg")#importamos la info entrenada en español con muchos datos

description = "Lote de 244 mt2 en Barrio Privado Santa Elena (en PH), desarrollado en 1,2 hectáreas. A solo 10 minutos del centro de la ciudad de La Plata. Acceso principal por asfalto por calle 609 y 5 bis. Portón de ingreso vehicular. El emprendimiento está compuesto por 35 lotes unifamiliares y 10 locales comerciales. Plano Municipal y de Propiedad Horizontal probados. Servicios: Luz - Agua. La obra del servicio de gas será abonada por los compradores de las unidades y el comienzo de obra dependerá de la empresa prestadora. Escrituración y posesión inmediatas. "

doc = nlp(description)# el doc tiene cada palabra/token
 
matcher = Matcher(nlp.vocab)
matcher.add("patron_analizado", 
        [
            [{"LOWER" : "Zona "},{"LOWER" : "countrys" }]         
        ])

print("El beio match es: ")
el_resultadongo = ""
matches_dep = matcher(doc)

for match_id, start, end in matches_dep:
    span = doc[start:end]
    el_resultadongo += " " + span.text

print(el_resultadongo.strip())

  