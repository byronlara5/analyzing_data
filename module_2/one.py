import pandas as pd
import matplotlib.pylab as plt
import numpy as np

file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_2/cars.csv'

headers = [
    "Symboling","Normalized-losses","Make","Fuel-type","Aspiration","Num-of-doors","Body-style",
    "Drive-wheels","Engine-location","Wheel-base","Length","Width","Height","Curb-weight","Engine-type",
    "Num-of-cylinders","Engine-size","Fuel-system","Bore","Stroke","Compression-ratio","HP","Peak-rpm",
    "City-mpg","Highway-mpg","Price"
]

df = pd.read_csv(file, names=headers)

# *************************** IDENTIFY AND HANDLE MISSING VALUES ***************************


# Convert to NaN
def replace():
    df.replace("?", np.nan, inplace=True)

# Count missing values
def countMissing():
    # The output is a boolean value
    missing_data = df.isnull()
    for column in missing_data.columns.values.tolist():
        print(column)
        print(missing_data[column].value_counts())
        print("")

replace()
#countMissing()

"""
    Replace by mean:
        "normalized-losses": 41 missing data, replace them with mean
        "stroke": 4 missing data, replace them with mean
        "bore": 4 missing data, replace them with mean
        "horsepower": 2 missing data, replace them with mean
        "peak-rpm": 2 missing data, replace them with mean
    Replace by frecuency:
        "num-of-doors": 2 missing data, replace them with "four".
        Reason: 84% sedans is four doors. Since four doors is most frequent, it is most likely to occur
    Drop the whole row:
        "price": 4 missing data, simply delete the whole row
        Reasons: Price is what we want to predict. Any Data without price can't be used for prediction
"""

def normalizedLosses():
    #Calculate and print the avg value of Normalized-losses
    print("="*10, "Normalized-losses", "="*10)
    avg_norm_loss = df["Normalized-losses"].astype("float").mean(axis=0)
    print("Average of Normalized-losses: ", avg_norm_loss)

    #Replace NaN value by mean value in Normalized column
    df["Normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

def stroke():
    #Calculate and print the avg value of Stroke
    print("=" * 10, "Stroke", "=" * 10)
    avg_stroke = df['Stroke'].astype("float").mean(axis=0)
    print("Average of Stroke", avg_stroke)

    #Replace NaN value by mean value in Stroke column
    df["Stroke"].replace(np.nan, avg_stroke, inplace=True)

def bore():
    #Calculate and print the avg value of Bore
    print("=" * 10, "Bore", "=" * 10)
    avg_bore = df["Bore"].astype("float").mean(axis=0)
    print("Average of Bore: ", avg_bore)

    #Replace NaN value by mean value in Bore column
    df["Bore"].replace(np.nan, avg_bore, inplace=True)

def horsePower():
    #Calculate and print the avg value of Horse Power
    print("=" * 10, "HP (Horse Power)", "=" * 10)
    avg_hp = df["HP"].astype('float').mean(axis=0)
    print("Average of HP: ", avg_hp)

    #Replace NaN value by mean value in HP column
    df["HP"].replace(np.nan, avg_hp, inplace=True)

def peakRpm():
    #Calculate and print the avg value of Peak-rpm
    print("=" * 10, "Peak-rpm", "=" * 10)
    avg_peak_rpm = df["Peak-rpm"].astype("float").mean(axis=0)
    print("Average peak-rpm: ", avg_peak_rpm)

    #Replace NaN value by mean value in Peak-rpm
    df["Peak-rpm"].replace(np.nan, avg_peak_rpm, inplace=True)

def numofDoors():
    #Print the frecuency value of Num-of-doors
    print("=" * 10, "Num of Doors", "=" * 10)
    print(df["Num-of-doors"].value_counts())
    print(df["Num-of-doors"].value_counts().idxmax())

    #Replace the missing Doors values by the most frequent
    df["Num-of-doors"].replace(np.nan, "four", inplace=True)

def price():
    #Drop the whole row with NaN value in Price column
    df.dropna(subset=["Price"], axis=0, inplace=True)

    #Reset index, because we dropped some rows
    df.reset_index(drop=True, inplace=True)

normalizedLosses()
stroke()
bore()
horsePower()
peakRpm()
numofDoors()
price()

print(df.head(10))
print(df.dtypes)

# Exporting new cleaned file
df.to_csv('cars_cleaned.csv', index=False)