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

    @property
    def data_from_file(self):
        return np.genfromtxt(self.data_file, delimiter=',', dtype=(float, float),
                             names=['time', 'concentration'], skip_header=1)

    def regression(self, order):
        if order == 0:
            reg = linregress(self.time.magnitude, self.concentration.magnitude)
        elif order == 1:
            reg = linregress(self.time.magnitude, np.log(self.concentration.magnitude))
        elif order == 2:
            reg = linregress(self.time.magnitude, 1/(self.concentration.magnitude))
        else:
            raise ValueError('Invalid order')
        return reg

    def linear_fit(self, order):
        x = np.linspace(self.time[0].magnitude, self.time[-1].magnitude, 2)
        y = self.regression(order).slope * x + self.regression(order).intercept
        return x, y

    def plot(self, order):
        fig, ax = plt.subplots(figsize=(8, 6))
        plot_params(ax)
        if order == 0:
            ax.plot(*self.linear_fit(0), color='red')
            ax.scatter(self.time, self.concentration)
            ax.text(0.5, 0.90, f'y = {self.regression(0).slope:.3e}x + {self.regression(0).intercept:.3e}',
                    fontsize=14, bbox=dict(facecolor='red', alpha=0.9), color='white',
                    transform=ax.transAxes, horizontalalignment='center')
            ax.set_xlabel(f'Time / {self.time.units:~P}', fontsize=18)
            ax.set_ylabel(f'Concentration / {self.concentration.units:~P}', fontsize=18)
        elif order == 1:
            ax.plot(*self.linear_fit(1), color='red')
            ax.scatter(self.time, np.log(self.concentration.magnitude))
            ax.text(0.5, 0.90, f'y = {self.regression(1).slope:.3e}x + {self.regression(1).intercept:.3e}',
                    fontsize=14, bbox=dict(facecolor='red', alpha=0.9), color='white',
                    transform=ax.transAxes, horizontalalignment='center')
            ax.set_xlabel(f'Time / {self.time.units:~P}', fontsize=18)
            ax.set_ylabel(f'ln(Concentration / {self.concentration.units:~P})', fontsize=18)
        elif order == 2:
            ax.plot(*self.linear_fit(2), color='red')
            ax.scatter(self.time, 1/(self.concentration.magnitude))
            ax.text(0.5, 0.90, f'y = {self.regression(2).slope:.3e}x + {self.regression(2).intercept:.3e}',
                    fontsize=14, bbox=dict(facecolor='red', alpha=0.9), color='white',
                    transform=ax.transAxes, horizontalalignment='center')
            ax.set_xlabel(f'Time / {self.time.units:~P}', fontsize=18)
            ax.set_ylabel(f'1/(Concentration / {self.concentration.units:~P})', fontsize=18)
        plt.show()
