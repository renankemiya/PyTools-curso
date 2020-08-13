from time import sleep


class Sessao:
    contador = 0
    usuarios = []

    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def listar(self):
        return self.usuarios

    def roll_back(self):
        self.usuarios = []
        self.contador = 0

    def fechar(self):
        pass


class Conexao:

    def __init__(self):
        sleep(1)

    @staticmethod
    def gerar_sessao():
        return Sessao()

    def fechar(self):
        pass
