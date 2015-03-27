import numpy as np
import matplotlib.pyplot as plt
import pdb

raw_data = np.loadtxt('isotherm.dat', comments = '#')

#initialize data
data = np.empty((0,2))

for p in np.unique(raw_data[:,0]):
    data = np.reshape(np.append(data, [p, max(x[1] for x in raw_data[raw_data[:,0] == p])]), (-1, 2))

#data = data[data[:,0].argsort()] #sorting data not needed

plt.figure()
plt.plot(data[:,0]/1.2, data[:,1]*0.0932, 'o-')
plt.ylim((0,800))
plt.ylabel('Argon Loading (cc N2/g C)')
plt.xlabel('Reduced Pressure P/Pvap')
plt.title('Argon Adsorption')
plt.savefig('isotherm-rect.pdf')

plt.figure()
plt.semilogx(data[:,0]/1.2, data[:,1]*0.0932, 'o-')
plt.ylim((0,800))
plt.ylabel('Argon Loading (cc N2/g C)')
plt.xlabel('Reduced Pressure P/Pvap')
plt.title('Argon Adsorption')
plt.savefig('isotherm-log.pdf')

np.savetxt('isotherm.txt', data, header = 'adsorption data from N2 on 20000 C atoms\np (atm) #N2 adsorbed')
