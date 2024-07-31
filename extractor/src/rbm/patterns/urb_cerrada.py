fincas = ["duggan" , "Duggan"]
def urb_cerrada()-> list:
    return list(
        [
            [{"LOWER" : "barrio"},{"LOWER" : "cerrado"}],
            [{"LOWER" : "Barrio"},{"LOWER" : "Privado."}],
            [{"LOWER" : "barrios"},{"LOWER" : "cerrados"}],
            [{"LOWER" : {"IN" : ["Club","club"]}},{"LOWER" : {"IN" : ["House","house"]}}],
            [{"LOWER" : "fincas"},{"LOWER" : "de"},{"LOWER" : {"IN" : fincas} }],
            [{"LOWER" : "condominio"},{"LOWER" : "cerrado"}],
        ]
    )

def urb_cerrada_DM()-> list:
    return list(
        [
           [
                {
                    "RIGHT_ID": "club",
                    "RIGHT_ATTRS": {"POS": "PROPN" },
                },
                {
                    "LEFT_ID": "club",
                    "REL_OP": "<",
                    "RIGHT_ID": "lindero",
                    "RIGHT_ATTRS": {"LOWER": "lindero"}
                },
                {
                    "LEFT_ID": "club",
                    "REL_OP": ">",
                    "RIGHT_ID": "con",
                    "RIGHT_ATTRS": {"POS": "ADP"}
                },
                {
                    "LEFT_ID": "club",
                    "REL_OP": ">",
                    "RIGHT_ID": "de",
                    "RIGHT_ATTRS": {"POS": "DET"}
                },
            ]
        ]
    )
# relizar dependency matcher para descartar los casos como: "lindero a club de campo Grand Bell"
