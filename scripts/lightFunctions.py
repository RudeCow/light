import numpy as np
import matplotlib.pyplot as plt
import imageio 
from numpy.core.fromnumeric import size

def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    cut = photo[400:1050, 1130:1290, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    fig = plt.figure(figsize=(11, 10), dpi=200)
    plt.plot(luma, 'w', label='{} / {}'.format(lamp, surface))
    plt.imshow(cut, origin='lower')
    plt.title('Интенсивность отражённого излучения')
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')
    plt.legend()
    plt.savefig(plotName) 
    return luma


