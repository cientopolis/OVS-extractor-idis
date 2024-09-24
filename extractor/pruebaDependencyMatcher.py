import spacy
from spacy.matcher import DependencyMatcher

SINONIMOS_PH = ["ph","PH","(ph)","(PH)","PH."]

NLP = spacy.load("es_core_news_lg")
matcher= DependencyMatcher(NLP.vocab)

matcher.add("APTO_SUBDIVISION_PH", [
    [
        {"RIGHT_ID": "PH",
        "RIGHT_ATTRS": {"ORTH": "PH)"}
        },

        {"LEFT_ID": "PH",
        "REL_OP": "<",
        "RIGHT_ID": "subdivisible",
        "RIGHT_ATTRS": {"POS": "PROPN"}
        },

        {"LEFT_ID": "subdivisible",
         "REL_OP": ">",
        "RIGHT_ID": "departamento",
        "RIGHT_ATTRS": {"POS": "ADP"}
        },

        
    ]
])

doc = NLP("En la localidad de Tandil sobre calle Entre Ríos al 300,  nos encontramos con estos excelentes y amplios lotes a la venta.  Los mismos cuentan con una superficie total aproximada de 2.370m2 con servicios de luz, agua corriente y gas.  UNIDADES DISPONIBLES:  - Parcela 4: 2.398m2 (32,45m de frente x 73,63m de fondo) - Parcela 5: 2.379m2 (32,45 de frente x 73,63m de fondo, menos ochava) - Parcela 6: 2.368m2 (32,45m de frente x 73m de fondo, menos ochava) - Parcela 7: 2.368m2 (32,45m de frente x 73m de fondo)  EL VALOR DE CADA PARCELA ES DE U$D85.000  INDICADORES URBANISTICOS:  ZONA: BARRIOS EN PROCESO DE CONSOLIDACIÓN FOS: 6,6 FOT: 0.8 DN: 280 ALT: 7,5 LADO MINIMO: 15M SUP. MINIMA: 375M2  USO: VIVIENDA MULTIFAMILAR AUTIRIZABLE (SUBDIVISILBLE EN PH)  Posibilidad de subdividir en propiedad plena y propiedad horizontal.  También se venden dos o más parcelas en Block. ")
#doc = NLP("APTO SUBDIVISIÓN EN PH.")
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

