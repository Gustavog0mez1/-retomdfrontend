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
