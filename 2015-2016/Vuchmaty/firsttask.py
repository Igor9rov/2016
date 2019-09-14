import matplotlib
import matplotlib.pyplot as plt

h = 1e-4
x = [i*h for i in range(0, 10001, 1)]

def poisky(a):
    y = [0 for j in range(0, 10001, 1)]
    y[0] = a
    i = 0
    for elem in y:
        k1 = x[i] + y[i] + y[i]*y[i]
        k2 = x[i] + h/2 + y[i] + h/2*k1 + (y[i] + h/2*k1)**2
        k3 = x[i] + h/2 + y[i] + h/2*k2 + (y[i] + h/2*k2)**2
        k4 = x[i] + h + y[i] + h*k3 + (y[i] + h*k3)**2
        y[i+1] = y[i] + h/6*(k1+2*k2+2*k3+k4)
        i = i +1
        if i == 10000:
            break
    return y
g = poisky(0.191243)
k = poisky(-1.20166)

plt.plot(x, g)
plt.plot(x, k)
plt.title('The Resulting Solutions')
plt.ylabel('Y')
plt.xlabel('X')
plt.grid(True)
plt.show()