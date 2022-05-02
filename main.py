from Model.Produto import Produto
from Model.Pessoa import Pessoa

# p1: Pessoa = Pessoa('Gabriel', 24)
# p1.comer("Mousse de maracuja")
# p1.comer("Mousse de maracuja")
# p1.parar_comer()
# p1.comer("Maça")
# p1.falar("Programação")
# p1.parar_comer()
# p1.falar("Programação")
# p1.falar("Esporte")
# p1.parar_falar()
# p1.parar_falar()
# p1.get_ano_nascimento()
#
# p2: Pessoa = Pessoa.por_ano_nascimento("Maria", 2000)
# print(p2.idade)
# p2.get_ano_nascimento()
# id:int = p2.gerar_id()
# print(id)

prod: Produto = Produto()
prod.nome = "XBOX ONE X"
prod.preco = 4500.00
prod.desconto(5.00)
print(f" Preço do {prod.nome} com desconto: {prod.preco_formatado(prod.preco)}")