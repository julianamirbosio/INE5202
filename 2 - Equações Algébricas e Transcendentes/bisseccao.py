import math
import numpy as np

# Definir um intervalo [a,b] e um erro e
a = 4
b = 5
e = 10**(-5)

# Definir uma função
def f(x):
    return np.exp(x) - x**3 - 7

# Teorema de Bolzano
#   Testamos se a raiz existe dentro do intervalo
iteracoes = 0
if f(a)*f(b) < 0:
    while (math.fabs(b-a)/2 > e):  # |b-a| > erro
        xi = (a+b)/2
        iteracoes += 1
        if f(xi) == 0:
            print("A raíz é:" ,xi)
            break
        else:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi
    print("Valor da raíz é: ", xi)
else:
    print("Não há raízes neste intervalo!")
print(iteracoes)
print(f(xi))