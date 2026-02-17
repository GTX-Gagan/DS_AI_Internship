import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample dataset
data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45, 50, 29],
    "Salary": [25000, 30000, 50000, 60000, 80000, 45000, 52000, 90000, 100000, 48000]
}
df = pd.DataFrame(data)
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)
# Min-Max Scaling
minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)
# Plot Original Salary
plt.figure()
plt.hist(df["Salary"], bins=5)
plt.title("Original Salary")
plt.show()
# Plot Standardized Salary
plt.figure()
plt.hist(df_standardized["Salary"], bins=5)
plt.title("Standardized Salary")
plt.show()
# Plot Normalized Salary
plt.figure()
plt.hist(df_normalized["Salary"], bins=5)
plt.title("Normalized Salary")
plt.show()
