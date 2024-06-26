import pandas as pd
arr = pd.Series([1,2,3,4,5])
print(arr)

data = {
    'name':['a','b','c'],
    'age':[23,34,45],
    'location':['pune','raipur','ranchi']
}
print(pd.DataFrame(data))