import numpy as np
import matplotlib.pyplot as plt

y1=np.fromfile("C://year/year1.txt",dtype=int,sep=",")
y2=np.fromfile("C://year/year2.txt",dtype=int,sep=",")
print(y1)
print(y2)
p1=np.fromfile("C://sales/sale1.txt",dtype=int,sep=",")
p2=np.fromfile("C://sales/sale2.txt",dtype=int,sep=",")
print(p1)
print(p2)
plt.plot(y1,p1,label="year")
plt.plot(y2,p2,label="price")

plt.xlabel("years")
plt.ylabel("prices")
plt.legend("upper right")
plt.show()