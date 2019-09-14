import matplotlib
import matplotlib.pyplot as plt

h = 1e-4
x = [i*h for i in range(0, 10001, 1)]
y = [0 for i in range(0, 10001, 1)]
a = [i/10 for i in range(-50,4,1)]
integral = [0 for i in range(len(a))]
j = 0
for znach in a:
    y[0] = znach
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
    print((y[0]*y[0] + 4*y[5000]*y[5000] + y[10000]*y[10000])/6, znach)

    integral[j] = (y[0]*y[0] + 4*y[5000]*y[5000] + y[10000]*y[10000])/6
    j = j + 1
    if j == len(a):
        break
plt.plot(a,integral)
plt.title('Integral ot y(0)')
plt.ylabel('Integral')
plt.xlabel('y(0)')
plt.grid(True)
plt.show()
