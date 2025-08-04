<<<<<<< HEAD
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

=======
import csv
from gpt_utils import evaluate_supplier_risk

with open("suppliers.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        comment = row["comment"]
        risk = evaluate_supplier_risk(comment)
        print(f"Comment: {comment}\n➡️ Risk Rating: {risk}/10\n")
>>>>>>> 3e78d2d (git commit -m "feat: build AI-powered supplier risk rating tool with OpenAI API")
