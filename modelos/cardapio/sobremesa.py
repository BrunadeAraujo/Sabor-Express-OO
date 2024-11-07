from cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
       self._preco -= (self._preco * 0.07)

sobremesa = Sobremesa(nome="Mousse de Chocolate", preco=15.00, descricao="Delicioso mousse de chocolate com raspas de chocolate.", tipo="Chocolate", tamanho="Pequena")

Sobremesa.aplicar_desconto()

print(f"Nome: {sobremesa.nome}")
print(f"Preço: R$ {sobremesa.preco:.2f}")
print(f"Tipo: {sobremesa.tipo}")
print(f"Tamanho: {sobremesa.tamanho}")
print(f"Descrição: {sobremesa.descricao}")