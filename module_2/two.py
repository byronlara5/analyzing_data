import pandas as pd
import matplotlib.pylab as plt
import numpy as np

file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_2/cars_cleaned.csv'

df = pd.read_csv(file)

# *************************** DATA STANDARDIZATION ***************************

print(df.dtypes)

#Convert data type in each column to proper format
df[["Bore", "Stroke"]] = df[["Bore", "Stroke"]].astype("float")
df[["Normalized-losses"]] = df[["Normalized-losses"]].astype("int")
df[["Price"]] = df[["Price"]].astype("float")
df[["Peak-rpm"]] = df[["Peak-rpm"]].astype("float")

print(df.dtypes)

#Convert mpg to L/100km for standardization (Formula: 235 divided by mpg)
df['City-L/100km'] = 235 / df["City-mpg"]
df['Highway-L/100km'] = 235 / df["Highway-mpg"]

print(df.head(10))

# Exporting new standardized file
df.to_csv('cars_standardized.csv', index=False)