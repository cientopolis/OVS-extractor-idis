import datetime
import spacy
import re

from src.helper import clean_direccion, reduce_superstrings 

NLP = spacy.load("es_core_news_lg")

RE_DOS = re.compile(r"\b(dos|doble|2|segundo)\b", re.IGNORECASE)
RE_TRES = re.compile(r"\b(tres|triple|3|tercer)\b", re.IGNORECASE)
class Oferta():

    def a_demoler(self, predichos: list):
        return True if predichos["a_demoler"] else ""
    
    def loteo_ph(self, predichos: list):
        if not predichos["loteo_ph_DM"] and (predichos["loteo_ph_M"]) : #or predichos["loteo_ph_DM_True"]):
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

 
    def _clear_inter_entre(self, result: list):
        for interseccion in result.get("dir_interseccion", []):
            for entre in result.get("dir_entre", []):
                if interseccion in entre and interseccion in result["dir_interseccion"]:
                    result["dir_interseccion"].remove(interseccion)
        return result

    
    def direccion(self, predichos: list):
        predichos = self._clear_inter_entre(predichos)
        # predichos = clear_altura_entre(predichos)
        matches_direccion_todos = (
            predichos["dir_entre"]
            + predichos["dir_interseccion"]
            + predichos["dir_nro"]
            + [";".join(reduce_superstrings(predichos["dir_lote"]))]
        )
        if matches_direccion_todos == []:
            return ""
        return clean_direccion(max(matches_direccion_todos, key=len))

    def fot_multiple(self, predichos):
        indicadores_multiplicidad_ocurridos=1
        for fot_string_predicho in predichos:
            for indicador_multiplicidad in ["res ", "com", "ind"]:
                if indicador_multiplicidad in fot_string_predicho.lower():
                    indicadores_multiplicidad_ocurridos+=1
        return indicadores_multiplicidad_ocurridos
    
    def replace(self, string):
        for replacement in ["RESIDENCIAL", "res ", "res.", "Res.", "Residencial"]:
            string = string.replace(replacement, "residencial")
        
        for replacement in ["COMERCIAL", "com ", "com.", "Com.", "Comercial"]:
            string = string.replace(replacement, "comercial")
        
        for replacement in ["INDUSTRIAL", "ind.", "indus.", "ind ", "Industrial"]:
            string = string.replace(replacement, "industrial")

        for replacement in ["Fot", "fot", "f.o.t", "F.O.T", "F.o.t"]:
            string = string.replace(replacement, "FOT")
        
        return string.replace(",",".").replace("/","")
    
    def fot(self, predichos: list):
        predichos = list(set(predichos["fot"]))
        veces_que_menciona_fot= self.fot_multiple(predichos)
        if (veces_que_menciona_fot == 1):
            result= max(predichos, key=len) if predichos else ""
        else: 
            predichos= reduce_superstrings(predichos)         
            result= self.replace(". ".join(predichos))
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
        seleccionadas= []
        for candidato in list(reduce_superstrings(set(predichos))):
            medidas_candidato=""
            if all(float(numero) >=5 for numero in list(map(str, self._get_numeros(candidato)))):
                for numero in list(map(str, self._get_numeros(candidato))):
                    medidas_candidato += numero + " x "
                seleccionadas.append(medidas_candidato.replace(",",".").rstrip(" x"))

            
        return ";".join(set(seleccionadas))



    def barrio(self, predichos: list):
        return max(predichos["barrio"], key=len) if predichos["barrio"] else ""
        # return re.compile(re.escape("Barrio"), re.IGNORECASE).sub("", mejor_match).strip()

    def esquina(self, predichos: list):
        return True if predichos["esquina"] else ""

    def pileta(self, predichos: list):
        return True if predichos["pileta"] else ""

    def urb_cerrada(self, predichos: list):
        if ((not predichos["urb_cerrada_DM"]) and predichos["urb_cerrada"]):
            return True
        return ""
    
    def urb_semicerrada(self, predichos: list):
        return True if predichos["urb_semicerrada"] else ""

    def indiviso(self, predichos: list):
        return True if predichos["indiviso"] else ""
    
    def es_multioferta(self, predichos: list):
        return True if predichos["es_multioferta"] else ""
    
    def indiviso(self, predichos: list):
        if not predichos["indiviso_DM"] and predichos["indiviso_M"]:
            return True 
        return ""

    def es_monetizable(self, predichos: list):
        if not self.a_demoler(predichos) and not self.preventa(predichos) and predichos["es_monetizable"]:
            return True
        return ""
    
    def posesion(self, predichos: list):
        return True if predichos["posesion"] else ""