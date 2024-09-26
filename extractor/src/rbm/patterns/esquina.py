sinonmios_esquina = ["esq.","esq","esqui","ochava","esquin",]


def esquina() -> list:
    return list ( 
    [
        [{"LOWER": "esquina"}],
        [{"LOWER" : {"IN" : sinonmios_esquina}}]
    ]
)

def frases_not_esquina() -> list:
    frases = ["próximo a la esquina","un puesto de control de la policía bonaerense en la esquina del barrio","puesto de control de la policía en la esquina"]
    return frases