import pytest
from imc import calcular_imc


def test_imc_correcto():
    assert calcular_imc(70, 1.75) == pytest.approx(22.86, 0.01)


def test_imc_caso_limite():
    assert calcular_imc(1, 1) == 1


def test_imc_error():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)