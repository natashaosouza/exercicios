import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

GAS_CONSTANT = Q_(0.082057366080960, 'atm * l / (mol * K)')


@ureg.wraps('liter', ('mol', 'K', 'atm'), strict=False)
def volume_molar(mole_number, temperature, pressure):
    """ Calcula o volume molar de um gás ideal

    Parâmetros:
    ----------
    numero de mol
    constante dos gases
    temperatura
    pressão

    Saída:
    -----
    volume molar
    """
    return mole_number * GAS_CONSTANT.magnitude * temperature / pressure
