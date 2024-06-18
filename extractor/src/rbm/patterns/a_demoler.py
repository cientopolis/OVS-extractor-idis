idealSinonimos = ["para", "ideal", "posibilidad"]
ideales  = ["edificar", "edificio", "edificios", "constructor","constructores", "construccion", "construcciones", "construcción", "inversor", "inversores", "emprendimiento", "emprendimientos", "desarrollo", "desarrollos"]
demolerSinonimos = ["reciclar", "refaccionar", "demoler", "demolicion", "demolición"]
casaSinonimos= ["casa", "construccion", "construcción"] #PH
antiguaSinonimos = ["antigua", "precaria"] #vieja

def a_demoler()->list:
    return  list([
        #a demoler
        [{"LOWER": {"IN": demolerSinonimos}}],
        [{"LOWER": {"IN": casaSinonimos}},{"LOWER": {"IN": antiguaSinonimos}}],

        #bueno para construir
        [{"LOWER": {"IN": idealSinonimos}}, {"TEXT": "de", "OP":"?"}, {"LOWER": {"IN": ideales}}],
        ])