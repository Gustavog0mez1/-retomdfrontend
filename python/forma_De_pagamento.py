class FormaPagamento:
    def __init__(self, id_pagamento, cartao, dinheiro, pix):
        self.id_pagamento = id_pagamento
        self.cartao = bool(cartao) # Converte BINARY (0/1) para booleano
        self.dinheiro = dinheiro
        self.pix = pix

    def __str__(self):
        cartao_str = "Sim" if self.cartao else "Não"
        return (f"ID Pagamento: {self.id_pagamento}\n"
                f"Cartão Disponível: {cartao_str}\n"
                f"Valor em Dinheiro (troco/desconto): R$ {self.dinheiro:.2f}\n"
                f"Valor em Pix (troco/desconto): R$ {self.pix:.2f}")

# Exemplo de uso:
forma_pagamento_exemplo = FormaPagamento(
    id_pagamento=1,
    cartao=1, # 1 para verdadeiro, 0 para falso
    dinheiro=0.00,
    pix=0.00
)
print("--- Dados da Forma de Pagamento ---")
print(forma_pagamento_exemplo)

forma_pagamento_exemplo_2 = FormaPagamento(
    id_pagamento=2,
    cartao=0,
    dinheiro=5.50, # Ex: troco a ser dado
    pix=0.00
)
print("\n--- Outro Exemplo de Forma de Pagamento ---")
print(forma_pagamento_exemplo_2)
print("\n")
