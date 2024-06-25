from src.rbm.extractor.oferta import Oferta
from src.rbm.extractor.multioferta import Multioferta

def select_best_candidate(prev_result: list, estructura: dict):
    for variable in estructura: 
        if prev_result["es_multioferta"]:
            metodo = getattr(Multioferta(), variable)
        else:
            metodo = getattr(Oferta(), variable)
        estructura[variable]= metodo(prev_result)
        
    return estructura