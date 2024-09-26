import re
import spacy
from spacy.matcher import DependencyMatcher
from spacy.matcher import Matcher as MatcherSpacy
from spacy.matcher import PhraseMatcher
from src.rbm.patterns.urb_semicerrada import urb_semicerrada
from src.rbm.patterns.barrio import barrio
from src.rbm.patterns.direccion import dir_entre, dir_interseccion, dir_lote, dir_nro #dir_lote_nro,
from src.rbm.patterns.fot import fot
from src.rbm.patterns.medidas import medidas
from src.rbm.patterns.urb_cerrada import urb_cerrada,urb_cerrada_DM,frases_urb_cerrada_PM
from src.rbm.patterns.posesion import posesion
from src.rbm.patterns.preventa import asegurados,cuotas,descartar,fecha,posibles
from src.rbm.patterns.a_demoler import asegurado, ideal
from src.rbm.patterns.indiviso import indiviso_M,indiviso_DM,frases_indiviso_PM
from src.rbm.patterns.edificacion_monetizable import construccion, mejorado, mejoras_country
from src.rbm.patterns.loteo_ph import loteo_ph_M,loteo_ph_DM,frases_loteo_ph_PM,frases_not_loteo_ph_PM
from src.rbm.patterns.pileta import pileta,pileta_barrio, no_pileta_DM
from src.rbm.patterns.esquina import esquina
from src.rbm.patterns.irregular import irregular,irregular_DM
from src.rbm.patterns.frentes import frentes

NLP = spacy.load("es_core_news_lg")

