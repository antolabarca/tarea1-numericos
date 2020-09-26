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


def f_95(a, tol):
    """
    Calcula el valor de f(a,tol)-0.95 para poder utilizar un algoritmo que busque 0s de una funcion y encontrar
    el valor de a que hace que f(a,tol)=0.95

    Params:
        :param a: el valor de a para el que se quiere calcular f, es decir, el lim superior de la integral
        :param tol: la tolerancia relativa deseada

    """
    return f(a,tol) - 0.95

a = np.linspace(0,30,50)
b = np.array([f_95(ai, 0.000001) for ai in a])

plt.clf()
plt.plot(a, b, label="f(a)")
plt.xlabel("x", fontsize=16)
plt.ylabel("$f_{0.95}(a)$", fontsize=16)
plt.axhline(0,color='g', label="y=0")
plt.legend(loc="lower right")
plt.show()