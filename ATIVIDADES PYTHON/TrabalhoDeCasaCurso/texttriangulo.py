for i in range(5):
    l =+ i
    i = '*'
    print(i*l)
base = 5  # Base do triângulo

base = 5  # Base do triângulo

for i in range(1, base + 1):
    # Calcula o número de espaços à esquerda para centralizar os asteriscos
    spaces = ' ' * (base - i)
    # Imprime a linha com espaços e asteriscos
    print(spaces + '*' * (2 * i - 1))