REGEX_LOTE= re.compile(r'\b(lote)\s+(\d+)\b(?![.,]\d+)(?!\s*[xX]\s*\d+)(?!\s*(?:x\s*\d+|\d+\s*x\s*\d+|mts|m2)\b)', re.MULTILINE | re.IGNORECASE)
# REGEX_LOTE= re.compile(r'\blote\b\s+\d+\b(?![\d.,]*\s*(?:x|m|,|\bpor\b))', re.MULTILINE | re.IGNORECASE)

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

        terms = frases_urb_cerrada_PM()
        patterns = [NLP(text) for text in terms]
        Matcher.phraseMatcher.add(
            "frases_urb_cerrada_PM",patterns
        )
        terms = frases_loteo_ph_PM()
        patterns = [NLP(text) for text in terms]
        Matcher.phraseMatcher.add(
            "frases_loteo_ph_PM",patterns
        )

        terms = frases_not_loteo_ph_PM()
        patterns = [NLP(text) for text in terms]
        Matcher.phraseMatcher.add(
            "frases_not_loteo_ph_PM",patterns
        )

        terms = frases_indiviso_PM()
        patterns = [NLP(text) for text in terms]
        Matcher.phraseMatcher.add(
            "frases_indiviso_PM",patterns
        )



        Matcher.matcher.add(
            "medidas", #para cada cantidad de medidas elijo si conviene obligar a tener una unidad o no. Luego, comento los patrones que no aportan precisión
            medidas()
        )
        Matcher.matcher.add(
            "pileta",
            pileta()
        )
        Matcher.matcher.add(
            "pileta_barrio",
            pileta_barrio()
        )
        Matcher.matcher.add(
            "esquina",
            esquina()
        )
        Matcher.matcher.add(
            "irregular",
            irregular()
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
        # Matcher.matcher.add(
        #     "dir_lote_nro", #dirrecciones platenses + no platenses y direcciones que en el nombre ponen numeros -> los casos posibles son muchisimos, por eso solo escribo los patrones que veo, por falta de tiempo
        #     dir_lote_nro()
        # )
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
            "a_demoler-asegurado", asegurado()
        )   

        Matcher.matcher.add(
            "a_demoler-ideal", ideal()
        )   


        Matcher.matcher.add(
            "es_multioferta", [
                [{"LOWER": {"IN": ["cada", "varios", "multiples", "múltiples"]}}, {"LOWER": {"IN": ["lotes", "lote", "terernos", "terreno", "parcela", "parcelas"]}}], #cada lote, varios lotes, multiples lotes
                [{"POS":"NUM"},{"LOWER": {"IN": ["lotes", "terrenos", "parcelas"]}}], #4 lotes
                [{"POS": "NUM", "OP":"?"},{"LOWER": {"IN": ["lotes", "terrenos", "parcelas"]}},{"OP":"{1,2}"}, {"LOWER": {"IN": ["venta","medidas"]}}], #lotes en venta, lotes a la venta, lotes de diferentes medidas
                [{"LOWER": {"IN": ["lotes",  "terrenos"]}}, {"POS":"NUM"},{"LOWER": {"IN": ["x", "por"]}}], # lotes 10x30
                [{"LOWER": "juntos"}, {"LOWER": "o"}, {"LOWER": "separados"}] #se venden juntos o separados
            ]
        )

        Matcher.matcher.add(
            "es_monetizable-construccion", construccion()
        )

        Matcher.matcher.add(
            "es_monetizable-mejorado", mejorado()
        )

        Matcher.matcher.add(
            "es_monetizable-mejoras_country", mejoras_country()
        )

        Matcher.matcher.add(        
            "es_monetizable-con_construccion", con_construccion()
        )

        Matcher.matcher.add(
            "mejora_posible_calle", mejora_posible_calle()
        )

        Matcher.matcher.add(
            "posible_country", posible_country()
        )


        Matcher.matcher.add(
            "loteo_ph_M",
            loteo_ph_M()
        )
        
        Matcher.dependencyMatcher = DependencyMatcher(NLP.vocab)

        Matcher.dependencyMatcher.add(
            "frentes",
            frentes()
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
        Matcher.dependencyMatcher.add("urb_cerrada_DM",
            urb_cerrada_DM()
        )
        Matcher.dependencyMatcher.add("irregular_DM",
            irregular_DM()
        )
        Matcher.dependencyMatcher.add("no_pileta_DM",
            no_pileta_DM()
        )
        Matcher.dependencyMatcher.add("no_mejora_DM",
            no_mejora_DM()
        )
        Matcher.dependencyMatcher.add("no_mejora_country_DM",
            no_mejora_country_DM()
        )
        Matcher.dependencyMatcher.add("no_con_construccion_DM",
            no_con_construccion_DM()
        )
        # Matcher.dependencyMatcher.add("lote_construccion_DM",
        #     no_mejora_country_DM()
        # )

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
            "dir_lote": [" ".join(x) for x  in re.findall(REGEX_LOTE, text)],
            # "dir_lote_nro": [],
            "fot": [],
            "irregular": [],
            "irregular_DM":[],
            "pileta": [],
            "pileta_barrio":[],
            "no_pileta_DM":[],
            "barrio": [],
            "esquina": [],
            "frentes": [],
            "urb_cerrada": [],
            "urb_cerrada_DM":[],
            "frases_urb_cerrada_PM":[],    
            "urb_semicerrada": [], 
            "posesion": [],
            "preventa": [],
            "indiviso_M": [],
            "indiviso_DM": [],
            "frases_indiviso_PM":[],
            "a_demoler-asegurado": [],
            "a_demoler-ideal": [],
            "es_multioferta": [],
            "pre-venta-asegurados": [],
            "pre-venta-posibles": [],
            "pre-venta-fecha": [],
            "pre-venta-cuotas": [],
            "pre-venta-descartar": [],
            "es_monetizable-construccion": [],
            "es_monetizable-con_construccion": [],
            "es_monetizable-mejorado": [],
            "es_monetizable-mejoras_country": [],
            "no_mejora_DM": [],
            "no_mejora_country_DM": [],
            "no_con_construccion_DM": [],
            # "lote_construccion_DM": [],
            "no_construccion-PM": [],
            "mejora_posible_calle": [],
            "posible_country": [],
            "loteo_ph_M": [],
            "loteo_ph_DM": [],
            "frases_loteo_ph_PM":[],
            "frases_not_loteo_ph_PM":[],
        }
        self.__get_matches(text, prev_result)
        self.__get_dep_matches(text, prev_result)
        self.__get_phrase_matches(text, prev_result)

        return prev_result
    
