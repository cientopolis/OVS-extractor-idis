def pileta() -> list:
    return list ( 
    [
        [
            {"LOWER": {"IN": ["piscina", "pileta","Pileta"]}},
        ]
    ]
    )
def pileta_barrio() -> list:
    return list (
        [
            [{"LOWER" : {"IN" : ["piscinas","piletas"]}}],
            [{"LOWER" : "pileta"},{"LOWER" : "climatizada"}],
            #[{"LOWER" : "pileta"},{"LOWER" : "semi-olímpica"}]
        ]
    )
