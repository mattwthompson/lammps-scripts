import pdb
import numpy as np
import matplotlib.pyplot as plt

log_file = 'log.quench'

read_headers = False
read_data = False
data = dict()
with open(log_file, 'r') as data_file:
    for line in data_file:
        if read_headers == True:
            labels = line.split()
            read_headers = False
            read_data = True
            i = 0
        if read_data == True:
            if line[:13] == 'Loop time of ':
                read_data = False
            elif i > 0:
                numbers = np.array(map(float, line.split()))
                data[numbers[0]] = numbers
                for i in range(len(numbers)):
                    data[numbers[0]]
                i += 1
            else:
                i += 1
        if line[0:29] == 'Memory usage per processor = ':
            read_headers = True

fp = labels[0] + '_data.txt'
#np.savetxt('fp',
temp = np.ndarray(shape=(len(data)))

i = 0

for j in range(len(labels)):
    file_name = labels[j] + '.txt'
    for key in sorted(data.keys()):
        temp[i] = data[key][j]
        i += 1
    i = 0
    np.savetxt(file_name,temp)

for j in range(len(labels)):
    if labels[j] != 'Step':
        txt_name = labels[j] + '.txt'
        fig_name = labels[j] + '.pdf'
        fig = plt.figure()
        plt.plot(np.loadtxt('Step.txt'),np.loadtxt(txt_name))
        plt.ylabel(labels[j])
        plt.xlabel('Step')
        plt.savefig(fig_name)
