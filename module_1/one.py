import pandas as pd

file = '/home/byron_lara/PycharmProjects/analyzing_data/venv/module_1/cars.csv'

df = pd.read_csv(file, header=None)
df.tail(10)

print(df.tail(10))
