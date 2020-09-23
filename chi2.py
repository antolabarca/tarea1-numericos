from gamma import gamma
import numpy as np
from matplotlib import pyplot as plt

k = 4.551

def chi2(x):
    """
    Calcula la funcion Chi^2 usando la funcion gamma para una tolerancia de 0.0000005 y k=4.551

    Params:
        :param x: el valor para el que se calculara chi
    """
    j = k/2
    denom = 2**j * gamma(j, 0.0000005)
    return x**((k/2-1)) * np.exp(-x/2) * (1/denom)


x=np.linspace(0,25, 100)
plt.plot(x, chi2(x))
plt.xlabel("x")
plt.ylabel("$\chi ^2(x)$")
plt.title("$\chi^2(x)$ para $x \in [0,25]$")
plt.show()