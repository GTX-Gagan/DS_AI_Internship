import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
data = np.random.exponential(scale=50000, size=10000)
sample_means = []
for _ in range(1000):
    sample = np.random.choice(data, size=30)
    sample_means.append(np.mean(sample))
plt.figure()
plt.hist(sample_means, bins=30, density=True)
plt.title("Distribution of Sample Means (CLT)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()
