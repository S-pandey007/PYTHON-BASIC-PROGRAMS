import pandas as pd
import numpy as np
data={
     'city':['Delhi','Bengaluru','Chennai','Mumbai','Kolkata'],
     'MaxTemp':[40,31,35,29,39],
     'MinTemp':[32,25,27,21,23],
     'RainFall':[24.1,36.2,40.8,35.2,41.8]
     }
df=pd.DataFrame(data)
print(df)

sum_of_maxtemp = df["MaxTemp"].sum()
print(f"sum of maxtemp : {sum_of_maxtemp}")

sum_of_mintemp = df["MinTemp"].sum()
print(f"sum of mintemp : {sum_of_mintemp}")
      
sum_of_rainfall =df["RainFall"].sum()
print(f"sum of rain fall : {sum_of_rainfall}")

mean_of_rainfall = df["RainFall"].mean()
print(f"mean of rainfall : {mean_of_rainfall}")

median_of_maxtemp = df["MaxTemp"].median()
print(f"median of maxtemp : {median_of_maxtemp}")

print(f"All Column name : {df.columns}")
