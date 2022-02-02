import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def collatz_conjecture(n):

    ax = plt.subplots()
    xp = []
    yp = []
    x = 0

    while n != 1:
        x += 1
        xp.append(x)

        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1

        yp.append(n)
        plt.plot(xp, yp)
        plt.show()
        plt.figure().clear()

collatz_conjecture(12345)