import spacy
from spacy.matcher import DependencyMatcher

NLP = spacy.load("es_core_news_lg")
matcher= DependencyMatcher(NLP.vocab)
matcher.add("aber", [
            [   # posible PH
                {
                    "RIGHT_ID": "division_ph",  # me paro en ph y miro flecha que ENTRA
                    "RIGHT_ATTRS": {"LOWER": {"IN": ["ph","PH"]}}, #ph o PH
                },
                {
                    "LEFT_ID": "division_ph", #
                    "REL_OP": "<",
                    "RIGHT_ID": "relacion_posible_division",
                    "RIGHT_ATTRS": {"POS": "PROPN"},
                }                
            ]
        ])

#doc = NLP("Lotes en berisso, a 10 minutos del caso urbano. Oportunidad de tener su primer lote. Fácil acceso, están ubicados a 200 metros de ruta 11 y de zona comercial; y a 3 cuadras de una escuela. Medidas de los lotes: 260, 325 y 390 mts2, frente de 9 mts. Son aptos PROCREAR y aptos crédito bancario. Están subdivididos por ph y tienen Escritura Definitiva. La zona cuenta con todos los servicios, electricidad, gas, agua, internet, cable. Calle de tierra. Posibilidad de financiación mediante oferta Desde 12.000 Usd, libre de todo gasto.")

doc = NLP("Lote interno (PH) en calle 512 bis e/ 8 y 9, tiene 9 mts de frente por 16 de fondo, con cochera descubierta compartida e ingreso al lote por pasillo interno. se encuentra en una zona Clave de Ringuelet a metros de Camino Centenario y de avenida 7. el lote cuenta con permiso de obra y planos")
#for token in doc:
#    print(token.text, token.dep_, token.pos_, token.lemma_)


print("El beio match es: ")
el_resultadongo=""
matches_dep = matcher(doc)
for match_id, token_ids in matches_dep:
    palabra = []
    for token_id in sorted(token_ids):
        token = doc[token_id]
        el_resultadongo+= " "+token.text

print(el_resultadongo.strip())

#spacy.displacy.serve(doc, style="dep")

