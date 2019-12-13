import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns

from scipy import stats


file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_3/cars_bins_and_dummy.csv'

df = pd.read_csv(file)

#ANOVA: Analysis of variance

"""
The Analysis of Variance (ANOVA) is a statistical method used to test whether there are significant
differences between the means of two or more groups. ANOVA returns two parameters:

F-test score: ANOVA assumes the means of all groups are the same, calculates how much the actual 
means deviate from the assumption, and reports it as the F-test score. A larger score means there is 
a larger difference between the means.

P-value: P-value tells how statistically significant is our calculated score value.

If our price variable is strongly correlated with the variable we are analyzing, 
expect ANOVA to return a sizeable F-test score and a small p-value
"""

#Let's try with Drive-wheels
#Note: Because the ANOVA algorithm averages the data automatically, we don't need to take the average before hand.

grouped_data = df[['Drive-wheels', 'Price']].groupby(['Drive-wheels'])
print(grouped_data.head(2))

#We can obtain the values of the method group using the method "get_group".
print(grouped_data.get_group('4wd')['Price'])

#we can use the function 'f_oneway' in the module 'stats' to obtain the F-test score and P-value.
f_val, p_val = stats.f_oneway(grouped_data.get_group('fwd')['Price'],
                              grouped_data.get_group('rwd')['Price'],
                              grouped_data.get_group('4wd')['Price'])

print("ANOVA results for the three groups: F= ", f_val ," P= ", p_val)

"""
    Conclusion:
    This is a great result, with a large F test score showing a strong correlation and a P value
    of almost 0 implying almost certain statistical significance.
    
    But does this mean all three tested groups are all this highly correlated?
"""

# Separately: fwd and rwd

f_val_two, p_val_two = stats.f_oneway(grouped_data.get_group('fwd')['Price'],
                              grouped_data.get_group('rwd')['Price'])

print("ANOVA results for fwd and rwd: F= ", f_val_two ," P= ", p_val_two)

# Separately: 4wd and rwd

f_val_three, p_val_three = stats.f_oneway(grouped_data.get_group('4wd')['Price'],
                              grouped_data.get_group('rwd')['Price'])

print("ANOVA results for 4wd and rwd: F= ", f_val_three ," P= ", p_val_three)

# Separately: 4wd and fwd

f_val_four, p_val_four = stats.f_oneway(grouped_data.get_group('4wd')['Price'],
                              grouped_data.get_group('fwd')['Price'])

print("ANOVA results for 4wd and fwd: F= ", f_val_four ," P= ", p_val_four)