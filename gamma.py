from funciones_gamma import g
import numpy as np
from matplotlib import pyplot as plt
import sys
import math

eps = sys.float_info.epsilon #el numero mas pequeno que es mayor a 0, para usarlo en vez de 0 al dividir

def gamma_n(z,n):
    """
    Calcula la funcion Gamma(z) para n intervalos, usando la regla de Simpson
    Se integra considerando el cambio de variable u = 1/(1+x) para integrar entre 0 y 1

    Params:
        :param z: el valor para el que se quiere calcular Gamma
        :param n: la cantidad de intervalos

    :return: el valor de Gamma(z) calculado con n intervalos
    """
    delta_x = 1.0/n
    s = 0
    s += g(eps,z) #se hace desde eps en vez de 0 directamente para evitar error de divide by zero
    #De todas formas la funcion era bastante plana en esa parte, por lo que la diferencia es pequena
    for i in range(1, n-1):
        g2i = g(2*i*delta_x, z)
        s +=2*g2i
    for i in range(1, n-1):
        g2i1 = g((2*i + 1)*delta_x, z)
        s +=4*g2i1
    s +=g(1, z)
    return s*(delta_x/3)

def gamma(z, tol):
    """
    Calcula la funcion Gamma(z) para una cierta tolerancia, usando la regla de Simpson y la funcion gamma_n para cada iteracion
    Se integra considerando el cambio de variable u = 1/(1+x) para no tener integrales infinitas

    Params:
        :param z: el valor para el que se quiere calcular Gamma
        :param tol: la precision relativa deseada
    """
    n=8
    Gn = gamma_n(z,n)
    G2n = gamma_n(z, 2*n)

    while abs((G2n - Gn)/Gn) >= tol:
        n *=2
        Gn = G2n
        G2n = gamma_n(z, 2*n)
    
    return G2n

#z = np.linspace(0, 12, num=100)
#z_int = np.arange(13)

#muestra los primeros 12 factoriales y gamma para esos numeros, y la diferencia entre ambos
#for i in range(1,13):
 #   gam=gamma(i, 0.00000005)
 #   fact=math.factorial(i-1)
 #   print("gamma("+str(i)+"): ")
 #   print(gam)
 #   print("("+str(i)+"-1)! :")
 #   print(fact)
 #   print("Diferencia:" + str(abs(gam-fact)))
 #   print(" ")