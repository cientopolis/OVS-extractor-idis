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

        ]
    )