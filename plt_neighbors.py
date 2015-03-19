import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('neighbors.txt')

plt.figure()
for i in range(4,9):
    plt.plot(range(4,9), np.sum(x[np.where(x[:,0] == i)][1:], axis = 0)[1:])
plt.legend(range(4,9), title = 'Ring Size Nj')
plt.xlabel('Size of neighboring rings Ni')
plt.ylabel('Quantity of neighbors of size Ni around ring of size Nj')
plt.savefig('neighbors.pdf')
