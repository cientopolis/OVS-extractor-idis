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
        "Lote de 946 m2 en esquina calle 501 y 132. 29 metros de frente por 32 metros de fondo aproximados. Altos de Sol. Muy fácil acceso a la cuidada de La Plata. Frente al desarrollo urbanístico La Cantera. Cercano a colegios, clubes y comercios. Zona en constante crecimiento frente al barrio Don Carlos, Posibilidad de dividir en PH en  dos lotes. Actualmente se están construyendo dos viviendas. El gas pasa por 501 y 132.",
        "Potosi esquina Colectora calle Mimosas (ex COLPAYO). Medidas y valores: Lotes 12x 30 mts USD 11.000. Lotes 12x25 mts USD 10.000. SE ACEPTA FINANCIACION DEL 50% DEL VALOR Y CUOTAS! ACEPTAMOS PROPUESTAS! NUEVO CONDOMINIO CERRADO. A solo 10’ de la Autopista Pte. Peron con una inmejorable ubicación, tranquilidad y espacios verdes para disfrutar en familia. CONTARA CON:  LUZ, SEGURIDAD, CERCO PERIMETRAL, PLAZAS DISTRIBUIDAS EN TODAS LAS MANZANAS. Calles de tosca y mejorado pavimental. LOTES DE 15x35. VALORES PREVENTA PRIMERAS 25 UF DE: U$D10.000 (contado). U$D12.000 (financiado). ACEPTAMOS CUOTAS O PROPUESTAS PERSONALIZADAS PARA LA COMODIDAD DE CADA CLIENTE! APTOS PARA ESCRITURAR DE MANERA INMEDIATA.","Barrio desarrollado en 16 hectáreas. Comprendido entre las calles 501 a 507 y 138 a 140. Una excelente zona de fácil acceso a las principales Avenidas 25, 31, 520 y Camino Gral. Belgrano. Se encuentra a 5 minutos de los principales colegios de la zona.  Un Hermoso lugar para vivir | LOTES en PH y Geodesia desde 230 m2",
        "Barrio abierto con 150 lotes entre 200 y 500 m2 distribuido en 6 manzanas A 15 minutos del centro platnese ubicado entre las calles 608 entre 18bis y 20 rápido acceso alejado del ruido de la ciudad encontra el lugar para tu futuro hogar",
        "Lotes en venta en Club de Campo Estancia Chica; el emprendimiento tiene como objetivo la realización de un barrio privado como complemento del complejo deportivo y recreativo \"Estancia Chica\".Muy bien ubicado, comprendido entre la ruta 36, calle 498, calle 202, diagonal 197 y calle 476; con fácil accesibilidad a La Plata (centro), City Bell y Capital Federal, alejado del tráfico y el ruido de la ciudad; un lugar para disfrutar en familia con grandes espacios recreativos y deportivos.EL PROYECTO El loteo a urbanizar consta de 742 lotes, de 20 metros de ancho por 30 metros de profundidad cada uno, con una superficie de 600 metros cuadrados. Se trata de un área de 88 hectáreas que en forma de herradura abraza y rodea al casco de Estancia Chica.URBANIZACIÓN Se comercializan 50 lotes en la 1° Etapa de PREVENTA, dispuestos a la derecha del acceso de calle 202 y 498. Ya se están realizando los primeros trabajos de desmalezado, trazado y consolidación de los lotes y calles que conformarán la primera etapa, red de agua potable, tendido eléctrico y luminarias de espacios comunes, alambrado perimetral y construcción de los pórticos de acceso. La siguiente etapa de obras de infraestructura comprende el desarrollo del sistema de desagües pluviales a cielo abierto, provisión de internet por fibra óptica, el sistema de provisión red cloacal, cumpliendo así con las requisitorias para el desarrollo de obras por parte de los entes gubernamentales.En la segunda etapa se comercializarán y urbanizarán los 398 lotes que se encuentran a la derecha del izquierda de calle 202 y 498, paralelo al Diagonal 197 y calle 476.Lotes propios. Escritura Inmediata dentro de los 60 días de conformada la reserva. Escribano Designado",
        "LOTES EN VENTA DESARROLLO BARRIO CERRADO EL MOLINO. CLUB DE CAMPO. Lotes en venta Desarrollo de barrio El Molino Club De Campo.  Ubicado en Ruta 2  Calle 531 Entre las rutas 2 y ruta 6. Lotes de: 15m x 30m = 450m2. 20m x 48m = 960m2. Lotes escriturables en parte indivisa. Posibilidad de financiar en los lotes de: Usd 6.000 contado: usd4.000, financiado en 12 meses de usd 170. Usd 11.000, contado: usd6.000, financiado en 12 meses de usd 450. El desarrollo contará con: Seguridad privada. Tendido eléctrico. Un muy buen movimiento de suelo. Una buena construcción tanto en Entrada como en La Garita de seguridad. Con ingreso exclusivo para los Propietarios y otro ingreso para los Servicios a su requerimiento. Con un excelente acceso y conexiones tanto Av. 520 & Av. 44. Salida rápida a Ruta 2 y Ruta 6  En una zona con un entorno natural. De campo.  Ideal para tu casa de fin de semana  Primeros terrenos disponibles en Preventa.",    
    ]
    
    data = []
    for description in input:
        for token in NLP(description):
            print(token.text, token.pos_, token.dep_)
        candidate_pairs = MATCHER.get_pairs(normalize(description))

        if (candidate_pairs["es_multioferta"]):
            if (len(medidas(candidate_pairs["medidas"]))>1):
                candidate_pairs["es_multioferta"]=True
            else:
                candidate_pairs["es_multioferta"]=""
            if (len(reduce_superstrings(set([x.lower() for x in candidate_pairs["dir_lote"]])))>1):
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