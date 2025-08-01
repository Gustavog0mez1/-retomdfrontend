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
