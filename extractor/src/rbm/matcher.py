import spacy
from spacy.matcher import DependencyMatcher
from spacy.matcher import Matcher as MatcherSpacy
from spacy.matcher import PhraseMatcher
from src.rbm.patterns.urb_semicerrada import urb_semicerrada
from src.rbm.patterns.barrio import barrio
from src.rbm.patterns.direccion import dir_entre, dir_interseccion, dir_lote, dir_nro
from src.rbm.patterns.fot import fot
from src.rbm.patterns.medidas import medidas
from src.rbm.patterns.urb_cerrada import urb_cerrada
from src.rbm.patterns.posesion import posesion
from src.rbm.patterns.preventa import asegurados,cuotas,descartar,fecha,posibles
from src.rbm.patterns.a_demoler import a_demoler
from src.rbm.patterns.indiviso import indiviso_M,indiviso_DM
from src.rbm.patterns.edificacion_monetizable import edificacion_monetizable
from src.rbm.patterns.loteo_ph import loteo_ph_M,loteo_ph_DM,loteo_ph_DM_True

NLP = spacy.load("es_core_news_lg")


class Matcher:

    def __init__(self) -> None:
        if Matcher.matcher is None:
            Matcher.initialize_matcher()

    matcher = None
    dependencyMatcher = None
    phraseMatcher = None
    
    @staticmethod
    def initialize_matcher():
        
        Matcher.matcher = MatcherSpacy(NLP.vocab)

        Matcher.phraseMatcher = PhraseMatcher(NLP.vocab, attr="LOWER")
        terms = ["barrio privado", "barrio cerrado", "club de campo", "urbanización cerrada", "country"]
        patterns = [NLP(text) for text in terms]
        Matcher.phraseMatcher.add(
            "urb_cerrada", patterns
        )

        Matcher.matcher.add(
            "medidas", #para cada cantidad de medidas elijo si conviene obligar a tener una unidad o no. Luego, comento los patrones que no aportan precisión
            medidas()
        )
        Matcher.matcher.add(
            "pileta",
            [
                [
                    {"LEMMA": {"IN": ["piscina", "pileta"]}},
                ]
            ],
        )
        Matcher.matcher.add(
            "esquina",
            [
                [
                    {"LOWER": "esquina"},
                ]
            ],
        )
        Matcher.matcher.add(
            "irregular",
            [
                [{"LEMMA": "irregular"}],
                [{"LOWER": {"IN": ["lote", "forma"]}}, {"POS": "ADJ"}],
            ],
        )
 
        Matcher.matcher.add(
            "fot",
            fot()
           
        )
        Matcher.matcher.add(
            "barrio",
            barrio()
        )

        Matcher.matcher.add(
            "dir_nro",
            dir_nro()
        )
        Matcher.matcher.add(
            "dir_interseccion", #direcciones no platenses = no numericas
            dir_interseccion()
        )
        Matcher.matcher.add(
            "dir_entre", #dirrecciones platenses + no platenses y direcciones que en el nombre ponen numeros -> los casos posibles son muchisimos, por eso solo escribo los patrones que veo, por falta de tiempo
            dir_entre()
        )
        Matcher.matcher.add(
            "dir_lote", 
            dir_lote()
        )

        Matcher.matcher.add(
            "urb_cerrada",
            urb_cerrada()
        )

        Matcher.matcher.add(
            "urb_semicerrada",
            urb_semicerrada()
        )

        Matcher.matcher.add(
            "posesion",
            posesion()
        )

        Matcher.matcher.add(
            "pre-venta-asegurados", 
                asegurados()
            
        )
        Matcher.matcher.add(
            "pre-venta-posibles", 
                posibles()
            
        )
        Matcher.matcher.add(
            "pre-venta-fecha", 
                fecha()
            
        )
        Matcher.matcher.add(
            "pre-venta-cuotas", 
                cuotas()
            
        )
        Matcher.matcher.add(
            "pre-venta-descartar", 
                descartar()
            
        )

        Matcher.matcher.add(
            "indiviso_M",
            indiviso_M()
        )

        Matcher.matcher.add(
            "a_demoler", a_demoler()
        )   

        Matcher.matcher.add(
            "es_multioferta", [
                [{"LEMMA": "lote", "MORPH": "Gender=Masc|Number=Plur"}]
             ]
        )

        Matcher.matcher.add(
            "es_monetizable", edificacion_monetizable()
        )

        Matcher.matcher.add(
            "loteo_ph_M",
            loteo_ph_M()
        )
        
        Matcher.dependencyMatcher = DependencyMatcher(NLP.vocab)
        Matcher.dependencyMatcher.add(
            "frentes",
            patterns=[
                [
                    {
                        "RIGHT_ID": "frentes",
                        "RIGHT_ATTRS": {"LOWER": {"IN": ["frente", "frentes"]}},
                    },
                    {
                        "LEFT_ID": "frentes",
                        "REL_OP": ">",
                        "RIGHT_ID": "num",
                        "RIGHT_ATTRS": {"DEP": {"IN": ["nummod", "amod"]}},
                    },
                ],
                [
                    {"RIGHT_ID": "frentes", "RIGHT_ATTRS": {"LOWER": "salida"}},
                    {
                        "LEFT_ID": "frentes",
                        "REL_OP": ">",
                        "RIGHT_ID": "calles",
                        "RIGHT_ATTRS": {"DEP": "obl"},
                    },
                    {
                        "LEFT_ID": "calles",
                        "REL_OP": ">",
                        "RIGHT_ID": "num",
                        "RIGHT_ATTRS": {"DEP": "nummod"},
                    },
                ],
            ],
        ) 
        Matcher.dependencyMatcher.add(
            "fot",
            patterns=[
                [
                    {
                        "RIGHT_ID": "fot",
                        "RIGHT_ATTRS": {"LOWER": {"IN": ["fot", "f.o.t"]}},
                    },
                    {
                        "LEFT_ID": "fot",
                        "REL_OP": ">",
                        "RIGHT_ID": "num",
                        "RIGHT_ATTRS": {"DEP": "nummod"},
                    },
                ]
            ],
        )
        Matcher.dependencyMatcher.add("loteo_ph_DM",
            loteo_ph_DM()
        )
        #Matcher.dependencyMatcher.add("loteo_ph_DM_True",
        #    loteo_ph_DM_True()
        #)
        Matcher.dependencyMatcher.add("indiviso_DM",
            indiviso_DM()
        )
    def __get_matches(self, text, prev_result):
        doc = NLP(text)
        matches = Matcher.matcher(doc)
        for match_id, start, end in matches:
            matched_span = doc[start:end]
            prev_result[NLP.vocab.strings[match_id]].append(matched_span.text)

    def __get_dep_matches(self, text, prev_result):
        doc = NLP(text)
        matches_dep = Matcher.dependencyMatcher(doc)
        for match_id, token_ids in matches_dep:
            palabra = []
            for token_id in sorted(token_ids):
                token = doc[token_id]
                palabra.append(token.text)
            prev_result[NLP.vocab.strings[match_id]].append(" ".join(palabra))

    def __get_phrase_matches(self, text, prev_result):
        doc = NLP(text)

        matches = Matcher.phraseMatcher(doc)
        for match_id, start, end in matches:
            matched_span = doc[start:end]
            prev_result[NLP.vocab.strings[match_id]].append(matched_span.text)


    def get_pairs(self, text: str):
        prev_result = {
            "medidas": [],
            "dir_nro": [],
            "dir_interseccion": [],
            "dir_entre": [],
            "dir_lote": [],
            "fot": [],
            "irregular": [],
            "pileta": [],
            "barrio": [],
            "esquina": [],
            "frentes": [],
            "urb_cerrada": [],
            "urb_semicerrada": [], 
            "posesion": [],
            "preventa": [],
            "indiviso_M": [],
            "indiviso_DM": [],
            "a_demoler": [],
            "es_multioferta": [],
            "pre-venta-asegurados": [],
            "pre-venta-posibles": [],
            "pre-venta-fecha": [],
            "pre-venta-cuotas": [],
            "pre-venta-descartar": [],
            "es_monetizable": [],
            "loteo_ph_M": [],
            "loteo_ph_DM": [],
            "loteo_ph_DM_True": [],
        }
        self.__get_matches(text, prev_result)
        self.__get_dep_matches(text, prev_result)
        self.__get_phrase_matches(text, prev_result)

        return prev_result