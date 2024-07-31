
def urb_cerrada()-> list:
    return list(
        [
            [{"LOWER" : "barrio"},{"LOWER" : "cerrado"}],
            [{"LOWER" : "barrios"},{"LOWER" : "cerrados"}],
            [{"LOWER" : "club"},{"LOWER" : "house"}],
            [{"LOWER" : "fincas"},{"LOWER" : "de"}],
            [{"LOWER" : "condominio"},{"LOWER" : "cerrado"}],
        ]
    )

# relizar dependency matcher para descartar los casos como: "lindero a club de campo Grand Bell"
