n1 = int(input('digite um numero: '))
n2 = int(input('digite um outro numero: '))

if n1 > n2:
    print(f'o maior numero eh: {n1}')
elif n1 == n2:
    print(f'os numeros {n1} e {n2} sao iguais')
else:
    print(f'o maior numero eh: {n2}')