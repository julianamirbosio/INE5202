import math

# Definir um intervalo [a,b] e um erro e
a = 2
b = 3
e = 0.01

# Definir uma função
def f(x):
    return x**2 - 5

# Teorema de Bolzano
#   Testamos se a raiz existe dentro do intervalo
if f(a)*f(b) < 0:
    while (math.fabs(b-a)/2 > e):  # |b-a| > erro
        xi = (a+b)/2
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