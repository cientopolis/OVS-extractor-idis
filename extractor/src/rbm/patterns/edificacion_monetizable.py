#construcción
PALABRAS_CLAVE_EDIFICADO = ["termotanque", "termotanques", "parquizado", "parquizada", "nivelado", "nivelada", "deposito", "depósito", "depositos", "depósitos", "zócalo", "zocalo", "zocalos"
                            ,"quincho", "quinchos", "galpon", "galpón", "galpones", "paredón", "paredon", "paredones", "comedor", "comedores", "cocina", "cocinas", "habitación", "habitacion", "habitaciones", "dormitorio", "dormitorios",  "ventana", "ventanas", "living", "livings", "lavadero", "lavaderos",  "muro", "muros", "hall", "halls", "cocina", "cocinas", "lavadero", "lavaderos", "balcón", "balcon", "balcones", "comedor", "comedores", "galería", "galeria", "galerías", "galerias"]

#con construcción
CONSTRUCCION_SINONIMOS = ["terraza", "terrazas", "piso", "pisos", "propiedad", "propiedades", "garaje", "garajes", "cabaña", "cabañas", "chalet", "chalets", "vivienda", "viviendas", "depto", "deptos", "construcción", "construccion", "construcciones", "edificación", "edificacion", "edificaciones", "local", "locales", "pórtico", "póritcos", "portico", "porticos", "porche", "porches", "casa", "casas", "casita", "casitas", "departamento", "departamentos", "edificado", "edificados", "cochera", "cocheras", "guardacoche", "guardacoches", "garage", "garages", ]

#mejoras
PALABRAS_CLAVE_MEJORADO = ["paredón", "paredon", "paredones", "contrapiso", "contrapisos", "medianera", "medianeras", "platea", "plateas", "loza", "lozas",]

#con mejoras
PALABRAS_CLAVE_MEJORADO_CON = ["mejora", "mejoras", "mejorado", "mejorada"]

PARRILLA = ["parrilla", "parrillas", ]
LOTE_SINONIMOS = ["lote", "lotes", "terreno", "terrenos", "parcela", "parcelas", "predio", "predios", "finca", "fincas", "propiedad", "propiedades"]
FIN_SINONIMOS = ["finalizada", "finalizadas", "finalizado", "finalizados", "terminada", "terminadas", "terminado", "terminados"]
CON_SINONIMOS = ["c", "c/", "con", "tiene", "posee", "hay"]
UN_SINONIMOS = ["un", "una", "unos", "unas"]
SUPERFICIE_SINONIMOS = ["superficie", "espacio", "sup", "sup."]
CUBIERTA_SINONIMOS = ["edificada", "edificadas", "edificado", "edificados", "cubierta", "cubierto", "cubiertas", "cubiertos", "semicubierta", "semicubierto", "semicubiertas", "semicubiertos"]
BASE_SINONIMOS = ["base", "bases"]
AREA = ["m2", "mts2", "mt2", "metros2", "metro2"] #fijarme sk matchea con M2 y similares
CONSTRUIDO_SINONIMOS = ["construido", "construida", "construidos", "construidas", "creada", "creado", "creadas", "creados"]
PORTON_SINONIMOS = ["portón", "porton", "portones"]
COSAS_COUNTRY = PORTON_SINONIMOS + ["alambrado", "alambrada", "cercado", "cercados", "cerco", "cercos", "playroom", "playrooms"]# pileta, piscina
#"portón", "porton", "portones", 
#EXTRA = ["paddle", "tennis", "tenis", "cancha", "canchas", "gimnasio", "gimnasios", "spa", "spas"]
POSIBLE_COUNTRY = ["cancha", "canchas", "futbol", "fútbol", "tenis", "tennis", "rugby", "spa", "spas", "gimnasio", "gimnasios", "paddle", "hockey", "polo"] #polo
CALLE_SINONIMOS = ["bv.", "bv", "avs", "avs.", "av", "av,","av.", "calle", "calles", "avenida", "avenidas", "diagonal", "diagonales", "dg", "dg.", "dgs", "dgs.","diag", "diasg.", "diags", "diags"]#tal vez dirá: "calle 5 entre calles 4 y 7"

