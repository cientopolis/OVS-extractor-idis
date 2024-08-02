NOMBRE_BARRIO = ["PROPN", "NUM", "NOUN", "ADJ"]

BARRIO_SINONIMOS = ["barrio", "estancia", "country", "club", "finca"] #debemos mejorar el helper.py
        
def barrio():
    return  list([
                #barrio sin DESCRIPCION -> no aportan precisión
                [
                    {"LOWER": {"IN":BARRIO_SINONIMOS}},
                    {"POS": {"IN": NOMBRE_BARRIO}, "OP":"{1,3}"}
                ],
                [
                    {"LOWER": {"IN":BARRIO_SINONIMOS}},
                    {"POS": {"IN": NOMBRE_BARRIO}, "OP":"?"},
                    {"POS": "DET", "OP":"?"},
                    {"POS": {"IN": NOMBRE_BARRIO}}
                ],
                [
                    {"LOWER": "club"},
                    {"LOWER": "de"},
                    {"LOWER": "campo"},
                    {"POS": {"IN": NOMBRE_BARRIO}, "OP":"{1,3}"}
                ],
                # [{"LOWER": {"IN":BARRIO_SINONIMOS}},{"POS": {"IN":INICIO_NOMBRE}},{"POS": {"IN": NOMBRE_BARRIO}, "OP":"*"},{"POS": "PROPN"}],

                #barrio con DESCRIPCION
                #no aporta
                #[{"LOWER": {"IN":BARRIO_SINONIMOS}},{"POS":{"IN":INICIO_DESCRIPCION}},{"POS": {"IN":DESCRIPCION}, "OP":"*"},{"POS": "PROPN"}],
                # [{"LOWER": {"IN":BARRIO_SINONIMOS}},{"POS":{"IN":INICIO_DESCRIPCION}},{"POS": {"IN":DESCRIPCION}, "OP":"*"},{"POS": {"IN":INICIO_NOMBRE}},{"POS": {"IN": NOMBRE_BARRIO}, "OP":"*"},{"POS": "PROPN"}],
                
                #no aporta
                #[
                #    {"LOWER": {"IN": ["estancia", "barrio", "country", "club"]}},
                #    {"POS": "PROPN", "OP": "+"},
                #],
            
            ])