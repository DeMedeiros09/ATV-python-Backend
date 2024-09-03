class Filme:
    def __init__(self, titulo: str):
        self.titulo = titulo

    def exibir(self):
        return f'o filme "{self.titulo}" esta sendo exibido'

class Cinema:
    def __init__(self, catalogo = None, filme = None):
        self.filme = filme
        
        if catalogo == None:
            self.catalogo = []
        else:
            self.catalogo = catalogo

    def add_filme(self):
        if self.filme:
            self.catalogo.append(self.filme.titulo)

    def listar_filmes(self):
        return self.catalogo
    
f1 = Filme('taxadas cinistras')
f2 = Filme('taxados')
f3 = Filme('taxade')

c1 = Cinema()

c1.filme = f1
c1.add_filme()

c1.filme = f2
c1.add_filme()

c1.filme = f3
c1.add_filme()

print(c1.listar_filmes())