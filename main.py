from tkinter import N
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math as m

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

def chaos():
    """
    Xn+1 = RXn (1-Xn)
    """
    ax = plt.subplots()
    xp = []
    yp = []

    n = 0
    r = 0

    while n != 10 and r != 10:
        x = n
        x = r * x * (1 - x)
        yp.append(x)
        xp.append(n)
        n += 1
        r += 1

    plt.plot(xp, yp)
    plt.show()

def circle():
    ax = plt.subplots()
    xp = []
    yp = []

    t = 0
    y = 0
    x = 0

    while t != 90:
        x = m.cos(t)
        y = m.sin(t)
        yp.append(y)
        xp.append(x)
        t += 1
    plt.plot(xp, yp)
    plt.show()


def parametric():
    ax = plt.figure().add_subplot(projection='3d')

    theta = np.linspace(-4*np.pi, 4*np.pi, 100)
    z = np.linspace(-2, 2, 100)
    x = np.sin(theta)
    y = np.cos(theta)

    ax.plot(x,y,z)
    plt.show()