def multioferta() -> list:
    return([
        [{"LOWER": {"IN": ["cada", "varios", "multiples", "múltiples"]}}, {"LOWER": {"IN": ["lotes", "lote", "terernos", "terreno", "parcela", "parcelas"]}}], #cada lote, varios lotes, multiples lotes
        [{"POS":"NUM"},{"LOWER": {"IN": ["lotes", "terrenos", "parcelas"]}}], #4 lotes
        [{"POS": "NUM", "OP":"?"},{"LOWER": {"IN": ["lotes", "terrenos", "parcelas"]}},{"OP":"{1,2}"}, {"LOWER": {"IN": ["venta","medidas"]}}], #lotes en venta, lotes a la venta, lotes de diferentes medidas
        [{"LOWER": {"IN": ["lotes",  "terrenos"]}}, {"POS":"NUM"},{"LOWER": {"IN": ["x", "por"]}}], # lotes 10x30
        [{"LOWER": "juntos"}, {"LOWER": "o"}, {"LOWER": "separados"}], 
        [{"LOWER": "son"},{"LIKE_NUM": True},{"LOWER" : "lotes"}],# son 4 (numero) lotes
        [{"LOWER" : "lotes"},{"LOWER" : "de","OP":"?"},{"LIKE_NUM" : True},{"LOWER" : "m2"}], #lotes de (num) m2
        [{"LOWER" : "barrio "},{"LOWER" : {"IN" :["abierto","cerrado"]},"OP":"?"},{"LOWER" : "con"},{"LIKE_NUM" : True},{"LOWER":"lotes"}]        
    ])

# futura posible mejora con el phraseMatcher
# frases = ["Barrio abierto con 150 lotes",""]
def frases_multioferta_PM() -> list:
    frases = ["",""]
    return frases

    