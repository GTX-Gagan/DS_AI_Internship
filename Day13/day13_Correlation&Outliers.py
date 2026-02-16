import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

corr = df.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

high_corr = corr[(corr > 0.8) & (corr < 1.0)]
print(high_corr.dropna(how="all").dropna(axis=1, how="all"))

sns.boxplot(x=df['Price'])
plt.show()
