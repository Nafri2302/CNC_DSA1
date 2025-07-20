import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
csv_path = "your_file.csv"  # Replace with your file name
df = pd.read_csv(csv_path)

print("\n✅ CSV Loaded Successfully!\n")

# Display first few rows
print("First 5 rows of the dataset:\n", df.head())

# Summary statistics
print("\nSummary Statistics:\n", df.describe())

# Data types and null values
print("\nInfo:\n")
print(df.info())

# Histograms
df.hist(figsize=(10, 8))
plt.suptitle("Histograms of Numerical Features")
plt.tight_layout()
plt.show()

# Boxplots
df.plot(kind='box', subplots=True, layout=(2, 3), figsize=(12, 6), sharex=False, sharey=False)
plt.suptitle("Boxplots of Features")
plt.tight_layout()
plt.show()