def construccion():
    return  list([
        # con construcción
        [{"LOWER": "consta"},{"LOWER": "de"},{"POS":"ADV", "OP":"?"},{"LOWER": {"IN":UN_SINONIMOS},"OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"POS": "ADJ", "OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],
        [{"LOWER": {"IN":CON_SINONIMOS}},{"POS":"ADV", "OP":"?"},{"LOWER": {"IN":UN_SINONIMOS},"OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"POS": "ADJ", "OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],
        [{"LOWER": {"IN":CON_SINONIMOS}},{"POS":"ADV", "OP":"?"},{"POS": "DET"},{"LIKE_NUM":True,"OP":"?"},{"POS": "ADJ", "OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],
        [{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}},{"LOWER":{"IN":CONSTRUIDO_SINONIMOS}}],

        #palabras que no requieren "con"
        [{"LOWER": {"IN":PALABRAS_CLAVE_EDIFICADO}}],

        #superficie cubierta
        [{"LOWER": {"IN":SUPERFICIE_SINONIMOS}},{"LOWER": "semi"},{"LOWER":"cubierta"}],
        [{"LOWER": {"IN":SUPERFICIE_SINONIMOS}},{"LOWER": "semi"},{"LOWER":"cubierto"}],
        [{"LOWER": {"IN":SUPERFICIE_SINONIMOS}},{"LOWER": {"IN":CUBIERTA_SINONIMOS}}],  
        [{"LIKE_NUM": True},{"LOWER": {"IN":AREA}},{"LOWER": "son", "OP":"?"},{"POS":"NOUN", "OP":"?"},{"LOWER": {"IN":CUBIERTA_SINONIMOS}}],

        #relacionado a Base
        [{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"LOWER": "metros"},{"LOWER": "cuadrados"}],
        [{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"LOWER": {"IN":AREA}}],
        [{"LOWER": {"IN":CON_SINONIMOS}},{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],
    ])


def mejorado():
    return  list([
        #con mejora
        [{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}},{"LOWER":{"IN":PALABRAS_CLAVE_MEJORADO_CON}}],
        [{"LOWER":{"IN":LOTE_SINONIMOS}},{"LOWER":{"IN":CON_SINONIMOS}},{"LOWER":{"IN":PALABRAS_CLAVE_MEJORADO_CON+PARRILLA}}],

    ])

def mejoras_country():
    return list([
        [{"LOWER": {"IN": COSAS_COUNTRY}}]
    ])

def posible_country():
    return list([
        [{"LOWER" : {"IN": POSIBLE_COUNTRY}}]
    ])

def mejora_posible_calle() -> list:
    return list([    #mejora
        [{"LOWER": {"IN":PALABRAS_CLAVE_MEJORADO}}],
    ])

def no_mejora_DM() -> list:
    return[
        [#calle mejorada
            {
                "RIGHT_ID": "calle",
                "RIGHT_ATTRS": {"LOWER": {"IN": CALLE_SINONIMOS}},
            },
                {
                "LEFT_ID": "calle",
                "REL_OP": ">",
                "RIGHT_ID": "mejora",
                "RIGHT_ATTRS": {"LOWER": {"IN":PALABRAS_CLAVE_MEJORADO_CON}},
            },
        ]
    ]

def no_mejora_country_DM() -> list:
    return[
        [#calle mejorada
            {
                "RIGHT_ID": "porton",
                "RIGHT_ATTRS": {"LOWER": {"IN": PORTON_SINONIMOS}},
            },
            {
                "LEFT_ID": "porton",
                "REL_OP": ">",
                "RIGHT_ID": "principal",
                "RIGHT_ATTRS": {"LOWER": "principal"},
            },
        ]
    ]

# def lote_construccion_DM() -> list:
#     return[
#         [#calle mejorada
#             {
#                 "RIGHT_ID": "lote",
#                 "RIGHT_ATTRS": {"LOWER": {"IN": LOTE_SINONIMOS}},
#             },
#             {
#                 "LEFT_ID": "lote",
#                 "REL_OP": ">",
#                 "RIGHT_ID": "construccion",
#                 "RIGHT_ATTRS": {"LOWER": {"IN":PALABRAS_CLAVE_MEJORADO_CON}},
#             },
#         ]
#     ]
