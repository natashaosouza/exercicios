from numero9 import volume_ideal, Q_
import numpy as np


def test_volume_molar_1():
    mole_number = Q_(2, 'mol')
    temperature = Q_(300, 'K')
    pressure = Q_(5, 'atm')
    resposta_esperada = Q_(9.84, 'liter')
    assert np.isclose(volume_ideal(mole_number, temperature, pressure), resposta_esperada, atol=0.01)


def test_volume_molar_2():
    mole_number = Q_(1, 'mol')
    temperature = Q_(273, 'K')
    pressure = Q_(1, 'atm')
    resposta_esperada = Q_(22.40, 'liter')
    assert np.isclose(volume_ideal(mole_number, temperature, pressure), resposta_esperada, atol=0.01)


def test_volume_molar_3():
    mole_number = Q_(3, 'mol')
    temperature = Q_(373, 'K')
    pressure = Q_(2, 'atm')
    resposta_esperada = Q_(45.91, 'liter')
    assert np.isclose(volume_ideal(mole_number, temperature, pressure), resposta_esperada, atol=0.01)
