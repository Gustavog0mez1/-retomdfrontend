
class ItemCardapio:
    def __init__(self, id_item_cardapio, id_produto, nome_exibicao, descricao_item, itens_disponiveis_no_cardapio):
        self.id_item_cardapio = id_item_cardapio
        self.id_produto = id_produto
        self.nome_exibicao = nome_exibicao
        self.descricao_item = descricao_item
        self.itens_disponiveis_no_cardapio = itens_disponiveis_no_cardapio

    def __str__(self):
        return (f"ID Item Cardápio: {self.id_item_cardapio}\n"
                f"ID Produto: {self.id_produto}\n"
                f"Nome Exibição: {self.nome_exibicao}\n"
                f"Descrição: {self.descricao_item}\n"
                f"Itens Disponíveis: {self.itens_disponiveis_no_cardapio}")

# Exemplo de uso:
item_cardapio_exemplo = ItemCardapio(
    id_item_cardapio=101,
    id_produto=1,
    nome_exibicao="X-Tudo Mega",
    descricao_item="Pão, 2 hambúrgueres, queijo, bacon, ovo, alface, tomate, milho, batata palha, maionese especial.",
    itens_disponiveis_no_cardapio="Sim" # Ou "Em falta", "Temporário", etc.
)
print("--- Dados do Item do Cardápio ---")
print(item_cardapio_exemplo)
print("\n")






PRODUTOS


class Produto:
    def __init__(self, id_produto, ingredientes, tamanho_lanche, nome_lanche, valor_lanche):
        self.id_produto = id_produto
        # `ingredientes` sendo VARCHAR(1,N) é um pouco ambíguo no diagrama.
        # Poderia ser uma lista de IDs de ingredientes (se houver outra tabela de ingredientes).
        # Aqui, vou tratar como uma string de texto.
        self.ingredientes = ingredientes
        self.tamanho_lanche = tamanho_lanche
        self.nome_lanche = nome_lanche
        self.valor_lanche = valor_lanche

    def __str__(self):
        return (f"ID Produto: {self.id_produto}\n"
                f"Nome do Lanche: {self.nome_lanche}\n"
                f"Tamanho: {self.tamanho_lanche}\n"
                f"Ingredientes (texto): {self.ingredientes}\n"
                f"Valor: R$ {self.valor_lanche:.2f}")

# Exemplo de uso:
produto_exemplo = Produto(
    id_produto=1,
    ingredientes="Hambúrguer, Queijo, Bacon, Alface, Tomate", # Tratado como string aqui
    tamanho_lanche="G",
    nome_lanche="X-Bacon Duplo",
    valor_lanche=25.90
)
print("--- Dados do Produto ---")
print(produto_exemplo)
print("\n")
