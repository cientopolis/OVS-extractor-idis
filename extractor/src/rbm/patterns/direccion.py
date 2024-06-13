
 #los uso con LEMMA
#calleSinonimos = ["Av", "av", "calle", "Calle", "ruta", "Ruta", "avenida", "Avenida", "diagonal", "Diagonal", "dg", "Dg", "diag", "Diag"]
#manzanaSinonimos = ["manzana", "Manzana", "mz", "Mz", "mza", "Mza"]
#numeroSinonimos = ["numero", "nro", "número", "número", "n", "n°", "nº", "nº", "n°", "nro."]

#los uso con LOWER
#calleSinonimos2 = ["avs", "av", "calle", "calles", "ruta", "rutas", "avenida", "avenidas", "diagonal", "diagonales", "dg", "dgs", "diag", "diags"]
CALLE_SINONIMOS = ["avs", "avs.", "av", "av.", "calle", "calles", "ruta", "rutas", "avenida", "avenidas", "diagonal", "diagonales", "dg", "dg.", "dgs", "dgs.", "diag", "diasg.", "diags", "diags"]#tal vez dirá: "calle 5 entre calles 4 y 7"
MANZANA_SINONIMOS = ["manzana", "mz", "mz.", "mza", "mza."]
NUMERO_SINONIMOS = ["numero", "numeros", "nro", "nros", "número", "números", "°", "n", "n°", "nº", "nº", "n°", "nro.", "ns", "n°s", "nºs", "nºs", "n°s", "nros."]
ANTE_NUMERO = ["km", "al", "altura", "altura:", "alt", "alt.", "kilometro", "km."]

NOMBRE_LARGO = ["PROPN", "DET", "ADP", "NOUN", "NUM"] #funciona que tenga el numero opcional, pero luego si o si al final termine con PROPN
CONECTORES = ["e/", "entre", "a", "a/", "esquina", "esq", "esq."]#pensé en sacarle lo de esquina pero fue contraproducente
UNION = ["y", "e", "esquina", "esq", "esq."]
#letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]#trae probleamos porque quiere matchear con la letra 'a' en las oraciones como: "a 5 metros de ahí"
LETRA_MAYUSCULA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#extra = ["bis"] + letra #empeora precisión
#PARA LOS MATCHERS DE DIRECCIÓN: LOS PATRONES COMENTADOS sin explicación es porque no aportan precisión, pero en una db más grande tal vez si (no están probados)

SOBRE_SINONIMOS = ["en","sobre"]
NOMBRE_LOTE = ["NUM", "PROPN"]
MEDIDAS = ["metro", "metros", "m", "ms", "mt", "mts", "m2"] 

def dir_nro():
    return  list([ #direcciones platenses = numericas
                #calle sin altura
                #[{"LOWER": {"IN":CALLE_SINONIMOS}},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER": "bis"}],
                [{"LOWER": {"IN":CALLE_SINONIMOS}},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN": UNION}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"LIKE_NUM":True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],
                [{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN": CONECTORES}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER":{"IN":UNION}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],
                #caso extra de "calles 3, 4 y 5"
                #[{"LOWER": {"IN":CALLE_SINONIMOS}}, {"TEXT": ",", "OP":"?"},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"TEXT": ","},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"TEXT": {"IN":UNION}},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],

                #calle con altura
                [{"LOWER": {"IN":CALLE_SINONIMOS}},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN":ANTE_NUMERO}, "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True},],
                #[{"LOWER": {"IN":CALLE_SINONIMOS}},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN":ANTE_NUMERO}, "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": CONECTORES}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"+"},{"LIKE_NUM":True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},],
                #[{"LOWER": {"IN":CALLE_SINONIMOS}},{"LIKE_NUM": True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN":ANTE_NUMERO}, "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": CONECTORES}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"+"},{"LIKE_NUM":True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER":{"IN":UNION}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"LIKE_NUM":True},{"TEXT": {"IN": LETRA_MAYUSCULA}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],
            ])

def dir_interseccion():
    return  list([
                #calle sin altura
                #[{"LOWER": {"IN":CALLE_SINONIMOS}},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis"}],
                [{"LOWER": {"IN":CALLE_SINONIMOS}},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN": CONECTORES}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LOWER":"bis", "OP":"?"}], #no entinedo porque tengo que usar 'concectores' en lugar de 'UNION' -> porque estoy overfitteando, sube la presición el usar conector porque hace que no encuentre nada y luego el helper no se confunda con cual es la mejor opción a usar
                [{"LOWER": {"IN":CALLE_SINONIMOS}},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN": CONECTORES}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis", "OP":"?"},{"LOWER":{"IN":UNION}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"}, {"LOWER": "bis", "OP":"?"},],
                #case extra de "calle Miguel, Santiago y Fulano"
                #[{"LOWER": {"IN":CALLE_SINONIMOS}}, {"TEXT": ",", "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis", "OP":"?"},{"TEXT": ","},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis", "OP":"?"},{"TEXT": {"IN":UNION}},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis", "OP":"?"}],#hay que mejorarle el helper asociado para sacar el inicio de "calles,"

                #calle con altura
                [{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis"}],#un caso sin poner calle al inicio, no se si estoy overfitteando
                [{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"+"},{"LIKE_NUM": True},],#otro caso sin poner calle al inicio, no se si estoy overfitteando
                
                [{"LOWER": {"IN":CALLE_SINONIMOS}},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN":ANTE_NUMERO}, "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True}],
                #[{"LOWER": {"IN":CALLE_SINONIMOS}},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN":ANTE_NUMERO}, "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": UNION}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis", "OP":"?"}],
                [{"LOWER": {"IN":CALLE_SINONIMOS}},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN":ANTE_NUMERO}, "OP":"?"},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": CONECTORES}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis", "OP":"?"},{"LOWER":{"IN":UNION}},{"LOWER": {"IN":CALLE_SINONIMOS}, "OP":"?"},{"POS":{"IN":NOMBRE_LARGO}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis", "OP":"?"}],#no entinedo porque debo sacarle el PROPN obligatorio del final

            ])

