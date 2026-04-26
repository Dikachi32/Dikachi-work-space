##-- Pandas is a Python library used for:  Working with structured data efficiently
#  Think of it like:  Excel on steroids ⚡, SQL + Python combined, 
# The “data brain” before machine learning starts

#.. The MAIN ROLE of Pandas in AI Engineering
#  Before any model learns anything, Pandas helps you: 1. Load data, 2. Inspect 
# 3. dataClean data, 4. Transform data, 5. Analyze data
# Prepare data for ML models👉 Without Pandas, your model will learn from garbage.

#--- Pandas Data Structures: Series (1D Data)
import pandas as pd

s = pd.Series([10, 20, 30, 40])
# print(s)


##-- Create a Series of 5 AI topics, Print the 3rd element, Change the index to custom names
# ai = pd.Series(["ML", "DL", "OOP", "NLP", "CNN"])
# print(ai[2])
# ai.index = ["Topic1", "Topic2", "Topic3", "Topic4", "Topic5"]
# print(ai)

# DataFrame (2D Table — MOST IMPORTANT)
data = {
    "Name": ["Dikachi", "Abuchi", "Akpa", "Ebuka"],
    "Age": [25, 30, 38, 42]
}

df = pd.DataFrame(data)
# print(df)


##.. Create a DataFrame of:
# Students, Scores, Passed (True/False)
# Add 5 rows: Print only the “Scores” column
info = {
    "Student": ["Dikachi", "Maluchi", "Philip", "Ebere", "Precious"],
    "Score": [75, 70, 68, 30, 20],
    "Passed": ["True", "True", "True", "False", "False"]
}

df = pd.DataFrame(info)
# print(df["Passed"])
# print(df)


##-- LOADING DATA (REAL-WORLD SKILL)
#. From CSV file
# df = pd.read_csv("data.csv")    # Reads a CSV file named "data.csv" and converts it into a DataFrame
# #. From Excel file              
# df = pd.read_excel("data.xlsx") # Reads an Excel file named "data.xlsx" and converts it into a DataFrame
# #. From Dictionary (Manual Data)
# df = pd.DataFrame(data)         # Converts a Python dictionary called 'data' into a DataFrame


##-- Download any dataset (e.g. student scores): Load it using Pandas: Print first 5 rows (head())
df = pd.read_csv("student-scores.csv")
# print(df.head())     # Shows only the first 5 rows of your dataset.
# print(df)          # Shows the entire dataset
# print(df.columns)  # How to Check your column names
# print(df.tail())   # How to check Last 5 rows
# print(df.info())   # Show the Data types + nulls or missing values info(Overview of the dataset)
# print(df.describe())   # Show the Statistics
# print(df.shape)        # Show the Rows, Columns
# print(df["id"])
# print(df["first_name"])


## Load a dataset Print: Shape, Column names, Data types
# Identify: Which column has missing values
df = pd.read_csv("student-scores.csv")
# print("Shape:", df.shape)
# print("Columns:", df.columns)

# df.info()

# print("\nMissing values:")
# print(df.isnull().sum())    # Show you how many missing values per column


##... DATA CLEANING (MOST CRITICAL SKILL)
# 1. Handling Missing Values
df.isnull().sum()
df.dropna()            # Remove missing
df.fillna(0)           # Replace missing
# 2. Removing Duplicates
df.drop_duplicates()
# 3. Renaming Columns
df.rename(columns={"old": "new"})

#--- Create a DataFrame with: Some missing values; Some duplicate rows
# Clean it: Remove duplicates'; Fill missing values
import pandas as pd

data = {
    "Name": ["Dikachi", "Maluchi", "Philip", "Ebere", "Ebere"],
    "Score": [75, None, 68, 30, 30],
    "Passed": [True, True, None, False, False]
}

df = pd.DataFrame(data)     # Convert the dictionary into a DataFrame (table)


print("Original Data:")   # Show the original data (with problems)
print(df)

df = df.drop_duplicates()   # 👉This removes rows that appear more than once

df["Score"] = df["Score"].fillna(df["Score"].mean())   # Replace missing Score with the average (mean) of all scores

df["Passed"] = df["Passed"].fillna(True)             # Replace missing Passed values with False

print("\nCleaned Data:")
print(df)
