palabraPreVenta = ["preventa", "pre-venta"]
desarrolloSinonimos = ["construcción", "construccion", "obra", "desarrollo"]
propuestaSinonimos = ["propuesta", "proyecto", "posible", "posibilidad", "destinado", "preparado"]#, "posible", "posibilidad", "destinado"
palabrasFuturoExactas = ["concretará", "contará","entregará", "entregarán", "entrega", "posesión", "posesión"]#las palabras en futuro deben tener los acentos obligatoriamente
cuotasIndicadorExacto = ["cuota", "cuotas", "cta", "ctas", "plan", "pozo", "anticipo", "fideicomiso"]
cuotasIndicadorAproximado = ["financiar","financiación", "financiacion"]#encontrarla en cualquier conjugación o palabra de la familia
tiempo = ["año", "años", "mes", "meses"]
relleno = ["DET", "ADP"]

def asegurados():
    return list([
        [{"LOWER":{"IN": palabraPreVenta}}],
        [{"LOWER": "pre"}, {"LOWER": "venta"}],
    ])

def posibles():
    return list([ #si matcheo algo de acá tal vez es una preventa
        [{"LOWER":{"IN": desarrolloSinonimos}}], #sacar desarrollo?
        [{"LOWER":{"IN": palabrasFuturoExactas}}],
        [{"LOWER": "primeras"}, {"LIKE_NUM": True}, {"LOWER": "unidades"}],
        #distingo si encuentro 'posesión' de 'posesión futura' ya que si ocurre la última el contador quedará en 2
        [{"LOWER": "posesión"}, {"LOWER": "futura"}],
        [{"LOWER": "posesión"}, {"LOWER": "a"}, {"LIKE_NUM": True}, {"LOWER": {"IN": tiempo}}],
    ])

def fecha():
    return list([ #si encuentra un año mayor al actual aporta, pero no es seguro que sea pre-venta
        [{"POS":"NUM"}] #solo si es como un número voy a poder comparar
    ])

def cuotas():
    return list([ #si matcheo algo de acá tal vez es una preventa
        [{"LOWER": {"IN": cuotasIndicadorExacto}}],
        [{"LEMMA": {"IN": cuotasIndicadorAproximado}}],
    ])

def descartar():
    return list([ #si matcheo algo de acá seguro no es una preventa
            [{"LEMMA": {"IN": propuestaSinonimos}}, {"POS": {"IN": relleno}}, {"LOWER": {"IN": desarrolloSinonimos}}]
        ])