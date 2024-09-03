class Veiculo: 
    def __init__(self):

        pass
    def mover(self):
        return f"O carro esta andando"
    
class Carro(Veiculo):
    def mover(self):
        return "o carro esta andando"
    
c1 = Carro()
print(c1.mover())


    

