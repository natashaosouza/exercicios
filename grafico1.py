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
ax.plot(x, y)
ax.scatter(time, concentration)

plt.show()
