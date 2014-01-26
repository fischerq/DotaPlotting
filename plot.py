from utils import *

import samples


filename = "data/position_data_raw.csv"
types = [int, int, float, float]
features = ["PlayerID", "GameTime", "X", "Y"]

position_format = samples.SampleFormat(features, types)
samples_positions = parse_csv(filename, position_format)
print "loaded csv"
def player_filter(sample):
    return sample[0] == 7





#samples_positions = filter_samples(samples_positions, player_filter)

from matplotlib import pyplot as plt
from matplotlib import cm as CM
from scipy.misc import imread

scores = []
threshold = 450

def reduce(list):
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
    global scores
    scores.append(score)
    return score


data = combine_features([samples_positions["PlayerID"],samples_positions["GameTime"]])
print "combined"
#PLT.subplot(211)
fig = plt.figure(figsize=(10.24, 10.24), dpi=100)
img = imread('Minimap.jpg')
plt.hexbin(samples_positions["X"], samples_positions["Y"],
           C=data, reduce_C_function=reduce,
           gridsize=100, cmap=CM.Blues, bins=None, alpha=0.7, edgecolors='none', mincnt=1)
plt.axis([-8200, 7930.0, -8400.0, 8080.0])
plt.colorbar()
plt.axis('off')
plt.imshow(img, zorder=0, extent=[-8200, 7930.0, -8400.0, 8080.0])
plt.savefig("save.png", bbox_inches='tight', dpi=100)
plt.show()
#

#PLT.subplot(212)
#PLT.axis([0, 250.0, 0.0, 100.0])
#PLT.hist(scores, bins=80)

