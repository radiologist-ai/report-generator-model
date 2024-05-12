import pandas as pd

file = pd.read_csv('id_label.csv', delimiter=',', index_col='id')

file.describe().to_csv("res.csv")
print(file.describe()['No Finding'])
