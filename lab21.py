# Лабораторная работа № 2.1
# Морозов-Леонов О.С., ІО-71
# №  n w    N
# 17 8 1200 1024

# Додаткове завдання: вивести час обчислень DFT для різних N

import random as r
import math
import matplotlib.pyplot as plt
import datetime

n = 17
w_max = 1200
N = 1024  # Початкове значення N - 1024. Для виконання додаткового завдання N змінюється від 64 до 10240 з кроком 64

w_real = [[math.cos(2 * math.pi * i * j / N) for j in range(N)] for i in range(N)]
w_imag = [[math.sin(2 * math.pi * i * j / N) for j in range(N)] for i in range(N)]


def graph(N):
    x = [0] * N

    for i in range(n):
        A = r.randrange(2)
        W = r.randrange(w_max)
        f = r.randrange(1e9)
        for t in range(N):
            x[t] += A * math.sin(W * t + f)
    return x


def dft(x: list):
    N = len(x)
    dftt = [[sum(w_real[p][k] * x[k] for k in range(N)), sum(w_imag[p][k] * x[k] for k in range(N))] for p in range(N)]
    return dftt


def timings(N_min, N_max, N_step):
    arg_data = [arg for arg in range(N_min, N_max+1, N_step)]
    X = graph(N)
    y_data = []
    for arg in arg_data:
        dt = datetime.datetime.now()
        dft(X[:arg])
        dt = datetime.datetime.now() - dt
        y_data.append(dt.seconds * 1e6 + dt.total_seconds())
    return arg_data, y_data


x_data, y_data = timings(64, 1024, 64)
#print(x_data)
#print(y_data)

plt.plot(x_data, y_data)
plt.show()
exit(0)


X = graph(N)
dftt = dft(X)
data_x = []
data_dft = []
for i in range(len(X)):
    data_x.append(X[i])
    a = math.sqrt(dftt[i][0] ** 2 + dftt[i][1] ** 2)
    data_dft.append(a)
plt.plot([i for i in range(len(data_x))], data_x)
plt.show()
plt.plot([i for i in range(len(data_dft))], data_dft)
plt.show()