class Autor:
    def __init__(self, nome):
        self.nome = nome
    
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def ler(self):
        return f"O livro '{self.titulo}' do autor {self.autor.nome} esta sendo lido"

a1 = Autor('Misael')

l1 = Livro('Don Kishot',a1)
print(l1.ler())