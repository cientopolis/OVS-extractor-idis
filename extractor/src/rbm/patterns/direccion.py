
 #los uso con LEMMA
#calleSinonimos = [ "av", "calle", "Calle", "ruta", "Ruta", "avenida", "diagonal", "Diagonal", "dg", "Dg", "diag", "Diag"]
#manzanaSinonimos = ["manzana", "Manzana", "mz", "Mz", "mza", "Mza"]
#numeroSinonimos = ["numero", "nro", "número", "número", "n", "n°", "nº", "nº", "n°", "nro."]

#los uso con LOWER
#calleSinonimos2 = ["avs", "av", "calle", "calles", "ruta", "rutas", "avenida", "avenidas", "diagonal", "diagonales", "dg", "dgs", "diag", "diags"]
CALLE_SINONIMOS = ["bv.", "bv", "avs", "avs.", "av", "av,","av.", "calle", "calles", "avenida", "avenidas", "diagonal", "diagonales", "dg", "dg.", "dgs", "dgs.","diag", "diasg.", "diags", "diags"]#tal vez dirá: "calle 5 entre calles 4 y 7"
MANZANA_SINONIMOS = ["manzana", "mz", "mz.", "mza", "mza."]
NUMERO_SINONIMOS = ["numero", "numeros", "nro", "nros", "número", "números", "°", "n", "n°", "nº", "nº", "n°", "nro.", "ns", "n°s", "nºs", "nºs", "n°s", "nros."]
ANTE_NUMERO = ["km", "al", "altura", "altura:", "alt", "alt.", "kilometro", "km.", "Km."]

ENTRE = ["e/", "entre", "a", "a/", "esquina", "esq", "esq."]#pensé en sacarle lo de esquina pero fue contraproducente
INTERSECCION = ["y", "e", "esquina", "esq", "esq."]
#letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]#trae probleamos porque quiere matchear con la letra 'a' en las oraciones como: "a 5 metros de ahí"
LETRA_MAYUSCULA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#extra = ["bis"] + letra #empeora precisión
#PARA LOS MATCHERS DE DIRECCIÓN: LOS PATRONES COMENTADOS sin explicación es porque no aportan precisión, pero en una db más grande tal vez si (no están probados)

SOBRE_SINONIMOS = ["en"]
NOMBRE_LOTE = ["NUM", "PROPN"]
MEDIDAS = ["metro", "metros", "m", "ms", "mt", "mts", "m2"] 
CONECTORES_MEDIDAS = ["x", "por"]
CALLE_SEGMENTO = ["bis", "Bis", "BIS"]  + LETRA_MAYUSCULA

