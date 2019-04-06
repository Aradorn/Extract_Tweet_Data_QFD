from unicodedata import normalize

class TextUtil:
    """
    Classe com métodos para tratamento de texto
    """

    def removerCaracteresEspeciais(self, text):
        """
        Método para remover caracteres especiais do texto
        """
        return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')