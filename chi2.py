from gamma import gamma
import numpy as np
from matplotlib import pyplot as plt

k = 4.551
gam = gamma(k/2, 0.0000001)

def chi2(x):
    """
    Calcula la funcion Chi^2 usando la funcion gamma calculada arriba y k=4.551

    Params:
        :param x: el valor para el que se calculara chi
    """
    denom = 2**(k/2) * gam
    return x**((k/2-1)) * np.exp(-x/2) * (1/denom)


#x=np.linspace(0,25, 100)
#plt.plot(x, chi2(x))
#plt.xlabel("x", fontsize=16)
#plt.ylabel("$\chi ^2(x)$", fontsize=16)
#plt.show()