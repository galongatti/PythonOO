class Computador:
    def __init__(self, marca: str):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca: str):
        self.__marca = marca

    def escrever(self):
        print("COMPUTADOR ESTÁ DIGITANDO...")