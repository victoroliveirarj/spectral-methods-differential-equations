import numpy as np
import matplotlib.pyplot as plt


def chebyshev_polynomial(n, x):
    return np.cos(n * np.arccos(x))


x = np.linspace(-1, 1, 400)

plt.figure(figsize=(8, 5))
for n in range(5):
    plt.plot(x, chebyshev_polynomial(n, x), label=f"T_{n}(x)")

plt.title("Chebyshev Polynomials")
plt.xlabel("x")
plt.ylabel("T_n(x)")
plt.legend()
plt.grid(True)
plt.show()
