# Compute basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Group by species and compute mean of numerical columns
grouped = df.groupby("species").mean()
print("\nMean values grouped by species:")
print(grouped)

# Identify interesting patterns
print("\nInteresting findings:")
print("Setosa has the smallest petal size, while Virginica has the largest.")
