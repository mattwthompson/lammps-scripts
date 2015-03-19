#uses mdtraj to calculate rdf
#only handles one frome, .pdb is a dummy file made with vmd from trj
import mdtraj as md
import numpy as np

traj = md.load('freeze.lammpstrj', top = 'freeze.pdb')
r, gofr = md.compute_rdf(traj)

np.savetxt('rdf-mdtraj.txt', np.hstack((r, gofr)))
