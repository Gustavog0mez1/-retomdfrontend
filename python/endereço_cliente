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

