import pandas as pd

file = pd.read_csv('chexpert_labeled.csv', delimiter=',', index_col='id')

file.describe().to_csv("res.csv")
print(file.describe()['No Finding'])
