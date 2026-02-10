import numpy as np
scores = np.random.randint(50, 100, size=(5, 3))

subject_means = scores.mean(axis=0)

centered_scores = scores - subject_means

print(" Original Scores:\n", scores)
print("\nSubject-wise Means:\n", subject_means)
print("\nCentered Scores:\n", centered_scores)
