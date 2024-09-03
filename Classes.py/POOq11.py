class Prato:
    def __init__(self, nome: str):
        self.nome = nome

    def exibir(self):
        return f"o prato '{self.nome}' esta sendo servido"

class Pedido():
    def __init__(self, itens = None, prato = None):
        self.prato = prato
        if itens == None:
            self.itens = []
        else:
            self.itens = itens

    def add_prato(self):
        if self.prato:
            self.itens.append(self.prato.nome)
    
    def list_pedido(self):
        return self.itens
    
class Restaurante:
    def __init__(self, listPedidos = None, pedido = None):
        self.pedido = pedido
        if listPedidos == None:
            self.listPedidos =[]
        else:
            self.listPedidos = listPedidos

    def fazer_pedido(self):
        self.listPedidos.append(self.pedido)
    
    def exibir_pedidos(self):
        return [pedido.list_pedido() for pedido in self.listPedidos]
    
p1 = Prato('strogonof')
p2 = Prato('macarrão')
p3 = Prato('torta de chocolate')

ped1 = Pedido()

ped2 = Pedido()

ped2.prato = p2
ped2.add_prato()
ped2.prato = p3
ped2.add_prato()

ped1.prato = p1
ped1.add_prato()
ped1.prato = p2
ped1.add_prato()
ped1.prato = p3
ped1.add_prato()

r1 = Restaurante()

r1.pedido = ped1
r1.fazer_pedido()

r1.pedido = ped2
r1.fazer_pedido()


print(r1.exibir_pedidos())