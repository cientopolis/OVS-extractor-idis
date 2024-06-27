numeros = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho"]
def loteo_ph() -> list:
    return list (
            [
                
                
                [{"LOWER":"compuesto"},{"LOWER" : {"IN" :["por","de"]}},{"LOWER" : {"IN" :numeros}},{"LOWER":"ph"}], #compuesto por/de "numero" ph

                [{"LOWER":"lote"},{"LOWER":"interno"},{"LOWER" : {"IN" :["ph","(PH)","(ph)"]}}],#lote interno ph/(ph)

                [{"LOWER":"ph"},{"LOWER" : "aprobado"}], #ph aprobado

                [{"LOWER":"lotes"},{"LOWER" : "en"},{"LOWER" : "venta"},{"LOWER" : "en"},{"LOWER" : "ph"}],#lotes en venta en ph

                [{"LOWER":"terreno"},{"LOWER" : "tipo","OP" : "?"},{"LOWER" : "ph"}],#terreno tipo (opcional) ph

                [{"LOWER":{"IN" :["lote","lotes"]}},{"LOWER" : "en", "OP" : "?" },{"LOWER" : "ph"}], #lote/lotes en(opcional) ph

                [{"LOWER" : {"IN" :["régimen","regimen"]}},{"LOWER" : "ph"}], #régimen/regimen ph
            
            ]
    ) 
     