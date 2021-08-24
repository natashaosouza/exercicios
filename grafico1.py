import numpy as np
import matplotlib.pyplot as plt
import pint
from scipy.stats import linregress
from helpers import plot_params


ureg = pint.UnitRegistry()
ureg.setup_matplotlib()

data_file = 'dados.csv'


class Kinetics:
    def __init__(self, data_file, time_unit='min', conc_unit='mole / litre'):
        self.data_file = data_file
        self.time = self.data_from_file['time'] * ureg(time_unit)
        self.concentration = self.data_from_file['concentration'] * ureg(conc_unit)
        self._order = None

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        if value in (0, 1, 2):
            self._order = value
        else:
            raise ValueError('Invalid order')

    @property
    def data_from_file(self):
        return np.genfromtxt(self.data_file, delimiter=',', dtype=(float, float),
                             names=['time', 'concentration'], skip_header=1)

    @property
    def regression(self):
        if self.order == 0:
            reg = linregress(self.time.magnitude, self.concentration.magnitude)
        elif self.order == 1:
            reg = linregress(self.time.magnitude, np.log(self.concentration.magnitude))
        elif self.order == 2:
            reg = linregress(self.time.magnitude, 1/(self.concentration.magnitude))
        else:
            raise ValueError('Order not defined')
        return reg

    @property
    def linear_fit(self):
        x = np.linspace(self.time[0].magnitude, self.time[-1].magnitude, 2)
        y = self.regression.slope * x + self.regression.intercept
        return x, y

    @property
    def rate_constant(self):
        return abs(self.regression.slope)

    def plot(self):
        fig, ax = plt.subplots(figsize=(8, 6))
        plot_params(ax)
        ax.plot(*self.linear_fit, color='red')
        ax.text(0.5, 0.90, f'y = {self.regression.slope:.3e}x + {self.regression.intercept:.3e}',
                fontsize=14, bbox=dict(facecolor='red', alpha=0.9), color='white',
                transform=ax.transAxes, horizontalalignment='center')
        if self.order == 0:
            ax.scatter(self.time, self.concentration)
            ax.set_xlabel(f'Time / {self.time.units:~P}', fontsize=18)
            ax.set_ylabel(f'Concentration / {self.concentration.units:~P}', fontsize=18)
        elif self.order == 1:
            ax.scatter(self.time, np.log(self.concentration.magnitude))
            ax.set_xlabel(f'Time / {self.time.units:~P}', fontsize=18)
            ax.set_ylabel(f'ln(Concentration / {self.concentration.units:~P})', fontsize=18)
        elif self.order == 2:
            ax.scatter(self.time, 1/(self.concentration.magnitude))
            ax.set_xlabel(f'Time / {self.time.units:~P}', fontsize=18)
            ax.set_ylabel(f'1/(Concentration / {self.concentration.units:~P})', fontsize=18)
        plt.show()
