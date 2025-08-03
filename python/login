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

