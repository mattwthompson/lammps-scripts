import copy
import numpy as np
#import cProfile, pstats, StringIO

class Rings(object):
    """ """
    def __init__(self, bonds_file, atoms, max_length):
        """ """
        self.rings = list()
        self.current_path = list()
        self.max_length = max_length
        self.atoms = dict()
        self.parse_reaxc(self.atoms, bonds_file)

        for atom in self.atoms:
            self.current_path = list()
            self.current_path.append(atom)
            self.step(atom)

    def parse_reaxc(self, atoms, bonds_file):
        cutoff = 0.3
        with open(bonds_file,'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                else:
                    fields = line.split()
                    nb = int(fields[2])
                    atom_index = int(fields[0])
                    atoms[atom_index] = list()
                    for b in range(nb):
                        if float(fields[4+nb+b]) > cutoff:
                            atoms[atom_index].append(int(fields[b+3]))
        return atoms

    def step(self, atom):
        neighbors = self.atoms[atom]
        if len(neighbors) > 1:
            for n in neighbors:
                # Check to see if we found a ring.
                current_length = len(self.current_path)
                if current_length > 2 and n == self.current_path[0]:
                    self.rings.append(copy.copy(self.current_path))
                # Prevent stepping backwards.
                elif n in self.current_path:
                    continue
                else:
                    if current_length < self.max_length:
                        # Take another step.
                        self.current_path.append(n)
                        self.step(n)
                    else:
                        # Reached max length.
                        continue
            else:
                # Finished looping over all neighbors.
                del self.current_path[-1]
        else:
            # Found a dead end.
            del self.current_path[-1]

if __name__ == '__main__':

    #pr = cProfile.Profile()
    #pr.enable()
    
    atoms = dict()
    #atoms = parse_reaxc('bonds.reaxc', 0)

    rings = Rings('bonds.reaxc', atoms, 8)
    
    counts = [0, 0, 0, 0, 0]

    for ring in rings.rings:
        ring_size = len(ring)
        counts[ring_size - 4] += 1
    for i, x in enumerate(counts):
        counts[i] = x / 2 / (i+4)

    print 'found {} rings'.format(len(rings.rings))
    print range(4,9)
    print counts

    data = [range(4,9), counts] 
    #np.savetxt('count.dat', zip(*data))
    with open('count.dat', 'w') as f:
        for i,row in enumerate(counts):
            f.write('{} {}\n'.format(i+4, counts[i]))
      
    fo = open('num_atoms_in_rings.txt', 'w')
    fo.write(str(len(np.unique([val for sublist in rings.rings for val in sublist]))))
    #pr.disable()
    #s = StringIO.StringIO()
    #sortby = 'time'
    #ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    #ps.print_stats()
    #print s.getvalue()
