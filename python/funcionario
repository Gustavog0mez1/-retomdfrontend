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



