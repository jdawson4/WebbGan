# Author: Jacob Dawson
#
# I'm just using this file to test/demonstrate some simply functionality with
# astropy on our data. The whole point of this repo is to kinda get used to
# using astropy, especially in an ml environment, so this is an important
# testing-ground

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

with fits.open('example_data/southern_ring.fits') as hdul:
    # using "with open" works with astropy

    hdul.info()
    data = hdul[1].data
    #print(np.amax(data)) # 47607.387
    #print(np.amin(data)) # -96.857056
    #print(np.mean(data)) # 222.7446

    # let's make a greyscale between 0-255
    data = np.clip(data, np.percentile(data, 20.0), np.percentile(data, 99.625))
    if (np.amin(data) < 0.0):
        data += np.amin(data)
    #data = np.log(data)
    data /= np.amax(data)
    data *= 255.0
    imgplot = plt.imshow(data, cmap="gray")
    plt.show()
