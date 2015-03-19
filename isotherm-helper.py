import numpy as np

def checkConvergence():
    counts = np.loadtxt('temp.dat', comments='#')[-10:]
    lin_coeffs = np.polyfit(counts[:,0], counts[:,1], 1)
    return lin_coeffs[0]

pressure = np.logspace(-3, np.log10(3), 10)

for p in pressure:
    #run lammps
    #check to see if converged
    slope = checkConvergence()
    print slope
