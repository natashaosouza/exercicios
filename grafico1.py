import numpy as np
import matplotlib.pyplot as plt
import pint
from scipy.stats import linregress
from helpers import plot_params


ureg = pint.UnitRegistry()
ureg.setup_matplotlib()

data_file = 'dados.csv'

data = np.genfromtxt(data_file, delimiter=',', dtype=(float, float),
                     names=['time', 'concentration'], skip_header=1)

time = data['time'] * ureg('min')
concentration = data['concentration'] * ureg('mole / litre')

# zero order
regression_zero_order = linregress(time.magnitude, concentration.magnitude)
x = np.linspace(time[0].magnitude, time[-1].magnitude, 2)
y = regression_zero_order.slope * x + regression_zero_order.intercept

fig, ax = plt.subplots(figsize=(8, 6))
plot_params(ax)
ax.plot(x, y, color='red')
ax.scatter(time, concentration)
ax.text(7.75, 0.90, f'y = {regression_zero_order.slope:.3e}x + {regression_zero_order.intercept:.3e}',
        fontsize=14, bbox=dict(facecolor='red', alpha=0.9), color='white')
ax.set_xlabel(f'Time / {time.units:~P}', fontsize=18)
ax.set_ylabel(f'Concentration / {concentration.units:~P}', fontsize=18)

# first order
regression_first_order = linregress(time.magnitude, np.log(concentration.magnitude))
x = np.linspace(time[0].magnitude, time[-1].magnitude, 2)
y = regression_first_order.slope * x + regression_first_order.intercept

fig, ax = plt.subplots(figsize=(8, 6))
plot_params(ax)
ax.plot(x, y, color='red')
ax.scatter(time, np.log(concentration.magnitude))
ax.text(7.75, 0.00, f'y = {regression_first_order.slope:.3e}x + {regression_first_order.intercept:.3e}',
        fontsize=14, bbox=dict(facecolor='red', alpha=0.9), color='white')
ax.set_xlabel(f'Time / {time.units:~P}', fontsize=18)
ax.set_ylabel(f'ln(Concentration / {concentration.units:~P})', fontsize=18)

plt.show()
