from numero1 import altura, velocidade
import pytest


def test_altura_inicial_0_velocidade_inicial_0_tempo_1():
    assert altura(0, 0, 1) == -4.9


def test_altura_inicial_0_velocidade_inicial_1_tempo_1():
    assert altura(0, 1, 1) == pytest.approx(-3.9, abs=0.001)


def test_altura_inicial_1_velocidade_inicial_0_tempo_2():
    assert altura(1, 0, 2) == -18.6


def test_velocidade_inicial_0_tempo_1():
    assert velocidade(0, 1) == -9.8


def test_velocidade_inicial_1_tempo_2():
    assert velocidade(1, 2) == -18.6


def test_velocidade_inicial_10_tempo_1():
    assert velocidade(10, 1) == pytest.approx(0.2, abs=0.001)
