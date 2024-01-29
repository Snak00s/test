import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])
x2 = np.array([1, 2, 3, 1])
y2 = np.array([3, 9, 5, 12])

plt.plot(x,y,'-', c='r', lw='5')
plt.plot(x2,y2,'-', c='b', lw='5')
plt.title('La taille du flop', loc='right')
plt.xlabel('temps')
plt.ylabel('taille du flop')
plt.show()