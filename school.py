# info in school
# for i in range(2, 10, 2):
#     print(i)

# (2, 10, 2) the first 2 is where the loop begins ; the ten where it ends and the last number the steps.
# i = 1
# while i > 0:
#     print(i)

import numpy as np

import matplotlib.pyplot as plt


def f(x):
    if x > 1:
        return np.cos(x)
    else:
        return np.sin(x)


X = np.linspace(-10, 10, 100)

Y = [np.cos(x) for x in X]
Z = [np.sin(x) for x in X]
plt.plot(X, Y, 'r.', label="h(x)")
plt.plot(Y, Z, 'g', label="h(x)")

plt.title("une fonction")
plt.legend(loc='upper left')

axes = plt.gca()
axes.spines["top"].set_visible(False)
axes.spines["right"].set_visible(False)
axes.spines["left"].set_position('center')
axes.spines["bottom"].set_position('center')
plt.show()


