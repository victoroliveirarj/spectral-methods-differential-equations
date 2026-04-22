import numpy as np
import matplotlib.pyplot as plt


def chebyshev_points(n):
    """
    Return Chebyshev-Gauss-Lobatto points in [-1, 1].
    """
    k = np.arange(n + 1)
    x = np.cos(np.pi * k / n)
    return x


n = 20
x = chebyshev_points(n)

plt.figure(figsize=(8, 4))
plt.plot(x, np.zeros_like(x), "o")
plt.title("Chebyshev-Gauss-Lobatto Points")
plt.xlabel("x")
plt.yticks([])
plt.grid(True)
plt.show()
