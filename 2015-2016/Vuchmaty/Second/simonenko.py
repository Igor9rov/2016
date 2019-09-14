import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

h = 0.05
dt =1.5*h

x = [i*h for i in range(-int(1/h), int(1 + 1/h))]
t = [i*dt for i in range(0, int(1 + 1/dt))]

b = 1
a = c = dt/h

u = np.zeros((1 + 1/dt, 1 + 2/h))
i = 0
for elem in u[1/dt]:
    u[1/dt][i] = math.sin(math.pi*x[i])
    i = i + 1
i = 0
for elem in u:
    u[i][2/h] = math.sin(math.pi*(t[i]+1))
    u[i][0] = math.sin(math.pi*t[i])
    i = i + 1
i = 2/h
for elem in u[1/dt -1]:
    u[1/dt - 1][i-1] = u[1/dt-1][i] + h/dt*(u[1/dt][i] - u[1/dt - 1][i])
    i = i - 1
    if i == 0:
        break

for i in reversed(range(2,int(1/dt)+1)):
    l = 0
    for k in range(1,1+int(2/h)-1):
        u[i-2][k] = (dt/h*(u[i-1][k-1] + u[i-1][k+1])+u[i-2][k])
        l = l + 1
        if l == 2/h:
            break
plt.title('Plot of U(t,x) in t =1')
plt.plot(x,u[0])
plt.grid(True)
plt.show()
plt.title('Plot of U(t,x) in t=0.5')
plt.plot(x,u[1/dt/2])
plt.grid(True)
plt.show()

