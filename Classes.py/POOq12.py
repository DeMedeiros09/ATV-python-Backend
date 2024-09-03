class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f'"{self.titulo}" por {self.autor}'

class Aluno:
    def __init__(self, nome = None, livros_emprestados = None):
        self.nome = nome
        if livros_emprestados == None:
            self.livros_emprestados = []
        else:
            self.livros_emprestados = livros_emprestados
    
    def emprestar_livro(self, livro):
        self.livro = livro
        self.livros_emprestados.append(self.livro)
    
    def lista_livros(self):
        return [livro.titulo for livro in self.livros_emprestados]

class Biblioteca:
    def __init__(self, alunos = None):
        if alunos == None:
            self.alunos = []
        else:
            self.alunos = alunos
    
    def registrar_aluno(self, aluno):
        self.aluno = aluno
        self.alunos.append(self.aluno)
    
    def exibir_alunos(self):
        return [aluno.nome for aluno in self.alunos]
    
livro1 = Livro('Biblia', 'Deus')
livro2 = Livro('flores', 'Vladimir P')
livro3 = Livro('hause', 'Jack G')



aluno1 = Aluno('Misael')
aluno2 = Aluno('Ingridy')
aluno3 = Aluno('Medeiros')

aluno1.emprestar_livro(livro3)
aluno2.emprestar_livro(livro2)
aluno3.emprestar_livro(livro1)

print(aluno1.lista_livros())


biblioteca1 = Biblioteca()
biblioteca1.registrar_aluno(aluno1)
biblioteca1.registrar_aluno(aluno2)
biblioteca1.registrar_aluno(aluno3)

print(biblioteca1.exibir_alunos())