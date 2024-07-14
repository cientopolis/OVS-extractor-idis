TIPOS_FOT = ["residencial", "comercial", "industrial", "res", "res.", "com", "com.", "ind", "ind."]
FOT_SINONIMOS = ['fot', 'f.o.t']
NUM_PORCENTAJE = ["NUM", "SYM"]
PREMIOS_SINONIMOS = ["premios", "premio"]
FOT_CONECTOR = ["de", ":", "es", ",", ".", "="]
FOT_UNIDAD = ["m2", "mts2", "metros2", "metros cuadrados", "m²", "mts²", "metros²", "metros cuadrados", "m2.", "mts2.", "metros2.", "metros cuadrados.", "m².", "mts².", "metros².", "metros cuadrados."]
ADICION_SINONIMOS = ["mas", "más", "con", "+"]    
def fot()->list:
    return  list([
            #1 fot
            [
                {'LOWER': {'IN':FOT_SINONIMOS}},
                {"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},
                {"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},
                {"POS": "NUM"},
                {"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"}
            ],
            [
                {'LOWER': {'IN':FOT_SINONIMOS}},
                {"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},
                {"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},
                {"LIKE_NUM": True},
                {"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"}
            ],
            [
                {'LOWER': {'IN':FOT_SINONIMOS}},
                {"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},
                {"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},
                {"POS": "NUM"},
                {"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"}, 
                {"IS_PUNCT":  True},
                {'LOWER': {'IN':FOT_SINONIMOS}, "OP":"?"},
                {"LOWER": {"IN":TIPOS_FOT}},
                {"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},
                {"POS": "NUM"},
                {"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"}
            ],
            [
                {'LOWER': {'IN':FOT_SINONIMOS}},
                {"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},
                {"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},
                {"LIKE_NUM": True},
                {"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"}, 
                {"IS_PUNCT":  True},
                {'LOWER': {'IN':FOT_SINONIMOS}, "OP":"?"},
                {"LOWER": {"IN":TIPOS_FOT}},
                {"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},
                {"LIKE_NUM": True},
                {"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"}
            ],

            [{"LOWER": "factor"},{"LOWER": "de"},{"LOWER": "ocupacion"},{"LOWER": "total"},{"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},{'LIKE_NUM': True},{"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"}],
                
            #1 fot con premios
            [{'LOWER': {'IN':FOT_SINONIMOS}},{"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},{"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},{"POS": "NUM"},{"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"},{"LOWER":{"IN":ADICION_SINONIMOS}}, {"POS": {"IN":NUM_PORCENTAJE}, "OP":"?"},{"LOWER": "en", "OP":"?"},{"LOWER": {"IN":PREMIOS_SINONIMOS}}],
            # [{"LOWER": "factor"},{"LOWER": "de"},{"LOWER": "ocupacion"},{"LOWER": "total"},{"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},{"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},{"POS": "NUM"},{"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"},{"LOWER":{"IN":ADICION_SINONIMOS}}, {"POS": {"IN":NUM_PORCENTAJE}, "OP":"?"},{"LOWER": "en"},{"LOWER": {"IN":PREMIOS_SINONIMOS}}],

            #2 fots sin premios
            #tengo problemas con el helper.py:
            # [{'LOWER': {'IN':FOT_SINONIMOS}},{"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},{"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},{"POS": "NUM"},{"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"},{"POS":"PUNCT", "OP":"?"},{'LOWER': {'IN':FOT_SINONIMOS}},{"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},{"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},{"POS": "NUM"},{"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"},]

            #2 fots con premios
            # [{'LOWER': {'IN':FOT_SINONIMOS}},{"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},{"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},{"POS": "NUM"},{"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"},{"LOWER":{"IN":ADICION_SINONIMOS}}, {"POS": {"IN":NUM_PORCENTAJE}, "OP":"?"},{"LOWER": "en"},{"LOWER": {"IN":PREMIOS_SINONIMOS}},{"POS":"PUNCT", "OP":"?"},{'LOWER': {'IN':FOT_SINONIMOS}},{"LOWER": {"IN":TIPOS_FOT}, "OP":"?"},{"TEXT":{"IN":FOT_CONECTOR}, "OP":"*"},{"POS": "NUM"},{"LOWER":{"IN":FOT_UNIDAD}, "OP":"?"},{"LOWER":{"IN":ADICION_SINONIMOS}}, {"POS": {"IN":NUM_PORCENTAJE}, "OP":"?"},{"LOWER": "en"},{"LOWER": {"IN":PREMIOS_SINONIMOS}}]
            
            #no aporta precisión
            #[
            #        {"LOWER": {"IN": ["fot", "f.o.t"]}},
            #        {
            #            "LOWER": {
            #                "IN": [
            #                   "res",
            #                    "residencial",
            #                    "comercial",
            #                    "com",
            #                    "industrial",
            #                ]
            #            },
            #            "OP": "?",
            #        },
            #        {"IS_PUNCT": True, "OP": "?"},
            #        {"POS": "NUM"},
            #    ]
            ]
    )   