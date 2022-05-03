from Model.Computador import Computador
from Model.Escritor import Escritor
from Model.Caneta import Caneta

escritor: Escritor = Escritor("Gabriel")
caneta: Caneta = Caneta("Bic")
computador: Computador = Computador("Dell")

print(f"Escritor: {escritor.nome}")
escritor.ferramenta = computador
escritor.ferramenta.escrever()