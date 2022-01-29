from cv2 import threshold
import matplotlib.pyplot as plt
import numpy as np


def mandelbrot_set():
    loop = 50 # number of interations
    div = 600 # divisions

    c = np.linspace(-2,2,div)[:,np.newaxis] + 1j*np.linspace(-2,2,div)[np.newaxis,:] 

    ones = np.ones(np.shape(c), np.int)

    color = ones * loop + 5
    z = 0
    for n in range(0,loop):
        z = z**2 + c
        diverged = np.abs(z)>2

        color[diverged] = np.minimum(color[diverged], ones[diverged]*n)

    plt.rcParams['figure.figsize'] = [12, 7.5]

    plt.contourf(c.real, c.imag, color)
    plt.xlabel("Real($c$)")
    plt.ylabel("Imag($c$)")
    plt.xlim(-2,2)
    plt.ylim(-1.5,1.5)
    plt.show()

mandelbrot_set()