
# LISTA

lista = [1,2,3]
lista.append(10) # adiciona um numero
print(lista)
lista.insert(1,9) # adiciona um numero na posiçao desejada no caso posiçao 1
print(lista)
lista.extend([9,3,10,1,2]) # adiciona varios numeros a sua lista de uma vez
print(lista)
lista.remove(2) # remove o primeiro valor expecificado
print(lista)
del lista[0] # remove o item na posiçao expecificado
print(lista)
lista[2] = 1000
print(lista)
print(lista[5]) # MOSTRA na tela o item expecificado que voce quer...
lista = tuple(lista) # transforma uma lista em tupla
print(lista)

# TUPLA

tupla = (1,2,3,9,17) # criou uma tupla
print(tupla)
tupla = list(tupla) # tranforma tupla em lista
print(tupla)

# DICIONARIO

dicionario = {'key1': 10,'key2': 21,'key3': 23} # criar um dicionario
dicionario['key1'] = 22 # adiciona ou substitui uma key
dicionario['key4'] = 'text key' # adiciona um numero
print(dicionario)
del dicionario['key4'] # deleta a chave expecificada
print(dicionario)
valor = dicionario['key3'] # pega um valor da chave expecificada
print(valor)
chaves = dicionario.keys() # pega todas as chaves
print(chaves)
valores = dicionario.values() # pega todos os valores do dicionario
print(valores)
itens = dicionario.items() # pega todos os itens
print(itens)