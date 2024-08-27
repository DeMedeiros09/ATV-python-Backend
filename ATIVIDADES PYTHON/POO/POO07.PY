class Produto:
    qtdProd = 0 
    
    def __init__(self, codigo, preco):
        self.__codigo = codigo
        self.__preco = preco
        Produto.qtdProd += 1

    def getcodigo(self):
        return self.__codigo
    
    def getpreco(self):
        return self.__preco
    
    def setcodigo(self, novoCodigo):
        self.__codigo = novoCodigo
        return self.__codigo
    
    def setpreco(self, novoPreco):
        self.__preco = novoPreco
        return self.__preco
    
class Gerenciador:
    
    def __init__(self):
        self.listproduto = []

    def getlista(self):
        return self.listproduto
        
    def adcProduto(self, produto):
        self.listproduto.append(produto)
        return self.listproduto
    
    def removProduto(self, codProduto):
        for pro in self.listproduto:
            if codProduto == pro.getcodigo():
                self.listproduto.remove(pro)
                break  # Evita remover múltiplas instâncias se houver duplicatas

    def precoTotal(self):
        preco_total = 0
        for produto in self.listproduto:
            preco_total += produto.getpreco()
        return preco_total

# Testes
p1 = Produto('12345', 12)
print(p1.getpreco())  # Saída: 12
print(p1.getcodigo())  # Saída: 12345
print(p1.setcodigo('9108'))  # Saída: 9108
print(Produto.qtdProd)  # Saída: 1 (contagem de produtos)

p2 = Produto('12353', 10)
print(Produto.qtdProd)  # Saída: 2 (contagem de produtos)

p3 = Produto('15242', 100)
print(Produto.qtdProd)  # Saída: 3 (contagem de produtos)

gerenciador1 = Gerenciador()  # Corrigido para instanciar Gerenciador
gerenciador1.adcProduto(p1)
gerenciador1.adcProduto(p2)
gerenciador1.adcProduto(p3)

print(gerenciador1.precoTotal())  # Saída: 122 (12 + 10 + 100)
