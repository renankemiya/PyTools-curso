from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renan', email='renankemiya@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Renan', email='renankemiya@gmail.com'),
                Usuario(nome='Kenji', email='renankemiya@gmail.com')
                ]
    sessao.roll_back()
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
