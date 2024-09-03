class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

    def ler(self):
        return f'O livro "{self.titulo}" está sendo lido.'

class Biblioteca:

    def __init__(self, livro, biblioteca=None):
        self.livro = livro
        if biblioteca is None:
            self.biblioteca = []
        else:
            self.biblioteca = biblioteca

    def ler_livro(self):
        return self.livro.ler()

    def add_livro(self):
        self.biblioteca.append(self.livro)

    def ver_livros(self):
        return [livro.titulo for livro in self.biblioteca]

l1 = Livro("Dom Quixote")
b1 = Biblioteca(l1)
b1.add_livro()

# Verificando os livros na biblioteca
print(b1.ver_livros())  # Exibe uma lista com os títulos dos livros

# Lendo o livro
print(b1.ler_livro())
