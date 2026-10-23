
# Assignment 6: Data Preprocessing using Pandas

import pandas as pd

# Load the dataset
filename = input("Enter CSV or Excel file name: ")

if filename.endswith(".csv"):
    df = pd.read_csv(filename)
elif filename.endswith(".xls") or filename.endswith(".xlsx"):
    df = pd.read_excel(filename)
else:
    print("Unsupported file format")
    exit()

# Display original dataset
print("\nOriginal Dataset:")
print(df)

# Explore the dataset
print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
for column in df.columns:
    if df[column].isnull().any():
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].mean())
        else:
            mode_value = df[column].mode()
            if not mode_value.empty:
                df[column] = df[column].fillna(mode_value[0])

print("\nDataset After Handling Missing Values:")
print(df)

# Remove duplicate records
df = df.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(df)

# Drop an irrelevant column if one exists
column_name = input(
    "\nEnter an irrelevant column name to remove "
    "(or press Enter to skip): "
)

if column_name in df.columns:
    df = df.drop(columns=[column_name])
    print("Column removed successfully.")
elif column_name != "":
    print("Column not found. No column removed.")

# Select and filter data using loc[]
print("\nSelect First Five Rows Using loc:")
print(df.loc[0:4])

# Filter rows if a Marks column exists
if "Marks" in df.columns:
    print("\nStudents with Marks >= 50:")
    print(df.loc[df["Marks"] >= 50])

# Save the cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_data.csv")
