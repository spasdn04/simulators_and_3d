import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

"""
def f(x, y):
    return np.sin(x) ** 2 + np.cos(5 + x * y) + 2 * np.cos(x)
    
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
dist_color = f(X, Y) + f(X, Y) * 0.7
dist_model = 0.6 * f(X, Y) -0.1 * f(X, Y)

matrix = np.outer(dist_color, dist_model)
# Contour

cs = plt.contourf(X, Y, Z, cmap='binary_r')
plt.contour(X, Y, Z, cmap='binary_r')
plt.show()
plt.imsave("funcion_1.png", matrix, cmap='binary_r', origin='lower', dpi=300)
"""

"""
def f(x, y):
    
    return np.log(np.sqrt(np.power(x, 2) + np.power(y, 2)))
x = np.linspace(-100, 5, 100)
y = np.linspace(-100, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
print(Z)
c = plt.contourf(X, Y, Z, levels=15, cmap='binary_r')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axis(False)
plt.savefig('funcion 2.png', dpi=300)
#plt.contour(X, Y, Z, cmap='binary_r')
plt.show()

#plt.imsave("funcion_2.png", cs, cmap='binary_r', origin='lower', dpi=300)
# """

"""
# Crear datos para los ejes x e y
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
x, y = np.meshgrid(x, y)

# Calcular los valores de la función
z = np.log(np.sqrt(np.power(x, 2) + np.power(y, 2)))

# Crear la figura y los ejes
fig = plt.figure()
ax = fig.add_subplot(111)

# Graficar la función
c = ax.contourf(x, y, z, levels=20, cmap='viridis')
plt.colorbar(c)

# Ajustar los límites de los ejes para mostrar todos los cuadrantes
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Mostrar la gráfica
plt.show()
"""

"""
ax = plt.axes(projection='3d')

x_data = np.arange(-10, 10, 0.1)
y_data = np.arange(-10, 10, 0.1)

X, Y = np.meshgrid(x_data, y_data)
Z = np.sin(X) + np.cos(Y)
matrix = np.outer()

ax.plot_surface(X, Y, Z, cmap='binary')
ax.view_init(azim=0, elev=90)
plt.savefig('funcion 3.png', dpi=300)
plt.show()"""

X, Y = np.meshgrid(np.linspace(-2, 2, 100),
                   np.linspace(-2, 2, 100))
Z = np.exp(- np.power(X, 2) - np.power(Y, 2)) * X

x, y = np.linspace(-2, 2, 100), np.linspace(-2, 2, 100)
z1 = 
matrix = np.outer(Z, Z)

# Contour relleno con etiquetas
fig, ax = plt.subplots()
ax.contourf(X, Y, Z, levels=50, cmap='binary')
plt.show()
print(matrix)
plt.imsave('funcion 4.png', matrix, cmap='binary_r', origin='lower',dpi=300)