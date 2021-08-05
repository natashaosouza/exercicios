import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

GAS_CONSTANT = Q_(0.082057366080960, 'atm * l / (mol * K)')


@ureg.wraps('liter', ('mol', 'K', 'atm'))
def volume_ideal(mole_number, temperature, pressure):
    """Evaluate the volume of an ideal gas

    Parameters:
    ----------
    mole_number : pint.Quantity
    temperature : pint.Quantity
    pressure : pint.Quantity

    Return:
    -------
    pint.Quantity
    """
    return mole_number * GAS_CONSTANT.magnitude * temperature / pressure
