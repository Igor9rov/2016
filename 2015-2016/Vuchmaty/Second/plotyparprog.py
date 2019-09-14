import matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,14,15,20,25,30,35,40,45,50,80,100]
y = [52.12,40.82,32.83,26.56,21.67,18.94,16.14,15.01,14.01,12.57,9.38,9.14,7.73,7.24,6.07,6.4,6.18,6.14,6.1,6,6.7]
z = []
for elem in y:
    z.append(52.12/elem)
plt.subplot(211)
plt.title('RUNTIME')
plt.ylabel('Time, s')
plt.xlabel('Numpers of process')
plt.plot(x,y,'bo',x,y)
plt.grid(True)
plt.subplot(212)
plt.xlabel('Numpers of process')
plt.ylabel('Boost')
plt.plot(x,z,'bo',x,z)
plt.show()

