while True:
    l =  input('digite (M) pra masculino ou (F) para feminino: ' )
    if l == 'F' or l == 'f':
        print('FEMININO')
        break
    elif l == 'M' or l == 'm':
        print('Masculino')
        break
    else:
        print('letra invalida por favor digite novamente o seu sexo')
