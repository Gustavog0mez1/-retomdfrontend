CADASTRO FUNCIONARIO



class CadastroFuncionario:
    def __init__(self, id_cadastro, cpf, email, telefone, endereco, senha, id_funcionario):
        self.id_cadastro = id_cadastro
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.senha = senha
        self.id_funcionario = id_funcionario

    def __str__(self):
        return (f"ID Cadastro: {self.id_cadastro}\n"
                f"CPF: {self.cpf}\n"
                f"Email: {self.email}\n"
                f"Telefone: {self.telefone}\n"
                f"Endereço: {self.endereco}\n"
                f"ID Funcionário: {self.id_funcionario}")

# Exemplo de uso da classe:
funcionario1 = CadastroFuncionario(
    id_cadastro=1,
    cpf=12345678901,
    email="joao.silva@empresa.com",
    telefone=9876543210,
    endereco="Rua A, 123",
    senha="senha_segura", # Em um sistema real, senhas devem ser hashadas!
    id_funcionario=101
)

print(funcionario1)









LOGIN FUNCIONARIO




class LoginFuncionario:
    def __init__(self, id_funcionario, email, senha, cpf, telefone):
        self.id_funcionario = id_funcionario
        self.email = email
        self.senha = senha  # ATENÇÃO: Em um sistema real, senhas NUNCA devem ser armazenadas em texto simples! Use hash (e.g., bcrypt, hashlib).
        self.cpf = cpf
        self.telefone = telefone

    def __str__(self):
        return (f"ID Funcionário: {self.id_funcionario}\n"
                f"Email: {self.email}\n"
                f"CPF: {self.cpf}\n"
                f"Telefone: {self.telefone}")

    # Método de exemplo para simular verificação de senha (para demonstração, não use em produção!)
    def verificar_senha(self, senha_digitada):
        # Em um sistema real, aqui você compararia o hash da senha_digitada com o hash armazenado
        return self.senha == senha_digitada

# Exemplo de uso da classe:
login1 = LoginFuncionario(
    id_funcionario=101,
    email="joao.silva@empresa.com",
    senha="senha_segura123", # Novamente, lembre-se da segurança de senhas!
    cpf=12345678901,
    telefone=9876543210
)

print(login1)

# Simulação de login
if login1.verificar_senha("senha_segura123"):
    print("Login bem-sucedido!")
else:
    print("Senha incorreta.")









FUNCIONARIOS.TB


import datetime

class Funcionario:
    def __init__(self, id_funcionario, nome, cargo, telefone, data_contratacao):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cargo = cargo
        self.telefone = telefone
        # Assumindo que data_contratacao é um timestamp Unix ou um inteiro que representa uma data
        self.data_contratacao = data_contratacao

    def __str__(self):
        # Tentando formatar a data de contratação se for um timestamp
        try:
            data_formatada = datetime.datetime.fromtimestamp(self.data_contratacao).strftime('%Y-%m-%d')
        except (TypeError, ValueError):
            data_formatada = str(self.data_contratacao) # Se não for um timestamp válido, manter como está

        return (f"ID Funcionário: {self.id_funcionario}\n"
                f"Nome: {self.nome}\n"
                f"Cargo: {self.cargo}\n"
                f"Telefone: {self.telefone}\n"
                f"Data de Contratação: {data_formatada}")

# Exemplo de uso da classe:
# Usando um timestamp Unix para 15 de janeiro de 2023 (aproximado)
funcionario_exemplo = Funcionario(
    id_funcionario=201,
    nome="Ana Paula Silva",
    cargo="Gerente de Vendas",
    telefone=11987654321,
    data_contratacao=1673750400 # Timestamp para 2023-01-15 00:00:00 UTC
)

print("--- Dados do Funcionário ---")
print(funcionario_exemplo)
print("\n")







PREPARAÇAO DE PEDIDOS


class PreparacaoPedido:
    def __init__(self, id_pedido, id_cliente, nome_produto, quantidade_produto):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.nome_produto = nome_produto
        self.quantidade_produto = quantidade_produto

    def __str__(self):
        return (f"ID Pedido: {self.id_pedido}\n"
                f"ID Cliente: {self.id_cliente}\n"
                f"Nome do Produto: {self.nome_produto}\n"
                f"Quantidade: {self.quantidade_produto}")

# Exemplo de uso da classe:
pedido_exemplo = PreparacaoPedido(
    id_pedido=1001,
    id_cliente=501,
    nome_produto="Laptop Gamer X",
    quantidade_produto=1
)

print("--- Dados do Pedido ---")
print(pedido_exemplo)
print("\n")










CADASTRO CLIENTE




class CadastroCliente:
    def __init__(self, id_cadastro, cpf, email, telefone, endereco, senha, cep, id_cliente):
        self.id_cadastro = id_cadastro
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.senha = senha  # ATENÇÃO: Senhas devem ser hashadas!
        self.cep = cep
        self.id_cliente = id_cliente

    def __str__(self):
        return (f"ID Cadastro: {self.id_cadastro}\n"
                f"CPF: {self.cpf}\n"
                f"Email: {self.email}\n"
                f"Telefone: {self.telefone}\n"
                f"Endereço: {self.endereco}\n"
                f"CEP: {self.cep}\n"
                f"ID Cliente: {self.id_cliente}")

# Exemplo de uso:
cadastro1 = CadastroCliente(
    id_cadastro=1,
    cpf=11122233344,
    email="cliente.teste@email.com",
    telefone=21998877665,
    endereco="Rua das Flores, 100",
    senha="senha_segura_aqui", # Não para produção!
    cep="12345-678",
    id_cliente=101
)
print("--- Dados de Cadastro de Cliente ---")
print(cadastro1)
print("\n")








