''' 
Método de Newton:
    O método é rápido quando a função tem boas propriedades, 
mas pode falhar ou convergir lentamente se a derivada for 
muito pequena ou inexistente em algum ponto.

Usa a fórmula:
            x{n+1} = n{n} - (f(x{n})/f'(x{n}))
'''

import numpy as np

# Função para a qual queremos encontrar a raiz
def f(x):
    return np.exp(x) - x**3 - 7

# Derivada da função
def derivada(x):
    return np.exp(x) + (-3)*(x**2)

def newton():
    x0 = 4.5  # Ponto inicial para a aproximação
    erro = 1e-5 # 10**(-10)
    fx = f(x0) 
    k = 0  # Contador de iterações

    while abs(fx) > erro:  
        k += 1  # Incrementa o contador de iterações
        dx = derivada(x0)  
        x0 = x0 - (fx / dx)  
        fx = f(x0) 

    # Exibe os resultados finais
    print(f'Iterações: {k}') 
    print(f'Raiz aproximada: {x0}') 
    print(f'f(x0): {fx}')  # Valor da função em x0, deve ser próximo de 0

newton()