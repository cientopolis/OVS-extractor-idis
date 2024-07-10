CON_SINONIMOS = ["c/", "con", "tiene", "posee", "hay"]
UN_SINONIMOS = ["un", "una", "unos", "unas"]
CONSTRUCCION_SINONIMOS = [ "pileta", "piletas", "piscina", "piscinas", "edificado", "edificados", "deposito", "depósito", "depositos", "depósitos", "mejora", "mejoras", "construcción", "construccion", "construcciones", "zócalo", "zocalo", "zocalos", "mejora", "mejoras", "edificación", "edificacion", "edificaciones", "quincho", "quinchos", "galpon", "galpón", "galpones", "local", "locales", "casa", "casas", "casita", "casitas", "paredón", "paredon", "paredones", "portón", "porton", "portones", "comedor", "comedores", "cocina", "cocinas", "cerco", "cercos", "habitación", "habitacion", "habitaciones", "alambrado", "alambrados", "parrilla", "parrillas", "plataforma", "plataformas", "loza", "lozas", "contrapiso", "contrapisos", "medianera", "medianeras", "garaje", "garajes", "cabaña", "cabañas", "chalet", "chalets", "dormitorio", "dormitorios", "cochera", "cocheras", "ventana", "ventanas", "living", "livings", "lavadero", "lavaderos", "pileta", "piletas", "guardacoche", "guardacoches", "platea", "plateas", "piso", "pisos", "muro", "muros", "hall", "halls", "terraza", "terrazas", "parrilla", "parrillas", "garage", "garages", "cocina", "cocinas", "portón", "porton", "portones", "lavadero", "lavaderos", "balcón", "balcon", "balcones", "oficina", "oficinas", "comedor", "comedores", "galería", "galeria", "galerías", "galerias", "playroom", "playrooms", "local", "locales", "cercado", "cercados", "pórtico", "póritcos", "portico", "porticos", "porche", "porches"]
SUPERFICIE_SINONIMOS = ["superficie", "espacio", "sup"]
CUBIERTA_SINONIMOS = ["edificada", "edificadas", "edificado", "edificados", "cubierta", "cubierto", "cubiertas", "cubiertos", "semicubierta", "semicubierto", "semicubiertas", "semicubiertos"]
BASE_SINONIMOS = ["base", "bases"]
AREA = ["m2", "mts2", "mt2", "metros2", "metro2"] #fijarme sk matchea con M2 y similares
PALABRAS_CLAVE = ["parquizado", "parquizada", "nivelado", "nivelada"]
CONSTRUIDO_SINONIMOS = ["construido", "construida", "construidos", "construidas", "creada", "creado", "creadas", "creados"]

def edificacion_monetizable():
    return  list([
        # #con construcción
        # [{"LOWER": "consta"},{"LOWER": "de"},{"POS":"ADV", "OP":"?"},{"LOWER": {"IN":UN_SINONIMOS},"OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"POS": "ADJ", "OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],
        # [{"LOWER": {"IN":CON_SINONIMOS}},{"POS":"ADV", "OP":"?"},{"LOWER": {"IN":UN_SINONIMOS},"OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"POS": "ADJ", "OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],
        # [{"LOWER": {"IN":CON_SINONIMOS}},{"POS":"ADV", "OP":"?"},{"POS": "DET"},{"LIKE_NUM":True,"OP":"?"},{"POS": "ADJ", "OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],
        # [{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}},{"LOWER":{"IN":CONSTRUIDO_SINONIMOS}}],

        #contrucción -> tal vez sea todo lo que necesite si lo junto con el Dependency Matcher
        [{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],

        #superficie cubierta
        [{"LOWER": {"IN":SUPERFICIE_SINONIMOS}},{"LOWER": "semi"},{"LOWER":"cubierta"}],
        [{"LOWER": {"IN":SUPERFICIE_SINONIMOS}},{"LOWER": "semi"},{"LOWER":"cubierto"}],
        [{"LOWER": {"IN":SUPERFICIE_SINONIMOS}},{"LOWER": {"IN":CUBIERTA_SINONIMOS}}],  
        [{"LIKE_NUM": True},{"LOWER": {"IN":AREA}},{"LOWER": "son", "OP":"?"},{"POS":"NOUN", "OP":"?"},{"LOWER": {"IN":CUBIERTA_SINONIMOS}}],

        #relacionado a Base
        [{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"LOWER": "metros"},{"LOWER": "cuadrados"}],
        [{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"LOWER": {"IN":AREA}}],
        #[{"LOWER": {"IN":CON_SINONIMOS}},{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],

        #palabras que no requieren "con"
        [{"LOWER": {"IN":PALABRAS_CLAVE}}],
        #si la construcción es futura entonces no ponerla
    ])