import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def TDMA(a,b,c,f):
    n = len(f)
    alpha = [0 for i in range(0,n)]
    beta = [0 for i in range(0,n)]
    x = [0 for i in range(0,n)]

    alpha[0] = -c[0]/b[0]
    beta[0] = f[0]/b[0]
    i = 0
    for elem in alpha:
        alpha[i+1] = (-c[i+1]/(a[i+1]*alpha[i] + b[i+1]))
        i = i+1
        if i == n-1:
            i = 0
            break
    for elem in beta:
        beta[i+1] = (f[i+1] - a[i+1]*beta[i])/(a[i+1]*alpha[i] + b[i+1])
        i = i+1
        if i == n-1:
            i = 0
            break
    x[n-1] = beta[n-1]
    for i in reversed(range(n-1)):
        x[i] = alpha[i]*x[i+1] + beta[i]
    return x


h = 0.05
dt = h**2/2

x = [int(i*h*100)/100 for i in range(0, int(1 + 1/h))]
t = [int(i*dt*100)/100 for i in range(0, int(1 + 1/dt))]

a = 1/h**2
b = 1/h**2 + 1/(2*dt)-(math.pi**2)/2
c = a

u = np.zeros((1 + 1/dt, 1 + 1/h))
i = 0
for elem in u[1/dt]:
    u[1/dt][i] = math.sin(math.pi*x[i])
    i = i + 1
i = 0
for elem in u:
    u[i][0] = math.sin(math.pi*t[i])
    u[i][1/h] = math.sin(math.pi*(t[i]+1))
    i = i + 1
i = 0
for elem in u[1/dt -1]:
    u[1/dt - 1][i+1] = u[1/dt][i+1] + dt*(math.pi*math.cos(math.pi*(t[0]+x[i+1])) + (math.pi**2 -
        2/h**2)*u[1/dt][i+1] + (1/h**2)*(u[1/dt][i] + u[1/dt][i+2]))
    i = i + 1
    if i == 1/h - 1:
        i = 0
        break


for i in reversed(range(2,int(1/dt)+1)):
    f = [0 for n in range(0,1+int(1/h))]
    l = 0
    for k in range(1,1+int(1/h)-1):
        f[l] = math.pi*math.cos(math.pi*(t[len(t)-1-i]+x[l])) + (1/(2*dt)+math.pi**2/2-1/h**2)*u[i][k]
        u[i-2][k] = (f[l] + a*u[i-1][k-1] + c*u[i-1][k+1])/b
        l = l + 1
        if l == 1/h:
            break
plt.title('The Resulting Solutions in t =1')
plt.plot(x,u[0])
plt.grid(True)
plt.show()
plt.title('The Resulting Solutions in t=1/2')
plt.plot(x,u[1/dt/2])
plt.grid(True)
plt.show()

