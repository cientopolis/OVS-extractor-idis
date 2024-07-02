import datetime
import spacy
import re

from src.helper import clean_direccion 

NLP = spacy.load("es_core_news_lg")

RE_DOS = re.compile(r"\b(dos|doble|2|segundo)\b", re.IGNORECASE)
RE_TRES = re.compile(r"\b(tres|triple|3|tercer)\b", re.IGNORECASE)
class Oferta():

    def a_demoler(self, predichos: list):
        return True if predichos["a_demoler"] else ""
    
    def loteo_ph(self, predichos: list):
        if predichos["loteo_ph_DM"] or predichos["loteo_ph_M"]:
            return True 
        return ""


    def preventa(self, predichos: list):
        matcheos = 0
        minimosMatcheos = 2
        maximoAniosLejanos = 15

        for pre in predichos["pre-venta-asegurados"]:
            matcheos += minimosMatcheos + 1

        matcheosAuxiliar = 0
        for pre in predichos["pre-venta-posibles"]:
            matcheosAuxiliar += 1
        if matcheosAuxiliar > 0:
            matcheos += 1

        matcheosAuxiliar = 0
        for span in predichos["pre-venta-fecha"]:
            span.replace('.', '') #para que no haya problemas con los puntos -> no se si me está dando efecto
            try:
                num = float(span)
                actualYear = datetime.datetime.now().year
                if (num > actualYear) and (num < actualYear + maximoAniosLejanos):
                    matcheosAuxiliar +=1
            except ValueError:
                pass
        if matcheosAuxiliar > 0:
            matcheos += 1

        matcheosAuxiliar = 0
        for pre in predichos["pre-venta-cuotas"]:
            matcheosAuxiliar += 1
        if matcheosAuxiliar > 0:
            matcheos += 1

        for pre in predichos["pre-venta-descartar"]:
            matcheos = 0

        return True if (matcheos >= minimosMatcheos) else ""

    def __clear_altura_entre(self, predichos: list):
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

 
    def __clear_inter_entre(self, result: list):
        for interseccion in result.get("dir_interseccion", []):
            for entre in result.get("dir_entre", []):
                if interseccion in entre and interseccion in result["dir_interseccion"]:
                    result["dir_interseccion"].remove(interseccion)
        return result


    def __clean_lote(self, predicciones_lote: list):
        if not predicciones_lote:
            return []
        candidatos= []
        for candidato in predicciones_lote:
            candidatos.append(" ".join(candidato.split()[:2]).strip() if len(candidato.split()) == 3 else candidato.rstrip(".").rstrip(","))
        return candidatos
    
    def direccion(self, predichos: list):
        predichos = self.__clear_inter_entre(predichos)
        # predichos = clear_altura_entre(predichos)
        matches_direccion_todos = (
            predichos["dir_entre"]
            + predichos["dir_interseccion"]
            + predichos["dir_nro"]
            + self.__clean_lote(predichos["dir_lote"])
        )
        if matches_direccion_todos == []:
            return ""
        return clean_direccion(max(matches_direccion_todos, key=len))


    
    def fot(self, predichos: list):
        predichos = list(set(predichos["fot"]))
        numeros = self._get_numeros(" ".join(predichos))
        if len(self._get_numeros((" ".join(predichos)))) == 1:
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


    def irregular(self, predichos: list):
        for predicho in predichos["irregular"]:
            if any(
                map(
                    lambda subs: subs.lower() in predicho.lower(),
                    ["irregular", "triangular", "martillo", "trapecio"],
                )
            ):
                return True
        return ""


    def _get_numeros(self, cadena: str):
        return re.findall(r"\b\d+(?:[.,]\d+)?\b", cadena)


    def __contiene_dos(self, texto):
        return bool(RE_DOS.findall(texto))


    def __contiene_tres(self, texto):
        return bool(RE_TRES.findall(texto))


    def frentes(self, predichos: list):
        predichos= predichos["frentes"]
        frentes_en_numeros = []
        for match in predichos:
            contiene_2 = self.__contiene_dos(match.lower())
            if contiene_2:
                frentes_en_numeros.append(2)
            else:
                contiene_3 = self.__contiene_tres(match.lower())
                if contiene_3:
                    frentes_en_numeros.append(3)

        return max(frentes_en_numeros) if len(frentes_en_numeros) != 0 else ""


    
    def medidas(self, predichos: list):
        """
        Si el aviso enuncia múltiples dimensiones, buscar cuál refiere al lote
        """
        predichos= predichos["medidas"]
        mejor_match= max(predichos, key=len) if predichos else ""
        
        if "martillo" in mejor_match:
            return mejor_match.replace(" mts", "")

        medidas = ""
        for numero in list(map(str, self._get_numeros(mejor_match))):
            medidas += numero + " x "
            
        medidas= medidas.replace(",",".")
        return medidas.rstrip(" x")



    def _reduce_superstrings(self, dimensions):
        reduced_dimensions = []
        for dim in dimensions:
            # Si la dimensión actual no es un superstring de ninguna dimensión ya incluida
            if not any(dim in existing or existing in dim for existing in reduced_dimensions):
                # Eliminar superstrings de la lista de resultados
                reduced_dimensions = [existing for existing in reduced_dimensions if dim not in existing and existing not in dim]
                # Agregar la dimensión actual a la lista de resultados
                reduced_dimensions.append(dim)
        return reduced_dimensions



    def barrio(self, predichos: list):
        return max(predichos["barrio"], key=len) if predichos["barrio"] else ""
        # return re.compile(re.escape("Barrio"), re.IGNORECASE).sub("", mejor_match).strip()

    
    def esquina(self, predichos: list):
        return True if predichos["esquina"] else ""

    def pileta(self, predichos: list):
        return True if predichos["pileta"] else ""

    def urb_cerrada(self, predichos: list):
        return True if predichos["urb_cerrada"] else ""
    
    def urb_semicerrada(self, predichos: list):
        return True if predichos["urb_semicerrada"] else ""

    def indiviso(self, predichos: list):
        return True if predichos["indiviso"] else ""
    
    def es_multioferta(self, predichos: list):
        return True if predichos["es_multioferta"] else ""
    
    def posesion(self, predichos: list):
        return True if predichos["posesion"] else ""

    def es_monetizable(self, predichos: list):
        return True if predichos["es_monetizable"] else ""