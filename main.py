import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def collatz_conjecture():

    x = 1234
    xp = []
    yp = []
    counter = 0
    while x != 1:

        xp.append(counter)
        counter+=1

        if x % 2 == 0:
            x = x / 2

        else:
            x = (x * 3) + 1

        yp.append(x)

    fig, ax = plt.subplots()
    ax.plot(xp, yp)
    plt.show()

collatz_conjecture()