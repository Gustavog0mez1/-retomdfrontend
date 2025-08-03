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
