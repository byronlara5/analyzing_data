import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns



file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_3/cars_bins_and_dummy.csv'

df = pd.read_csv(file)

"""
    === Descriptive statistical analysis ===
    We can take a look at the variables by using the method: describe()
    This will show:
        -The count of the variable
        -The mean
        -The standard deviation(std)
        -The minimum value
        -The IQR (Interquartile Range: 25%, 50%, 75%)
        -The maximum value
    
    Note: the default setting of 'describe' skips variables of type: 'object'. 
    If you want to apply the method to variables of type 'object'. You can do it like this:
    include=['object']
"""

# ********** Describing the dataframe **********
print(df.describe())
print(df.describe(include='object'))

"""
    === Value counts ===
    Value-counts is a good way of understanding how many units of each characteristic/variable we have.
    We can apply the "value_counts" method on the column 'drive-wheels'. 
    
    Note:
    The method "value_counts" only works on Pandas series, not Pandas Dataframes. As a result,
    we only include one bracket "df['drive-wheels']" not two brackets "df[['drive-wheels']]".
"""

# ********** Value counts the 'Drive-wheels' column **********
print(df['Drive-wheels'].value_counts())

# We can convert the series to dataframe like this:
print(df['Drive-wheels'].value_counts().to_frame())

"""
    === Basics of grouping ===
    The "groupby" method groups data by different categories. The data is grouped base on one or several
    variables and analysis is performed on the individual groups.
"""
# We can see the different categories by this:
print(df['Drive-wheels'].unique())

#Grouping the columns to calculate the mean:
df_group_one = df[['Drive-wheels', 'Price']]
df_group_one = df_group_one.groupby(['Drive-wheels'],as_index=False).mean()
print(df_group_one)

#Grouping multiple columns to calculate the mean:
df_group_two = df[['Drive-wheels', 'Body-style', 'Price']]
df_group_two = df_group_two.groupby(['Drive-wheels', 'Body-style'], as_index=False).mean()
print(df_group_two)

#Grouping Body-style to calculate the mean:
df_group_three = df[['Body-style', 'Price']]
df_group_three = df_group_two.groupby(['Body-style'], as_index=False).mean()
print(df_group_three)



