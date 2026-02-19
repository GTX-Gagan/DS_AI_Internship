import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# -------------------------------
# 1. Normal Distribution (Heights)
# -------------------------------
heights = pd.Series(np.random.normal(loc=170, scale=10, size=1000))

print("Normal Distribution (Heights)")
print("Mean:", heights.mean())
print("Median:", heights.median())
print()

plt.figure()
heights.plot(kind='hist', bins=30, density=True)
heights.plot(kind='kde')
plt.title("Normal Distribution (Human Heights)")
plt.xlabel("Height")
plt.ylabel("Density")
plt.show()


# -------------------------------------
# 2. Right-Skewed Distribution (Income)
# -------------------------------------
incomes = pd.Series(np.random.exponential(scale=50000, size=1000))

print("Right-Skewed Distribution (Incomes)")
print("Mean:", incomes.mean())
print("Median:", incomes.median())
print()

plt.figure()
incomes.plot(kind='hist', bins=30, density=True)
incomes.plot(kind='kde')
plt.title("Right-Skewed Distribution (Household Incomes)")
plt.xlabel("Income")
plt.ylabel("Density")
plt.show()


# --------------------------------------
# 3. Left-Skewed Distribution (Scores)
# --------------------------------------
scores = pd.Series(100 - np.random.exponential(scale=10, size=1000))

print("Left-Skewed Distribution (Exam Scores)")
print("Mean:", scores.mean())
print("Median:", scores.median())
print()

plt.figure()
scores.plot(kind='hist', bins=30, density=True)
scores.plot(kind='kde')
plt.title("Left-Skewed Distribution (Easy Exam Scores)")
plt.xlabel("Score")
plt.ylabel("Density")
plt.show()
