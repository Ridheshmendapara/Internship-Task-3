import pandas as pd
import os

# Replace the following with the actual name of your CSV file
csv_file_name = "Data.csv"
folder_path = "F:/RIDHESH DOC/Task-3"

# Construct the full path to the CSV file
csv_file_path = os.path.join(F:/RIDHESH DOC/Task-3,Data.csv)

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv(F:/RIDHESH DOC/Task-3)

# Display the first few rows
print("First few rows:")
print(df.head())

# Display the last few rows
print("\nLast few rows:")
print(df.tail())

# Statistical summary
print("\nStatistical summary:")
print(df.describe())

# DataFrame information
print("\nDataFrame information:")
print(df.info())
