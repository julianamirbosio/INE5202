import numpy as np
import matplotlib.pyplot as plt

# Dados conhecidos
x = [-1, 0, 1]
y = [4, 1, -1]
n = len(x)

# Criar a matriz a
a = np.zeros((n, n))  # Matriz de coeficientes

for i in range(n):
    for j in range(n):
        a[i][j] = x[i]**(j)

# Resolver o sistema linear para encontrar os coeficientes
c = np.linalg.solve(a, y)

# Função para calcular o polinômio interpolador
def polinomio(xx, c):
    px = 0
    for i in range(len(c)):
        px += c[i] * (xx ** i)
    return px

# Valores para plotar o gráfico
x1 = np.linspace(min(x), max(x), 100)  # Intervalo para o gráfico
y1 = [polinomio(xx, c) for xx in x1]   # Valores do polinômio

# Plotar os pontos conhecidos e o polinômio interpolado
plt.plot(x1, y1, label="Polinômio Interpolado")
plt.scatter(x, y, color='red', label="Pontos Conhecidos")
plt.grid(True)
plt.legend()
plt.show()

# Calcular o valor interpolado em um ponto específico
xx = 0.5
px = polinomio(xx, c)
print(f"Valor interpolado em x = {xx}: {px}")
