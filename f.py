from chi2 import chi2
import numpy as np
from matplotlib import pyplot as plt

def f_n(a,n):
    """
    Calcula la funcion f(a), es decir, la integral de chi^2 entre 0 y a, para n intervalos, usando la regla de Simpson

    Params:
        :param a: el limite superior de la integral
        :param n: la cantidad de intervalos

    :return: el valor de la integral de chi^2 entre 0 y a calculado con n intervalos
    """
    delta_x = a/n
    s = 0
    s += chi2(0) 
    for i in range(1, n-1):
        chi2i = chi2(2*i*delta_x, z)
        s +=2*chi2i
    for i in range(1, n-1):
        chi2i1 = chi2((2*i + 1)*delta_x, z)
        s +=4*chi2i1
    s +=chi2(1, z)
    return s*(delta_x/3)