import numpy as np 
import pandas as pd 

ar = np.array([1,2,3,3,4,5,3,5,6,7])
ser = pd.Series(ar)
count = ser.value_counts()
print(count)