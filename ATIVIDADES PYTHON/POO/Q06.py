class Aluno():
    contador = 0
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        Aluno.contador +=1

class Equipe():
    def __init__(self, listaAluno, projeto):
        self.listaAluno = listaAluno
        self.projeto = projeto

class GerenciadorEquipes():
    def __init__(self, listaEquipe,):
        self.listaEquipe = listaEquipe

    def criarEquipe(self):
        return self.listaEquipe.listaAluno

a1 = Aluno('misael', 70324746407)
a2 = Aluno('ingridy', 90009090009)
eq1 = Equipe([a1],'python')

print(Aluno.contador)


