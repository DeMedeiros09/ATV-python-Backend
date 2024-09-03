n1 = int(input('digite sua primeira nota: '))
n2 = int(input('digite sua segunda nota: '))

s = (n1 + n2)/ 2 

if s >= 7 and s < 10:
    print(f'sua nota foi {s}, aprovado')
elif s < 7:
    print(f'sua nota foi {s}, reprovado')
elif s == 10:
    print(f'sua nota foi {s}, aprovado com distincao')

