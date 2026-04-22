import numpy as np
import matplotlib.pyplot as plt


n_values = np.array([4, 8, 12, 16, 20, 24])
errors = np.exp(-0.3 * n_values)

plt.figure(figsize=(8, 5))
plt.semilogy(n_values, errors, "o-")
plt.title("Illustrative Spectral Convergence")
plt.xlabel("Number of modes")
plt.ylabel("Error")
plt.grid(True)
plt.show()
