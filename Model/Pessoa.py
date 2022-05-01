
class Pessoa:
    def __init__(self, nome:str, idade:int, comendo:bool = False, falando:bool = False):
        """
        Construtor
        :param nome: Nome da pessoa(str)
        :param idade: Idade da pessoa(int)
        :param comendo: Se está comendo(bool)
        :param falando: Se está falando(bool)
        """
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        pass

    def falar(self, assunto):
        if(self.comendo):
            print(f"{self.nome} não pode falar enquanto come...")
            return

        if(self.falando):
            print(f"{self.nome} já está falando")
            return

        print(f"{self.nome} está falando sobre: {assunto}")
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando")
            return

        print(f"{self.nome} parou de falar")
        self.falando = False

    def comer(self, alimento:str):
        """
        Método para realizar a ação de comer
        :param alimento: Alimento
        :return: nenhum
        """
        if self.comendo:
            print(f"{self.nome} já está comendo...")
            return

        print(f"{self.nome} está comendo {alimento}...")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo")
            return
        print(f"{self.nome} parou de comer")
        self.comendo = False

