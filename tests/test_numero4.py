from numero7_funcao import delta, raizes
from math import sqrt


def test_delta_a_3_b_7_c_4():
    assert delta(3, 7, 4) == 1


def test_delta_a_2_b_4_c_3():
    assert delta(2, 4, 3) == -8


def test_delta_a_1_b_2_c_1():
    assert delta(1, 2, 1) == 0


def test_delta_a_4_b_10_c_2():
    assert delta(4, 10, 2) == 68


def test_delta_a_5_b_8_c_5():
    assert delta(5, 8, 5) == -36


def test_duas_raizes_1_1_0():
    assert raizes(1, 1, 0) == (0, -1)


def test_duas_raizes_1_2_1():
    assert raizes(1, 2, 1) == (-1, -1)


def test_raiz_complexa():
    assert raizes(1, 1, 1) == (complex(-0.5, sqrt(3)/2), complex(-0.5, -sqrt(3)/2))
