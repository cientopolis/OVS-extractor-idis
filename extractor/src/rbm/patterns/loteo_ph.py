numeros = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho"]
def posesion() -> list:
    return list (
            [
                
                
                [{"LOWER":"compuesto"},{"LOWER" : {"IN" :["por","de"]}},{"LOWER" : {"IN" :[numeros]}},{"LOWER":"ph"}], 
                
                [{"LOWER":"ph"},{"LOWER" : "aprobado"}],

                [{"LOWER":"terreno"},{"LOWER" : "tipo","OP" : "?"},{"LOWER" : "ph"}],

                [{"LOWER":{"IN" :["lote","lotes"]}},{"LOWER" : "en", "OP" : "?" },{"LOWER" : "ph"}], 

                [{"LOWER" : {"IN" :["régimen","regimen"]}},{"LOWER" : "ph"}],    
            
            ]
    ) 
    