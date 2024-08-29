piletaSinonimos = ["pileta", "piscina", "Pileta", "Piscina"]
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
            [{"LOWER" : {"IN" : ["piscinas","piletas"]}}],
            [{"LOWER" : "pileta"},{"LOWER" : "climatizada"}],
            #[{"LOWER" : "pileta"},{"LOWER" : "semi-olímpica"}]

            #pileta a refaccionar
            # [{"LOWER": {"IN": piletaSinonimos}},{"LOWER": {"IN":conectores}},{"LOWER": {"IN": demolerSinonimos}}],
            # [{"LOWER": {"IN": piletaSinonimos}},{"LOWER": {"IN": antiguaSinonimos}}]
        ]
    )
