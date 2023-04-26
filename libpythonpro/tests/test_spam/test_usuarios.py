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
        pass

    def fechar(self):
        pass


class Conexao:
    def gerar_usuario(self):
        return Sessao()

    def fechar(self):
        pass

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None



def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_usuario()
    usuario = Usuario(nome="Rogerio")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_usuario()
    usuarios = [Usuario(nome="Rogerio"), Usuario(nome="Maria")]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
