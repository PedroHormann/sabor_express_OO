class Avaliacao:
    """Representa uma avaliação feita por um cliente."""

    def __init__(self, cliente, nota):
        """
        Inicializa uma instância de Avaliacao.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (int): A nota dada pelo cliente (de 1 a 5, por exemplo).
        """
        self._cliente = cliente
        self._nota = nota