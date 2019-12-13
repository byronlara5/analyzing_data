import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns

from scipy import stats


file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_3/cars_bins_and_dummy.csv'

df = pd.read_csv(file)

#Correlation and Causation



"""
    Correlation: a measure of the extent of interdependence between variables.
    Causation: the relationship between cause and effect between two variables.
    
    Note: It is important to know the difference between these two and that 
    correlation does not imply causation. Determining correlation is much simpler,
    determining causation requires independent experimentation
    
Pearson Correlation

    The Pearson Correlation measures the linear dependence between two variables X and Y.
    The resulting coefficient is a value between -1 and 1 inclusive, where:

    1: Total positive linear correlation.
    0: No linear correlation, the two variables most likely do not affect each other.
    -1: Total negative linear correlation.

    Whe use the method: .corr() to calculate the correlation
"""

print(df.corr())

"""
    === P-value ===
    The P-value is the probability value that the correlation between these two variables
    is statistically significant. Normally we choose a significant level of 0.005, which means
    that we are 95% confident that the correlation between these two variables is significant.
    
    When:
    
    -the p-value is <0.001: we say there is strong evidence that the correlation is significant.
    -the p-value is <0.05: there is moderate evidence that the correlation is significant.
    -the p-value is <0.1: there is weak evidence that the correlation is significant.
    -the p-value is >0.1: there is no evidence that the correlation is significant.
"""

#Let's calculate the P-value of Wheel-base and 'Price'
#First let's import the 'stats' module in the scipy library (from scipy import stats)

pearson_coef, p_value = stats.pearsonr(df['Wheel-base'], df['Price'])
print("="*10, " Wheel-base and Price ", "="*10)
print("The pearson correlation coefficient is ", pearson_coef, " with a P-value of ", p_value)

"""
    Conclusion:
    Since the p-value is < 0.001, the correlation between wheel-base and price is 
    statistically significant, although the linear relationship isn't extremely strong (~0.585)
"""

#Let's calculate the P-value of horse power and 'Price'
pearson_coef_hp, p_value_hp = stats.pearsonr(df['HP'], df['Price'])
print("="*10, " Horse Power and Price ", "="*10)
print("The pearson correlation coefficient is ", pearson_coef_hp, " with a P-value of ", p_value_hp)

"""
    Conclusion:
    Since the p-value is < 0.001, the correlation between horsepower and price is
    statistically significant, and the linear relationship is quite strong (~0.809, close to 1)
"""

#Let's calculate the P-value of engine-size and price
pearson_coef_ez, p_value_ez = stats.pearsonr(df['Engine-size'], df['Price'])
print("="*10, " Engine Size and Price ", "="*10)
print("The pearson correlation coefficient is ", pearson_coef_ez, " with a P-value of ", p_value_ez)

"""
    Conclusion:
    Since the p-value is < 0.001, the correlation between engine-size and price is
    statistically significant, and the linear relationship is very strong (~0.872).
"""

#Let's calculate the P-value of city-mpg and price
pearson_coef_mpg, p_value_mpg = stats.pearsonr(df['City-mpg'], df['Price'])
print("="*10, " Miles per gallon and Price ", "="*10)
print("The pearson correlation coefficient is ", pearson_coef_mpg, " with a P-value of ", p_value_mpg)

"""
    Conclusion:
    Since the p-value is < 0.001, the correlation between city-mpg and price is
    statistically significant, and the coefficient of ~ -0.687 shows that the 
    relationship is negative and moderately strong.
"""
