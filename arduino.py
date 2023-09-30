import serial # Permite realizar la comunicación serial
import time # Proporciona funciones relacionadas con el tiempo
import collections # Implementa tipos de datos de contendores especializados
import matplotlib.pyplot as plt # Permite realizar gráficos
import matplotlib.animation as animation # Permite animar las gráficas
from matplotlib.lines import Line2D
import numpy as np # Permite trabajar con vectores y matrices
#---------------------------------------------

def getSerialData(self, Samples, numData, serialConnection, lines):
    # Obtenemos la lectura de cada uno de los sensores
    for i in range(numData):
        value = float(serialConnection.readline().strip())
        data[i].append(value)
        # Actualizamos la gráfica mediante nuevas líneas
        lines[i].set_data(range(Samples), data[i])
        
SerialPort = "COM9" # Puerto serial de Arduino
baudRate = 9600 # Velocidad de baudios

# Inicializamos nuestro objeto Serial con los parámetros declarados
try:
    serialConnection = serial.Serial(SerialPort, baudRate)
except:
    print("No se logró la conexión con el puerto")
    
Samples = 200 # Número de muestras
sampleTime = 100 # Tiempo de muestreo
numData = 2 # Número de sensores

# Límites de los ejes para nuestra gráfica
xmin = 0
xmax = Samples

ymin = [-50, 0]
ymax = [50, 100]
lines = []
data = []

for i in range(numData):
    # Lista donde almacenamos las lecturas de nuestro sensor
    data.append(collections.deque([0] * Samples, maxlen = Samples))
    # Empleamos líneas en 2D para la gráfica de datos
    lines.append(Line2D([], [], color = "blue"))

# Creamos la 1ra figura
fig = plt.figure()
# Agregar la 1ra gráfica dentro de la figura
ax1 = fig.add_subplot(1, 2, 1, xlim = (xmin, xmax), ylim = (ymin[0], ymax[0]))
ax1.title.set_text("Temperatura") # type: ignore
ax1.set_xlabel("Número de muestras")
ax1.set_ylabel("Valor(C°)")
ax1.add_line(lines[0])

# Agregar la 2da gráfica dentro de la figura
ax2 = fig.add_subplot(1, 2, 2, xlim = (xmin, xmax), ylim = (ymin[1], ymax[1]))
ax2.title.set_text("Humedad") # type: ignore
ax2.set_xlabel("Número de muestras")
ax2.set_ylabel("Valor(%)")
ax2.add_line(lines[1])

# Animamos nuestra gráfica
anim = animation.FuncAnimation(fig, getSerialData, fargs = (Samples, numData, serialConnection, lines), interval = sampleTime) # type: ignore
plt.show() # Mostramos la gráfica

# Cerramos el puerto serial
serialConnection.close() # type: ignore