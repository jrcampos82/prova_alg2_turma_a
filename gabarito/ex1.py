def media_vendas(vendas, minimo):
    """
    Calcula a média de vendas para cada produto e retorna um dicionário contendo apenas
    os produtos cuja média de vendas seja maior ou igual a 'minimo'.
    
    Parâmetros:
      vendas (dict): Dicionário onde as chaves são nomes de produtos e os valores são listas de inteiros (vendas mensais).
      minimo (int ou float): Valor mínimo para a média de vendas.
    
    Retorna:
      dict: Dicionário com produtos que possuem média de vendas >= minimo, onde a média está arredondada para duas casas decimais.
    """
    # Calcula a média de vendas para cada produto usando dictionary comprehension.
    media_por_produto = {
        produto: sum(vendas_list) / len(vendas_list)
        for produto, vendas_list in vendas.items() if vendas_list
    }
    
    # Filtra os produtos cuja média é maior ou igual ao valor mínimo e arredonda para duas casas decimais.
    resultado = {produto: round(media, 2) for produto, media in media_por_produto.items() if media >= minimo}
    return resultado


# Exemplo de uso:
if __name__ == "__main__":
    vendas = {
        "Produto A": [100, 200, 150],
        "Produto B": [50, 60, 70],
        "Produto C": [300, 250, 400]
    }
    resultado = media_vendas(vendas, 150)
    print("Médias de vendas (mínimo 150):", resultado)
    # Esperado (exemplo): {'Produto A': 150.0, 'Produto C': 316.67}
