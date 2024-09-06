piletaSinonimos = ["pileta", "piscina"]
antiguaSinonimos = ["antigua", "precaria"]
demolerSinonimos = ["reciclar", "refaccionar", "demoler", "demolicion", "demolición"]
conectores = ["para", "a"]#que necesita, se encuentra a , destinada para, ideal para (ya son muchas cosas posibles, conviene un DM)
POSIBLE_COUNTRY = ["cancha", "canchas", "futbol", "fútbol", "tenis", "tennis", "rugby", "spa", "spas", "gimnasio", "gimnasios", "paddle", "hockey", "polo"] #polo
DE_SINONIMOS = ["de", "para"]
NATACION_SINONIMOS = ["natacion", "natación"]
#dm
refaccionar_sinonimos = ["refaccionar", "reciclar", "demoler"]
barrio_sinonimos = ["barrio", "complejo", "loteo", "zona", "terraza"]
pileta_sinonimos = ["pileta", "piscina"]
cuenta_sinonimos = ["con", "cuenta", "tiene"]
compartida_sinonimos = ["compartida", "mutua", "vecinal", "barrial", "municipal", "popular"]
vista_sinonimos = ["vista", "paisaje"]
lona_sinonimos = ["lona", "plastico", "removible", "inflable"]

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

def no_pileta_DM() -> list:
    return[
        [#de lona
            {
                "RIGHT_ID": "pileta",
                "RIGHT_ATTRS": {"LOWER": {"IN": pileta_sinonimos}},
            },
                {
                "LEFT_ID": "pileta",
                "REL_OP": ">",
                "RIGHT_ID": "lona",
                "RIGHT_ATTRS": {"LOWER": {"IN":lona_sinonimos}},
            },
        ]
        ,
        [#a refaccionar
            {
                "RIGHT_ID": "pileta",
                "RIGHT_ATTRS": {"LOWER": {"IN": pileta_sinonimos}},
            },
                {
                "LEFT_ID": "pileta",
                "REL_OP": ">",
                "RIGHT_ID": "refaccionar",
                "RIGHT_ATTRS": {"LOWER": {"IN":refaccionar_sinonimos}},
            },
        ]
        ,
        [#barrio con pileta
            {
                "RIGHT_ID": "pileta",
                "RIGHT_ATTRS": {"LOWER": {"IN": pileta_sinonimos}},
            },
                    {
                "LEFT_ID": "pileta",
                "REL_OP": "<",
                "RIGHT_ID": "barrio",
                "RIGHT_ATTRS": {"LOWER": {"IN":barrio_sinonimos}},
            },
        ]
        ,
        [#el barrio cuenta con una pileta
            {
                "RIGHT_ID": "cuenta",
                "RIGHT_ATTRS": {"LOWER": {"IN": cuenta_sinonimos}},
            },
            {
                "LEFT_ID": "cuenta",
                "REL_OP": ">",
                "RIGHT_ID": "barrio",
                "RIGHT_ATTRS": {"LOWER": {"IN":barrio_sinonimos}},
            },
            {
                "LEFT_ID": "cuenta",
                "REL_OP": ">",
                "RIGHT_ID": "pileta",
                "RIGHT_ATTRS": {"LOWER": {"IN":pileta_sinonimos}},
            },
        ]
        ,
        [#pileta inflable
            {
                "RIGHT_ID": "pileta",
                "RIGHT_ATTRS": {"LOWER": {"IN": pileta_sinonimos}},
            },
                {
                "LEFT_ID": "pileta",
                "REL_OP": ">",
                "RIGHT_ID": "compartida",
                "RIGHT_ATTRS": {"LOWER": {"IN":compartida_sinonimos}},
            },
        ]
        ,
        [#vista a la pileta del country
            {
                "RIGHT_ID": "pileta",
                "RIGHT_ATTRS": {"LOWER": {"IN": pileta_sinonimos}},
            },
            {
                "LEFT_ID": "pileta",
                "REL_OP": "<",
                "RIGHT_ID": "vista",
                "RIGHT_ATTRS": {"LOWER": {"IN":vista_sinonimos}},
            },
        ]
    # ,
    # # cuenta_vista=[
    #     [#el lote cuenta con una vista a la pileta
    #         {
    #             "RIGHT_ID": "cuenta_vista",
    #             "RIGHT_ATTRS": {"LOWER": {"IN": cuenta_sinonimos}},
    #         },
    #         {
    #             "LEFT_ID": "cuenta_vista",
    #             "REL_OP": ">",
    #             "RIGHT_ID": "vista2",
    #             "RIGHT_ATTRS": {"LOWER": {"IN":vista_sinonimos}},
    #         },
    #         {
    #             "LEFT_ID": "cuenta_vista",
    #             "REL_OP": "<",
    #             "RIGHT_ID": "pileta2",
    #             "RIGHT_ATTRS": {"LOWER": {"IN":pileta_sinonimos}},
    #         },
    #     ]
    ]