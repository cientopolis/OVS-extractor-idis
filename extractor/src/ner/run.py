import pandas as pd
import spacy

from src.helper import (
    procesar_fot,
    procesar_frentes,
    procesar_irregular,
    procesar_medidas,
)


def ner(input: pd.DataFrame):
    NLP = spacy.load("output-merge/model-best")

    data = []
    for _, row in input.iterrows():
        respuestas = {
            "DIRECCION": [],
            "FOT": [],
            "IRREGULAR": [],
            "DIMENSIONES": [],
            "ESQUINA": [],
            "NOMBRE_BARRIO": [],
            "CANT_FRENTES": [],
            "PILETA": [],
        }
        doc = NLP(row["descripcion"])
        for ent in doc.ents:
            if ent.text not in respuestas[ent.label_]:
                respuestas[ent.label_].append(ent.text)

        respuestas["DIRECCION"] = (
            max(respuestas["DIRECCION"], key=len) if respuestas["DIRECCION"] else ""
        )
        respuestas["FOT"] = procesar_fot(respuestas["FOT"]) if respuestas["FOT"] else ""
        respuestas["DIMENSIONES"] = (
            procesar_medidas(respuestas["DIMENSIONES"])
            if respuestas["DIMENSIONES"]
            else ""
        )
        respuestas["IRREGULAR"] = (
            procesar_irregular(respuestas["IRREGULAR"])
            if respuestas["IRREGULAR"]
            else ""
        )
        respuestas["ESQUINA"] = (
            True
            if respuestas["ESQUINA"] or "esquina" in respuestas["DIRECCION"]
            else ""
        )
        respuestas["NOMBRE_BARRIO"] = (
            max(respuestas["NOMBRE_BARRIO"], key=len)
            if respuestas["NOMBRE_BARRIO"]
            else ""
        )
        respuestas["CANT_FRENTES"] = (
            procesar_frentes(respuestas["CANT_FRENTES"])
            if respuestas["CANT_FRENTES"]
            else ""
        )
        respuestas["PILETA"] = True if respuestas["PILETA"] else ""

        data.append(
            {
                "descripcion": row["descripcion"],
                "direccion": respuestas["DIRECCION"],
                "fot": respuestas["FOT"],
                "irregular": respuestas["IRREGULAR"],
                "medidas": respuestas["DIMENSIONES"],
                "esquina": respuestas["ESQUINA"],
                "barrio": respuestas["NOMBRE_BARRIO"],
                "frentes": respuestas["CANT_FRENTES"],
                "pileta": respuestas["PILETA"],
            }
        )

    return pd.DataFrame(data, index=None)