def dir_nro():
    return  list([ #direcciones platenses = numericas
                [
                    # calle montevideo 412
                    # calle 7 412
                    # calle 7 bis al 400
                    # calle montevideo n° 412
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": "PUNCT", "OP":"?"},
                    {"POS": "PROPN", "OP":"?"},
                    {"POS": "PUNCT", "OP":"?"},
                    {"POS": "PROPN", "OP":"{1,3}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"?"},
                    {"LIKE_NUM":True},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                [
                    # calle 9 de julio 412
                    # Av. de los quilmes n° 123
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": "PUNCT", "OP":"?"},
                    {"POS": {"IN": ["PROPN","NUM"]}},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"?"},
                    {"LIKE_NUM":True},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                [
                    # moreno n° 123
                    # moreno al 123
                    # Av. De los Quilmes N° X
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": {"IN": ["PROPN", "ADP", "DET"]}, "OP":"{1,3}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}},
                    {"LIKE_NUM":True},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                # [
                #     # 9 n° 123
                #     # 9 al 123
                #     {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                #     {"POS": "NUM"},
                #     {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                #     {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}},
                #     {"LIKE_NUM":True},
                # ],           
            ])

def dir_interseccion():
    return  list([
                # calle moreno y san martin
                # calle moreno 1231 y san martin bis
                # calle moreno n° 1231 y san martin bis
                [
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": {"IN": ["PROPN", "DET", "ADP"]}, "OP":"{1,3}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LIKE_NUM": True, "OP": "?"},
                    {"LOWER": {"IN": INTERSECCION}},
                    {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                    {"POS": "PROPN", "OP":"{1,2}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                [
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": {"IN": ["PROPN", "DET", "ADP"]}, "OP":"{1,3}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LIKE_NUM": True, "OP": "?"},
                    {"LOWER": {"IN": INTERSECCION}},
                    {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                    {"POS": "NUM"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                # moreno n° 1231 y san martin bis
                [
                    {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                    {"POS": "PROPN", "OP":"?"},
                    {"POS": "PUNCT", "OP":"?"},
                    {"POS": "PROPN", "OP": "{1,3}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS}},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LIKE_NUM": True},
                    {"LOWER": {"IN": INTERSECCION}},
                    {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                    {"POS": "PROPN", "OP":"{1,3}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                # calle 7 y 48
                # calle 1 1359 y 61
                [
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": "NUM"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LIKE_NUM": True, "OP": "?"},
                    {"LOWER": {"IN": INTERSECCION}},
                    {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                    {"POS": "NUM"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                # calle 25 de mayo y 9 de julio
                [
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": {"IN": ["PROPN","NUM"]}},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LIKE_NUM": True, "OP": "?"},
                    {"LOWER": {"IN": INTERSECCION}},
                    {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                    {"POS": {"IN": ["PROPN","NUM"]}},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                #calle moreno y 9 de julio
                [
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": {"IN":["PROPN", "NOUN", "NUM", "PUNCT"]}, "OP":"{1,3}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LIKE_NUM": True, "OP": "?"},
                    {"LOWER": {"IN": INTERSECCION}},
                    {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                    {"POS": {"IN": ["PROPN","NUM"]}},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ],
                # calle 25 de mayo y san martin
                [
                    {"LOWER": {"IN":CALLE_SINONIMOS}},
                    {"POS": {"IN": ["PROPN","NUM"]}},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LIKE_NUM": True, "OP": "?"},
                    {"LOWER": {"IN": INTERSECCION}},
                    {"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},
                    {"POS": {"IN":["PROPN", "NOUN", "NUM", "ADP"]}, "OP":"+"},
                    {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
                    {"LOWER": {"NOT_IN": MEDIDAS}}
                ]
                
            ])

def dir_entre():
    return [
        [
            # calle la hermosura 1231 e/ calle moreno y san martin
            # calle la hermosura n° 1231 e/ calle moreno y san martin bis
            # calle la hermosura n° 1231, entre calle moreno y san martin bis
            # calle 7 n° 1231, entre calle moreno y san martin bis
            # calle la hermosura n° 1231, entre calle 7 y 8 BIS
            {"LOWER": {"IN":CALLE_SINONIMOS},  "OP": "?"}, 
            {"POS": "PROPN", "OP":"?"},
            {"POS": "PUNCT", "OP":"?"},
            {"POS": {"IN": ["DET","PROPN", "ADP"]}, "OP":"{1,3}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}, 
            {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"}, 
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": {"IN": ENTRE}}, 
            {"POS": "DET", "OP": "?"},
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN", "NUM", "DET"]}, "OP": "+"}, 
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
            {"LOWER": {"IN": INTERSECCION}}, 
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN", "NUM", "DET"]}, "OP": "+"}, 
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}
        ],
        [
            # calle 7 n° 1231, entre calle moreno y san martin bis
            # calle 13 C e/ 471 y 472
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": "NUM"}, 
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}, 
            {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"}, 
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": {"IN": ENTRE}}, 
            {"POS": "DET", "OP": "?"},
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN", "NUM"]}, "OP": "{1,3}"}, 
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
            {"LOWER": {"IN": INTERSECCION}}, 
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN", "NUM"]}, "OP": "{1,3}"}, 
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}
        ],
        [
             # calle 9 de julio 1231 e/ 25 de mayo Y 3 de febrero
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}, 
            {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"}, 
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": {"IN": ENTRE}}, 
            {"POS": "DET", "OP": "?"},
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
            {"LOWER": {"IN": INTERSECCION}}, 
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}
        ],
        [
             # calle moreno 1231 e/ 25 de mayo Y san martín
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}, 
            {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"}, 
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": {"IN": ENTRE}}, 
            {"POS": "DET", "OP": "?"},
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
            {"LOWER": {"IN": INTERSECCION}}, 
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}
        ],
        [
             # calle moreno 1231 e/ 25 de mayo Y san martín
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}, 
            {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"}, 
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": {"IN": ENTRE}}, 
            {"POS": "DET", "OP": "?"},
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
            {"LOWER": {"IN": INTERSECCION}}, 
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}
        ],
        [
             # calle moreno 1231 e/ 25 de mayo Y san martín
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},{"POS": {"IN":["ADP", "DET"]}},{"POS": "PROPN", "OP":"{0,1}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}, 
            {"LOWER": {"IN":NUMERO_SINONIMOS+ANTE_NUMERO}, "OP":"*"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"}, 
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": {"IN": ENTRE}}, 
            {"POS": "DET", "OP": "?"},
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"},
            {"LOWER": {"IN": INTERSECCION}}, 
            {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, 
            {"POS": {"IN": ["PROPN","NUM"]}, "OP":"{1,2}"},
            {"ORTH": {"IN": CALLE_SEGMENTO}, "OP": "?"}
        ]
   ]


def dir_lote():
    return  list([
                #manzana letrada
                [
                    {"LOWER": "lote"},
                    {"LOWER": {"IN":NUMERO_SINONIMOS}},
                    {"POS": {"IN": NOMBRE_LOTE}},
                ],
                [
                    {"LOWER": "lote"}, 
                    {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},
                    {"POS": {"IN": NOMBRE_LOTE}},
                    {"LOWER": {"IN": SOBRE_SINONIMOS}, "OP":"?"},
                    {"LOWER": {"IN": MANZANA_SINONIMOS}},
                    {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},
                    {"TEXT": {"IN": LETRA_MAYUSCULA}}
                ],
                [
                    {"LOWER": "lote"}, 
                    {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},
                    {"POS": {"IN": NOMBRE_LOTE}},
                    {"LOWER": {"IN": SOBRE_SINONIMOS}, "OP":"?"},
                    {"LOWER": {"IN": MANZANA_SINONIMOS}},
                    {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},
                    {"POS": {"IN": NOMBRE_LOTE}}
                ],
                [
                    {"LOWER": {"IN": MANZANA_SINONIMOS}},
                    {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},
                    {"TEXT": {"IN": LETRA_MAYUSCULA}},
                    {"IS_PUNCT": True, "OP":"?"},
                    {"LOWER": "lote"}, 
                    {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},
                    {"POS": {"IN": NOMBRE_LOTE}},
                ],
                [
                    {"LOWER": {"IN": MANZANA_SINONIMOS}},
                    {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},
                    {"POS": {"IN": NOMBRE_LOTE}},
                    {"IS_PUNCT": True, "OP":"?"},
                    {"LOWER": "lote"}, 
                    {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},
                    {"POS": {"IN": NOMBRE_LOTE}},
                ]
                # #manzana numerada
                # [{"LOWER": "lote"},{"POS": {"IN": NOMBRE_LOTE}},{"LOWER": {"IN": SOBRE_SINONIMOS}, "OP":"?"},{"LOWER": {"IN": MANZANA_SINONIMOS}},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True}],
                # [{"LOWER": {"IN": MANZANA_SINONIMOS}},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": SOBRE_SINONIMOS}, "OP":"?"},{"LOWER": "lote"},{"POS": {"IN": NOMBRE_LOTE}}],
            
                # [
                #    {
                #        "LOWER": {"IN": ["calle", "avenida", "av", "diagonal", "diag"]},
                #        "OP": "?",
                #    },
                #    {"TEXT": ".", "OP": "?"},
                #    {"POS": "PROPN", "OP": "+"},
                #    {"LOWER": "al", "OP": "?"},
                #    {"LIKE_NUM": True},
                #],

                #no aporta
                #[
                #    {
                #        "LOWER": {"IN": CALLE_SINONIMOS},
                #        "OP": "?",
                #    },
                #    #{"TEXT": ".", "OP": "?"},
                #    {"POS": "PROPN", "OP": "+"},
                #    {"LOWER": "n"},
                #    {"TEXT": "°"},
                #    {"LIKE_NUM": True},
                #],
            
            #resta precisión
            #[
            #        {
            #            "LOWER": {"IN": ["calle", "avenida", "av", "diagonal", "diag"]},
            #            "OP": "?",
            #        },
            #        {"TEXT": ".", "OP": "?"},
            #        {"POS": {"IN": ["PROPN", "NUM"]}, "OP": "+"},
            #        {"LOWER": {"IN": ["y", "esquina", "esq.", "e"]}},
            #        {
            #            "LOWER": {"IN": ["calle", "avenida", "av", "diagonal", "diag"]},
            #            "OP": "?",
            #        },
            #        {"TEXT": ".", "OP": "?"},
            #        {"POS": {"IN": ["PROPN", "NUM"]}, "OP": "+"},
            #    ]
            
            #este caso particular funciona bien poniendo a CALLE_SINONIMOS opcional
            # [
            #         {
            #             "LOWER": {"IN": CALLE_SINONIMOS},
            #             "OP": "?",
            #         },
            #         #{"TEXT": ".", "OP": "?"},
            #         {"POS": {"IN": NOMBRE_LOTE}, "OP": "+"},
            #         {"LOWER": {"IN": CONECTORES}},
            #         {
            #             "LOWER": {"IN": CALLE_SINONIMOS},
            #             "OP": "?",
            #         },
            #         #{"TEXT": ".", "OP": "?"},
            #         {"POS": {"IN": NOMBRE_LOTE}, "OP": "+"},
            #         {"LOWER": "y"},
            #         {
            #             "LOWER": {"IN": CALLE_SINONIMOS},
            #             "OP": "?",
            #         },
            #         #{"TEXT": ".", "OP": "?"},
            #         {"POS": {"IN": NOMBRE_LOTE}, "OP": "+"},
            #     ]
            ])