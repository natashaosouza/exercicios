import numpy as np
import matplotlib.pyplot as plt
import pint
from scipy.stats import linregress
from helpers import plot_params


ureg = pint.UnitRegistry()
ureg.setup_matplotlib()


def _data_from_file(data_file):
    return np.genfromtxt((data_file), delimiter=',', dtype=(float, float), names=['tempo / min', 'conc / mol/l'], skip_header=1)


class grafico_1:

 def __init__(self, tempo, concentraçao, data_file):
    self.tempo = tempo
    self.concentraçao = concentraçao
    self.data = self._data_from_file(data_file)


@property
def tempo(self):
    return self.tempo['tempo / min'] * ureg('min')


@property
def concentraçao(self):
    return self.concentraçao['conc / mol/l'] * ureg('mol/l')


@property
def regression(self):
    tempo_por_concentraçao = self.tempo / self.concentraçao
    return linregress(self.concentraçao.magnitude, tempo_por_concentraçao.magnitude)


def plot(self):
    fig, ax = plt.subplots(figsize=(8, 6), nrows=1, ncols=1, tight_layout=True)
    plot_params(ax)
