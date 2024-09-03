

while True:
    n = float(input('digite uma nota entre 0 e 10: '))
    if n >= 0 and n <= 10:
        print('\n'+'='*28)
        print(f'a nota {n} eh um valor valido')
        print('='*28 +'\n')
        break
    else:
        print('\n'+'='*28)
        print(f'{n:.0f} eh um valor invalido\npor favor digite outra nota')
        print('='*28 + '\n')
