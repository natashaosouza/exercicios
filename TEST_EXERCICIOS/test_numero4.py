from numero7_funcao import delta
import pytest


def test_delta_a_3_b_7_c_4():
    assert delta(3, 7, 4) == 1


def test_delta_a_2_b_4_c_3():
    assert delta(2, 4, 3) == -8


def test_delta_a_1_b_2_c_1():
    assert delta(1, 2, 1) == 0


def test_delta_a_4_b_10_c_2():
    assert delta(4, 10, 2) == 68

