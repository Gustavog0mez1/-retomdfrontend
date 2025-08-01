
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
