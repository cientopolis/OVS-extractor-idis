from src.helper import clean_direccion, medidas_terrenos, reduce_superstrings
from src.rbm.extractor.oferta import Oferta


class Multioferta(Oferta):  
    def medidas(self, predichos: list):
        """
        Si el aviso es multioferta, devolver todas las dimensiones
        """

        predichos= medidas_terrenos(predichos["medidas"])
        if not predichos:
            return ""
        result= []
        for candidato in list(reduce_superstrings(set(predichos))):
            medidas = ""
            for numero in list(map(str, self._get_numeros(candidato))):
                medidas += numero + " x "
            
            if (medidas.count("x")>1):
                medidas= medidas.replace(",",".")
                result.append(medidas.rstrip(" x"))


        if len(set(result))>1:
            return ";".join(result)
        return "".join(set(result))
    
    def direccion(self, predichos: list):
        predichos = self._clear_inter_entre(predichos)
        # predichos = clear_altura_entre(predichos)
        matches_direccion_todos = (
            predichos["dir_entre"]
            + predichos["dir_interseccion"]
            + predichos["dir_nro"]
        )
        direccion_loteo=None
        if matches_direccion_todos != []:
            direccion_loteo= clean_direccion(max(matches_direccion_todos, key=len))
        
        lotes_en_venta= ";".join(reduce_superstrings(predichos["dir_lote"]))
        
        if lotes_en_venta:
            return f"{direccion_loteo}. {lotes_en_venta}" if direccion_loteo else lotes_en_venta
        return direccion_loteo

        