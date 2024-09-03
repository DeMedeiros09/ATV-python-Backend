n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
m = (n1 + n2) / 2

if m == 10:
    print('APROVADO com DISTINCAO')
elif m >= 7:
    print('APROVADO')
else:
    print('REPROVADO')