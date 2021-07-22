from numero1 import altura, velocidade
import pytest


@pytest.mark.parametrize(
    "altura_inicial, velocidade_inicial, tempo, esperado", (
        (0, 0, 1, -4.9),
        (0, 1, 1, -3.9),
        (1, 0, 2, -18.6),
    )
)
def test_altura(altura_inicial, velocidade_inicial, tempo, esperado):
    assert altura(altura_inicial, velocidade_inicial, tempo) == pytest.approx(esperado, abs=1E-3)


@pytest.mark.parametrize(
    "argumentos, esperado", (
        ((0, 1), -9.8),
        ((1, 2), -18.6),
        ((10, 1), 0.2),
    )
)
def test_velocidade(argumentos, esperado):
    assert velocidade(*argumentos) == pytest.approx(esperado, abs=1E-3)
