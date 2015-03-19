import numpy as np
import matplotlib.pyplot as plt

gofr = np.loadtxt('gofr_rerun.dat')

r = gofr[:,0]
g = gofr[:,1]

q = np.linspace(5, 35, num=1000)

l = 1.54
rho = 20000/(37.44*2)**3

S = np.ndarray(shape=(0,1))

for qq in q:
    f = (g-1)*(r*np.sin(qq*r))/qq
    S = np.append(S, 1+4*np.pi*rho*np.trapz(f,r))

np.savetxt('pdf.dat', np.column_stack((q,S)))

#plt.figure()
#plt.plot(2*theta,S)
#plt.ylabel('Intensity, arbitrary units')
##plt.xlabel('q, inv. Angstroms')
#plt.xlabel('Angle, degrees')
##plt.ylim((0, 6))
#plt.savefig('xrd-theta.pdf')

plt.figure()
plt.plot(q,S)
plt.ylabel('Intensity, arbitrary units')
plt.xlabel('q, 1/A')
plt.savefig('pdf.pdf')

#plt.figure()
#plt.plot(r, g)
#plt.ylabel('Radial Distribution Function')
#plt.xlabel('Radius, A')
##plt.ylim((0,6))
#plt.xlim((0,10))
#plt.savefig('rdf.pdf')
