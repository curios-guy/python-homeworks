import numpy as np

first_arr = np.random.randint(1,10, (5,3))
second_arr = np.random.randint(1, 10, (3,2))
product = np.dot(first_arr, second_arr)
print(product)