import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Generate 100 random integers between 1 and 10
values = np.random.randint(1, 11, size=100)

# Calculate relative frequency of each value
unique, counts = np.unique(values, return_counts=True)
relative_freq = counts / len(values)

# Plot the relative frequencies
plt.bar(unique, relative_freq)
plt.xlabel('Valor')
plt.ylabel('Frecuencia relativa')
plt.title('Frecuencia relativa de 100 números aleatorios')
plt.xticks(unique)
plt.show()
