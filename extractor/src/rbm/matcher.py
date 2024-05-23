import spacy
from spacy.matcher import DependencyMatcher as DependencyMatcherSpacy
from spacy.matcher import Matcher as MatcherSpacy

from src.helper import (
    procesar_barrio,
    procesar_direccion,
    procesar_fot,
    procesar_frentes,
    procesar_irregular,
    procesar_medidas,
)

NLP = spacy.load("es_core_news_lg")


class Matcher:

    def __init__(self) -> None:
        if Matcher.matcher is None:
            Matcher.initialize_matcher()

    matcher = None
    dependencyMatcher = None
    
    @staticmethod
    def initialize_matcher():
        dimension = ["frente", "fondo", "lateral", "ancho", "alto", "profundidad", "largo", "anchura", "longitud", "espesor"]
        conectoresMedidas = ["x", "y", "por", "de", "con", ","]#me caga que separen con puntos las medidas, si pongo ahora '.' en el arreglo baja la presición
        medidas = ["metro", "metros", "m", "ms", "mt", "mts"] #el LEMMA no funciona con "m" porque cree que es un número en lugar de una palabra
        relleno = ["ADP", "ADV", "PROPN", "NOUN", "DET", "ADJ"] # sacarle el DET y ADJ? -> por ahora da buenos resultados sin perjudicar
        noRelleno = ["NUM", "PUNCT"]
        
        Matcher.matcher = MatcherSpacy(NLP.vocab)
        Matcher.matcher.add(
            "medidas", #para cada cantidad de medidas elijo si conviene obligar a tener una unidad o no. Luego, comento los patrones que no aportan precisión
            [ 
            
            #2 medidas, con la unidad opcional
            [{"LIKE_NUM":True},{"LOWER": {"IN":medidas}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS":{"IN":relleno}, "OP":"*"},{"LOWER":{"IN":conectoresMedidas}}, {"LIKE_NUM":True, "OP":"+"}, {"LOWER": {"IN":medidas}, "OP":"?"}],
            #2 medidas, que tenga la unidad en algún lado -> anda peor que el patrón de arriba
            #[{"LIKE_NUM":True},{"LOWER": {"IN":medidas}}, {"POS":{"IN":relleno}, "OP":"*"},{"LOWER":{"IN":conectoresMedidas}}, {"LIKE_NUM":True, "OP":"+"}, {"LOWER": {"IN":medidas}, "OP":"?"}],
            #[{"LIKE_NUM": True}, {"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN":conectoresMedidas}}, {"LIKE_NUM":True, "OP":"+"}, {"LOWER": {"IN":medidas}}],
 
            #3 medidas, con la unidad opcional -> anda peor que la opcion de abajo
            #[{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}],
            #3 medidas, que tenga la unidad en algún lado
            [{"LIKE_NUM": True},{"LOWER": {"IN": medidas}},{"TEXT":",", "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}],
            [{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}],
            [{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": medidas}}],

            #4 medidas, con la unidad opcional
            #[{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}],     
            #4 medidas, que tenga la unidad en algún lado 
            [{"LIKE_NUM": True},{"LOWER": {"IN": medidas}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": medidas}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}],     
            [{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"},{"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": medidas}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}],     
            [{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": medidas}}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}],     
            [{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"}, {"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"TEXT":",", "OP":"?"},{"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": medidas}, "OP":"?"},{"TEXT":",", "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"}, {"LOWER": {"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": medidas}}],     

            #solo hay un caso con 5 medidas y no anda porque separa con puntos a las dimensiones
            #5 medidas, con la unidad opcional
            #[{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}]
            #5 medidas, que tenga la unidad en algún lado
            #[{"LIKE_NUM": True},{"LOWER": {"IN": medidas}}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}],
            #[{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}],
            #[{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}],
            #[{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}],
            #[{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}, "OP":"?"}, {"POS": {"IN": relleno}, "OP": "*"},{"LOWER":{"IN": conectoresMedidas}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": medidas}}],
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
            ],
        )
        Matcher.matcher.add(
            "pileta",
            [
                [
                    {"LEMMA": {"IN": ["piscina", "pileta"]}},
                ]
            ],
        )
        Matcher.matcher.add(
            "esquina",
            [
                [
                    {"LOWER": "esquina"},
                ]
            ],
        )
        Matcher.matcher.add(
            "irregular",
            [
                [{"LEMMA": "irregular"}],
                [{"LOWER": {"IN": ["lote", "forma"]}}, {"POS": "ADJ"}],
            ],
        )

        fotSinonimos = ['fot', 'f.o.t']
        conectorFot = ["de", ":", "es", ",", ".", "="]
        unidadFot = ["m2", "mts2", "metros2", "metros cuadrados", "m²", "mts²", "metros²", "metros cuadrados", "m2.", "mts2.", "metros2.", "metros cuadrados.", "m².", "mts².", "metros².", "metros cuadrados."]
        masSinonimos = ["mas", "más", "con", "+"]
        premiosSinonimos = ["premios", "premio"]
        #tipoFot = ["ADJ", "PROPN"]
        numeroPorcentaje = ["NUM", "SYM"]
        nombresFot = ["residencial", "comercial", "industrial", "res", "res.", "com", "com.", "ind", "ind."]

        Matcher.matcher.add(
            "fot",
            [
            #1 fot
            [{'LOWER': {'IN':fotSinonimos}},{"LOWER": {"IN":nombresFot}, "OP":"?"},{"TEXT":{"IN":conectorFot}, "OP":"*"},{"LIKE_NUM": True},{"LOWER":{"IN":unidadFot}, "OP":"?"}],
            [{"LOWER": "factor"},{"LOWER": "de"},{"LOWER": "ocupacion"},{"LOWER": "total"},{"TEXT":{"IN":conectorFot}, "OP":"*"},{'LIKE_NUM': True},{"LOWER":{"IN":unidadFot}, "OP":"?"}],

            #1 fot con premios
            [{'LOWER': {'IN':fotSinonimos}},{"LOWER": {"IN":nombresFot}, "OP":"?"},{"TEXT":{"IN":conectorFot}, "OP":"*"},{"LIKE_NUM": True},{"LOWER":{"IN":unidadFot}, "OP":"?"},{"LOWER":{"IN":masSinonimos}}, {"POS": {"IN":numeroPorcentaje}, "OP":"?"},{"LOWER": "en"},{"LOWER": {"IN":premiosSinonimos}}],
            #[{"LOWER": "factor"},{"LOWER": "de"},{"LOWER": "ocupacion"},{"LOWER": "total"},{"LOWER": {"IN":nombresFot}, "OP":"?"},{"TEXT":{"IN":conectorFot}, "OP":"*"},{"LIKE_NUM": True},{"LOWER":{"IN":unidadFot}, "OP":"?"},{"LOWER":{"IN":masSinonimos}}, {"POS": {"IN":numeroPorcentaje}, "OP":"?"},{"LOWER": "en"},{"LOWER": {"IN":premiosSinonimos}}],

            #2 fots sin premios
            #tengo problemas con el helper.py:
            #[{'LOWER': {'IN':fotSinonimos}},{"LOWER": {"IN":nombresFot}, "OP":"?"},{"TEXT":{"IN":conectorFot}, "OP":"*"},{"LIKE_NUM": True},{"LOWER":{"IN":unidadFot}, "OP":"?"},{"POS":"PUNCT", "OP":"?"},{'LOWER': {'IN':fotSinonimos}},{"LOWER": {"IN":nombresFot}, "OP":"?"},{"TEXT":{"IN":conectorFot}, "OP":"*"},{"LIKE_NUM": True},{"LOWER":{"IN":unidadFot}, "OP":"?"},]

            #2 fots con premios
            #[{'LOWER': {'IN':fotSinonimos}},{"LOWER": {"IN":nombresFot}, "OP":"?"},{"TEXT":{"IN":conectorFot}, "OP":"*"},{"LIKE_NUM": True},{"LOWER":{"IN":unidadFot}, "OP":"?"},{"LOWER":{"IN":masSinonimos}}, {"POS": {"IN":numeroPorcentaje}, "OP":"?"},{"LOWER": "en"},{"LOWER": {"IN":premiosSinonimos}},{"POS":"PUNCT", "OP":"?"},{'LOWER': {'IN':fotSinonimos}},{"LOWER": {"IN":nombresFot}, "OP":"?"},{"TEXT":{"IN":conectorFot}, "OP":"*"},{"LIKE_NUM": True},{"LOWER":{"IN":unidadFot}, "OP":"?"},{"LOWER":{"IN":masSinonimos}}, {"POS": {"IN":numeroPorcentaje}, "OP":"?"},{"LOWER": "en"},{"LOWER": {"IN":premiosSinonimos}}]
            
            #no aporta precisión
            #[
            #        {"LOWER": {"IN": ["fot", "f.o.t"]}},
            #        {
            #            "LOWER": {
            #                "IN": [
            #                   "res",
            #                    "residencial",
            #                    "comercial",
            #                    "com",
            #                    "industrial",
            #                ]
            #            },
            #            "OP": "?",
            #        },
            #        {"IS_PUNCT": True, "OP": "?"},
            #        {"LIKE_NUM": True},
            #    ]
            ],
        )
        inicioNombre = ["PROPN","DET"]
        nombreBarrio = ["PROPN", "DET", "ADP", "NUM"]
        descripcion = ["PRON", "VERB", "ADP", "NOUN", "DET", "ADJ"]
        inicioDescripcion = ["PRON", "VERB", "NOUN"]

        barrioSinonimos = ["barrio", "estancia", "country", "club", "finca", "sector", "urbanizacion"] #debemos mejorar el helper.py
        Matcher.matcher.add(
            "barrio",
            [
                #barrio sin descripcion -> no aportan precisión
                [{"LOWER": {"IN":barrioSinonimos}},{"POS": "PROPN"}],
                [{"LOWER": {"IN":barrioSinonimos}},{"POS": {"IN":inicioNombre}},{"POS": {"IN": nombreBarrio}, "OP":"*"},{"POS": "PROPN"}],

                #barrio con descripcion
                #no aporta
                #[{"LOWER": {"IN":barrioSinonimos}},{"POS":{"IN":inicioDescripcion}},{"POS": {"IN":descripcion}, "OP":"*"},{"POS": "PROPN"}],
                [{"LOWER": {"IN":barrioSinonimos}},{"POS":{"IN":inicioDescripcion}},{"POS": {"IN":descripcion}, "OP":"*"},{"POS": {"IN":inicioNombre}},{"POS": {"IN": nombreBarrio}, "OP":"*"},{"POS": "PROPN"}],
                
                #no aporta
                #[
                #    {"LOWER": {"IN": ["estancia", "barrio", "country", "club"]}},
                #    {"POS": "PROPN", "OP": "+"},
                #],
            
            ]
        )
        
        #los uso con LEMMA
        #calleSinonimos = ["Av", "av", "calle", "Calle", "ruta", "Ruta", "avenida", "Avenida", "diagonal", "Diagonal", "dg", "Dg", "diag", "Diag"]
        #manzanaSinonimos = ["manzana", "Manzana", "mz", "Mz", "mza", "Mza"]
        #numeroSinonimos = ["numero", "nro", "número", "número", "n", "n°", "nº", "nº", "n°", "nro."]

        #los uso con LOWER
        #calleSinonimos2 = ["avs", "av", "calle", "calles", "ruta", "rutas", "avenida", "avenidas", "diagonal", "diagonales", "dg", "dgs", "diag", "diags"]
        calleSinonimos3 = ["avs", "avs.", "av", "av.", "calle", "calles", "ruta", "rutas", "avenida", "avenidas", "diagonal", "diagonales", "dg", "dg.", "dgs", "dgs.", "diag", "diasg.", "diags", "diags"]#tal vez dirá: "calle 5 entre calles 4 y 7"
        manzanaSinonimos2 = ["manzana", "mz", "mz.", "mza", "mza."]
        numeroSinonimos2 = ["numero", "numeros", "nro", "nros", "número", "números", "°", "n", "n°", "nº", "nº", "n°", "nro.", "ns", "n°s", "nºs", "nºs", "n°s", "nros."]
        anteNumero = ["km", "al", "altura", "altura:", "alt", "alt.", "kilometro", "km."]

        nombreLargo = ["PROPN", "DET", "ADP", "NOUN", "NUM"] #funciona que tenga el numero opcional, pero luego si o si al final termine con PROPN
        conectores = ["e/", "entre", "a", "a/", "esquina", "esq", "esq."]#pensé en sacarle lo de esquina pero fue contraproducente
        union = ["y", "e", "esquina", "esq", "esq."]
        #letra = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]#trae probleamos porque quiere matchear con la letra 'a' en las oraciones como: "a 5 metros de ahí"
        letraMay = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        #extra = ["bis"] + letra #empeora precisión
        #PARA LOS MATCHERS DE DIRECCIÓN: LOS PATRONES COMENTADOS sin explicación es porque no aportan precisión, pero en una db más grande tal vez si (no están probados)

        sobreSinonimos = ["en","sobre"]
        nombreLote = ["NUM", "PROPN"]

        Matcher.matcher.add(
            "dir_nro",[ #direcciones platenses = numericas
                #calle sin altura
                #[{"LOWER": {"IN":calleSinonimos3}},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER": "bis"}],
                [{"LOWER": {"IN":calleSinonimos3}},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN": union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LIKE_NUM":True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],
                [{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN": conectores}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER":{"IN":union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],
                #caso extra de "calles 3, 4 y 5"
                #[{"LOWER": {"IN":calleSinonimos3}}, {"TEXT": ",", "OP":"?"},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"TEXT": ","},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"TEXT": {"IN":union}},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],

                #calle con altura
                [{"LOWER": {"IN":calleSinonimos3}},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN":anteNumero}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"*"},{"LIKE_NUM": True},],
                #[{"LOWER": {"IN":calleSinonimos3}},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN":anteNumero}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": conectores}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"+"},{"LIKE_NUM":True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},],
                #[{"LOWER": {"IN":calleSinonimos3}},{"LIKE_NUM": True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN":anteNumero}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": conectores}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"+"},{"LIKE_NUM":True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"},{"LOWER":{"IN":union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LIKE_NUM":True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],
            ]
        )
        Matcher.matcher.add(
            "dir_interseccion", #direcciones no platenses = no numericas
            [
                #calle sin altura
                #[{"LOWER": {"IN":calleSinonimos3}},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis"}],
                [{"LOWER": {"IN":calleSinonimos3}},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN": conectores}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LOWER":"bis", "OP":"?"}], #no entinedo porque tengo que usar 'concectores' en lugar de 'union' -> porque estoy overfitteando, sube la presición el usar conector porque hace que no encuentre nada y luego el helper no se confunda con cual es la mejor opción a usar
                [{"LOWER": {"IN":calleSinonimos3}},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN": conectores}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis", "OP":"?"},{"LOWER":{"IN":union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"}, {"LOWER": "bis", "OP":"?"},],
                #case extra de "calle Miguel, Santiago y Fulano"
                #[{"LOWER": {"IN":calleSinonimos3}}, {"TEXT": ",", "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis", "OP":"?"},{"TEXT": ","},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis", "OP":"?"},{"TEXT": {"IN":union}},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis", "OP":"?"}],#hay que mejorarle el helper asociado para sacar el inicio de "calles,"

                #calle con altura
                [{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER":"bis"}],#un caso sin poner calle al inicio, no se si estoy overfitteando
                [{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"+"},{"LIKE_NUM": True},],#otro caso sin poner calle al inicio, no se si estoy overfitteando
                
                [{"LOWER": {"IN":calleSinonimos3}},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN":anteNumero}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"*"},{"LIKE_NUM": True}],
                #[{"LOWER": {"IN":calleSinonimos3}},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN":anteNumero}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis", "OP":"?"}],
                [{"LOWER": {"IN":calleSinonimos3}},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN":anteNumero}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"*"},{"LIKE_NUM": True},{"LOWER": {"IN": conectores}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis", "OP":"?"},{"LOWER":{"IN":union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LOWER": "bis", "OP":"?"}],#no entinedo porque debo sacarle el PROPN obligatorio del final

            ],
        )
        Matcher.matcher.add(
            "dir_entre", #dirrecciones platenses + no platenses y direcciones que en el nombre ponen numeros -> los casos posibles son muchisimos, por eso solo escribo los patrones que veo, por falta de tiempo
            [
                [{"LOWER": {"IN":calleSinonimos3}},{"POS":{"IN":nombreLargo}, "OP":"*"},{"POS": "PROPN"},{"LIKE_NUM": True, "OP": "?"},{"LOWER": "bis", "OP":"?"},{"LOWER": {"IN": union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LIKE_NUM":True},{"TEXT": {"IN": letraMay}, "OP":"?"},{"LOWER":"bis", "OP":"?"}],
                [{"LOWER": {"IN":calleSinonimos3}},{"LIKE_NUM": True},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN": conectores}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LIKE_NUM":True},{"LOWER":"bis", "OP":"?"},{"LOWER":{"IN":union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS": "PROPN", "OP":"?"},{"LIKE_NUM": True},{"LOWER": "bis", "OP":"?"}],
                #[{"LOWER": {"IN":calleSinonimos3}},{"LIKE_NUM": True},{"LOWER":"bis", "OP":"?"},{"LOWER": {"IN":anteNumero}, "OP":"?"},{"LOWER": {"IN":numeroSinonimos2}, "OP":"?"},{"LIKE_NUM": True},{"LOWER": {"IN": conectores}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"LIKE_NUM":True},{"LOWER":"bis", "OP":"?"},{"LOWER":{"IN":union}},{"LOWER": {"IN":calleSinonimos3}, "OP":"?"},{"POS": "PROPN", "OP":"?"},{"LIKE_NUM": True},{"LOWER": "bis", "OP":"?"}],
            ],
        )
        Matcher.matcher.add(
            "dir_lote", [ #direccion de lote
                [{"LOWER": "lote"}, {"POS": {"IN": nombreLote}}],
                #[{"LOWER": "lote"}, {"POS": {"IN": nombreLote}},{"LOWER": {"NOT_IN": medidas}}],#debería mejorar el helper para sacar el último token que toma

                #manzana letrada
                [{"LOWER": "lote"}, {"POS": {"IN": nombreLote}},{"LOWER": {"IN": sobreSinonimos}, "OP":"?"},{"LOWER": {"IN": manzanaSinonimos2}},{"TEXT": {"IN": letraMay}}],
                [{"LOWER": {"IN": manzanaSinonimos2}},{"TEXT": {"IN": letraMay}}, {"LOWER": {"IN": sobreSinonimos}, "OP":"?"},{"LOWER": "lote"},{"POS": {"IN": nombreLote}}],

                #manzana numerada
                [{"LOWER": "lote"},{"POS": {"IN": nombreLote}},{"LOWER": {"IN": sobreSinonimos}, "OP":"?"},{"LOWER": {"IN": manzanaSinonimos2}},{"LOWER": {"IN":numeroSinonimos2}, "OP":"*"},{"LIKE_NUM": True}],
                [{"LOWER": {"IN": manzanaSinonimos2}},{"LOWER": {"IN":numeroSinonimos2}, "OP":"*"},{"LIKE_NUM": True}, {"LOWER": {"IN": sobreSinonimos}, "OP":"?"},{"LOWER": "lote"},{"POS": {"IN": nombreLote}}],
            
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
                #        "LOWER": {"IN": calleSinonimos3},
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
            
            #este caso particular funciona bien poniendo a calleSinonimos3 opcional
            [
                    {
                        "LOWER": {"IN": calleSinonimos3},
                        "OP": "?",
                    },
                    #{"TEXT": ".", "OP": "?"},
                    {"POS": {"IN": nombreLote}, "OP": "+"},
                    {"LOWER": {"IN": conectores}},
                    {
                        "LOWER": {"IN": calleSinonimos3},
                        "OP": "?",
                    },
                    #{"TEXT": ".", "OP": "?"},
                    {"POS": {"IN": nombreLote}, "OP": "+"},
                    {"LOWER": "y"},
                    {
                        "LOWER": {"IN": calleSinonimos3},
                        "OP": "?",
                    },
                    #{"TEXT": ".", "OP": "?"},
                    {"POS": {"IN": nombreLote}, "OP": "+"},
                ]
                
                #no aporta
                #[{"LOWER": "lote"}, {"POS": {"IN": ["NUM", "PROPN"]}}]
            ],
        )

        Matcher.dependencyMatcher = DependencyMatcherSpacy(NLP.vocab)
        Matcher.dependencyMatcher.add(
            "frentes",
            patterns=[
                [
                    {
                        "RIGHT_ID": "frentes",
                        "RIGHT_ATTRS": {"LOWER": {"IN": ["frente", "frentes"]}},
                    },
                    {
                        "LEFT_ID": "frentes",
                        "REL_OP": ">",
                        "RIGHT_ID": "num",
                        "RIGHT_ATTRS": {"DEP": {"IN": ["nummod", "amod"]}},
                    },
                ],
                [
                    {"RIGHT_ID": "frentes", "RIGHT_ATTRS": {"LOWER": "salida"}},
                    {
                        "LEFT_ID": "frentes",
                        "REL_OP": ">",
                        "RIGHT_ID": "calles",
                        "RIGHT_ATTRS": {"DEP": "obl"},
                    },
                    {
                        "LEFT_ID": "calles",
                        "REL_OP": ">",
                        "RIGHT_ID": "num",
                        "RIGHT_ATTRS": {"DEP": "nummod"},
                    },
                ],
            ],
        )
        Matcher.dependencyMatcher.add(
            "fot",
            patterns=[
                [
                    {
                        "RIGHT_ID": "fot",
                        "RIGHT_ATTRS": {"LOWER": {"IN": ["fot", "f.o.t"]}},
                    },
                    {
                        "LEFT_ID": "fot",
                        "REL_OP": ">",
                        "RIGHT_ID": "num",
                        "RIGHT_ATTRS": {"DEP": "nummod"},
                    },
                ]
            ],
        )

    def __get_matches(self, text, prev_result):
        doc = NLP(text)

        matches = Matcher.matcher(doc)
        for match_id, start, end in matches:
            matched_span = doc[start:end]
            prev_result[NLP.vocab.strings[match_id]].append(matched_span.text)

    def __get_dep_matches(self, text, prev_result):
        doc = NLP(text)
        matches_dep = Matcher.dependencyMatcher(doc)
        for match_id, token_ids in matches_dep:
            palabra = []
            for token_id in sorted(token_ids):
                token = doc[token_id]
                palabra.append(token.text)
            prev_result[NLP.vocab.strings[match_id]].append(" ".join(palabra))

    def __merge(self, dic1, dic2):
        for clave, valores in dic1.items():
            if clave in dic2:
                dic2[clave].extend(valores)
            else:
                dic2[clave] = valores

        return dic2

    def obtener_mejor_resultado(self, predichos):
        return {
            "direccion": procesar_direccion(predichos),
            "fot": procesar_fot(predichos["fot"]) if predichos["fot"] else "",
            "irregular": (
                procesar_irregular(predichos["irregular"])
                if len(predichos["irregular"]) > 0
                else ""
            ),
            "medidas": (
                procesar_medidas(predichos["medidas"]) if predichos["medidas"] else ""
            ),
            "esquina": True if len(predichos["esquina"]) > 0 else "",
            "barrio": (
                procesar_barrio(predichos["barrio"]) if predichos["barrio"] else ""
            ),
            "frentes": (
                procesar_frentes(predichos["frentes"]) if predichos["frentes"] else ""
            ),
            "pileta": True if len(predichos["pileta"]) > 0 else "",
        }

    def get_pairs(self, text: str):
        prev_result = {
            "medidas": [],
            "dir_nro": [],
            "dir_interseccion": [],
            "dir_entre": [],
            "dir_lote": [],
            "fot": [],
            "irregular": [],
            "pileta": [],
            "barrio": [],
            "esquina": [],
            "frentes": [],
        }
        self.__get_matches(text, prev_result)
        self.__get_dep_matches(text, prev_result)

        a = self.obtener_mejor_resultado(prev_result)
        return a
