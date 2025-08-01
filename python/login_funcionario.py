
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
