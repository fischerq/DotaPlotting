from utils import *

import samples

filename = "data/homework02.csv"
types = [float, float, float,]
features = ["PlayerID", "GameTime", "X", "Y"]

position_format = samples.SampleFormat(features, types)
samples_regression = parse_csv(filename, regression_format)