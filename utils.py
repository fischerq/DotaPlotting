import random
import numpy as np

def load_csv(filename, delimiter=',', select=(lambda x:True), skiprows=0, dtype=float):
    def iter_func():
        with open(filename, 'r') as infile:
            for _ in range(skiprows):
                next(infile)
            for line in infile:
                line = line.rstrip().split(delimiter)
                if select(line):
                    #yield line[col]
                    for item in line:
                        yield dtype(item)
        load_csv.rowlength = len(line)

    data = np.fromiter(iter_func(), dtype=dtype)
    data = data.reshape((-1, load_csv.rowlength))
    return data


class TimesliceSelect:
    def __init__(self, i):
        self.step = 30*60*10
        self.min = i*self.step
        self.max = (i+1)*self.step

    def select(self, line):
        return int(line[1]) >= self.min and int(line[1]) < self.max


random.seed()


def random_select(line):
    return random.randint(0,3)>2

class Evaluator:
    def __init__(self):
        self.visit_threshold = 450
        self.scores = []
        self.max_score = 15000
        self.divider = 40

    def normalize(self, score):
        #if score < self.max_score:
            return score
        #else:
        #    return self.max_score+(score-self.max_score)/self.divider

    def visits(self, times):

    def time(self, times):

    def evaluate(self, times):

    def compute_visits(self, list):
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
                if (times[i] - times[i-1]) > self.visit_threshold:
                    n_visits += 0
                else:
                    n_visits += (times[i] - times[i-1])
            score += n_visits
        self.scores.append(score)
        return self.normalize(score)