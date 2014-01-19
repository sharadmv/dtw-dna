#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
from dtw import normalize

vec = eval(sys.stdin.readline())
plt.plot(range(len(vec)), vec)
temp = [0, 1, 3, 2, 3, 2, 3, 2, 0, 1, -1, -3, -4, -2, -1, -2, -3, -4, -6, -8, -10, -9, -7, -6]
#plt.plot(range(len(temp)), temp)
plt.show()
