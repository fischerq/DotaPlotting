import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm as CM
from scipy.misc import imread
import random

random.seed()

def iter_rndload(filename, delimiter=',', skiprows=0, dtype=float):
    def iter_func():
        with open(filename, 'r') as infile:
            for _ in range(skiprows):
                next(infile)
            for line in infile:
                line = line.rstrip().split(delimiter)
                if(random.randint(0,3)>2):
                    #yield line[col]
                    for item in line:
                        yield dtype(item)
        iter_rndload.rowlength = len(line)

    data = np.fromiter(iter_func(), dtype=dtype)
    data = data.reshape((-1, iter_rndload.rowlength))
    return data

#generate_text_file()
data= iter_rndload('data/position_data_raw.csv', delimiter=",", skiprows=1)
print "loaded"
#data = np.genfromtxt("data/position_data_raw.csv", delimiter=",", skip_header=1)
X = data[:,2]
Y = data[:,3]
#
ID = data[:,0]
T = data[:,1]

C = np.hstack((ID[:,np.newaxis],T[:,np.newaxis]))
print C

threshold = 450

def compute_visits(list):
    players_lists = {}
    for feature in list:
        player, time = feature
        if player in players_lists.keys():
            players_lists[player].append(time)
        else:
            players_lists[player] = [time]
    score = 0
    for player in players_lists.keys():
        times = players_lists[player]
        times.sort()
        n_visits = 1
        new_differences = []
        for i in range(1, len(times)):
            new_differences.append(times[i] - times[i-1])
            if (times[i] - times[i-1]) > threshold:
                n_visits += 1
        score += n_visits
    return score

fig = plt.figure(figsize=(10.24, 10.24), dpi=100)
img = imread('Minimap.jpg')
plt.hexbin(X, Y, C=C,
            reduce_C_function=compute_visits,
           gridsize=150, cmap=CM.jet, bins=None, alpha=1, edgecolors='none', mincnt=1)
plt.axis([-8200, 7930.0, -8400.0, 8080.0])
plt.colorbar()
plt.axis('off')
plt.imshow(img, zorder=0, extent=[-8200, 7930.0, -8400.0, 8080.0])
plt.savefig("save.png", bbox_inches='tight', dpi=100)
plt.show()

