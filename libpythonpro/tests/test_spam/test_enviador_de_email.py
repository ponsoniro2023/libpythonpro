from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.enviador_de_email import EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None



@pytest.mark.parametrize(
    'remetente',
    ['rogerio.ponsoni@protectme.com.br', 'mguisolberto@gmail.com']
)
def test_remetente(remetente):
    enviador=Enviador()

    resultado = enviador.enviar(
        remetente,
        'rogerio.ponsoni@gmail.com,',
        'Primeiro teste enviador de email',
        'teste enviador'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'mguisolberto']
)
def test_remetente(remetente):
    enviador=Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'rogerio.ponsoni@gmail.com,',
            'Primeiro teste enviador de email',
            'teste enviador'
        )



