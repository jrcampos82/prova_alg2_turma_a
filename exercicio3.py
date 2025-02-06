"""
Exercício 03 – Profundidade Máxima de Listas Aninhadas (Recursividade)

Objetivo:
Crie uma função recursiva chamada `max_depth` que receba uma lista que pode conter outras listas aninhadas e retorne a profundidade máxima de aninhamento.

Requisitos:
  - Se a lista não contiver nenhuma outra lista, a profundidade deve ser 1.
  - Se a lista contiver outras listas, a função deve analisar cada uma delas recursivamente e determinar a profundidade máxima.
  - Utilize recursividade para explorar as listas aninhadas.

Exemplos:
    max_depth([1, 2, 3])               # Deve retornar 1.
    max_depth([1, [2, 3], 4])           # Deve retornar 2.
    max_depth([1, [2, [3, 4]], 5])      # Deve retornar 3.

Exemplo de uso:
    lista_aninhada = [1, [2, [3, 4], 5], 6]
    profundidade = max_depth(lista_aninhada)
    print("Profundidade máxima:", profundidade)
    
Dica: Percorra cada elemento da lista e verifique se ele é do tipo list. Se for, chame recursivamente a função e compare as profundidades.
"""
# Sua solução aqui
