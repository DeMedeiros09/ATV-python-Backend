l = input('digite uma letra entre F/M: ')

while True:
    if l == 'F' or l == 'f':
        print('Feminino')
        break
    elif l == 'M' or l == 'm':
        print('Masculino')
        break
    else:
        l = input('digite uma letra entre F/M: ')
        print('letra invalida!\ndigite outra letra')