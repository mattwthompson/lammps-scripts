import numpy as np
import pdb
import matplotlib.pyplot as plt

gofr = np.loadtxt('gofr_rerun.dat')

r = gofr[:,0]
g = gofr[:,1]

qq = np.logspace (-2, 1, num=1000)
#qq = np.logspace(-2,0, num=100)
rho = 20000/(37.44*2)**3

S = np.ndarray(shape=(0,1))

for q in qq:
    f = (g-1)*(r*np.sin(q*r))/q
    S = np.append(S, 1+4*np.pi*rho*np.trapz(f,r))

P = 6
I = S*P #multiply by form factor for SAXS

np.savetxt('saxs.dat', np.column_stack((qq,S)))

plt.figure()
plt.semilogx(qq,S,'.')
plt.ylabel('Intensity, arbitrary units')
plt.xlabel('q, inv. Angstroms')
#plt.ylim((0, 6))
plt.savefig('saxs.pdf')
