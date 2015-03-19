import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt('rdf.txt')
#vmd_data = np.loadtxt('gofr.dat')
mdtraj_data = np.loadtxt('rdf-mdtraj.txt')

plt.figure()
#plt.plot(data[:,0], data[:,1], lw=0.5)
#plt.plot(vmd_data[:,0], vmd_data[:,1], lw=0.5)
plt.plot(mdtraj_data[:,0]*10, mdtraj_data[:,1], lw=0.5)
plt.hlines(1.0, xmin = 0, xmax = 10.0)
plt.xlim((0.0, 10.0))
#plt.legend(['group-code', 'VMD', 'mdtraj'])
plt.savefig('rdf.pdf')
