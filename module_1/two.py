import pandas as pd

file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_1/cars.csv'

# Creating DataFrame with the Cars file
df = pd.read_csv(file)

# List of headers for the CSV File
headers = [
    "Symboling","Normalized-losses","Make","Fuel-type","Aspiration","Num-of-doors","Body-style",
    "Drive-wheels","Engine-location","Wheel-base","Length","Width","Height","Curb-weight","Engine-type",
    "Num-of-cylinders","Engine-size","Fuel-system","Bore","Stroke","Compression-ratio","HP","Peak-rpm",
    "City-mpg","Highway-mpg","Price"
]

# Assigning the headers
df.columns = headers

# Dropping missing values in the column Price
df.dropna(subset=["Price"], axis=0)

print(df.head(10))
