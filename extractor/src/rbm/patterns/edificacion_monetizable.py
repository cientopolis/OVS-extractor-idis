CON_SINONIMOS = ["c/", "con", "tiene", "posee"]
UN_SINONIMOS = ["un", "una", "unos", "unas"]
CONSTRUCCION_SINONIMOS = ["mejora", "mejoras", "construcción", "construccion", "construcciones", "zócalo", "zocalo", "zocalos", "mejora", "mejoras", "edificación", "edificacion", "edificaciones", "quincho", "quinchos", "pileta", "piletas", "galpon", "galpón", "galpones", "local", "locales", "casa", "casas", "casita", "casitas", "paredón", "paredon", "paredones", "portón", "porton", "portones", "comedor", "comedores", "cocina", "cocinas", "cerco", "cercos", "habitación", "habitacion", "habitaciones", "alambrado", "alambrados", "parrilla", "parrillas", "plataforma", "plataformas", "loza", "lozas", "contrapiso", "contrapisos", "medianera", "medianeras", "garaje", "garajes", "cabaña", "cabañas"]
SUPERFICIE_SINONIMOS = ["superficie", "espacio", "sup"]
CUBIERTA_SINONIMOS = ["cubierta", "cubierto", "cubiertas", "cubiertos", "semicubierta", "semicubierto", "semicubiertas", "semicubiertos"]
BASE_SINONIMOS = ["base", "bases"]
AREA = ["m2", "mts2", "mt2", "metros2", "metro2"] #fijarme sk matchea con M2 y similares
PALABRAS_CLAVE = ["parquizado", "parquizada", "nivelado", "nivelada"]

def edificacion_monetizable():
    return  list([
        [{"LOWER": {"IN":CON_SINONIMOS}},{"LOWER": {"IN":UN_SINONIMOS},"OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"POS": "ADJ", "OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],
        
        [{"LOWER": {"IN":SUPERFICIE_SINONIMOS}},{"LOWER": "semi"},{"LOWER":"cubierta"}],
        [{"LOWER": {"IN":SUPERFICIE_SINONIMOS}},{"LOWER": {"IN":CUBIERTA_SINONIMOS}}],  

        [{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"LOWER": "metros"},{"LOWER": "cuadrados"}],
        [{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LIKE_NUM":True,"OP":"?"},{"LOWER": {"IN":AREA}}],
        [{"LOWER": {"IN":CON_SINONIMOS}},{"LOWER": {"IN":BASE_SINONIMOS}},{"LOWER":"de","OP":"?"},{"LOWER":{"IN":CONSTRUCCION_SINONIMOS}}],

        [{"LOWER": {"IN":PALABRAS_CLAVE}}],


        #si la construcción es futura entonces no ponerla
    ])