import matplotlib.pyplot as plt
import numpy as np


width, height = 100, 100
density = np.zeros((width, height))
density[50, 60] = 1.0
density[40, 40] = 1.0
density[50, 10] = 1.0

def diffuse(density, diffusion_rate, dt):
    for _ in range(100):
        density[1:-1, 1:-1] = (density[1:-1, 1:-1] +
                               diffusion_rate * (density[:-2, 1:-1] +
                                                 density[2:, 1:-1] +
                                                 density[1:-1, :-2] +
                                                 density[1:-1, 2:] -
                                                 4 * density[1:-1, 1:-1])) * dt


diffusion_rate = 0.1
dt = 0.01

diffuse(density, diffusion_rate, dt)
plt.imshow(density, cmap='viridis', vmin=0.0, vmax=1.0)
plt.colorbar()
plt.show()