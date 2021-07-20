from numero2 import V
import pytest


def test_V0_1_a_1_z_1():
    assert V(1, 1, 1) == 0.5


def test_V0_1_a_1_z_2():
    assert V(1, 1, 2) == 0.10


def test_V0_1_a_2_z_2():
    assert V(1, 2, 2) == 0.29
