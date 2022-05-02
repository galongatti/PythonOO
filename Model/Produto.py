class Produto:

    def desconto(self, percentual: float):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    @property
    def nome(self):
        return self._nome

    # Setter
    @preco.setter
    def preco(self, valor: float):
        self._preco = valor

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    @staticmethod
    def preco_formatado(valor):
        precoAux: str = valor.__format__('.2f')
        return precoAux.replace('.', ',')
