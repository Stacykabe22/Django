import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Line Chart (simulated index as time)
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal_length'], label='Sepal Length')
plt.plot(df.index, df['petal_length'], label='Petal Length')
plt.title("Sepal and Petal Length Over Entries")
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# Bar Chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal_length", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# Histogram: Distribution of sepal width
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal_width'], bins=15, kde=True)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
