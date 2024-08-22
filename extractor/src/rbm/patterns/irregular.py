def irregular() -> list:
    return list ( 
    [
        [{"LOWER": {"IN" : ["irregular","irregulares"]}}],
        [{"LOWER": {"IN": ["lote", "forma"]}}, {"POS": "ADJ"}],
        [{"LOWER" : "lote","OP" :"?"},{"LOWER" : "martillo"}]
    ]
)
def irregular_DM() -> list:
    return list (
        [
            [
                {
                    "RIGHT_ID": "L",
                    "RIGHT_ATTRS": {"POS": "PROPN"},
                },
                {
                    "LEFT_ID": "L",
                    "REL_OP": ">",
                    "RIGHT_ID": "en",
                    "RIGHT_ATTRS": {"POS": "ADP"}
                },
                {
                    "LEFT_ID": "L",
                    "REL_OP": "<",
                    "RIGHT_ID": "terreno",
                    "RIGHT_ATTRS": {"POS": "NOUN"}
                }  
            ] 
        ]
    )