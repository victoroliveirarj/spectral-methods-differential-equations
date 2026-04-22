import numpy as np
import matplotlib.pyplot as plt


def exact_solution(x):
    return np.sin(np.pi * x)


x = np.linspace(-1, 1, 300)
y = exact_solution(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Exact solution")
plt.title("Example Function for Spectral Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
