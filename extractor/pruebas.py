import pandas as pd
import spacy

from src.rbm.select_best_candidate import select_best_candidate

from src.rbm.matcher import Matcher
from normalize import normalize
NLP = spacy.load("es_core_news_lg")


def rbm():
    MATCHER = Matcher()
    input= [
"Departamento de un dormitorio en venta ubicado sobre calle Almirante Brown entre 9 de Julio y Republica Oriental del Uruguay (Morón, Buenos Aires). Desarrollado en piso alto por ascensor, con disposición frente y orientación al sur.El mismo posee cocina independiente equipada con muebles sobre y bajo mesada, living comedor, un dormitorio con placard empotrado y un baño completo. Amplio y luminoso, cuenta con balcón y equipo de aire acondicionado central.La propiedad tiene una superficie total de aproximadamente 48mts2, de los cuales 43mts2 son cubiertos. Las expensas al día 17/04/2024 son de aproximadamente $104.000.",       
"Ubicados sobre la Calle De Luca entre calle Alsina y Av. San Martín (arteria principal de acceso). A sólo 350 metros de la Ruta Provincial N° 6. Localidad de Los Cardales, Partido de Exaltación de la Cruz, Provincia de Buenos Aires. Características: Se trata de dos terrenos ubicados en el casco urbano de Los Cardales. Se encuentran dentro de la Zona Residencial Comercial de Densidad Media Baja (RCmb) acorde al Código de Planeamiento de Exaltación de la Cruz en la cuál se admite la edificación de departamentos y locales comerciales. Con indicadores de ocupación de: FOS: O.6 y FOT: 1.", 
"Fincas Don Eugenio II, un nuevo emprendimiento Situado en hermosa zona de estancias, rodeado de naturaleza y tranquilidad. Está ubicado en la Localidad de Gral. Rodríguez a 40 de Capital Federal y 15 de Acceso Oeste. Por Ruta N 6 Calle CAMINO NAVARRO. Cuenta con lotes a partir de los 300m2. Sus Valores los podemos identificar en plano como n colores: VALOR HASTA EL 26/03/2023 USD 10.948 EN LOTES SELECCIONADOS O LOTES DESDE USD 15.640. La posesión de los lotes son a 3 meses aproximadamente. Todos los lotes se entregan con quincho , parrilla y cerco de Alambre. Cuando se realiza la posesión se comienza a pagar un mínimo de expensas de $3.000, luego cuando todos los espacios en común estén terminados, se pagará $7.000 mensuales . El Barrio cuenta con ESCRITURA. Para que cada propietario pueda escriturar , deberá esperar un plazo estimativo de 1 a 2 años , ya que la ley nos pide tener un 60% del Barrio loteado. Porque se escritura por partes indivisas. Contamos con Normativas de Construcción , es importante leer con detalle. Respecto a los modelos de casas , hay flexibilidad. Se pueden construir Casas  en seco, Casas Alpinas, Cabañas, de material o estilo Streel Framing. No contamos con Financiación.",
    ]
    data = []
    for description in input:
        for token in NLP(description):
            print(token.text, token.pos_, token.dep_)
        candidate_pairs = MATCHER.get_pairs(normalize(description))

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