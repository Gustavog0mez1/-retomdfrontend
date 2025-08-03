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
