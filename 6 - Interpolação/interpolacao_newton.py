'''Interpolação diferenças divididas de Newton'''

def dif_newton():
    # Entradas
    x = [0, 1, 2, 3]
    y = [-3, -2, 4, 0]
    n = len(x)

    # Criar matriz nxn para obter os resultados
    a = [[0] * n for _ in range(n)]

    # Define a primeira coluna como os valores de y
    for i in range(n):
        a[i][0] = y[i]

    for j in range(1,n):
        for i in range(j, n):
            # a[i, j] = (a[i, j - 1] - a[i - 1, j - 1]) / (x[i] - x[i - j])
            a[i][j] = (a[i][j - 1] - a[i - 1][j - 1]) / (x[i] - x[i - j])

    print("Matriz de diferenças divididas (a):")
    print(a)

    # valor interpolado em um ponto específico xx
    # Uso do gráfico
    xx = 1.5
    px = poli(x, n, a, xx)
    print(px)

def poli(x, n, a, xx):
    p = 0
    for i in range(n):
        m = 1
        for j in range(i):
            m *= (xx - x[j])
        p += a[i][i] * m
    return p

dif_newton()