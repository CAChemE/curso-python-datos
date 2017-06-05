"""
=========================================================
Demo of the histogram (hist) function from .dat file
=========================================================

In addition to the basic histogram, this demo shows a few optional
features:

    * Setting the number of data bins
    * The ``normed`` flag, which normalizes bin heights so that the
      integral of the histogram is 1. The resulting histogram is an
      approximation of the probability density function.

Selecting different bin counts and sizes can significantly affect the
shape of a histogram. The Astropy docs have a great section on how to
select these parameters:
http://docs.astropy.org/en/stable/visualization/histogram.html
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy import io as sio
import matplotlib

plt.style.use('default')
matplotlib.rcParams.update({'font.size': 22})

datamat = sio.loadmat("../data/anglesDp125.mat")
#print(sio.whosmat("2DanglesDp125.mat"))
data_angles = datamat['angles2D'][0]

data_angles_cut = data_angles[data_angles>20]
data_angles_cutcut = data_angles_cut[data_angles_cut<160]
x = data_angles_cutcut

num_bins = 20

mu = data_angles_cutcut.mean()
sigma = data_angles_cutcut.std()

fig, ax = plt.subplots(figsize=(10,6))

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, normed=1)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--', linewidth=5)
ax.set_xlabel(r'$\alpha(°)$')
ax.set_ylabel('Probability density')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()

plt.savefig('histogram2D.png', bbox_inches='tight', format='png')
plt.show()