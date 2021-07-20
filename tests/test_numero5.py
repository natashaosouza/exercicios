from numero8 import perimetro


def test_numero_de_lados():
    assert perimetro(3) == 2.59807621135


def test_numero_de_lados():
    assert perimetro(4) == 2.82842712475


def test_numero_de_lados():
    assert perimetro(5) == 2.93892626146


def test_numero_de_lados():
    assert perimetro(100) == 3.14107590781
