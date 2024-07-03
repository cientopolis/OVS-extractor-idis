import spacy
from spacy.matcher import DependencyMatcher

NLP = spacy.load("es_core_news_lg")
matcher= DependencyMatcher(NLP.vocab)
matcher.add("aber", [
            [
                {
                    "RIGHT_ID": "no_es_parte_indivisa",  # me paro en ph y miro flecha que ENTRA
                    "RIGHT_ATTRS": {"LOWER": {"IN": ["indivisa", "indiviso"]}}, #ph o PH
                },
                {
                    "LEFT_ID": "no_es_parte_indivisa", #
                    "REL_OP": "<",
                    "RIGHT_ID": "relacion_no_es_indviso",
                    "RIGHT_ATTRS": {"POS": "NOUN"},
                },
                {
                    "LEFT_ID": "relacion_no_es_indviso", #
                    "REL_OP": ">",
                    "RIGHT_ID": "ADV_no",
                    "RIGHT_ATTRS": {"POS":{"IN" : ["ADV" , "CCONJ"]}},  #aca en realidad tendrias que matchear por el morfologico: que este en presente el verbo ese además
                }
            ]
        ])

#doc = NLP("Lotes en berisso, a 10 minutos del caso urbano. Oportunidad de tener su primer lote. Fácil acceso, están ubicados a 200 metros de ruta 11 y de zona comercial; y a 3 cuadras de una escuela. Medidas de los lotes: 260, 325 y 390 mts2, frente de 9 mts. Son aptos PROCREAR y aptos crédito bancario. Están subdivididos por ph y tienen Escritura Definitiva. La zona cuenta con todos los servicios, electricidad, gas, agua, internet, cable. Calle de tierra. Posibilidad de financiación mediante oferta Desde 12.000 Usd, libre de todo gasto.")

doc = NLP("Av 38 y 147 San Carlos. Exclusivos lotes en barrio semicerrado \"ALTOS DE DON PEDRO\" ,a minutos de la\nCiudad, OPORTUNIDAD Ãºnica, casa alquilada ($103.000) sobre lote arbolado de 10.70 x 28 metros (PH), 2\ndormitorios, cocina comedor equipada, lavadero, baÃ±o completo, 67 m2 cubiertos, fondo. Apto Banco.\nIMPORTANTE escritura inmediata. por UF no es parte indivisa. Tel - 2455 o 221 15 .")
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

