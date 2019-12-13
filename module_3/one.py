import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns



file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_3/cars_bins_and_dummy.csv'

df = pd.read_csv(file)


# ********** Finding the correlation between these columns **********
print(df[['Bore', 'Stroke', 'Compression-ratio', 'HP']].corr())

# ********** Finding the scatter plot (or correlation) of 'Engine-size' and 'Price' **********
#sns.regplot(x='Engine-size', y='Price', data=df)
#plt.ylim(0,)
#plt.show()

# ********** Finding the scatter plot (or correlation) of 'Highway-mpg' and 'Price' **********
#sns.regplot(x='Highway-mpg', y='Price', data=df)
#plt.ylim(0,)
#plt.show()

# ********** Finding the scatter plot (or correlation) of 'Stroke' and 'Price' **********
#sns.regplot(x='Stroke', y='Price', data=df)
#plt.ylim(0,)
#plt.show()

"""
    
    Uncomment in each line to execute the code 

"""
