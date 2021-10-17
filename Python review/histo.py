########################################################################
# histo.py
# Author David
# matplotlib tutorial
########################################################################

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 10, 1000)

#plt.hist(x)

plt.hist(x, bins=20)

plt.show()