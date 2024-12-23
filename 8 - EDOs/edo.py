import math

a = 0
b = 0.5
n = 5
h = (b-a)/n
x = [a + i * h for i in range(n + 1)]

def f(x,y):
    return -2*x - y

# --------------------- Euler ------------------------
y1 = [0 for i in range(n + 1)]
y1[0] = -1
# Calcula os valores de y pela série de Taylor
for i in range(1,n+1):
    y1[i] = y1[i-1] + h*f(x[i-1],y1[i-1])

print("Euler = ", y1)


# --------------- (RK2) Runge-Kutta ------------------
y2 = [0 for i in range(n + 1)]
y2[0] = -1
for i in range(1,n+1):
    k1 = h * f(x[i-1], y2[i-1])
    k2 = h * f(x[i-1] + h, y2[i-1] + k1)
    y2[i] = y2[i-1] + (k1 + k2)/2

print("RK2 = ", y2)

# --------------- (RK4) Runge-Kutta ------------------
y3 = [0 for i in range(n + 1)]
y3[0] = -1
for i in range(1,n+1):
    k1 = h * f(x[i-1], y3[i-1])
    k2 = h * f(x[i-1] + h/2, y3[i-1] + k1/2)
    k3 = h * f(x[i-1] + h/2, y3[i-1] + k2/2)
    k4 = h * f(x[i-1], y3[i-1] + k3)
    y3[i] = y3[i-1] + (k1 + 2*k2 + 2*k3 + k4)/2

print("RK4 = ", y3)

# --------------------- exata ----------------------
ye = [-3 * math.exp(-x[i]) - 2 * x[i] + 2 for i in range(len(x))]


# --------------------- erros ----------------------
erro1 = [abs(ye[i] - y1[i]) for i in range(len(ye))]
erro2 = [abs(ye[i] - y2[i]) for i in range(len(ye))]
erro3 = [abs(ye[i] - y3[i]) for i in range(len(ye))]

print()
print("Erros:")
print("Euler = ", erro1)
print("RK2 = ", erro2)
print("RK4 = ", erro3)