import time
import serial
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from itertools import count
import pandas as pd

serialPort = serial.Serial(
        port='/dev/ttyACM0',
        baudrate=9600,
        bytesize= serial.EIGHTBITS
        )


print('Place the obstacle at 15cm')
x_vals = []
sensorReadings = []
plt.style.use('fivethirtyeight')
fig = plt.figure(1)
#start_time = time.time()
#while (time.time() < start_time + 20):

index = count()

def animate(i):
    x_vals.append(next(index))
    
    if (serialPort.in_waiting > 0):
        value = serialPort.readline()
        value = int(value[:-2].decode("utf-8"))
    sensorReadings.append(value)

    plt.cla()
    plt.plot(x_vals, sensorReadings)


ani = FuncAnimation(fig, animate, interval=100)
plt.tight_layout()
plt.show()

serialPort.close()
