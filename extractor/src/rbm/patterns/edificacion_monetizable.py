#construcción
PALABRAS_CLAVE_EDIFICADO = ["termotanque", "termotanques", "parquizado", "parquizada", "nivelado", "nivelada", "deposito", "depósito", "depositos", "depósitos", "zócalo", "zocalo", "zocalos"
                            ,"quincho", "quinchos", "parrilla", "parrillas", "galpon", "galpón", "galpones", "paredón", "paredon", "paredones", "comedor", "comedores", "cocina", "cocinas", "habitación", "habitacion", "habitaciones", "parrilla", "parrillas", "dormitorio", "dormitorios",  "ventana", "ventanas", "living", "livings", "lavadero", "lavaderos",  "muro", "muros", "hall", "halls", "terraza", "terrazas", "cocina", "cocinas", "lavadero", "lavaderos", "balcón", "balcon", "balcones", "comedor", "comedores", "galería", "galeria", "galerías", "galerias", "playroom", "playrooms"]

#con construcción
CONSTRUCCION_SINONIMOS = ["piso", "pisos", "propiedad", "propiedades", "garaje", "garajes", "cabaña", "cabañas", "chalet", "chalets", "vivienda", "viviendas", "depto", "deptos", "construcción", "construccion", "construcciones", "edificación", "edificacion", "edificaciones", "local", "locales", "pórtico", "póritcos", "portico", "porticos", "porche", "porches", "casa", "casas", "casita", "casitas", "departamento", "departamentos", "edificado", "edificados", "cochera", "cocheras", "guardacoche", "guardacoches", "garage", "garages", ]

#mejoras
PALABRAS_CLAVE_MEJORADO = ["paredón", "paredon", "paredones", "contrapiso", "contrapisos", "medianera", "medianeras", "platea", "plateas", "loza", "lozas",]

#con mejoras
PALABRAS_CLAVE_EDIFICADO_CON = ["mejora", "mejoras", "mejorado", "mejorada"]

FIN_SINONIMOS = ["finalizada", "finalizadas", "finalizado", "finalizados", "terminada", "terminadas", "terminado", "terminados"]
CON_SINONIMOS = ["c/", "con", "tiene", "posee", "hay"]
UN_SINONIMOS = ["un", "una", "unos", "unas"]
SUPERFICIE_SINONIMOS = ["superficie", "espacio", "sup", "sup."]
CUBIERTA_SINONIMOS = ["edificada", "edificadas", "edificado", "edificados", "cubierta", "cubierto", "cubiertas", "cubiertos", "semicubierta", "semicubierto", "semicubiertas", "semicubiertos"]
BASE_SINONIMOS = ["base", "bases"]
AREA = ["m2", "mts2", "mt2", "metros2", "metro2"] #fijarme sk matchea con M2 y similares
CONSTRUIDO_SINONIMOS = ["construido", "construida", "construidos", "construidas", "creada", "creado", "creadas", "creados"]
COSAS_COUNTRY = ["portón", "porton", "portones", "alambrado", "alambrada", "cercado", "cercados", "cerco", "cercos"]# pileta, piscina
#"portón", "porton", "portones", 
#EXTRA = ["paddle", "tennis", "tenis", "cancha", "canchas", "gimnasio", "gimnasios", "spa", "spas"]
POSIBLE_COUNTRY = ["cancha", "canchas", "futbol", "fútbol", "tenis", "tennis", "rugby", "spa", "spas", "gimnasio", "gimnasios", "paddle", "hockey", "polo"] #polo

def construccion():
    return  list([
        #con construcción
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
        #mejora
        [{"LOWER": {"IN":PALABRAS_CLAVE_MEJORADO}}],

        #con mejora
        [{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}},{"LOWER":{"IN":PALABRAS_CLAVE_EDIFICADO_CON}}],
    ])

def mejoras_country():
    return list([
        [{"LOWER": {"IN": COSAS_COUNTRY}}]
    ])

def posible_country():
    return list([
        [{"LOWER" : {"IN": POSIBLE_COUNTRY}}]
    ])