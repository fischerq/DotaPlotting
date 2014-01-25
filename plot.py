from utils import *

import samples

filename = "data/position_data_raw.csv"
types = [int, int, float, float]
features = ["PlayerID", "GameTime", "X", "Y"]

position_format = samples.SampleFormat(features, types)
samples_positions = parse_csv(filename, position_format)

from matplotlib import pyplot as PLT
from matplotlib import cm as CM

gridsize=50
PLT.subplot(111)

# if 'bins=None', then color of each hexagon corresponds directly to its count
# 'C' is optional--it maps values to x-y coordinates; if 'C' is None (default) then
# the result is a pure 2D histogram

PLT.hexbin(samples_positions["X"], samples_positions["Y"], C=None, gridsize=gridsize, cmap=CM.jet, bins=None)
PLT.axis([-8576, 9216.0, -7680.0, 8192.0])

cb = PLT.colorbar()
cb.set_label('mean value')
PLT.show()