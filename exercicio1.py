"""
Exercício 01 – Análise de Vendas

Objetivo:
Você recebeu um dicionário representando as vendas mensais de uma loja. Cada chave é o nome de um produto e o valor é uma lista de inteiros representando as vendas mensais.
Sua tarefa é:
  1. Criar uma função chamada `media_vendas` que calcule a média de vendas para cada produto.
  2. Retornar um novo dicionário contendo apenas os produtos cuja média de vendas seja maior ou igual a um valor mínimo (parâmetro da função).

Requisitos:
  - Utilize um dictionary comprehension para calcular as médias.
  - Use funções built-in como `sum` e `len` para calcular a média.
  - Utilize estruturas condicionais para filtrar os produtos de acordo com o valor mínimo fornecido.
  
Exemplo de uso:
    vendas = {
        "Produto A": [100, 200, 150],
        "Produto B": [50, 60, 70],
        "Produto C": [300, 250, 400]
    }
    resultado = media_vendas(vendas, 150)
    print(resultado)
    # Saída esperada (exemplo): {'Produto A': 150.0, 'Produto C': 316.67}
    
Observação: Formate a média como número float com duas casas decimais, se desejar.
"""
# Sua solução aqui
