import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm as CM
import matplotlib as mpl
from scipy.misc import imread

from utils import *

for i in range(0,6):
    data = load_csv('data/position_data_raw.csv', delimiter=",", select=TimesliceSelect(i).select, skiprows=1)
    print "loaded"

    ID = data[:, 0]
    T = data[:, 1]
    X = data[:, 2]
    Y = data[:, 3]
    print len(X)
    C = np.hstack((ID[:, np.newaxis], T[:, np.newaxis]))

    eval = Evaluator()
    fig=plt.figure(figsize=(10.24, 20.24), dpi=100)
    #fig.add_subplot(211)
    img = imread('Minimap.jpg')
    plt.hexbin(X, Y, C=C,
               reduce_C_function=eval.compute_visits,
               gridsize=120, cmap=CM.jet, bins=None, alpha=1, edgecolors='none', norm=mpl.colors.LogNorm(), mincnt=1)
    plt.axis([-8200, 7930.0, -8400.0, 8080.0])
    #plt.colorbar()
    plt.axis('off')
    plt.imshow(img, zorder=0, extent=[-8200, 7930.0, -8400.0, 8080.0])
    #fig.add_subplot(212)
    #plt.hist(eval.scores, bins=100)
    plt.savefig("time_{}.png".format(i), bbox_inches='tight', dpi=100)
    plt.clf()

