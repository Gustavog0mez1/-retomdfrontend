
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
