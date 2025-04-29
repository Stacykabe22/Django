import pandas as pd

# Load the Iris dataset from a CSV file
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Display the first few rows
print("First five rows:")
print(df.head())

# Check data types and missing values
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset: drop or fill missing values (in this case, none)
df = df.dropna()
