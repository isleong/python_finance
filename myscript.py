import numpy as np
import pandas as pd

from pandas import Series, DataFrame

series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'])
print(series_obj)

print(series_obj['row 7'])

print(series_obj[[0,7]])

np.random.seed(25)
df_obj = DataFrame(np.random.rand(36).reshape(6,6), index=['row 1', 'row 2', 'row 3', 'row 4','row 5', 'row 6'],
                   columns=['column 1', 'column 2', 'column 3', 'column 4','column 5', 'column 6'])

print(df_obj)

# using ix()
print(df_obj.ix[['row 2', 'row 5'], ['column 5', 'column 2']])

#slicing data
print(series_obj['row 3' : 'row 7'])

# comparison operators work on all elements in arrays
print(df_obj < 0.2)

# Find all rows with a value greater than 6
print(series_obj[series_obj > 6])

series_obj['row 1', 'row 5', 'row 8'] = 8
print(series_obj)