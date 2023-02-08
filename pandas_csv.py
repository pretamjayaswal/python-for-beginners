import pandas as pd

file = pd.read_csv('test_log.csv')
# print(file)
sample = file[file['salary'] > 20000]

# sample.head()

print(sample)
