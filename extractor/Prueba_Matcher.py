fincas = ["duggan" , "Duggan"]
#importamos todo
import spacy    #para el nlp()

from spacy.matcher import Matcher #importo spacy matcher para hacer los patrones

from spacy.matcher import PhraseMatcher # importo spacy phrasematcher para futuras pruebas

nlp = spacy.load("es_core_news_lg")#importamos la info entrenada en español con muchos datos

description = "Oportunidad de inversión a valores de pre-venta: Barrio abierto Los Aromos, sin expensas, en la mejor zona de 20 de Junio, Matanza El proyecto contempla para la venta 80 Lotes de 900 y 1000m2 que se entregarán ESCRITURADOS en una fecha estimada cercana a DICIEMBRE 2026, y que gracias a una impecable gestión, hoy ya cuenta con Planos Aprobados en el Municipio de Matanza, y ARBA, en la La Plata. Para tal logro, serán necesarias todas las obras de infraestructura viales tales como: -Apertura de cinco calles nuevas -Aporte de suelo cemento -Aporte de tosca compactada -Aporte de cascote fino como terminaciÃ³n final -CordÃ³n cuneta de HormigÃ³n Armado en todas las nuevas calles a ceder con acceso vehicular y desagÃ¼e pluvial. El proyecto urbano tambiÃ©n contempla un plan hidrÃ¡ulico de evacuaciÃ³n de las aguas de lluvia mediante sumideros, zanjas y entubados perimetrales aprobados por el municipio de La Matanza Por otro lado, se contempla toda la iluminaciÃ³n pÃºblica y tendido elÃ©ctrico; mejorado de calles aledaÃ±as y desmalezado. El emprendimiento contará con un sector de 10.000mÂ² para el esparcimiento público.",


doc = nlp(description)# el doc tiene cada palabra/token
 
matcher = Matcher(nlp.vocab)
matcher.add("patron_analizado", 
        [
            [{"LOWER" : "venta"},{"LIKE_NUM" : True},{"LOWER" : "lotes"}], # venta (num)lotes 
        ])

print("El beio match es: ")
el_resultadongo = ""
matches_dep = matcher(doc)

for match_id, start, end in matches_dep:
    span = doc[start:end]
    el_resultadongo += " " + span.text

print(el_resultadongo.strip())

  