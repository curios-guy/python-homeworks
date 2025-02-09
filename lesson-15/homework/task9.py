import numpy as np
import time

first_arr = np.random.randint(1, 10, (3,3))
second_arr = np.full((3,3), fill_value=5)
time.sleep(2)
product = np.dot(first_arr,second_arr)
print(product)
