def analisar_argumentos(*args):
    """
    Analisa os argumentos fornecidos e retorna informações sobre os argumentos numéricos.
    
    Parâmetros:
      *args: Lista arbitrária de argumentos.
    
    Retorna:
      dict: Dicionário contendo:
            - 'maior': maior número encontrado.
            - 'menor': menor número encontrado.
            - 'media': média dos números.
            - 'quantidade': quantidade de argumentos numéricos considerados.
    """
    # Filtra somente os argumentos que são do tipo int ou float.
    numeros = [x for x in args if isinstance(x, (int, float))]
    quantidade = len(numeros)
    
    if quantidade == 0:
        return {'maior': None, 'menor': None, 'media': None, 'quantidade': 0}
    
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / quantidade
    
    return {'maior': maior, 'menor': menor, 'media': media, 'quantidade': quantidade}


# Exemplo de uso:
if __name__ == "__main__":
    resultado = analisar_argumentos(10, "texto", 5.5, 3, [1, 2], 8)
    print("Análise dos argumentos numéricos:", resultado)
    # Esperado (exemplo): {'maior': 10, 'menor': 3, 'media': 6.625, 'quantidade': 4}
