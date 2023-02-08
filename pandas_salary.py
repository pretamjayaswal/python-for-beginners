import pandas as pd

try:

    file = pd.read_csv('salary.csv')
except FileNotFoundError:
    print("File Not Found")



print(file.iloc[4:10])