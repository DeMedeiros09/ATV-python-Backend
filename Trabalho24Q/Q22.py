import time
p1 = input('digite uma palavra or frase: ')
p2 = input('digite outra palavra ou frase: ')

print('\n comparando as strings...')

time.sleep(1)

print(f'\nstring 1: {p1}\nstring 2: {p2}')
print(f'\ntamanho de ({p1}): {len(p1)} caracter(es)\ntamanho de ({p2}): {len(p2)} caracter(es)')

if len(p1) == len(p2):
    print(f'As duas strings são de tamanhos iguais')
else:
    print('As duas strings são de tamanhos diferentes')

if p1 == p2:
    print('As duas strings possuem conteúdos iguais')
else:
    print('As duas strings possuem conteúdos diferentes')
