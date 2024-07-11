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
    ] 
)
   