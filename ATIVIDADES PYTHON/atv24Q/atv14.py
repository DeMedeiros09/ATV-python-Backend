
nome = input('digite um nome com mais de 3 caracteres: ')
idade = int(input('digite sua idade (entre 0 e 150): '))
salario = int(input('digite seu salario (maior que zero): '))
sexo = input('digite F/M: ')
EstCivil = input('digite seu estado covil (s, c, v, d): ')

nome = len(nome)

if nome > 3 and idade > 0 and idade < 150 and salario > 0 and sexo == 'f' or sexo =='m' and EstCivil == 's' or EstCivil == 'c' or EstCivil == 'v' or EstCivil == 'd':
    print('informaçôes validas')
else:
    print('informações invalidas')


    



