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
    r = 1

    while n != 1:
        x = n
        x = r * x * (1 - x)
        yp.append(x)
        xp.append(n)
        n += 0
    
    plt.plot(xp, yp)
    plt.show()

def circle():
    ax = plt.subplots()
    xp = []
    yp = []

    t = 0
    y = 0
    x = 0
    
    while t != 100:
        x = m.sin(t)
        y = m.cos(t)
        yp.append(y)
        xp.append(x)
        t+=0.1
    plt.plot(xp, yp)
    plt.show()

circle()