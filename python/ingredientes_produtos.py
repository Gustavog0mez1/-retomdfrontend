

class IngredienteProduto:
    def __init__(self, id_ingrediente, nome_ingrediente, unidade_medida, estoque_atual, estoque_minimo):
        self.id_ingrediente = id_ingrediente
        self.nome_ingrediente = nome_ingrediente
        self.unidade_medida = unidade_medida # Ex: 1.0 para kg, 0.5 para litro
        self.estoque_atual = estoque_atual   # Ex: "10 kg", "50 unidades"
        self.estoque_minimo = estoque_minimo # Ex: "5 kg", "20 unidades"

    def __str__(self):
        return (f"ID Ingrediente: {self.id_ingrediente}\n"
                f"Nome Ingrediente: {self.nome_ingrediente}\n"
                f"Unidade de Medida: {self.unidade_medida}\n"
                f"Estoque Atual: {self.estoque_atual}\n"
                f"Estoque Mínimo: {self.estoque_minimo}")

# Exemplo de uso:
ingrediente_exemplo = IngredienteProduto(
    id_ingrediente="HAMBURGUER001", # ID como string
    nome_ingrediente="Carne Moída (Patty)",
    unidade_medida=0.150, # Ex: 0.150 kg por patty
    estoque_atual="100 patties",
    estoque_minimo="20 patties"
)
print("--- Dados do Ingrediente do Produto ---")
print(ingrediente_exemplo)
print("\n")
