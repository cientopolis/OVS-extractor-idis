from src.rbm.extractor.oferta import Oferta


class Multioferta(Oferta):  
    def medidas(self, predichos: list):
        """
        Si el aviso es multioferta, devolver todas las direcciones
        """

        predichos= predichos["medidas"] 
        if not predichos:
            return ""
        result= []
        for candidato in list(self._reduce_superstrings(set(predichos))):
            medidas = ""
            for numero in list(map(str, self._get_numeros(candidato))):
                medidas += numero + " x "
            
            if (medidas.count("x")>1):
                medidas= medidas.replace(",",".")
                result.append(medidas.rstrip(" x"))


        if len(result)>1:
            return ";".join(result)
        return "".join(result)