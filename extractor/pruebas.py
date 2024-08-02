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
# "2 Lotes en venta en zona Rio Negro y Remedios de Escalada, a pasos de la Ruta 2. Venta en block o separados. Lote 1: 16 m de frente x 43.30 m de fondo. U$s 39.000. Lote 2: 27.30 m x 27.30 m. U$s 50.000.",
#  "EXCELENTE LOTE DE 720 M² | BARRIO EL SOSIEGO VENTA DE CASA QUINTA | LOTES POR SEPARADO Excelente lote en barrio El Sosiego, Mar del Plata, con frente a calle Los Plátanos, entre calles Los Nogales y Los Álamos. Fácil y rápido acceso desde Autovía 2, 250 metros por calle mejorada, y a solo ocho minutos de Mar del Plata. Servicios: recolección de residuos, luz, agua de pozo (bomba de agua), gas con garrafa (existe red de gas natural), excepto cloaca, teléfono, Wifi internet. Colectivo a la ciudad Línea 542, con parada a 250 mts. sobre la ruta. Transporte Escolar. POSIBILIDAD DE ADICIONAR LOTES LINDEROS. DUQUE WILLIAMS PROPIEDADES Registro 3814 Playa Grande, Mar del Plata",
# "LOCAL CON OFICINAS | DEPÓSITO CON ENTRADA DE VEHÍCULOS | LOTE 750 M Superficie Lote 750 m². Frente de 17.32 mts. Fondo de 43.30 mts. Superficie construida aproximada 440 m",
"VENTA DE LOTE EN BARRIO EL MARQUESADO TU PROXIMA VIVNEDA O LUGAR DE DESCANSO ESTA EN ESTE LUGAR! VENTA DE LOTE DE 15 MTROS DE FRENTE POR 30 MTROS DE FONDO! URBANIZACION EN LA ZONA! CALLE ABIERTA A 15 CUADRAS DE LA RUTA Y ACCESO A LA PLAYA! LISTO PARA ESCRITURAR!",
"Lotes en el Marquesado 15 x 25 Mts 4 LOTES EN EL MARQUESADO: 2 lotes Nº 10 y 11 de la manzana 238 (calle 9 e/ 6 y 12)",
"EN LA APRECIADA ZONA DE COLINAS DE PERALTA RAMOS OFRECEMOS: VENTA EN BLOCK: LOCAL + CHALET + LOTE EXCELENTE INVERSIÓN PARA VIVIENDA Y/O USO COMERCIAL EN RUBROS COMO GASTRONOMIA, CENTRO EDUCATIVO, SALUD, GERIATRICO, CENTRO DE DIA, CONSULTORIOS y MUCHOS MAS !!!! Importante propiedad en esquina sobre 3 lotes, con un total de 800 m2, de los cuales son 500 m2 cubiertos y 300 m2 parquizados. PB: LOCAL 140M2 con 3 entradas, garage quincho (3) y lote de 10 x 29 mts PA: Chalet 5 ambientes con gran living comedor principal de 7 x 4.5 mts, cÃmoda cocina comedor de 7 x 4.3 mts, 4 habitaciones con placard, 2 baños completos y compartimentados, lavadero de 3 x 3.50 mts, terraza de 25 m2, balcÃn saliente y corrido en todo el perimetro. Calefacción central por radiadores. Excelente calidad de construcción, impecable estado!! Todos los ambientes externos!! Todo el sol!! CONSULTE SU VALOR TALIERCIO ASOC. Negocios Inmobiliarios. Rawson N 1369 Mar del Plata | Buenos Aires | Argentina (0223) 486 4686 | (223) 155 412120 normataliercio@gmail.com www.taliercioprop.co",
"Century 21 Recanatti se complace en comercializar este lote terreno, ubicado al Sur de la ciudad de Mar del Plata, en el creciente barrio Playa los Lobos, este terreno de 472 m², de 15 mts de frente por 31 mts de fondo. El lote se encuentra en la calle Las Ostras entre Los Salmones y Los Nautilus"
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