from cv2 import threshold
import matplotlib.pyplot as plt
import numpy as np

n1, n2 = 0, 1
count = 0
terms = 10
xp = []
yp = []
while count < terms:
    xp.append(count)
    yp.append(n1)
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count+=1

plt.plot(xp, yp)
plt.show()