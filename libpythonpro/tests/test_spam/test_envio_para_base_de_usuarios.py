from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renan', email='renankemiya@gmail.com'),
            Usuario(nome='Kenji', email='albertomiyashiro26@gmail.com')
        ],
        [
            Usuario(nome='Renan', email='renankemiya@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renankemiya@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renan', email='renankemiya@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'albertomiyashiro26@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'albertomiyashiro26@gmail.com',
        'renankemiya@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
