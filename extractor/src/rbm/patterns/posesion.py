def posesion() -> list:
    return list (
            [
                [{"LOWER":"posesión"}],
                [{"LOWER":"derechos"},{"LOWER":"posesorios"},{"IS_PUNCT":True,"OP":"?"}], #derechos posesorios
                [{"LOWER":"usucapión"}] #usucapion        
            ]
    # se intento matchear con 3$ posesion (LIKE_NUM + IS_PUNCT + "posesion") y con boleto de/con posesion para evitar los falsos positivos (no es posesion) que se dan al matchear solo con la palabra posesion pero 
    # no se pudo lograr matchear con LIKE_NUM + IS_PUNCT + "posesion") por lo que se descarto por el momento el segundo patron si matchea boleto de/con posesion
    
    #[{"LIKE_NUM" : True},{"IS_PUNCT" : True},{"LOWER" : "posesión"}], # numero + % + posesion
    #[{"LOWER":"boleto"},{"LEMMA" : {"IN" :["con","de"]}},{"LOWER":"posesión"}], #boleto de/con posesion
    
    )
    
  