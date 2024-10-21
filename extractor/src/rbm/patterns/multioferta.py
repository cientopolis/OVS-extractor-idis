def multioferta() -> list:
    return([
        [{"LOWER": {"IN": ["cada", "varios", "multiples", "múltiples"]}}, {"LOWER": {"IN": ["lotes", "lote", "terernos", "terreno", "parcela", "parcelas"]}}], #cada lote, varios lotes, multiples lotes
        [{"POS":"NUM"},{"LOWER": {"IN": ["lotes", "terrenos", "parcelas"]}}], #4 lotes
        [{"POS": "NUM", "OP":"?"},{"LOWER": {"IN": ["lotes", "terrenos", "parcelas"]}},{"OP":"{1,2}"}, {"LOWER": {"IN": ["venta","medidas"]}}], #lotes en venta, lotes a la venta, lotes de diferentes medidas
        [{"LOWER": {"IN": ["lotes",  "terrenos"]}}, {"POS":"NUM"},{"LOWER": {"IN": ["x", "por"]}}], # lotes 10x30
        [{"LOWER": "juntos"}, {"LOWER": "o"}, {"LOWER": "separados"}], #se venden juntos o separados
        [{"LOWER": "son"},{"LIKE_NUM": True},{"LOWER":"lotes."}],
    ])

def frases_multioferta_PM() -> list:
    frases = ["",""]
    return frases

    