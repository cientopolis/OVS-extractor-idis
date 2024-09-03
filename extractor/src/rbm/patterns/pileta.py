piletaSinonimos = ["pileta", "piscina"]
antiguaSinonimos = ["antigua", "precaria"]
demolerSinonimos = ["reciclar", "refaccionar", "demoler", "demolicion", "demolición"]
conectores = ["para", "a"]#que necesita, se encuentra a , destinada para, ideal para (ya son muchas cosas posibles, conviene un DM)

def pileta() -> list:
    return list ( 
    [
        [
            {"LOWER": {"IN": piletaSinonimos}},
        ]
    ]
    )
def pileta_barrio() -> list:
    return list (
        [
            #dentro del barrio
            [{"LOWER" : {"IN" : ["piscinas","piletas"]}}], #dejarlo porque hay veces que lo dicen en plural y singular en la misma publicación
            [{"LOWER" : {"IN": ["pileta"]}},{"LOWER" : "climatizada"}], #poner , piscina"?
            [{"LOWER" : {"IN": piletaSinonimos}},{"LOWER" : "semi-olímpica"}]

            #pileta a refaccionar -> no mejora nada por ahora
            # [{"LOWER": {"IN": piletaSinonimos}},{"LOWER": {"IN":conectores}},{"LOWER": {"IN": demolerSinonimos}}],
            # [{"LOWER": {"IN": piletaSinonimos}},{"LOWER": {"IN": antiguaSinonimos}}]
        ]
    )
