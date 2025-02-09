import numpy as np

rand_list = np.random.randint(0, 100, (10, 10))
print(rand_list.max(0))
print(rand_list.min(1))