LOGIN



class Login:
    def __init__(self, id_login, cpf, senha, id_cliente, telefone):
        self.id_login = id_login
        self.cpf = cpf
        self.senha = senha # ATENÇÃO: Senhas devem ser hashadas!
        self.id_cliente = id_cliente
        self.telefone = telefone

    def __str__(self):
        return (f"ID Login: {self.id_login}\n"
                f"CPF: {self.cpf}\n"
                f"ID Cliente Associado: {self.id_cliente}\n"
                f"Telefone: {self.telefone}")

    # Método de exemplo para simular verificação de senha (NÃO PARA PRODUÇÃO!)
    def verificar_senha(self, senha_digitada):
        return self.senha == senha_digitada

# Exemplo de uso:
login_cliente = Login(
    id_login=1001,
    cpf=11122233344,
    senha="senha_login_segura", # Não para produção!
    id_cliente=101,
    telefone=21998877665
)
print("--- Dados de Login ---")
print(login_cliente)
if login_cliente.verificar_senha("senha_login_segura"):
    print("Login simulado bem-sucedido.")
print("\n")










CLIENTE


class Cliente:
    def __init__(self, cpf, nome, telefone, email, senha, id_cliente, cep):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha # ATENÇÃO: Senhas devem ser hashadas!
        self.id_cliente = id_cliente
        self.cep = cep

    def __str__(self):
        return (f"ID Cliente: {self.id_cliente}\n"
                f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Email: {self.email}\n"
                f"Telefone: {self.telefone}\n"
                f"CEP: {self.cep}")

# Exemplo de uso:
cliente_dados = Cliente(
    cpf=11122233344,
    nome="Maria da Silva",
    telefone="(21) 99887-7665", # Exemplo de telefone como string
    email="maria.silva@email.com",
    senha="outra_senha_segura", # Não para produção!
    id_cliente=101,
    cep="12345-678"
)
print("--- Dados do Cliente (detalhes) ---")
print(cliente_dados)
print("\n")








PEDIDO CLIENTE




class PedidoCliente:
    def __init__(self, id_pedido, entregador_funcionario, endereco_entrega, produto_pedido, nome_cliente):
        self.id_pedido = id_pedido
        self.entregador_funcionario = entregador_funcionario
        self.endereco_entrega = endereco_entrega
        self.produto_pedido = produto_pedido
        self.nome_cliente = nome_cliente

    def __str__(self):
        return (f"ID Pedido: {self.id_pedido}\n"
                f"Entregador (ID Func.): {self.entregador_funcionario}\n"
                f"Endereço de Entrega: {self.endereco_entrega}\n"
                f"Produto Pedido (ID/Código): {self.produto_pedido}\n"
                f"Nome do Cliente: {self.nome_cliente}")

# Exemplo de uso:
pedido_cliente_exemplo = PedidoCliente(
    id_pedido=2001,
    entregador_funcionario=None, # Pode ser 0 ou None se não houver entregador atribuído
    endereco_entrega="Av. Principal, 500 - Apt 10",
    produto_pedido=5001, # Ex: ID do produto
    nome_cliente="Carlos Eduardo"
)
print("--- Dados do Pedido do Cliente ---")
print(pedido_cliente_exemplo)
print("\n")






PAGINA INICIAL




class PaginaInicial:
    def __init__(self, id_pagina_inicial, cardapio, id_perfil, carrinho_produto, avaliacoes_loja):
        self.id_pagina_inicial = id_pagina_inicial
        self.cardapio = cardapio
        self.id_perfil = id_perfil
        self.carrinho_produto = carrinho_produto
        self.avaliacoes_loja = avaliacoes_loja

    def __str__(self):
        return (f"ID Página Inicial: {self.id_pagina_inicial}\n"
                f"Cardápio: {self.cardapio}\n"
                f"ID Perfil Associado: {self.id_perfil}\n"
                f"Carrinho de Produto: {self.carrinho_produto}\n"
                f"Avaliações da Loja: {self.avaliacoes_loja:.2f}")

# Exemplo de uso:
pagina_inicial_exemplo = PaginaInicial(
    id_pagina_inicial=1,
    cardapio="Lanches, Pizzas, Bebidas",
    id_perfil=101,
    carrinho_produto="Item A, Item B (2)",
    avaliacoes_loja=4.75 # Ex: nota 4.75 de 5
)
print("--- Dados da Página Inicial ---")
print(pagina_inicial_exemplo)
print("\n")








PERFIL CLIENTE



class PerfilCliente:
    def __init__(self, id_perfil, nome, cep, cidade, estado, cpf):
        self.id_perfil = id_perfil
        self.nome = nome
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.cpf = cpf

    def __str__(self):
        return (f"ID Perfil: {self.id_perfil}\n"
                f"Nome: {self.nome}\n"
                f"CEP: {self.cep}\n"
                f"Cidade: {self.cidade}\n"
                f"Estado: {self.estado}\n"
                f"CPF: {self.cpf}")

# Exemplo de uso:
perfil_cliente_exemplo = PerfilCliente(
    id_perfil=101,
    nome="Mariana Souza",
    cep=12345000,
    cidade="São Paulo",
    estado="SP",
    cpf=98765432109
)
print("--- Dados do Perfil do Cliente ---")
print(perfil_cliente_exemplo)
print("\n")










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



