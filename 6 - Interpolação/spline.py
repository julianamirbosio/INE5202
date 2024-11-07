'''Não vai cair :P'''

import matplotlib.pyplot as plt

# Função principal que realiza a interpolação de Lagrange e exibe o gráfico
def lagrange_interpolation():
    # Dados de entrada
    x = [-1, 0, 1]
    y = [4, 1, -1]
    n = len(x)

    # Configuração do gráfico
    h = (max(x) - min(x)) / 10  # Divide pelo número de intervalos
    x1 = [min(x) + i * h for i in range(11)]  # Pontos para o gráfico

    # Calcula o valor de interpolação para um ponto específico
    xx = 0.5
    px = lagrange(x, y, n, xx)

    # Calcula a interpolação para os pontos no intervalo x1
    p1 = [lagrange(x, y, n, xi) for xi in x1]

    # Gráficos dos pontos e da interpolação
    plt.plot(x, y, 'o', label='Pontos Originais')
    plt.plot(x1, p1, label='Interpolação de Lagrange')
    plt.plot(xx, px, 'go', label=f'Ponto xx = {xx}')
    plt.grid(True)
    plt.legend()
    plt.show()

# Função que calcula a interpolação de Lagrange para um ponto xx
def lagrange(x, y, n, xx):
    p = 0
    for i in range(n):
        num = 1
        den = 1
        for j in range(n):
            if j != i:
                num *= (xx - x[j])
                den *= (x[i] - x[j])
        L = num / den
        p += y[i] * L
    return p

# Executa a função de interpolação
lagrange_interpolation()
