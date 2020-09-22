from matplotlib import pyplot as plt
import numpy as np

def g_gamma(x,z):
    """
    Calcula la función que se integra de 0 a infty al calcular la funcion Gamma(z)
    
    Params:
        z: el valor para el que se quiere evaluar Gamma(z)
        x: el valor sobre el que se integra (es decir, la integral es en dx)
    """
    return (x**(z-1)) * np.exp(-x)

def g(u,z):
    """
    Calcula la funcion que se integra de 0 a 1 al calcular la funcion Gamma(z) con el c.v. u=1/(x+1)

    Params:
        z: el valor para el que se quiere evaluar Gamma(z)
        u: el valor sobre el que se integra (es decir, la integral es en du)
    """
    return ((1/u) - 1)**(z-1) * np.exp(1 - (1/u)) * 1/(u**2)

k = 4.551
z = k/2
x = np.linspace(0, 70, num=200)
u = np.linspace(0, 1, num=200)

plt.clf()

plt.figure(1)
plt.plot(x, g_gamma(x,z))
plt.xlabel('x')
plt.ylabel('$g_{\Gamma}(x,z)$')
plt.title("$g_{\Gamma}(x,z)$ con $z=k/2$ fijo y $x \in [0, 70]$")

plt.figure(2)
plt.plot(u, g(u,z))
plt.xlabel('u')
plt.ylabel('$g(u,z)$')
plt.title("$g(u,z)$ con $z=k/2$ fijo y $u \in [0,1]$")

plt.show()