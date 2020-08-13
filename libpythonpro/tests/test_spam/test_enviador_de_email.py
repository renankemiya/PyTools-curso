import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'renankemiya@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()

    resultado = enviador.enviar(
        remetente,
        'albertomiyashiro26@gmail.com',
        'Cursos Python Pro',
        'Testando o código.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'renankemiya']
)
def test_remetente(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'albertomiyashiro26@gmail.com',
            'Cursos Python Pro',
            'Testando o código.'
        )
    return resultado
