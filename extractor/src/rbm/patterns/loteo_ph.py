numeros = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho"]
ph_similares = ["PH","ph","(PH)","(ph)","ph.","PH."]
def loteo_ph_M() -> list:
    return list ( 
            [
                #[{"LOWER" : {"IN" : ph_similares}}], 

                [{"LOWER" : "por"},{"LOWER" : "ph"}],

                [{"LOWER" : "Lote"},{"LOWER" : "interno"},{"LOWER" : {"IN" : ph_similares}}],  #Lote interno (PH)

                [{"LOWER" : "diferentes"},{"LOWER" : "medidas"},{"LOWER": "en"},{"LOWER": {"IN" : ph_similares}}], # diferentes medidas en ph

                [{"LOWER":"compuesto"},{"LOWER" : {"IN" :["por","de"]}},{"LOWER" : {"IN" :numeros}},{"LOWER": {"IN" : ph_similares}}], #compuesto por/de "numero" ph
                
                [{"LOWER":"subdivididos"},{"LOWER" : {"IN" :["por","en"]}},{"LOWER":"ph"}],#subdivididos por/en ph
                
                [{"LOWER":"Lote"},{"LOWER" : "interno("},{"LOWER" : {"IN" :ph_similares}}],# lote interno (PH)

                [{"LOWER":"terreno"},{"LOWER" : "en"},{"LOWER":"ph"}],#terreno en ph
                
                [{"LOWER":"lote"},{"LOWER":"interno"},{"LOWER" : {"IN" :ph_similares}}],#lote interno ph/(ph)

                [{"LOWER":"ph"},{"LOWER" : "aprobado"}], #ph aprobado

                [{"LOWER":"lotes"},{"LOWER" : "en"},{"LOWER" : "venta"},{"LOWER" : "en"},{"LOWER" : "ph"}],#lotes en venta en ph

                [{"LOWER":"terreno"},{"LOWER" : "tipo","OP" : "?"},{"LOWER" : "ph"}],#terreno tipo (opcional) ph

                [{"LOWER":{"IN" :["lote","lotes"]}},{"LOWER" : "en", "OP" : "?" },{"LOWER" : "ph"}], #lote/lotes en(opcional) ph

                [{"LOWER" : {"IN" :["régimen","regimen"]}},{"LOWER" : "ph"}], #régimen/regimen ph
            
            ] 
    )

def loteo_ph_DM() -> list:
    return [   
            [   
                # matchea "no afectado PH"
                {
                    "RIGHT_ID": "no_afectado_ph",  # me paro en ph y miro flecha que ENTRA
                    "RIGHT_ATTRS": {"LOWER": {"IN": ["ph","PH"]}}, #ph o PH
                },
                {
                    "LEFT_ID": "no_afectado_ph", #
                    "REL_OP": "<",
                    "RIGHT_ID": "relacion_no_afectado",
                    "RIGHT_ATTRS": {"POS": "ADJ"},
                },
                {
                    "LEFT_ID": "relacion_no_afectado", #
                    "REL_OP": ">",
                    "RIGHT_ID": "ADV_no",
                    "RIGHT_ATTRS": {"POS":{"IN" : ["ADV"]}},  #aca en realidad tendrias que matchear por el morfologico: que este en presente el verbo ese además
                }
            ],   
            [    # posibilidad dividir ph
                {
                    "RIGHT_ID": "dividir_ph",  # me paro en ph y miro flecha que ENTRA
                    "RIGHT_ATTRS": {"LOWER": {"IN": ["ph","PH"]}}, #ph o PH
                },
                {
                    "LEFT_ID": "dividir_ph", #
                    "REL_OP": "<",
                    "RIGHT_ID": "relacion_posible_dividir",
                    "RIGHT_ATTRS": {"POS": "VERB"},
                },
                {
                    "LEFT_ID": "relacion_posible_dividir", #
                    "REL_OP": "<",
                    "RIGHT_ID": "posibilidad",
                    "RIGHT_ATTRS": {"POS":"NOUN"},  #aca en realidad tendrias que matchear por el morfologico: que este en presente el verbo ese además
                }              
            ]
    ]

def frases_loteo_ph_PM() -> list:
    frases = ["(en PH)","en PH","(PH)","se encuentra sujeta al Régimen de PH","(PH Cerrado)"]
    return frases

def frases_not_loteo_ph_PM() -> list:
    not_frases = ["departamento en ph.-en","APTO SUBDIVISIÓN EN PH","Posibilidad de dividir en PH","LOTE DIVISIBLE PH","LOTE EN L COMPUESTO POR TRES PH","posible ph",]
    return not_frases
