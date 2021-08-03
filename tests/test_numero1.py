from numero1 import altura, velocidade
from numero1 import ureg
import pytest

Q_ = ureg.Quantity


@pytest.mark.parametrize(
    "altura_inicial, velocidade_inicial, tempo, esperado", (
        (0, 0, 1, -4.9),
        (0, 1, 1, -3.9),
        (1, 0, 2, -18.6),
    )
)
def test_altura_strict_false(altura_inicial, velocidade_inicial, tempo, esperado):
    resultado = altura(altura_inicial, velocidade_inicial, tempo)
    assert resultado.magnitude == pytest.approx(esperado, abs=1E-3)
    assert resultado.units == 'meter'


def test_altura_unidades_de_entrada():
    altura_inicial = Q_('100 cm')
    velocidade_inicial = Q_('0 cm / s')
    tempo = Q_('2 s')
    resultado = altura(altura_inicial, velocidade_inicial, tempo)
    assert resultado.magnitude == pytest.approx(-18.6, abs=1E-3)
    assert resultado.units == 'meter'


@pytest.mark.parametrize(
    "argumentos, esperado", (
        ((0, 1), -9.8),
        ((1, 2), -18.6),
        ((10, 1), 0.2),
    )
)
def test_velocidade(argumentos, esperado):
    assert velocidade(*argumentos) == pytest.approx(esperado, abs=1E-3)
