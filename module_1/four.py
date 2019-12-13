import pandas as pd

file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_1/cars_new.csv'

df = pd.read_csv(file)

# Check the data type of data frame "df" by .dtypes
print(df.dtypes)


#  This shows the statistical summary of all numeric-typed (int, float) columns.
print(df.describe())

# Describe all the columns in "df"
print(df.describe(include = "all"))

# Describe the columns specified below
print(df[["Length","Compression-ratio"]].describe())

