def indiviso_M() -> list:
    return list (
            [
                [{"LOWER":"indiviso"}],#indiviso 
                [{"LOWER":"indivisa"}],#indivisa
                [{"LOWER" : "partes"},{"LOWER" : "indivisas"}],
                #[{"LOWER" : "escritura"},{"LOWER" : "indvisa(proximo"}],#error humano indivisa(proximo  
                #[{"LOWER": "escritura"},{"LOWER" : "indivisa("}]     
            ]
    )
def indiviso_DM() -> list:
    return [   
            [
                {
                    "RIGHT_ID": "no_es_parte_indivisa",  # me paro en indivisa y miro flecha que ENTRA
                    "RIGHT_ATTRS": {"LOWER": {"IN": ["indivisa", "indiviso"]}}, #indvisa o indviso
                },
                {
                    "LEFT_ID": "no_es_parte_indivisa", #
                    "REL_OP": "<",
                    "RIGHT_ID": "relacion_no_es_indviso",
                    "RIGHT_ATTRS": {"POS": "NOUN"},
                },
                {
                    "LEFT_ID": "relacion_no_es_indviso", #
                    "REL_OP": ">",
                    "RIGHT_ID": "ADV_no",
                    "RIGHT_ATTRS": {"POS":{"IN" : ["ADV" , "CCONJ"]}},  # no/ni parte indivisa
                }
            ],
            #[
            #    {
            #        "RIGHT_ID": "indiviso).",
            #        "RIGHT_ATTRS": {"POS": "ADJ"},
            #    },
            #    {
            #        "LEFT_ID": "indiviso).",
            #        "REL_OP": ">",
            #        "RIGHT_ID": "NO",
            #        "RIGHT_ATTRS": {"POS": "ADV"}
            #    }            
            #]
        ]
  