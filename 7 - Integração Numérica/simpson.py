# Definindo os parâmetros
a = 0
b = 1
n = 4
h = (b - a) / n

# Calculando os valores de x e y
x = [a + i * h for i in range(n + 1)]
y = [(xi**2 + 1) for xi in x]  # Usando a aproximação de e para exp(x)

# Aplicando o método do Trapézio
s = 0
for i in range(1, n):
    s += y[i]

T = (h / 2) * (y[0] + 2*s + y[n])  # Fórmula do Trapézio

# Simpson
s2 = 0
s4 = 0
for i in range (0, n/2):
    s2 = s2 + y[2*i]
    s4 = s4 + y[2*i + 1]
s2 = s2 + y[n]
S = (h/3)*(y[0] + 4*s2 + 2*s4 + y[n])

# Exibindo o resultado
print("Valor da integral aproximada (Método do Trapézio):", T)
print("Valor da integral aproximada (Método do Simpson):", S)
