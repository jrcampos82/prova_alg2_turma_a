def max_depth(lst):
    """
    Retorna a profundidade máxima de aninhamento de sublistas em 'lst'.

    Requisitos:
      - Se a lista não contiver nenhuma sublista, retorna 1.
      - Se houver sublistas, retorna 1 + a maior profundidade entre elas.

    Parâmetro:
      lst (list): Lista que pode conter outras listas aninhadas.

    Retorna:
      int: A profundidade máxima de aninhamento.
    """
    # Inicializa a profundidade atual como 1 (nível da própria lista)
    current_depth = 1

    # Percorre cada elemento da lista
    for item in lst:
        # Se o elemento for uma lista, calcula sua profundidade recursivamente
        if isinstance(item, list):
            sub_depth = max_depth(item)
            # Atualiza a profundidade atual, considerando o nível do item aninhado
            current_depth = max(current_depth, 1 + sub_depth)
    
    return current_depth


# Exemplos de uso:
if __name__ == "__main__":
    # Exemplo 1: sem sublistas
    exemplo1 = [1, 2, 3]
    print("max_depth([1, 2, 3]) =", max_depth(exemplo1))  # Deve retornar 1

    # Exemplo 2: com uma sublista
    exemplo2 = [1, [2, 3], 4]
    print("max_depth([1, [2, 3], 4]) =", max_depth(exemplo2))  # Deve retornar 2

    # Exemplo 3: com sublistas aninhadas
    exemplo3 = [1, [2, [3, 4]], 5]
    print("max_depth([1, [2, [3, 4]], 5]) =", max_depth(exemplo3))  # Deve retornar 3