def dir_entre():
    return [
        [{"LOWER": {"IN":CALLE_SINONIMOS}}, {"POS": {"IN":NOMBRE_LARGO}, "OP": "*"}, {"POS": "PROPN"}, {"LIKE_NUM": True, "OP": "?"}, {"LOWER": "bis", "OP": "?"}, {"LOWER": {"IN": UNION}}, {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, {"LIKE_NUM": True}, {"TEXT": {"IN": LETRA_MAYUSCULA}, "OP": "?"}, {"LOWER": "bis", "OP": "?"}],
        [{"LOWER": {"IN":CALLE_SINONIMOS}}, {"LIKE_NUM": True}, {"LOWER": "bis", "OP": "?"}, {"LOWER": {"IN": CONECTORES}}, {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, {"LIKE_NUM": True}, {"LOWER": "bis", "OP": "?"}, {"LOWER": {"IN": UNION}}, {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, {"POS": "PROPN", "OP": "?"}, {"LIKE_NUM": True}, {"LOWER": "bis", "OP": "?"}]
        # Uncomment and edit the following pattern as needed
        # [{"LOWER": {"IN":CALLE_SINONIMOS}}, {"LIKE_NUM": True}, {"LOWER": "bis", "OP": "?"}, {"LOWER": {"IN":ANTE_NUMERO}, "OP": "?"}, {"LOWER": {"IN":NUMERO_SINONIMOS}, "OP": "?"}, {"LIKE_NUM": True}, {"LOWER": {"IN": CONECTORES}}, {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, {"LIKE_NUM": True}, {"LOWER": "bis", "OP": "?"}, {"LOWER": {"IN": UNION}}, {"LOWER": {"IN":CALLE_SINONIMOS}, "OP": "?"}, {"POS": "PROPN", "OP": "?"}, {"LIKE_NUM": True}, {"LOWER": "bis", "OP": "?"}]
    ]


def dir_lote():
    return  list([ #direccion de lote
                [{"LOWER": "lote"}, {"POS": {"IN": NOMBRE_LOTE}}],
                [{"LOWER": "lote"}, {"POS": {"IN": NOMBRE_LOTE}},{"LOWER": {"IN": MEDIDAS}, "OP":"!"}],#debería mejorar el helper para sacar el último token que toma

                #manzana letrada
                [{"LOWER": "lote"}, {"POS": {"IN": NOMBRE_LOTE}},{"LOWER": {"IN": SOBRE_SINONIMOS}, "OP":"?"},{"LOWER": {"IN": MANZANA_SINONIMOS}},{"TEXT": {"IN": LETRA_MAYUSCULA}}],
                [{"LOWER": {"IN": MANZANA_SINONIMOS}},{"TEXT": {"IN": LETRA_MAYUSCULA}}, {"LOWER": {"IN": SOBRE_SINONIMOS}, "OP":"?"},{"LOWER": "lote"},{"POS": {"IN": NOMBRE_LOTE}}],

                #manzana numerada
                [{"LOWER": "lote"},{"POS": {"IN": NOMBRE_LOTE}},{"LOWER": {"IN": SOBRE_SINONIMOS}, "OP":"?"},{"LOWER": {"IN": MANZANA_SINONIMOS}},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True}],
                [{"LOWER": {"IN": MANZANA_SINONIMOS}},{"LOWER": {"IN":NUMERO_SINONIMOS}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": SOBRE_SINONIMOS}, "OP":"?"},{"LOWER": "lote"},{"POS": {"IN": NOMBRE_LOTE}}],
            
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
            [
                    {
                        "LOWER": {"IN": CALLE_SINONIMOS},
                        "OP": "?",
                    },
                    #{"TEXT": ".", "OP": "?"},
                    {"POS": {"IN": NOMBRE_LOTE}, "OP": "+"},
                    {"LOWER": {"IN": CONECTORES}},
                    {
                        "LOWER": {"IN": CALLE_SINONIMOS},
                        "OP": "?",
                    },
                    #{"TEXT": ".", "OP": "?"},
                    {"POS": {"IN": NOMBRE_LOTE}, "OP": "+"},
                    {"LOWER": "y"},
                    {
                        "LOWER": {"IN": CALLE_SINONIMOS},
                        "OP": "?",
                    },
                    #{"TEXT": ".", "OP": "?"},
                    {"POS": {"IN": NOMBRE_LOTE}, "OP": "+"},
                ]
                
                #no aporta
                #[{"LOWER": "lote"}, {"POS": {"IN": ["NUM", "PROPN"]}}]
            ])