sinonimos_inmuebles = ["terrenos","lotes","casas","inmuebles","propiedades"]
def multioferta() -> list:
    return([
        [{"LOWER": {"IN": ["cada", "varios", "multiples", "múltiples"]}}, {"LOWER": {"IN": ["lotes", "lote", "terernos", "terreno", "parcela", "parcelas"]}}], #cada lote, varios lotes, multiples lotes
        #[{"POS":"NUM"},{"LOWER": {"IN": ["lotes", "terrenos", "parcelas"]}}], #4 lotes
        [{"POS": "NUM", "OP":"?"},{"LOWER": {"IN": ["lotes", "terrenos", "parcelas"]}},{"OP":"{1,2}"}, {"LOWER": {"IN": ["venta","medidas"]}}], #lotes en venta, lotes a la venta, lotes de diferentes medidas
        [{"LOWER": {"IN": ["lotes",  "terrenos"]}}, {"POS":"NUM"},{"LOWER": {"IN": ["x", "por"]}}], # lotes 10x30
        [{"LOWER": "son"},{"LIKE_NUM": True},{"LOWER" : "lotes"}],# son 4 (numero) lotes
        [{"LOWER" : "lotes"},{"LOWER" : "de","OP":"?"},{"LIKE_NUM" : True},{"LOWER" : "m2"}], #lotes de (num) m2
        [{"LOWER" : "barrio "},{"LOWER" : {"IN" :["abierto","cerrado"]},"OP":"?"},{"LOWER" : "con"},{"LIKE_NUM" : True},{"LOWER":"lotes"}], # barrio abierto con 150 lotes # ANDA EN RAMA DE PRUEBA PERO NO ACA
        [{"LOWER": "juntos"}, {"LOWER": "o"}, {"LOWER": "separados"}], #se venden juntos o separados
        # POSIBLES MEJORAS
        [{"LOWER": "son"},{"LIKE_NUM": True},{"LOWER" : "lotes"}],# son 4 (numero) lotes
        [{"LOWER" : "compuesto"},{"LOWER" : "por"},{"LIKE_NUM" : True},{"LOWER" : "unidades"},{"LOWER" : "funcionales"}], # compuesto por (num) unidades funcionales
        [{"LOWER" : "venta"},{"LIKE_NUM" : True},{"LOWER" : "de","OP" : "?"},{"LOWER" : "lotes"}],# venta {de(op)} (num) lotes
        #[{"LOWER" : "venta"},{"LOWER" : "de","OP" : "?"},{"LOWER" : {"IN" : [sinonimos_inmuebles]}}],# venta {de (op)} sinonimos_inmuebles 
        [{"LOWER" : "venta"},{"LOWER" : "en","OP" : "?"},{"LOWER" : "block"}], # venta {en (op)} block
        [{"LOWER" : "son"},{"LIKE_NUM" : True},{"LOWER" : "lotes"}], #son (num) lotes  # ANDA EN ARCHIVO DE PRUEBA PERO NO ACA
        [{"LOWER" : "venta"},{"LOWER" : "lotes"}], #venta lotes
        [{"LOWER" : "lotes"},{"LOWER" : "de","OP":"?"},{"LIKE_NUM" : True}], # lotes de (num)  #ANDA EN RAMA DE PRUEBA PERO NO ACA
        [{"LOWER": "con"},{"LIKE_NUM" : True},{"LOWER":"locales"}],#con 4 locales
        [{"LOWER":"venta"},{"LIKE_NUM": True},{"LOWER": "Lotes"}],#venta 80 lotes # ANDA EN RAMA DE PRUEBA PERO NO ACA 
    ])

def frases_multioferta_PM() -> list:
    frases = ["Disponemos a la venta amplios lotes","disponemos a la venta amplios terrenos","disponemos a la venta inmbuebles",
              "Medidas de los lotes","Medidas de los terrenos","medidas de los lotes","Lotes en PH",
              "El inmueble consta de tres lotes","terreno consta de tres lotes","La propiedad consta de tres lotes","El inmueble consta de cuatro lotes",
              "El inmueble consta de dos lotes","El inmueble consta de cinco lotes","dos lotes","tres lotes","cuatro lotes","cinco lotes",
              "Opción de sumar otro lote lindero","Opción de sumar otro lindero","venta de unidades funcionales","Venta de terrenos","venta de lotes","VENTA EN BLOCK",
              "Disponemos a la venta amplios lotes","Medidas de los lotes","LOTES en","posibilidad de venderse por separado o en bloque",
              "El inmueble consta de tres lotes","se puede comprar lotes contiguos","DOS LOTES EN BLOQUE","para la venta Lotes","ideal para desarrollos multifamiliares",
              "ideal desarrollos multifamiliares","venta 80 lotes","barrio abierto con 150 lotes","son 4 lotes"
              ]#Las ultimas 3 frases la idea es hacerlas con el Matcher y no con el PM, se deja asi porque andan con el PM pero no con el M
    return frases

    