from f import f_95
from chi2 import chi2
from matplotlib import pyplot as plt

print("uwus")

def cero(f, df, x0, tol):
    """
    busca un 0 de la funcion f con derivada df usando el algoritmo de Newton,
    con tolerancia tol, partiendo desde x_0

    Params:
        :param f: la funcion a evaluar
        :param df: la derivada de la funcion f
        :param x0: la aproximacion inicial del 0 de f
        :param tol: la tolerancia con la que se quiere buscar el 0

    :return: el valor de a tal que |f(a)|< tol
    """
    x_i=x0
    c=1
    f_ans=f(x_i, 0.00001)
    while abs(f_ans)>=tol:
        x_i = x_i - (f(x_i, 0.00001)/df(x_i))
        c +=1
        f_ans=f(x_i, 0.00001)
    return (x_i, c, f_ans)


#arreglos para ir guardando los resultados
val_a = [] #valores de a
iters = [] #cantidad de iteraciones
val_f = [] #valor de f(a)

a = cero(f_95, chi2, 4, 10**(0))
val_a.append(a[0])
iters.append(a[1])
val_f.append(a[2])

for i in range(1, 5):
    a = cero(f_95, chi2, val_a[i-1], 10**(-i)) #se calcula para el valor obtenido anteriormente de a para mayor rapidez

    #se agregan los nuevos valores a los respectivos arreglos
    val_a.append(a[0])
    iters.append(a[1]+iters[i-1]) #se suman las iteraciones para el valor obtenido de a, ya que se está reutilizando el cálculo
    val_f.append(a[2])
    print(i)

#prints:
print(val_a)
print(iters)
print(val_f)

#grafico de precision vs iteraciones
plt.clf()
f, ax = plt.subplots()
plt.plot(range(5), iters, 'ro')
plt.xlabel("precision", fontsize=16)
plt.ylabel("cantidad de iteraciones", fontsize=16)
ax.set_xticks(range(5))
ax.set_xticklabels(["1", "$10^{-1}$", "$10^{-2}$", "$10^{-3}$", "$10^{-4}$", "$10^{-5}$"])

plt.show()
