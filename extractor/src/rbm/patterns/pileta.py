piletaSinonimos = ["pileta", "piscina"]
antiguaSinonimos = ["antigua", "precaria"]
demolerSinonimos = ["reciclar", "refaccionar", "demoler", "demolicion", "demolición"]
conectores = ["para", "a"]#que necesita, se encuentra a , destinada para, ideal para (ya son muchas cosas posibles, conviene un DM)
POSIBLE_COUNTRY = ["cancha", "canchas", "futbol", "fútbol", "tenis", "tennis", "rugby", "spa", "spas", "gimnasio", "gimnasios", "paddle", "hockey", "polo"] #polo
DE_SINONIMOS = ["de", "para"]
NATACION_SINONIMOS = ["natacion", "natación"]

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
            #[{"LOWER" : {"IN": piletaSinonimos}},{"LOWER" : "climatizada"}], #baja rendimiento

            #piletas grandes
            [{"LOWER" : {"IN": piletaSinonimos}},{"LOWER" : "semi-olímpica"}],
            #[{"LOWER" : {"IN": piletaSinonimos}},{"LOWER" : {"IN": DE_SINONIMOS}},{"LOWER" : {"IN": NATACION_SINONIMOS}}],#pileta de natación
            #gran pileta

            #posible country, aunque no lo sea no quiero matchear con la pileta
            [{"LOWER" : {"IN": POSIBLE_COUNTRY}}]

            #pileta a refaccionar -> no mejora nada por ahora
            # [{"LOWER": {"IN": piletaSinonimos}},{"LOWER": {"IN":conectores}},{"LOWER": {"IN": demolerSinonimos}}],
            # [{"LOWER": {"IN": piletaSinonimos}},{"LOWER": {"IN": antiguaSinonimos}}]
            #pileta de lona
            #con vista a piscina
        ]
    )
