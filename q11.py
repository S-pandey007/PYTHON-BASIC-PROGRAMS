import numpy as np
import pandas as pd
ar = np.array([
    [1,2,3],
    [1,2,5],
    [1,3,6],
    [1,1,8]
    ])
df = pd.DataFrame(ar)
print(df)
print(f" column 1 mean : {df[0].mean()}")
print(f"  column 2 mean : {df[1].mean()}")
print(f" column 3 mean :{df[2].mean()}")

