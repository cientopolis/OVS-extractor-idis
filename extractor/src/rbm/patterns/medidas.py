CONECTORES_MEDIDAS = ["x", "por"]
MEDIDAS = ["metro", "metros", "m", "ms", "mt", "mts", "m2", "m."] 
RELLENO = ["ADP", "ADV", "PROPN", "NOUN", "DET", "ADJ"] # sacarle el DET y ADJ? -> por ahora da buenos resultados sin perjudicar
FRENTE= ["frente", "ancho"]
FONDO= ["fondo", "largo"]
def medidas():
    return  list([            
            # 5 mt x 10 mt 
            [
                {"LIKE_NUM":True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"TEXT":",", "OP":"?"}, 
                {"LOWER":{"IN":CONECTORES_MEDIDAS}}, 
                {"LIKE_NUM":True}
             ],
             # 5 mt x 10 mt x 40 mt
             [
                {"LIKE_NUM":True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"TEXT":",", "OP":"?"}, 
                {"LOWER":{"IN":CONECTORES_MEDIDAS}}, 
                {"LIKE_NUM":True}, 
                {"LOWER": {"IN":MEDIDAS}, "OP": "?"},
                {"LOWER":{"IN":CONECTORES_MEDIDAS}}, 
                {"LIKE_NUM":True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"}
             ],
             # 5 mt x 10 mt x 40 mt x 5 mt
             [
                {"LIKE_NUM":True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"TEXT":",", "OP":"?"}, 
                {"LOWER":{"IN":CONECTORES_MEDIDAS}}, 
                {"LIKE_NUM":True}, 
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"LOWER":{"IN":CONECTORES_MEDIDAS}}, 
                {"LIKE_NUM":True}, 
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"LOWER":{"IN":CONECTORES_MEDIDAS}}, 
                {"LIKE_NUM":True}, 
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"}
             ],
             #Frente de x mts y Fondo de x mts
             [
                {"LOWER": {"IN": FRENTE}},
                {"POS": "ADP", "OP":"?"},
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"LOWER":{"IN":CONECTORES_MEDIDAS+["y", "con"]}, "OP": "?"}, 
                {"LOWER": {"IN": FONDO}},
                {"POS": "ADP", "OP":"?"},
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
             ],
             #frente de 15.85 mts y 25 de fondo
             [
                {"LOWER": {"IN": FRENTE}},
                {"POS": "ADP", "OP":"?"},
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"LOWER":{"IN":CONECTORES_MEDIDAS+["y", "con"]}, "OP": "?"}, 
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"POS": "ADP", "OP":"?"},
                {"LOWER": {"IN": FONDO}},
             ],
             # 8 de frente por 35 de largo
             [
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"POS": "ADP", "OP":"?"},
                {"LOWER": {"IN": FRENTE}},
                {"LOWER":{"IN":CONECTORES_MEDIDAS+["y", "con"]}, "OP": "?"}, 
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"POS": "ADP", "OP":"?"},
                {"LOWER": {"IN": FONDO}},
             ],
             #Frente: x mts y Fondo: x mts
             [
                {"LOWER": {"IN": FRENTE}},
                {"IS_PUNCT": True},
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"LOWER":{"IN":CONECTORES_MEDIDAS+["y", "con", "."]}, "OP": "?"}, 
                {"LOWER": {"IN": FONDO}},
                {"IS_PUNCT": True},
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
             ],
             # 12 METROS DE FRENTE X 12 DE FONDO
             [
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"POS": "ADP", "OP":"?"},
                {"LOWER": {"IN": FRENTE}},
                {"LOWER":{"IN":CONECTORES_MEDIDAS+["y", "con"]}, "OP": "?"}, 
                {"LIKE_NUM": True},
                {"LOWER": {"IN":MEDIDAS}, "OP":"?"},
                {"POS": "ADP", "OP":"?"},
                {"LOWER": {"IN": FONDO}},
             ],
             
            #2 MEDIDAS, que tenga la unidad en algún lado -> anda peor que el patrón de arriba
            #[{"LIKE_NUM":True},{"LOWER": {"IN":MEDIDAS}}, {"POS":{"IN":RELLENO}, "OP":"*"},{"LOWER":{"IN":CONECTORES_MEDIDAS}}, {"LIKE_NUM":True, "OP":"+"}, {"LOWER": {"IN":MEDIDAS}, "OP":"?"}],
            #[{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN":CONECTORES_MEDIDAS}}, {"LIKE_NUM":True, "OP":"+"}, {"LOWER": {"IN":MEDIDAS}}],
 
            #3 MEDIDAS, con la unidad opcional -> anda peor que la opcion de abajo
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],
            #3 MEDIDAS, que tenga la unidad en algún lado            [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],
            # [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],
            # [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}}],

            # # #4 MEDIDAS, con la unidad opcional
            # # #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],     
            # # #4 MEDIDAS, que tenga la unidad en algún lado 
            # [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],     
            # [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],     
            # [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],     
            # [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}}],     

            # # #solo hay un caso con 5 MEDIDAS y no anda porque separa con puntos a las DIMENSIONes
            # # #5 MEDIDAS, con la unidad opcional
            # # #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}]
            # # #5 MEDIDAS, que tenga la unidad en algún lado
            # # #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}],
            # # #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}],
            # # #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}],
            # # #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}],
            # # #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}],
            # [
            #     {"LIKE_NUM": True},
            #     {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            #     {"LOWER": "x"},
            #     {"LIKE_NUM": True},
            #     {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            #     {"LOWER": "x", "OP": "?"},
            #     {"LIKE_NUM": True, "OP": "?"},
            #     {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            #     {"LOWER": "x", "OP": "?"},
            #     {"LIKE_NUM": True, "OP": "?"},
            #     {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            # ],
            # [
            #     {"LIKE_NUM": True},
            #     {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            #     {"LOWER": "x"},
            #     {"LIKE_NUM": True},
            #     {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            #     {"OP": "?"},
            #     {"LOWER": "martillo"},
            #     {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            #     {"LOWER": "x", "OP": "?"},
            #     {"LIKE_NUM": True, "OP": "?"},
            #     {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            # ],

                #no aporta precisión:
            #    [
            #       {"LIKE_NUM": True},
            #        {"LOWER": {"IN": ["m", "mts", "metros"]}, "OP": "?"},
            #        {"LOWER": "de", "OP": "?"},
            #        {"LOWER": {"IN": FRENTE}},
            #        {"LOWER": {"IN": ["por", "x", "y"]}, "OP": "?"},
            #        {"LIKE_NUM": True},
            #        {"LOWER": {"IN": ["m", "mts", "metros"]}, "OP": "?"},
            #        {"LOWER": "de", "OP": "?"},
            #        {"LOWER": {"IN": FONDO}},
            #    ],
            ]
    )

