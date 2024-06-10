import re
import spacy
from spacy.tokens import Doc, Span
import datetime

NLP = spacy.load("es_core_news_lg")

RE_DOS = re.compile(r"\b(dos|doble|2|segundo)\b", re.IGNORECASE)
RE_TRES = re.compile(r"\b(tres|triple|3|tercer)\b", re.IGNORECASE)

def procesar_preventa(predichos: list):
    matcheos = 0
    minimosMatcheos = 2
    maximoAniosLejanos = 15

    for match_id, start, end in predichos["asegurados"]:
        matcheos += minimosMatcheos + 1

    matcheosAuxiliar = 0
    for match_id, start, end in predichos["posibles"]:
        matcheosAuxiliar += 1
    if matcheosAuxiliar > 0:
        matcheos += 1

    matcheosAuxiliar = 0
    for match_id, start, end in predichos["fecha"]:
        span = doc[start:end]
        span.text.replace('.', '') #para que no haya problemas con los puntos -> no se si me está dando efecto
        try:
            num = float(span.text)
            actualYear = datetime.datetime.now().year
            if (num > actualYear) and (num < actualYear + maximoAniosLejanos):
                matcheosAuxiliar +=1
        except ValueError:
            pass
    if matcheosAuxiliar > 0:
        matcheos += 1

    matcheosAuxiliar = 0
    for match_id, start, end in predichos["cuotas"]:
        matcheosAuxiliar += 1
    if matcheosAuxiliar > 0:
        matcheos += 1

    for match_id, start, end in predichos["descartar"]:
        matcheos = 0

    return (matcheos >= minimosMatcheos)

def clear_altura_entre(predichos: list):
    if predichos["dir_nro"] and predichos["dir_entre"]:
        dir_altura = max(predichos["dir_nro"], key=len)
        dir_entre = max(predichos["dir_entre"], key=len)
        if dir_entre.startswith(dir_altura):
            predichos["dir_entre"] = [dir_entre]
        else:
            numero = dir_altura.split()[-1]
            dir_entre = dir_entre.replace(numero, "").strip()
            predichos["dir_entre"] = [dir_altura + dir_entre]
            predichos["dir_nro"] = []
    return predichos


def clear_inter_entre(result: list):
    for interseccion in result.get("dir_interseccion", []):
        for entre in result.get("dir_entre", []):
            if interseccion in entre and interseccion in result["dir_interseccion"]:
                result["dir_interseccion"].remove(interseccion)
    return result


def procesar_direccion(predichos: list):
    predichos = clear_inter_entre(predichos)
    # predichos = clear_altura_entre(predichos)
    matches_direccion_todos = (
        predichos["dir_entre"]
        + predichos["dir_interseccion"]
        + predichos["dir_nro"]
        + predichos["dir_lote"]
    )
    if matches_direccion_todos == []:
        return ""
    mejor_match = max(matches_direccion_todos, key=len)

    return re.sub(r"^\. ", "", mejor_match)


def procesar_fot(predichos: list):
    predichos = list(set(predichos))
    numeros = get_numeros(" ".join(predichos))
    if len(get_numeros((" ".join(predichos)))) == 1:
        unidad = re.search(r"\b(m2|mts2|mt2)\b", " ".join(predichos))
        if unidad:
            return " ".join(set(numeros)) + " " + unidad.group()

        return " ".join(set(numeros))
    else:
        if len(predichos) == 2:
            result = predichos[0] + ". " + predichos[1]
            result = result.replace("Res.", "residencial:")
            result = result.replace("Com.", "comercial:")
            result = result.replace("Fot", "FOT")
            result = result.replace("fot", "FOT")
            return result
        else:
            result = "".join(predichos).rstrip(".")
            result = result.replace("Fot", "FOT")
            result = result.replace("fot", "FOT")
            return result


def procesar_irregular(predichos: list):
    for predicho in predichos:
        if any(
            map(
                lambda subs: subs.lower() in predicho.lower(),
                ["irregular", "triangular", "martillo", "trapecio"],
            )
        ):
            return True
    return ""


def get_numeros(cadena: str):
    return re.findall(r"\b\d+(?:[.,]\d+)?\b", cadena)


def contiene_dos(texto):
    return bool(RE_DOS.findall(texto))


def contiene_tres(texto):
    return bool(RE_TRES.findall(texto))


def procesar_frentes(frentes_predichos):
    frentes_en_numeros = []
    for match in frentes_predichos:
        contiene_2 = contiene_dos(match.lower())
        if contiene_2:
            frentes_en_numeros.append(2)
        else:
            contiene_3 = contiene_tres(match.lower())
            if contiene_3:
                frentes_en_numeros.append(3)

    return max(frentes_en_numeros) if len(frentes_en_numeros) != 0 else ""


def procesar_medidas(predichos_todos: list):
    """
    Si el aviso enuncia múltiples dimensiones, buscar cuál refiere al lote
    """
    mejor_match= max(predichos_todos, key=len) if predichos_todos else ""
    
    if "martillo" in mejor_match:
        return mejor_match.replace(" mts", "")

    medidas = ""
    for numero in list(map(str, get_numeros(mejor_match))):
        medidas += numero + " x "
        
    medidas= medidas.replace(",",".")
    return medidas.rstrip(" x")

def procesar_medidas_multi(predichos_todos: list):
    """
    Si el aviso es multioferta, devolver todas las direcciones
    """
    result= []
    for candidato in list(__reduce_superstrings(set(predichos_todos))):
        medidas = ""
        for numero in list(map(str, get_numeros(candidato))):
            medidas += numero + " x "
        
        if (medidas.count("x")>1):
            medidas= medidas.replace(",",".")
            result.append(medidas.rstrip(" x"))


    if len(result)>1:
        return ";".join(result)
    return "".join(result)



def __reduce_superstrings(dimensions):
    reduced_dimensions = []
    for dim in dimensions:
        # Si la dimensión actual no es un superstring de ninguna dimensión ya incluida
        if not any(dim in existing or existing in dim for existing in reduced_dimensions):
            # Eliminar superstrings de la lista de resultados
            reduced_dimensions = [existing for existing in reduced_dimensions if dim not in existing and existing not in dim]
            # Agregar la dimensión actual a la lista de resultados
            reduced_dimensions.append(dim)
    return reduced_dimensions



def procesar_barrio(predichos: list):
    return max(predichos, key=len)
    # return re.compile(re.escape("Barrio"), re.IGNORECASE).sub("", mejor_match).strip()


def descubrir_nuevos(predichos: dict):
    if predichos["irregular"] == "" and (
        len(set(get_numeros(predichos["medidas"]))) > 2
        or "martillo" in predichos["medidas"]
    ):
        predichos["irregular"] = True

    if predichos["esquina"] and predichos["frentes"] == "":
        predichos["frentes"] = 2.0

    return predichos

def es_multioferta(predichos: list):
    return True if predichos else ""