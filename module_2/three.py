import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import pandas as pd
import numpy as np



file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_2/cars_standardized.csv'

df = pd.read_csv(file)

# *************************** DATA NORMALIZATION ***************************

#replace (original value) by (original value)/(maximum value)
df['Length'] = df['Length'] / df['Length'].max()
df['Width'] = df['Width'] / df['Width'].max()
df['Height'] = df['Height'] / df['Height'].max()

print(df.head())

# *************************** DATA BINNING ***************************

#Converting HP
df['HP'] = df['HP'].astype(int, copy=True)

#Visualization
#plt.hist(df["HP"])

#plt.xlabel('HP')
#plt.ylabel('count')
#plt.title('Horsepower Bins')
#plt.show()

"""
-We would like 3 bins of equal size bandwidth so we use numpy's linspace(start_value, end_value, numbers_generated function.

-Since we want to include the minimum value of horsepower we want to set start_value=min(df["horsepower"]).

-Since we want to include the maximum value of horsepower we want to set end_value=max(df["horsepower"]).

-Since we are building 3 bins of equal length, there should be 4 dividers, so numbers_generated=4.

"""

bins = np.linspace(min(df["HP"]), max(df["HP"]), 4)

#We set group names
group_names = ["Low", "Medium", "High"]

#We apply the function "cut" to determine what each value of HP belongs to
df["HP-binned"] = pd.cut(df["HP"], bins, labels=group_names, include_lowest=True)

#Lets see the bins:
print(df[["HP", "HP-binned"]].head(20))

#Now lets see the number of vehicles in each bin:
print(df['HP-binned'].value_counts())

#Lets visualize the plot distribution of each bin
#plt.bar(group_names, df["HP-binned"].value_counts())

#plt.xlabel("HP")
#plt.ylabel("Count")
#plt.title("Horsepower BINS")
#plt.show()

# *************************** DUMMY VARIABLE ***************************

dummy_fuel_type = pd.get_dummies(df['Fuel-type'])
print(dummy_fuel_type)

dummy_aspiration = pd.get_dummies(df['Aspiration'])
print(dummy_aspiration)

#Mergin the new columns to the dataframe
df = pd.concat([df, dummy_fuel_type], axis=1)
#Drop original column "Fuel-type"
df.drop('Fuel-type', axis=1, inplace=True)

df = pd.concat([df, dummy_aspiration], axis=1)
df.drop('Aspiration', axis=1, inplace=True)

# Exporting new standardized file
df.to_csv('cars_bins_and_dummy.csv', index=False)