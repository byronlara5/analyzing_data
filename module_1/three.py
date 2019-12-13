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
# axis=0 drops the entire row, axis=1 drops the entire column
df.dropna(subset=["Price"], axis=0)

# Saving the dataset (We do this in order to add the new header to the file
df.to_csv("cars_new.csv", index=False)

"""
    We can also read and save to other file formats, like this:
    (pd meaning: pandas, df meaning: dataframe)
    
    Data Formate    |       Read        |       Save        |
    =========================================================
        CSV             pd.read_csv()         df.to_csv()
        JSON            pd.read_json()        df.to_json()
        EXCEL           pd.read_excel()       df.to_excel()
        HDF             pd.read_hdf()         df.to_hdf()
        SQL             pd.read_sql()         df.to_sql()
    =========================================================                  


"""