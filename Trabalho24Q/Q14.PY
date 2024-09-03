nome = input('digite seu nome com mais de 3 caracteres: ')
idade = int(input('digite sua idade (entre 0 e 150): '))
salario = int(input('digite seu salario (maior que zero): '))
sexo = input('digite seu sexo M/F: ')
civil = input('digite seu estado civil (s,c,v,d): ')

nome = len(nome)

if nome > 3 and idade > 0 and idade < 150 and salario > 0 and sexo == 'm' or sexo == 'f' and civil == 's' or civil == 'c' or civil == 'v' or civil == 'd':
    print('informacoes validadas')
