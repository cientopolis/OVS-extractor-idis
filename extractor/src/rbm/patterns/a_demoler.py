idealSinonimos = ["para", "ideal", "destino"]#  "posibilidad"
ideales  = ["comercial", "proyecto", "proyectos", "inversión", "inversion", "edificar", "edificio", "edificios", "constructor","constructores", "construccion", "construcciones", "construcción", "inversor", "inversores", "emprendimiento", "emprendimientos", "desarrollo", "desarrollos"] #"proyecto", "proyectos", 
demolerSinonimos = ["demoler", "demolicion", "demolición", "demolerse"]#"acondicionar", "reciclar", "refaccionar",  "refaccionarse", "reciclarse", "acondicionarse" 
casaSinonimos= ["casa", "construccion", "construcción"] #PH
antiguaSinonimos = ["precaria"] #vieja, "antigua", #si es vieja no importa, importa si está en mal estado
CONSTRUCCION_SINONIMOS = ["vivienda", "viviendas", "depto", "deptos", "departamento", "departamentos", "pileta", "piletas", "piscina", "piscinas", "edificado", "edificados", "deposito", "depósito", "depositos", "depósitos", "mejora", "mejoras", "construcción", "construccion", "construcciones", "zócalo", "zocalo", "zocalos", "mejora", "mejoras", "edificación", "edificacion", "edificaciones", "quincho", "quinchos", "galpon", "galpón", "galpones", "local", "locales", "casa", "casas", "casita", "casitas", "paredón", "paredon", "paredones", "portón", "porton", "portones", "comedor", "comedores", "cocina", "cocinas", "cerco", "cercos", "habitación", "habitacion", "habitaciones", "alambrado", "alambrados", "parrilla", "parrillas", "loza", "lozas", "contrapiso", "contrapisos", "medianera", "medianeras", "garaje", "garajes", "cabaña", "cabañas", "chalet", "chalets", "dormitorio", "dormitorios", "cochera", "cocheras", "ventana", "ventanas", "living", "livings", "lavadero", "lavaderos", "pileta", "piletas", "guardacoche", "guardacoches", "platea", "plateas", "piso", "pisos", "muro", "muros", "hall", "halls", "terraza", "terrazas", "parrilla", "parrillas", "garage", "garages", "cocina", "cocinas", "portón", "porton", "portones", "lavadero", "lavaderos", "balcón", "balcon", "balcones", "comedor", "comedores", "galería", "galeria", "galerías", "galerias", "playroom", "playrooms", "local", "locales", "cercado", "cercados", "pórtico", "póritcos", "portico", "porticos", "porche", "porches"]
LOTE_SINONIMOS = ["lote", "lotes", "terreno", "terrenos", "parcela", "parcelas", "predio", "predios"]
VALOR_SINONIMOS = ["valor", "precio", "dinero"]

def asegurado()->list:
    return  list([
        #a demoler
        [{"LOWER": {"IN": demolerSinonimos}}],
        [{"LOWER": {"IN": casaSinonimos}},{"LOWER": {"IN": antiguaSinonimos}}], #esto en realidad no importa
        [{"LOWER": {"IN":["vende", "venden"]}},{"LOWER": "como"},{"LOWER": {"IN":LOTE_SINONIMOS}}],
        [{"LOWER": "toma"},{"LOWER": "menor"},{"LOWER": {"IN":VALOR_SINONIMOS}}],
        [{"LOWER": "se"},{"LOWER": "considera"},{"LOWER": "el"},{"LOWER":{"IN":LOTE_SINONIMOS}}],
        ])

def ideal()->list:
    return  list([
        #bueno para construir
        [{"LOWER": {"IN": idealSinonimos}}, {"TEXT": {"IN":["de", "para"]}, "OP":"?"}, {"LOWER": {"IN": ideales}}], #esto lo tengo que sacar?
        ])
