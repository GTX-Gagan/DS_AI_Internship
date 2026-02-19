import pandas as pd
import numpy as np
np.random.seed(42)
data = pd.DataFrame({
    "value": np.random.normal(loc=50, scale=10, size=1000)
})
data.loc[1001] = 120
data.loc[1002] = -30
mean = data["value"].mean()
std = data["value"].std()
print("Mean (μ):", mean)
print("Standard Deviation (σ):", std)
data["z_score"] = (data["value"] - mean) / std
outliers = data[np.abs(data["z_score"]) > 3]
print("\nOutliers Detected:")
print(outliers)
