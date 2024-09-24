import spacy
from spacy.matcher import DependencyMatcher

SINONIMOS_PH = ["ph","PH","(ph)","(PH)","PH."]

NLP = spacy.load("es_core_news_lg")
matcher= DependencyMatcher(NLP.vocab)

matcher.add("APTO_SUBDIVISION_PH", [
    [
        {"RIGHT_ID": "PH",
        "RIGHT_ATTRS": {"ORTH": "PH"}
        },

        {"LEFT_ID": "PH",
        "REL_OP": "<",
        "RIGHT_ID": "EN",
        "RIGHT_ATTRS": {"ORTH": "EN"}
        },

        {"LEFT_ID": "EN", "REL_OP": "<",
        "RIGHT_ID": "SUBDIVISION",
        "RIGHT_ATTRS": {"ORTH": "SUBDIVISIÓN"}
        },

        {"LEFT_ID": "SUBDIVISION",
        "REL_OP": "<",
        "RIGHT_ID": "APTO",
        "RIGHT_ATTRS": {"ORTH": "APTO"}
        }
    ]
])

doc = NLP("El Equipo Remax Sierras Vende Lote (parcela 8a) en la zona norte de la ciudad, ubicado sobre calle Primera Junta casi Magallanes. Se encuentra a 1 cuadra de la Ruta Nacional 226 y a 10 minutos del centro de la ciudad. Cuenta con una superficie de 347,4 m2, con medidas de 12 metros de frente y 28,95 metros de fondo. APTO SUBDIVISIÓN EN PH. También disponemos de otros lotes de mayores medidas. Servicios Disponibles: electricidad, agua y cloacas. El lote presenta un retiro obligatorio de 6 metros sobre calle Primera Junta. El barrio se encuentra en desarrollo, con potencial residencial y comercial. Según el Plan de Desarrollo Territorial de Tandil cuenta con los siguientes indicadores: *Zona: Barrio Usos Mixtos *FOS: 0,6 *FOT: 0,8 *Densidad: 200 hab/ha *Altura Construcción: 7,5 metros USOS: Vivienda Unifamiliar, Vivienda Multifamiliar, comercios minoristas y mayoristas, servicios generales y oficinas, taller doméstico, taller automotor, depósitos.")
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

