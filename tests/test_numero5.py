from numero8 import perimetro
import pytest


@pytest.mark.parametrize(
    "numero_de_lados, esperado", (
        (3, 2.598),
        (4, 2.828),
        (5, 2.938),
        (100, 3.141),
    )
)
def test_perimetro(numero_de_lados, esperado):
    assert perimetro(numero_de_lados) == pytest.approx(esperado, abs=1E-3)


# def test_numero_de_lados_tres():
#     assert perimetro(3) == 2.59807621135


# def test_numero_de_lados_quatro():
#     assert perimetro(4) == 2.82842712475


# def test_numero_de_lados_cinco():
#     assert perimetro(5) == 2.93892626146


# def test_numero_de_lados_cem():
#     assert perimetro(100) == 3.14107590781
