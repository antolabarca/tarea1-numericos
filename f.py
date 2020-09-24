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
        chi2i = chi2(2*i*delta_x)
        s +=2*chi2i
    for i in range(1, n-1):
        chi2i1 = chi2((2*i + 1)*delta_x)
        s +=4*chi2i1
    s +=chi2(a)
    return s*(delta_x/3)


def f(a, tol):
    """
    Calcula la integral de chi^2 desde 0 hasta a para una cierta tolerancia, usando la regla de Simpson
    y la funcion f_n para cada iteracion

    Params:
        :param a: el valor para el que se quiere calcular f(a), es decir, el lim superior de la integral
        :param tol: la precision relativa deseada
    """
    n=8
    fn = f_n(a,n)
    f2n = f_n(a, 2*n)

    while abs((f2n - fn)/fn) >= tol:
        n *=2
        fn = f2n
        f2n = f_n(a, 2*n)
    
    return f2n