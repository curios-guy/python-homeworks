import numpy as np

l1 = np.random.randint(1,10,(5,5))

row_wise = np.sum(l1, axis = 1)
col_wise = np.sum(l1, axis = 0)
print(f"Row-wise: {row_wise}")
print(f"Column-wise: {col_wise}")