import functools

# Solicita ao usuário uma lista de números separados por vírgula.
numbers_input = input("Digite uma lista de números separados por vírgula: ")

# Converte a entrada para uma lista de inteiros, removendo espaços desnecessários.
numbers_list = [int(x.strip()) for x in numbers_input.split(",")]

# Calcula o cubo de cada número utilizando map e converte o resultado para uma lista.
cubes = list(map(lambda x: x ** 3, numbers_list))

# Filtra apenas os cubos pares utilizando filter e converte o resultado para uma lista.
even_cubes = list(filter(lambda x: x % 2 == 0, cubes))

# Soma os cubos pares utilizando reduce.
# Se a lista estiver vazia, atribui 0 para evitar erro na função reduce.
total = functools.reduce(lambda a, b: a + b, even_cubes) if even_cubes else 0

# Exibe a soma dos cubos pares.
print("A soma dos cubos pares é:", total)

# --- Linhas adicionadas para calcular e exibir o maior cubo par ---
if even_cubes:
    maior_cubo = max(even_cubes)
    print("O maior cubo par é:", maior_cubo)
else:
    print("Não há cubos pares na lista.")
