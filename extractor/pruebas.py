from collections import OrderedDict
import pandas as pd
import spacy

from src.helper import reduce_superstrings
from src.rbm.select_best_candidate import select_best_candidate

from src.rbm.matcher import Matcher
from normalize import normalize
NLP = spacy.load("es_core_news_lg")
import re

def get_numeros(cadena: str):
        return re.findall(r"\b\d+(?:[.,]\d+)?\b", cadena)


def medidas(predichos):
    if not predichos:
        return ""
    result= []
    for candidato in list(reduce_superstrings(set(predichos))):
        medidas = ""
        for numero in list(map(str, get_numeros(candidato))):
            medidas += numero + " x "
        
        if (medidas.count("x")>1):
            medidas= medidas.replace(",",".")
            result.append(medidas.rstrip(" x"))
    return result

def rbm():
    MATCHER = Matcher()

    input= [
"Calle 141 y 515. El barrio “San Patricio 2” se desarrolla, más precisamente entre las calles 515 a 517 y 141 a 142. Es un barrio de amplios y cómodos lotes en PH, rodeados de mucho verde. Tiene un rápido acceso a la ciudad por avenida 520, lo que permite estar en 15 minutos en el centro platense. Este desarrollo cuenta con 40 lotes de diferentes medidas que van desde los 200m² a los 1000m².  Lotes de 12x40  480m2 U$S 48.000  Lotes de 12x41  492m2 U$S49.200  Lotes de 12x52  624m2   U$S 62.400  Lotes de 12x55  660m2 U$S 66.000  Servicios: luz, agua y gas. Consulte por financiación en pesos y en dólares.",
"Propiedad de 2000 metros cuadrados con 4 locales, hoy Dupplex. Lote 25 de 200M2 arbolado, sin mejoras con portón de reja en dos hojas  Lote 26 de 200M2 arbolado sin mejoras con tejido artístico al frente.  Lote 27 de 191M2 esquina arbolado sin mejoras solo una parrilla de material.  Lote 28 de 200M2ante esquina garaje  3,16 x 10,6 cubierto techo de abovedado con losa, piso de cemento portón de reja de 2 hojas Lote 2 de 200M2sin mejoras al frente portón de reja  Lote 1 de 191M2esquina sin mejoras. Lote 4,92 x 5,1 29 de 400M2con dos locales. Locales 4,92 x 5,1 c/u edificados de mampostería con techo de hormigón armado, hoy en día son dúplex  Comedor con piso de cerámica, ventanas de aluminio con reja divisiones con la cocina con una pared de machimbre.  Cocina 4,48 x 4,88 con piso de cerÃ¡mica, mesada de material revestida en cerámica con dos hachas de acero inoxidable, instalación de agua frÃa y caliente, extracto, escalera metÃ¡lica con escalones de madera a entrepiso  Baño con piso y paredes revestidas en cerÃ¡mica instalado con inodoro y lavamanos con pie ducha con agua fría y caliente, termotanque eléctrico. Entrepiso 4,89 x 5,02 con piso de machimbre ventana de aluminio con reja  Duplex 4,85 x 9,53 siguiente similar a terminar y sin división entre la cocina y el comedor. Galpón 9 x 10 de mamposterÃa con techo de chapa a un agua  Lote  30 de 400M2similar al anterior con escalera a terraza accesible desde la calle, con patio.",
"Equipo RE/MAX Cordillera Vende RE/MAX vende lote soleado y vegetación nativa en Villa Lago Meliquina.\r\nTerreno muy soleado, con vegetación nativa con hermosas vistas en todas las direcciones.   Ubicado en Meliquina II,  cuenta con un fácil acceso desde la ruta 63 tomando la calle 22 . Posee vistas hacía el Cerro Ventana y el Cerro Muela y vistas panorámicas a las montañas.\r\nUbicación: Manzana Y lote 9. Metros cuadrados: 990,63 m2. Acceso: frente a la Ruta 63 a 3 km del Lago (frente a cervecería artesanal de Meliquina) por calle 22. Servicios: Loteo sin servicios de red. Uso de energías renovables y agua tomada de arroyos o vertientes. (sistemas alternativos propios de uso individual). VALOR PUBLICADO DE CONTADO U$D 19.000 (sin posibilidad de negociación). IMPORTANTE FINANCIACION con ESCRITURA Hipotecaria: 50% al momento de la escritura U$D 10.200 + 6 cuotas bimestrales fijas de U$D 1800en dólares. ( valor final U$D 21.000 ). OPORTUNIDAD: posibilidad de comprar el lote lindante de 962,26 m2; del mismo propietario, y poder hacer un uso turístico para cabañas, hosterías o varias construcciones en los ambos lotes.",
 "Lote en PH Barrio Abierto Don Uriel. Ubicación: Mz 146, lote 25. Lote de 235,38 m2 (10,81m X 23,19m) Servicios: Calles con cordón cuneta y mejorado. Red de tendido eléctrico. Alumbrado publico con luminarias LED. Agua corriente. Gas natural.  Sistema de venta por Fideicomiso con asignación de lote individual (no indiviso).",
       ]
    data = []
    for description in input:
        for token in NLP(description):
            print(token.text, token.pos_, token.dep_)
        candidate_pairs = MATCHER.get_pairs(normalize(description))

        if (candidate_pairs["es_multioferta"] or "lotes" in description.lower()):
            # enumera más de una medida de lote, o mas de un numero de lote
            if description.lower().split().count("lotes")>1 or (len(reduce_superstrings(set([x.lower() for x in candidate_pairs["es_multioferta"]])))>2) or (len(medidas(candidate_pairs["medidas"]))>1) or (len(reduce_superstrings(set([x.lower() for x in candidate_pairs["dir_lote"]])))>1):
                candidate_pairs["es_multioferta"]=True
            else:
                candidate_pairs["es_multioferta"]=""
        

        estructura =  {
            "direccion": None,
            "fot": None,
            "irregular":None,
            "medidas": None,
            "esquina": None,
            "barrio": None,
            "frentes": None,
            "pileta": None,
            "urb_cerrada":  None,
            "posesion": None,
            "urb_semicerrada": None,
            "preventa": None,
            "indiviso": None,
            "a_demoler": None,
            "es_multioferta": None,
            "es_monetizable": None
        }

        select_best_candidate(candidate_pairs, estructura)
        estructura["description"] = description
        data.append(estructura)
    return pd.DataFrame(data, index=None)

rbm()