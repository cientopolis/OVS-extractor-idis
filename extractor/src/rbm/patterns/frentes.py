def frentes() -> list :
    return list (
    [
        [
            {
                "RIGHT_ID": "frentes",
                "RIGHT_ATTRS": {"LOWER": {"IN": ["frente", "frentes","Frentes"]}},
            },
            {
                "LEFT_ID": "frentes",
                "REL_OP": ">",
                "RIGHT_ID": "num",
                "RIGHT_ATTRS": {"DEP": {"IN": ["nummod", "amod"]}},
            }
        ],
        [
            {"RIGHT_ID": "frentes", "RIGHT_ATTRS": {"LOWER": "salida"}},
            {
                "LEFT_ID": "frentes",
                "REL_OP": ">",
                "RIGHT_ID": "calles",
                "RIGHT_ATTRS": {"DEP": "obl"},
            },
            {
                "LEFT_ID": "calles",
                "REL_OP": ">",
                "RIGHT_ID": "num",
                "RIGHT_ATTRS": {"DEP": "nummod"},
            }
        ],
        [
            {
                "RIGHT_ID": "calles",
                "RIGHT_ATTRS": {"LOWER": {"IN": ["calle", "calles","avenida","avenidas"]}},
            },
            {
                "LEFT_ID": "calles",
                "REL_OP": "<",
                "RIGHT_ID": "acceso",
                "RIGHT_ATTRS": {"POS": "NOUN"},
            },
            {
                "LEFT_ID": "calles",
                "REL_OP": ">",
                "RIGHT_ID": "por",
                "RIGHT_ATTRS": {"POS": "ADP"}
            },
            {
                "LEFT_ID": "calles",
                "REL_OP": ">",
                "RIGHT_ID": "numero",
                "RIGHT_ATTRS": {"POS": "NUM"}
            }
        ],
        [
            {
                "RIGHT_ID": "terreno",
                "RIGHT_ATTRS": {"LOWER": {"IN": ["terreno", "lote","inmueble","parcela"]}},
            },
            {
                "LEFT_ID": "terreno",
                "REL_OP": ">",
                "RIGHT_ID": "triple",
                "RIGHT_ATTRS": {"POS": "NUM"}
            },
            {
                "LEFT_ID": "triple",
                "REL_OP": ">",
                "RIGHT_ID": "de",
                "RIGHT_ATTRS": {"POS": "ADP"}
            },
            {
                "LEFT_ID": "terreno",
                "REL_OP": ">",
                "RIGHT_ID": "frente",
                "RIGHT_ATTRS": {"POS": "NOUN"},
            }
        ],
        [
            {
                "RIGHT_ID": "casa",
                "RIGHT_ATTRS": {"POS": "PROPN" },
            },
            {
                "LEFT_ID": "casa",
                "REL_OP": ">",
                "RIGHT_ID": "doble",
                "RIGHT_ATTRS": {"POS": "ADJ"}
            },
            {
                "LEFT_ID": "casa",
                "REL_OP": ">",
                "RIGHT_ID": "frente",
                "RIGHT_ATTRS": {"LOWER": "frente"}
            },    
        ]    
    ] 
)
   