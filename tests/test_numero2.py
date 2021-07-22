from numero2 import V
import pytest


@pytest.mark.parametrize(
    "V0, a, z, esperado", (
        (1, 1, 1, 0.292),
        (1, 1, 2, 0.105),
        (1, 2, 2, 0.292),
    )
)
def test_V(V0, a, z, esperado):
    assert V(V0, a, z) == pytest.approx(esperado, abs=1E-3)
