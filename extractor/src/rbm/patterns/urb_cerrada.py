
def urb_cerrada()-> list:
    return list(
        [
            # [ 
            #     {"LOWER": {"IN": ["barrio privado", "barrio cerrado", "club de campo","urbanización privada","barrio boutique","country","countries"]}},{"POS":"PROPN", "OP":"*"}
            # ], no agarra bien los tokens entonces no matchea
            # [{"LOWER": "barrio"}, {"LOWER": "privado"}],
            # [{"LOWER": "barrio"}, {"LOWER": "cerrado"}],
            # [{"LOWER": "club"}, {"LOWER": "de"}, {"LOWER": "campo"}],
            # [{"LOWER": "urbanización"}, {"LOWER": "privada"}],
            # [{"LOWER": "barrio"}, {"LOWER": "boutique"}],
            # [{"LOWER": "country"}],
            # [{"LOWER": "countries"}],
            # [
            #     {"LEMMA": {"IN": ["cerrado", "privado"]}}
            # ],
            # [
            #     {"LOWER": "lote"},{"IS_DIGIT": True}
            # ], baja la presicion porque matchea muchos que no so
            # [
            #     {"LOWER": "lote"},{"TEXT":{"REGEX": "[A-Za-z]\d+"}}
            # ],por si solo no es indicativo de que sea barrio privado entonces resta presicion
            [
                {"LOWER": "seguridad"}
            ],
            [
                {"LOWER": "amenities"}, {"LOWER": "generales", "OP":"?"}
            ],
            [
                {"LOWER": "cancha"}, {"LOWER": "de"}, {"LOWER": {"REGEX": ".*"}}
            ]
        ]
    )