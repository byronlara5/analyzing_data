import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns



file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_3/cars_bins_and_dummy.csv'

df = pd.read_csv(file)

"""
    === Categorical variables ===
    These are variables that describe a 'characteristic' of a data unit, 
    and are selected from a small group of categories. The categorical variables can 
    have the type: 'object' or 'int64'. A good way to visualize categorical variables
    is by using boxplots.
"""

# ********** Finding the relationship between 'Body-style' and 'Price' **********
#sns.boxplot(x='Body-style', y='Price', data=df)
#plt.ylim(0,)
#plt.show()

# ********** Finding the relationship between 'Engine-location' and 'Price' **********
#sns.boxplot(x='Engine-location', y='Price', data=df)
#plt.ylim(0,)
#plt.show()

# ********** Finding the relationship between 'Drive-wheels' and 'Price' **********
#sns.boxplot(x='Drive-wheels', y='Price', data=df)
#plt.ylim(0,)
#plt.show()

"""

    Uncomment in each line to execute the code 

"""