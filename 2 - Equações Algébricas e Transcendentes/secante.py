''' 
Método da Secante:
    O método da secante é uma técnica iterativa para encontrar 
raízes de funções que se assemelha ao método de Newton, mas 
em vez de usar a derivada da função, ele utiliza uma 
aproximação da derivada baseada em dois pontos anteriores.

Usa a fórmula:
x{n+1} = n{n} - (f(x{n}).(x{n} - x{n-1})/(f(x{n})-f(x{n-1})))

    O método da secante não exige a derivada da função.
    Porém, pode ser um pouco menos ficiente do que o método de
Newton em termos de convergência, pois ele usa uma aproximação
da derivada em vez do valor exato. 
'''
import numpy as np

# Função para a qual queremos encontrar a raiz
def funcao(x):
    return np.exp(x) - x**3 - 7

def secante():
    x0 = 5  # Primeiro ponto inicial
    x1 = 6  # Segundo ponto inicial
    erro = 1e-5
    fx0 = funcao(x0)  
    fx1 = funcao(x1)  
    k = 0  # Contador de iterações

    while abs(fx1) > erro: 
        k += 1 
        
        # Próximo valor usando a fórmula da secante
        x_next = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        
        # Atualiza x0 e x1 para os próximos valores
        x0 = x1
        x1 = x_next
        fx0 = funcao(x0)  
        fx1 = funcao(x1)  

    print(f'Iterações: {k}')  
    print(f'Raiz aproximada: {x1}')  
    print(f'f(x1): {fx1}')  # Valor da função em x1, deve ser próximo de 0

secante()
