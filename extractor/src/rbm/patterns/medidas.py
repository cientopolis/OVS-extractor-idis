DIMENSION = ["frente", "fondo", "lateral", "ancho", "alto", "profundidad", "largo", "anchura", "longitud", "espesor"]
CONECTORES_MEDIDAS = ["x", "y", "por", "de", "con", ","]#me caga que separen con puntos las MEDIDAS, si pongo ahora '.' en el arreglo baja la presición
MEDIDAS = ["metro", "metros", "m", "ms", "mt", "mts"] #el LEMMA no funciona con "m" porque cree que es un número en lugar de una palabra
RELLENO = ["ADP", "ADV", "PROPN", "NOUN", "DET", "ADJ"] # sacarle el DET y ADJ? -> por ahora da buenos resultados sin perjudicar
noRELLENO = ["NUM", "PUNCT"]

def medidas():
    return  list([
            
            #2 MEDIDAS, con la unidad opcional
            [{"LIKE_NUM":True},{"LOWER": {"IN":MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS":{"IN":RELLENO}, "OP":"*"},{"LOWER":{"IN":CONECTORES_MEDIDAS}}, {"LIKE_NUM":True, "OP":"+"}, {"LOWER": {"IN":MEDIDAS}, "OP":"?"}],
            #2 MEDIDAS, que tenga la unidad en algún lado -> anda peor que el patrón de arriba
            #[{"LIKE_NUM":True},{"LOWER": {"IN":MEDIDAS}}, {"POS":{"IN":RELLENO}, "OP":"*"},{"LOWER":{"IN":CONECTORES_MEDIDAS}}, {"LIKE_NUM":True, "OP":"+"}, {"LOWER": {"IN":MEDIDAS}, "OP":"?"}],
            #[{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN":CONECTORES_MEDIDAS}}, {"LIKE_NUM":True, "OP":"+"}, {"LOWER": {"IN":MEDIDAS}}],
 
            #3 MEDIDAS, con la unidad opcional -> anda peor que la opcion de abajo
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],
            #3 MEDIDAS, que tenga la unidad en algún lado
            [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],
            [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],
            [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}}],

            #4 MEDIDAS, con la unidad opcional
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],     
            #4 MEDIDAS, que tenga la unidad en algún lado 
            [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],     
            [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],     
            [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}],     
            [{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"}, {"LOWER": {"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": MEDIDAS}}],     

            #solo hay un caso con 5 MEDIDAS y no anda porque separa con puntos a las DIMENSIONes
            #5 MEDIDAS, con la unidad opcional
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}]
            #5 MEDIDAS, que tenga la unidad en algún lado
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}],
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}],
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}],
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}],
            #[{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}, "OP":"?"}, {"POS": {"IN": RELLENO}, "OP": "*"},{"LOWER":{"IN": CONECTORES_MEDIDAS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": MEDIDAS}}],
            [
                {"LIKE_NUM": True},
                {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
                {"LOWER": "x"},
                {"LIKE_NUM": True},
                {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
                {"LOWER": "x", "OP": "?"},
                {"LIKE_NUM": True, "OP": "?"},
                {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
                {"LOWER": "x", "OP": "?"},
                {"LIKE_NUM": True, "OP": "?"},
                {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            ],
            [
                {"LIKE_NUM": True},
                {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
                {"LOWER": "x"},
                {"LIKE_NUM": True},
                {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
                {"OP": "?"},
                {"LOWER": "martillo"},
                {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
                {"LOWER": "x", "OP": "?"},
                {"LIKE_NUM": True, "OP": "?"},
                {"LOWER": {"IN": ["mts", "m", "metros"]}, "OP": "?"},
            ],

                #no aporta precisión:
            #    [
            #       {"LIKE_NUM": True},
            #        {"LOWER": {"IN": ["m", "mts", "metros"]}, "OP": "?"},
            #        {"LOWER": "de", "OP": "?"},
            #        {"LOWER": "frente"},
            #        {"LOWER": {"IN": ["por", "x", "y"]}, "OP": "?"},
            #        {"LIKE_NUM": True},
            #        {"LOWER": {"IN": ["m", "mts", "metros"]}, "OP": "?"},
            #        {"LOWER": "de", "OP": "?"},
            #        {"LOWER": "fondo"},
            #    ],
            ]
    )