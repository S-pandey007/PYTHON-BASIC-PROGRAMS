import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
print("Display first 10 rows")
print(df.head(10))
print("Display list of all columns")
print(df.columns)