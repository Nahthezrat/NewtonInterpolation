import matplotlib.pyplot as plt
import math
import numpy


# Интерполяция методом Ньютона
def newton_interpolation(nodes_x, nodes_y, n, x):
    # Вычисление конечных разностей
    diff_arr = [nodes_y]
    for i in range(1, n):
        diff = []
        for j in range(n-i):
            diff.append(diff_arr[i-1][j+1] - diff_arr[i-1][j])
        diff_arr.append(diff)

    # Построение полинома Ньютона
    q = 1
    p = 0
    for i in range(n):
        p += (diff_arr[i][0]*q)/math.factorial(i)
        q *= (x-nodes_x[0])/(nodes_x[1]-nodes_x[0]) - i
    return p


# Загрузка узловых точек из файла
f = open('nodes.in')
NodesX = []
NodesY = []
for line in f:
    NodesX.append(float(line.rstrip('\n').split(' ')[0]))
    NodesY.append(float(line.rstrip('\n').split(' ')[1]))

# Вычисление значения полинома в точках интерполяции
t = 0.001  # Отступ при вычислении новой точки
InterpolationX = []
InterpolationY = []
for f in numpy.arange(NodesX[0], NodesX[-1], t):
    InterpolationX.append(f)
    InterpolationY.append(newton_interpolation(NodesX, NodesY, len(NodesX), f))

# График в matplotlib
fig = plt.figure()
# Описания к графику
plt.title('Newton-1 Interpolation')
plt.xlabel('x')
plt.ylabel('F(x)')
# Построение точечного графика
plt.scatter(NodesX, NodesY, color='red')
# Построение графика интерполяции
plt.plot(InterpolationX, InterpolationY)
# Вывод графика в IDE
plt.show()
# Сохранение в png
fig.savefig('NewtonInterpolation.png')
