idealSinonimos = ["para", "ideal", "posibilidad"]
ideales  = ["proyecto", "proyectos", "inversión", "inversion", "edificar", "edificio", "edificios", "constructor","constructores", "construccion", "construcciones", "construcción", "inversor", "inversores", "emprendimiento", "emprendimientos", "desarrollo", "desarrollos"] #"proyecto", "proyectos", 
demolerSinonimos = ["reciclar", "refaccionar", "demoler", "demolicion", "demolición", "refaccionarse", "reciclarse", "demolerse"]
casaSinonimos= ["casa", "construccion", "construcción"] #PH
antiguaSinonimos = ["antigua", "precaria"] #vieja
CONSTRUCCION_SINONIMOS = ["vivienda", "viviendas", "depto", "deptos", "departamento", "departamentos", "pileta", "piletas", "piscina", "piscinas", "edificado", "edificados", "deposito", "depósito", "depositos", "depósitos", "mejora", "mejoras", "construcción", "construccion", "construcciones", "zócalo", "zocalo", "zocalos", "mejora", "mejoras", "edificación", "edificacion", "edificaciones", "quincho", "quinchos", "galpon", "galpón", "galpones", "local", "locales", "casa", "casas", "casita", "casitas", "paredón", "paredon", "paredones", "portón", "porton", "portones", "comedor", "comedores", "cocina", "cocinas", "cerco", "cercos", "habitación", "habitacion", "habitaciones", "alambrado", "alambrados", "parrilla", "parrillas", "loza", "lozas", "contrapiso", "contrapisos", "medianera", "medianeras", "garaje", "garajes", "cabaña", "cabañas", "chalet", "chalets", "dormitorio", "dormitorios", "cochera", "cocheras", "ventana", "ventanas", "living", "livings", "lavadero", "lavaderos", "pileta", "piletas", "guardacoche", "guardacoches", "platea", "plateas", "piso", "pisos", "muro", "muros", "hall", "halls", "terraza", "terrazas", "parrilla", "parrillas", "garage", "garages", "cocina", "cocinas", "portón", "porton", "portones", "lavadero", "lavaderos", "balcón", "balcon", "balcones", "comedor", "comedores", "galería", "galeria", "galerías", "galerias", "playroom", "playrooms", "local", "locales", "cercado", "cercados", "pórtico", "póritcos", "portico", "porticos", "porche", "porches"]

def asegurado()->list:
    return  list([
        #a demoler
        [{"LOWER": {"IN": demolerSinonimos}}],
        [{"LOWER": {"IN": casaSinonimos}},{"LOWER": {"IN": antiguaSinonimos}}],
        ])

def ideal()->list:
    return  list([
        #bueno para construir
        [{"LOWER": {"IN": idealSinonimos}}, {"TEXT": "de", "OP":"?"}, {"LOWER": {"IN": ideales}}], #esto lo tengo que sacar?
        ])

