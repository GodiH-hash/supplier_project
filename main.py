# This tells Python to use the pandas library
import pandas as pd

# Load the supplier table from the CSV file
df = pd.read_csv("suppliers.csv")

# Show the table
print("📄 Supplier Table:")
print(df)

# Add a new column: Price Per Unit
df["Price Per Unit"] = df["Total Cost"] / df["Quantity"]

# Show the new table with calculated values
print("\n💡 Updated Table with Price Per Unit:")
print(df)

