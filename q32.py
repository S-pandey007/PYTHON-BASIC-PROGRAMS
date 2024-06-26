import pandas as pd
file=pd.read_csv('data.csv')
df=pd.DataFrame(file)
print(df['attendance'].isnull().sum())

mean = df['attendance'].mean()
df['attendance']=df['attendance'].fillna(mean)
print(df.tail())