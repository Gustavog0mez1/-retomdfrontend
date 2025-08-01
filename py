




ENDEREÇO CLIENTE




class EnderecoCliente:
    def __init__(self, id_endereco, id_cliente, rua, numero, bairro, cidade, estado, cep):
        self.id_endereco = id_endereco
        self.id_cliente = id_cliente
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep # CEP geralmente é string por causa de hífens

    def __str__(self):
        return (f"ID Endereço: {self.id_endereco}\n"
                f"ID Cliente Associado: {self.id_cliente}\n"
                f"Endereço: {self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}\n"
                f"CEP: {self.cep}")

# Exemplo de uso:
endereco_cliente_exemplo = EnderecoCliente(
    id_endereco=1,
    id_cliente=101,
    rua="Rua Avelino",
    numero=123,
    bairro="Centro",
    cidade="Rio de Janeiro",
    estado="RJ",
    cep="20000-000"
)
print("--- Dados do Endereço do Cliente ---")
print(endereco_cliente_exemplo)
print("\n")








FORMAS DE PAGAMENTO




class FormaPagamento:
    def __init__(self, id_pagamento, cartao, dinheiro, pix):
        self.id_pagamento = id_pagamento
        self.cartao = bool(cartao) # Converte BINARY (0/1) para booleano
        self.dinheiro = dinheiro
        self.pix = pix

    def __str__(self):
        cartao_str = "Sim" if self.cartao else "Não"
        return (f"ID Pagamento: {self.id_pagamento}\n"
                f"Cartão Disponível: {cartao_str}\n"
                f"Valor em Dinheiro (troco/desconto): R$ {self.dinheiro:.2f}\n"
                f"Valor em Pix (troco/desconto): R$ {self.pix:.2f}")

# Exemplo de uso:
forma_pagamento_exemplo = FormaPagamento(
    id_pagamento=1,
    cartao=1, # 1 para verdadeiro, 0 para falso
    dinheiro=0.00,
    pix=0.00
)
print("--- Dados da Forma de Pagamento ---")
print(forma_pagamento_exemplo)

forma_pagamento_exemplo_2 = FormaPagamento(
    id_pagamento=2,
    cartao=0,
    dinheiro=5.50, # Ex: troco a ser dado
    pix=0.00
)
print("\n--- Outro Exemplo de Forma de Pagamento ---")
print(forma_pagamento_exemplo_2)
print("\n")





CARDAPIO


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










INGREDIENTES PRODUTOS




class IngredienteProduto:
    def __init__(self, id_ingrediente, nome_ingrediente, unidade_medida, estoque_atual, estoque_minimo):
        self.id_ingrediente = id_ingrediente
        self.nome_ingrediente = nome_ingrediente
        self.unidade_medida = unidade_medida # Ex: 1.0 para kg, 0.5 para litro
        self.estoque_atual = estoque_atual   # Ex: "10 kg", "50 unidades"
        self.estoque_minimo = estoque_minimo # Ex: "5 kg", "20 unidades"

    def __str__(self):
        return (f"ID Ingrediente: {self.id_ingrediente}\n"
                f"Nome Ingrediente: {self.nome_ingrediente}\n"
                f"Unidade de Medida: {self.unidade_medida}\n"
                f"Estoque Atual: {self.estoque_atual}\n"
                f"Estoque Mínimo: {self.estoque_minimo}")

# Exemplo de uso:
ingrediente_exemplo = IngredienteProduto(
    id_ingrediente="HAMBURGUER001", # ID como string
    nome_ingrediente="Carne Moída (Patty)",
    unidade_medida=0.150, # Ex: 0.150 kg por patty
    estoque_atual="100 patties",
    estoque_minimo="20 patties"
)
print("--- Dados do Ingrediente do Produto ---")
print(ingrediente_exemplo)
print("\n")



