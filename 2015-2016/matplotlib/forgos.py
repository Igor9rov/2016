import matplotlib
import matplotlib.pyplot as plt


x = [i for i in range(-29,100,1)]
y = x
for i in range(0,len(x)):
    x[i] = x[i]/10
    print(x[i])
print(x)
for j in range(0,len(x)):
    y[j] = ((2*x[j]+1)/(x[j]+3))**2
    print(y[j])
print(y)
print(x)
plt.plot(x,y)
plt.grid(True)
plt.show()

